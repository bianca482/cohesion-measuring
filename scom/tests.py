import json
from cohesion_calculator.cohesion import calculate_connection_intensity, extract_logs, group_logs, scom, calculate_scom, filter_empty_apis
from cohesion_calculator.log import Log, extract_table_names

def test_extract_tables():
    sql_statements = [
        "SELECT name, email FROM employees;",
        "SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id;",
        "INSERT INTO orders (customer_id, product_id, order_date) VALUES (1, 2, '2024-05-25');",
        "UPDATE employees SET position = 'Manager' WHERE id = 1;",
        "DELETE FROM customers WHERE id = 1;",
    ]

    table_names = []

    for sql in sql_statements:
        table_names.append(extract_table_names(sql))

    assert table_names[0] == ["employees"]
    assert table_names[1] == ["employees", "customers"]
    assert table_names[2] == ["orders"]
    assert table_names[3] == ["employees"]
    assert table_names[4] == ["customers"]


reference_tags = [
    {'key': 'http.flavor', 'type': 'string', 'value': '1.1'}, 
    {'key': 'http.host', 'type': 'string', 'value': 'persistence:8080'}, 
    {'key': 'http.method', 'type': 'string', 'value': 'GET'}, 
    {'key': 'http.response_content_length', 'type': 'int64', 'value': 347}, 
    {'key': 'http.scheme', 'type': 'string', 'value': 'http'}, 
    {'key': 'http.server_name', 'type': 'string', 'value': 'persistence'},
    {'key': 'http.status_code', 'type': 'int64', 'value': 200}, 
    {'key': 'http.target', 'type': 'string', 'value': '/products'}, 
]
    
tags = [
   {
      "key":"db.statement",
      "type":"string",
      "value":"SELECT * FROM products"
   },
]

reference_tags2 = [
    {'key': 'http.flavor', 'type': 'string', 'value': '1.1'}, 
    {'key': 'http.host', 'type': 'string', 'value': 'persistence:8080'}, 
    {'key': 'http.method', 'type': 'string', 'value': 'GET'}, 
    {'key': 'http.response_content_length', 'type': 'int64', 'value': 347}, 
    {'key': 'http.scheme', 'type': 'string', 'value': 'http'}, 
    {'key': 'http.server_name', 'type': 'string', 'value': 'persistence'},
    {'key': 'http.status_code', 'type': 'int64', 'value': 200}, 
    {'key': 'http.target', 'type': 'string', 'value': '/employees'}, 
]

tags2 = [
   {
      "key":"db.statement",
      "type":"string",
      "value":"SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id"
   },
]

log = Log("1", reference_tags, tags)
log2 = Log("2", reference_tags2, tags2)
empty_log = Log("3", [], [])

def test_get_endpoint_name():
    assert log.get_endpoint_name() == "/products/"
    assert log2.get_endpoint_name() == "/employees/"
    assert empty_log.get_endpoint_name() == None

def test_get_db_statement(): 
    assert log.get_db_statement() == ["SELECT * FROM products"]
    assert log2.get_db_statement() == ["SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id"]
    assert empty_log.get_db_statement() == None

def test_get_table_names():
    assert log.get_table_names() == ["products"]
    assert log2.get_table_names() == ["employees", "customers"]
    assert empty_log.get_table_names() == None

def test_extract_logs_with_nested_url(): 
    file = open("../test_data/scenario1.json")
    result = json.load(file)
    file.close()

    logs = extract_logs(result)

    assert logs[0].span_id == "8d3dc819cbc44469"
    assert logs[0].get_endpoint_name() == "/orders/"
    assert logs[0].get_db_statement() == ['SELECT * FROM products']
    assert logs[0].get_table_names() == ["products"]

    assert logs[1].span_id == "e519b5b19e3394ab"
    assert logs[1].get_endpoint_name() == "/orders/"
    assert logs[1].get_db_statement() == ['SELECT * FROM orders']
    assert logs[1].get_table_names() == ["orders"]

def test_group_logs():
    logs = [log, log2, empty_log]
    grouped_logs = group_logs(logs)

    assert grouped_logs == {
        "/products/": ["products"],
        "/employees/": ["employees", "customers"]
    }

def test_group_logs_duplicate_values():
    logs = [log, log2, log2, empty_log]
    grouped_logs = group_logs(logs)

    assert grouped_logs == {
        "/products/": ["products"],
        "/employees/": ["employees", "customers"]
    }

def test_calculate_connection_intensity_worst(): 
    grouped_logs = {
        "/orders/": ["products"],
        "/customers/": ["customers"]
    }

    connection_intensity = calculate_connection_intensity(grouped_logs["/orders/"], grouped_logs["/customers/"])
    assert connection_intensity == 0
    
def test_calculate_connection_intensity_best(): 
    grouped_logs = {
        "/orders/": ["products", "customers"],
        "/customers/": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_logs["/orders/"], grouped_logs["/customers/"])
    assert connection_intensity == 1

def test_calculate_connection_intensity_middle(): 
    grouped_logs = {
        "/orders/": ["products", "employees"],
        "/customers/": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_logs["/orders/"], grouped_logs["/customers/"])
    assert connection_intensity == 0.5
    
def test_scom_too_few_endpoints(): 
    grouped_logs = {
        "/orders/": ["products", "employees"]
    }

    assert scom(grouped_logs) == "Too few endpoints"
        
def test_scom_best(): 
    grouped_logs = {
        "/orders/": ["products", "customers"],
        "/customers/": ["customers", "products"]
    }

    assert scom(grouped_logs) == 1

def test_scom_worst(): 
    grouped_logs = {
        "/orders/": ["products"],
        "/customers/": ["customers"]
    }

    assert scom(grouped_logs) == 0

def test_scom_middle(): 
    grouped_logs = {
        "/orders/": ["products", "employees"],
        "/customers/": ["customers", "products"]
    }

    assert scom(grouped_logs) == 0.5

def test_all():
    file = open("../test_data/scenario2.json")
    result = json.load(file)
    file.close()

    scom = calculate_scom(result)
    assert scom == 1

def test_filter_empty_apis():
    input = {'/employees/': ['employees'], 'customers/': ['customers'], 'customers/test/': []}
    result = filter_empty_apis(input)

    assert result == {'/employees/': ['employees'], 'customers/': ['customers']}









