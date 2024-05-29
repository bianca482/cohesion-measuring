import json
from scom.cohesion import calculate_connection_intensity, extract_logs, group_logs, scom
from scom.log import Log, extract_table_names

def test_extract_tables():
    sql_statements = [
        "SELECT name, email FROM employees;",
        "SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id;",
        "INSERT INTO orders (customer_id, product_id, order_date) VALUES (1, 2, '2024-05-25');",
        "UPDATE employees SET position = 'Manager' WHERE id = 1;",
        "DELETE FROM customers WHERE id = 1;",
        "CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR(100));",
        "DROP TABLE orders;"
    ]

    table_names = []

    for sql in sql_statements:
        table_names.append(extract_table_names(sql))

    assert table_names[0] == ["employees"]
    assert table_names[1] == ["employees", "customers"]
    assert table_names[2] == ["orders"]
    assert table_names[3] == ["employees"]
    assert table_names[4] == ["customers"]
    assert table_names[5] == ["products"]
    assert table_names[6] == ["orders"]


spans = [ 
    {
        "traceID": "e64522db188e37a765bdb819551f76bc",
        "spanID": "72a7a685cda0570a",
        "operationName": "/orders",
        "references": [],
        "startTime": 1716793796726460,
        "duration": 67054,
    }
]
    
tags = [
    { "key": "db.name", "type": "string", "value": "szenariodb" },
    {
        "key": "db.statement",
        "type": "string",
        "value": "SELECT * FROM products"
    },
    { "key": "db.system", "type": "string", "value": "postgresql" },
    { "key": "db.user", "type": "string", "value": "postgres" },
]

spans2 = [ 
    {
        "traceID": "e64522db188e37a765bdb819551f76bc",
        "spanID": "72a7a685cda0570a",
        "operationName": "/employees",
        "references": [],
        "startTime": 1716793796726460,
        "duration": 67054,
    }
]

tags2 = [
    { "key": "db.name", "type": "string", "value": "szenariodb" },
    {
        "key": "db.statement",
        "type": "string",
        "value": "SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id"
    },
    { "key": "db.system", "type": "string", "value": "postgresql" },
    { "key": "db.user", "type": "string", "value": "postgres" },
]

log = Log("1", spans, tags)
log2 = Log("2", spans2, tags2)
empty_log = Log("3", [], [])

def test_get_operation_name():
    assert log.get_operation_name() == "orders"
    assert log2.get_operation_name() == "employees"
    assert empty_log.get_operation_name() == None

def test_get_db_statement(): 
    assert log.get_db_statements() == ["SELECT * FROM products"]
    assert log2.get_db_statements() == ["SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id"]
    assert empty_log.get_db_statements() == None

def test_get_table_names():
    assert log.get_table_names() == ["products"]
    assert log2.get_table_names() == ["employees", "customers"]
    assert empty_log.get_table_names() == None

def test_extract_logs_with_nested_url(): 
    file = open("../test_data/insert.json")
    result = json.load(file)
    file.close()

    logs = extract_logs(result)

    assert logs[0].span_id == "c7649170f4eba7b5"
    assert logs[0].get_operation_name() == None
    assert logs[0].get_db_statements() == None
    assert logs[0].get_table_names() == None

    assert logs[1].span_id == "a4eea99d6c296179"
    assert logs[1].get_operation_name() == "employees"
    assert logs[1].get_db_statements() == ['INSERT INTO employees (name, position, start_date) VALUES (%s, %s, %s)']
    assert logs[1].get_table_names() == ["employees"]

    assert logs[2].span_id == "34bc2bae63d2ca1e"
    assert logs[2].get_operation_name() == "employees"
    assert logs[2].get_db_statements() == ['SELECT * FROM customers']
    assert logs[2].get_table_names() == ["customers"]

    assert logs[3].span_id == "c488e474bb7cfb21"
    assert logs[3].get_operation_name() == None
    assert logs[3].get_db_statements() == None
    assert logs[3].get_table_names() == None

def test_group_logs():
    logs = [log, log2, empty_log]
    grouped_logs = group_logs(logs)

    assert grouped_logs == {
        "orders": ["products"],
        "employees": ["employees", "customers"]
    }

def test_group_logs_duplicate_values():
    logs = [log, log2, log2, empty_log]
    grouped_logs = group_logs(logs)

    assert grouped_logs == {
        "orders": ["products"],
        "employees": ["employees", "customers"]
    }

def test_calculate_connection_intensity_worst(): 
    grouped_logs = {
        "orders": ["products"],
        "customers": ["customers"]
    }

    connection_intensity = calculate_connection_intensity(grouped_logs["orders"], grouped_logs["customers"])
    assert connection_intensity == 0
    
def test_calculate_connection_intensity_best(): 
    grouped_logs = {
        "orders": ["products", "customers"],
        "customers": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_logs["orders"], grouped_logs["customers"])
    assert connection_intensity == 1

def test_calculate_connection_intensity_middle(): 
    grouped_logs = {
        "orders": ["products", "employees"],
        "customers": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_logs["orders"], grouped_logs["customers"])
    assert connection_intensity == 0.5
    
def test_scom_too_few_endpoints(): 
    grouped_logs = {
        "orders": ["products", "employees"]
    }

    assert scom(grouped_logs, 2) == "Too few endpoints"
        
def test_scom_best(): 
    grouped_logs = {
        "orders": ["products", "customers"],
        "customers": ["customers", "products"]
    }

    assert scom(grouped_logs, 2) == 1

def test_scom_worst(): 
    grouped_logs = {
        "orders": ["products"],
        "customers": ["customers"]
    }

    assert scom(grouped_logs, 2) == 0

def test_scom_middle(): 
    grouped_logs = {
        "orders": ["products", "employees"],
        "customers": ["customers", "products"]
    }

    assert scom(grouped_logs, 3) == 0.5








