import json
from cohesion_calculator.cohesion import calculate_connection_intensity, scom, calculate_scom, filter_empty_apis
from cohesion_calculator.log import Log, extract_table_names, extract_logs, group_logs, retrieve_grouped_logs_from_file, set_parent_endpoints
"""
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

log = Log("1", "abc", None, ["SELECT * FROM products"], "/service1/products")
log2 = Log("2", "abc", "1", ["SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id"], "/service1/employees?id=10")
empty_log = Log("3", "def", None, [], None)

def test_get_endpoint_name():
    assert log.get_endpoint_name() == "service1/products/"
    assert log2.get_endpoint_name() == "service1/employees/"
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
    file = open("../test_scenarios/test_data/scenario1.json")
    result = json.load(file)
    file.close()

    logs = extract_logs(result, "scenario1")

    assert logs[0].span_id == "186e4c8f97c57c94"
    assert logs[0].get_endpoint_name() == "scenario1/orders/"
    assert logs[0].get_db_statement() == None
    assert logs[0].get_table_names() == None

    assert logs[1].span_id == "9eb9be13e922fc0e"
    assert logs[1].get_endpoint_name() == "scenario1/orders/"
    assert logs[1].get_db_statement() == ['SELECT * FROM orders']
    assert logs[1].get_table_names() == ["orders"]

def test_group_logs():
    logs = [log, log2, empty_log]
    logs = set_parent_endpoints(logs, "service1")
    
    grouped_logs = group_logs(logs)

    assert grouped_logs == {'service1/products/': ['products', 'employees', 'customers']}

def test_group_logs_duplicate_values():
    logs = [log, log2, log2, empty_log]
    logs = set_parent_endpoints(logs, "service1")
    
    grouped_logs = group_logs(logs)

    assert grouped_logs == {
        "service1/products/": ["products", "employees", "customers"]
    }

def test_calculate_connection_intensity_worst(): 
    grouped_logs = {
        "service1/orders/": ["products"],
        "service1/customers/": ["customers"]
    }

    connection_intensity = calculate_connection_intensity(grouped_logs["service1/orders/"], grouped_logs["service1/customers/"])
    assert connection_intensity == 0
    
def test_calculate_connection_intensity_best(): 
    grouped_logs = {
        "service1/orders/": ["products", "customers"],
        "service1/customers/": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_logs["service1/orders/"], grouped_logs["service1/customers/"])
    assert connection_intensity == 1

def test_calculate_connection_intensity_middle(): 
    grouped_logs = {
        "service1/orders/": ["products", "employees"],
        "service1/customers/": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_logs["service1/orders/"], grouped_logs["service1/customers/"])
    assert connection_intensity == 0.5
    
def test_scom_too_few_endpoints(): 
    grouped_logs = {
        "service1/orders/": ["products", "employees"]
    }

    assert scom(grouped_logs) == "Too few endpoints"
        
def test_scom_best(): 
    grouped_logs = {
        "service1/orders/": ["products", "customers"],
        "service1/customers/": ["customers", "products"]
    }

    assert scom(grouped_logs) == 1

def test_scom_worst(): 
    grouped_logs = {
        "service1/orders/": ["products"],
        "service1/customers/": ["customers"]
    }

    assert scom(grouped_logs) == 0

def test_scom_middle(): 
    grouped_logs = {
        "service1/orders/": ["products", "employees"],
        "service1/customers/": ["customers", "products"]
    }

    assert scom(grouped_logs) == 0.5

def test_calculate_scom():
    file = open("../test_scenarios/test_data/scenario2.json")
    result = json.load(file)
    file.close()

    scom = calculate_scom(result, "scenario2")
    assert scom == 1

def test_filter_empty_apis():
    input = {'service1/employees/': ['employees'], 'service1/customers/': ['customers'], 'service1/customers/test/': []}
    result = filter_empty_apis(input)

    assert result == {'service1/employees/': ['employees'], 'service1/customers/': ['customers']}

def test_retrieve_grouped_logs(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    result = retrieve_grouped_logs_from_file(data, "scenario1")

    assert result == {
        'scenario1/employees/': ['customers', 'employees'],
        'scenario1/orders/': ['orders', 'products']
    }"""


def test_set_parent_endpoints(): 
    log = Log("1", "abc", None, ["SELECT * FROM products"], "/service1/products")
    log2 = Log("2", "abc", "1", ["SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id"], "/service1/employees?id=10")
    log3 = Log("3", "def", "4", [], "/service2/test")
    log4 = Log("4", "def", "1", [], "/service1/test")
    log5 = Log("5", "abc", "2", ["SELECT * FROM orders"], "/service1/orders")

    assert log.parent_endpoint == None
    assert log2.parent_endpoint == None
    assert log3.parent_endpoint == None
    assert log4.parent_endpoint == None
    assert log5.parent_endpoint == None

    logs = [log, log2, log3, log4, log5]
    set_parent_endpoints(logs, "service1")

    assert log.parent_endpoint == "service1/products/"
    assert log2.parent_endpoint == "service1/products/"
    assert log3.parent_endpoint == "service1/test/"
    assert log4.parent_endpoint == "service1/test/"
    assert log5.parent_endpoint == "service1/products/"



