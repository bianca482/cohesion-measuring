import json
from cohesion_calculator.cohesion import calculate_connection_intensity, scom, calculate_scom, filter_empty_apis
from cohesion_calculator import trace 


trace1 = trace.Trace("span1", "trace1", ["SELECT * FROM products"], "/service1/products", 1)
trace2 = trace.Trace("span2", "trace1", ["SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id"], "/service1/employees?id=10", 2)
empty_trace = trace.Trace("span3", "trace2", [], "", 3)

span1 = trace.Trace("span1", "trace1", ["SELECT * FROM products"], "/service1/products", 10)
span2 = trace.Trace("span2", "trace1", ["SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id"], "/service1/employees?id=10", 20)
span3 = trace.Trace("span3", "trace2", [], "/service2/test", 5)
span4 = trace.Trace("span4", "trace2", [], "/service1/test", 30)
span5 = trace.Trace("span5", "trace2", ["SELECT * FROM orders"], "/service1/orders", 45)


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
        table_names.append(trace.extract_table_names(sql))

    assert table_names[0] == ["employees"]
    assert table_names[1] == ["employees", "customers"]
    assert table_names[2] == ["orders"]
    assert table_names[3] == ["employees"]
    assert table_names[4] == ["customers"]

def test_get_endpoint_name():
    assert trace1.get_endpoint_name() == "service1/products/"
    assert trace2.get_endpoint_name() == "service1/employees/"
    assert empty_trace.get_endpoint_name() == "/"

def test_get_table_names():
    assert trace1.get_table_names() == ["products"]
    assert trace2.get_table_names() == ["employees", "customers"]
    assert empty_trace.get_table_names() == None

def test_is_number(): 
    assert trace.is_number(1) == True
    assert trace.is_number("34") == True
    assert trace.is_number("kjdfh") == False
    assert trace.is_number("+") == False

def test_group_traces_by_trace_id():
    result = trace.group_traces_by_trace_id([span1, span2, span3, span4, span5])
    assert result == {"trace1": [span1, span2], "trace2": [span3, span4, span5]}

def test_set_parent_endpoints(): 
    assert span1.parent_endpoint == None
    assert span2.parent_endpoint == None
    assert span3.parent_endpoint == None
    assert span4.parent_endpoint == None
    assert span5.parent_endpoint == None

    traces = [span1, span2, span3, span4, span5]
    trace.set_parent_endpoints(traces, "service1")

    assert span1.parent_endpoint == "service1/products/"
    assert span2.parent_endpoint == "service1/products/"
    assert span3.parent_endpoint == "service1/test/"
    assert span4.parent_endpoint == "service1/test/"
    assert span5.parent_endpoint == "service1/test/"

def test_group_traces():
    traces = [trace1, trace2, empty_trace]
    traces = trace.set_parent_endpoints(traces, "service1")
    
    grouped_traces = trace.group_traces(traces)

    assert grouped_traces == {'service1/products/': ['products', 'employees', 'customers']}

def test_group_traces_duplicate_values():
    traces = [trace1, trace2, trace2, empty_trace]
    traces = trace.set_parent_endpoints(traces, "service1")
    
    grouped_traces = trace.group_traces(traces)

    assert grouped_traces == {
        "service1/products/": ["products", "employees", "customers"]
    }

def test_extract_traces(): 
    traces = [trace1, trace2]

    assert traces[0].get_endpoint_name() == "service1/products/"
    assert traces[0].get_table_names() == ["products"]

    assert traces[1].get_endpoint_name() == "service1/employees/"
    assert traces[1].get_table_names() == ["employees", "customers"]


def test_calculate_connection_intensity_worst(): 
    grouped_traces = {
        "service1/orders/": ["products"],
        "service1/customers/": ["customers"]
    }

    connection_intensity = calculate_connection_intensity(grouped_traces["service1/orders/"], grouped_traces["service1/customers/"])
    assert connection_intensity == 0
    
def test_calculate_connection_intensity_best(): 
    grouped_traces = {
        "service1/orders/": ["products", "customers"],
        "service1/customers/": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_traces["service1/orders/"], grouped_traces["service1/customers/"])
    assert connection_intensity == 1

def test_calculate_connection_intensity_middle(): 
    grouped_traces = {
        "service1/orders/": ["products", "employees"],
        "service1/customers/": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_traces["service1/orders/"], grouped_traces["service1/customers/"])
    assert connection_intensity == 0.5
    
def test_scom_too_few_endpoints(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    traces = trace.extract_traces(data, "scenario7", "json")
    grouped_traces = trace.group_traces(traces, "json")
    endpoint_calls = trace.get_number_of_endpoint_calls(traces)

    assert scom(grouped_traces, endpoint_calls) == "Undefined (There are too few endpoints to calculate SCOM)"
        
def test_scom_best(): 
    file = open("../test_scenarios/test_data/scenario2.json")
    data = json.load(file)
    file.close()

    traces = trace.extract_traces(data, "scenario2", "json")
    grouped_traces = trace.group_traces(traces, "json")
    endpoint_calls = trace.get_number_of_endpoint_calls(traces)

    assert scom(grouped_traces, endpoint_calls) == 1

def test_scom_worst(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    traces = trace.extract_traces(data, "scenario1", "json")
    grouped_traces = trace.group_traces(traces, "json")
    endpoint_calls = trace.get_number_of_endpoint_calls(traces)

    assert scom(grouped_traces, endpoint_calls) == 0

def test_scom_middle(): 
    file = open("../test_scenarios/test_data/scenario3.json")
    data = json.load(file)
    file.close()

    traces = trace.extract_traces(data, "scenario3", "json")
    grouped_traces = trace.group_traces(traces, "json")
    endpoint_calls = trace.get_number_of_endpoint_calls(traces)

    assert scom(grouped_traces, endpoint_calls) == 0.5

def test_calculate_scom():
    file = open("../test_scenarios/test_data/scenario2.json")
    result = json.load(file)
    file.close()

    scom = calculate_scom(result, "scenario2", False, "json")
    assert scom == 1

def test_filter_empty_apis():
    input = {'service1/employees/': ['employees'], 'service1/customers/': ['customers'], 'service1/customers/test/': []}
    result = filter_empty_apis(input)

    assert result == {'service1/employees/': ['employees'], 'service1/customers/': ['customers']}

def test_retrieve_grouped_traces(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    result = trace.get_grouped_traces_from_file(data, "scenario1", "json")
    print(result)

    assert result == {
        'scenario1/employees/': ['customers', 'employees'],
        'scenario1/orders/': ['products', 'orders']
    }

def test_get_number_of_calls():
    traces = [trace1, trace2, empty_trace]

    result = trace.get_number_of_calls_per_table(traces)

    assert result == {'service1/products/': {'customers': 1, 'employees': 1, 'products': 1}}


def test_get_number_of_endpoint_calls_from_file(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    result = trace.get_number_of_endpoint_calls_from_file(data, "scenario1", "json")

    assert result == {
        'scenario1/orders/': {'orders': 1, 'products': 1},
        'scenario1/employees/': {'employees': 2, 'customers': 2}
    }

def test_get_number_of_endpoint_calls_from_file():
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    result = trace.get_number_of_endpoint_calls_from_file(data, "scenario1", "json")

    assert result == {
        'scenario1/orders/': 3, 
        'scenario1/employees/': 5
    }




