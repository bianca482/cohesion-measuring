import json
from cohesion_calculator.cohesion import calculate_connection_intensity, scom, calculate_scom, filter_empty_apis
from cohesion_calculator import span 


empty_span = span.Span("span3", "trace2", [], "", 3)
span1 = span.Span("span1", "trace1", ["SELECT * FROM products"], "/service1/products", 10)
span2 = span.Span("span2", "trace1", ["SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id"], "/service1/employees?id=10", 20)
span3 = span.Span("span3", "trace2", [], "/service2/test", 5)
span4 = span.Span("span4", "trace2", [], "/service1/test", 30)
span5 = span.Span("span5", "trace2", ["SELECT * FROM orders"], "/service1/orders", 45)


def test_extract_table_names():
    sql_statements = [
        "SELECT name, email FROM employees;",
        "SELECT * FROM employees e JOIN customers c ON e.id = c.employee_id;",
        "INSERT INTO orders (customer_id, product_id, order_date) VALUES (1, 2, '2024-05-25');",
        "UPDATE employees SET position = 'Manager' WHERE id = 1;",
        "DELETE FROM customers WHERE id = 1;",
    ]

    table_names = []

    for sql in sql_statements:
        table_names.append(span.extract_table_names(sql))

    assert table_names[0] == ["employees"]
    assert table_names[1] == ["employees", "customers"]
    assert table_names[2] == ["orders"]
    assert table_names[3] == ["employees"]
    assert table_names[4] == ["customers"]

def test_get_endpoint_name():
    assert span1.get_endpoint_name() == "service1/products/"
    assert span2.get_endpoint_name() == "service1/employees/"
    assert empty_span.get_endpoint_name() == "/"

def test_get_table_names():
    assert span1.get_table_names() == ["products"]
    assert span2.get_table_names() == ["employees", "customers"]
    assert empty_span.get_table_names() == None

def test_is_number(): 
    assert span.is_number(1) == True
    assert span.is_number("34") == True
    assert span.is_number("kjdfh") == False
    assert span.is_number("+") == False

def test_group_spans_by_trace_id():
    result = span.group_spans_by_trace_id([span1, span2, span3, span4, span5])
    assert result == {"trace1": [span1, span2], "trace2": [span3, span4, span5]}

def test_set_parent_endpoints(): 
    assert span1.parent_endpoint == None
    assert span2.parent_endpoint == None
    assert span3.parent_endpoint == None
    assert span4.parent_endpoint == None
    assert span5.parent_endpoint == None

    spans = [span1, span2, span3, span4, span5]
    span.set_parent_endpoints(spans, "service1")

    assert span1.parent_endpoint == "service1/products/"
    assert span2.parent_endpoint == "service1/products/"
    assert span3.parent_endpoint == "service1/test/"
    assert span4.parent_endpoint == "service1/test/"
    assert span5.parent_endpoint == "service1/test/"

def test_group_spans():
    spans = [span1, span2, empty_span]
    spans = span.set_parent_endpoints(spans, "service1")
    
    grouped_spans = span.group_spans(spans)

    assert grouped_spans == {'service1/products/': ['products', 'employees', 'customers']}

def test_group_spans_duplicate_values():
    spans = [span1, span2, span2, empty_span]
    spans = span.set_parent_endpoints(spans, "service1")
    
    grouped_spans = span.group_spans(spans)

    assert grouped_spans == {
        "service1/products/": ["products", "employees", "customers"]
    }

def test_extract_spans(): 
    spans = [span1, span2]

    assert spans[0].get_endpoint_name() == "service1/products/"
    assert spans[0].get_table_names() == ["products"]

    assert spans[1].get_endpoint_name() == "service1/employees/"
    assert spans[1].get_table_names() == ["employees", "customers"]


def test_calculate_connection_intensity_worst(): 
    grouped_spans = {
        "service1/orders/": ["products"],
        "service1/customers/": ["customers"]
    }

    connection_intensity = calculate_connection_intensity(grouped_spans["service1/orders/"], grouped_spans["service1/customers/"])
    assert connection_intensity == 0
    
def test_calculate_connection_intensity_best(): 
    grouped_spans = {
        "service1/orders/": ["products", "customers"],
        "service1/customers/": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_spans["service1/orders/"], grouped_spans["service1/customers/"])
    assert connection_intensity == 1

def test_calculate_connection_intensity_middle(): 
    grouped_spans = {
        "service1/orders/": ["products", "employees"],
        "service1/customers/": ["customers", "products"]
    }

    connection_intensity = calculate_connection_intensity(grouped_spans["service1/orders/"], grouped_spans["service1/customers/"])
    assert connection_intensity == 0.5
    
def test_scom_too_few_endpoints(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    spans = span.extract_spans(data, "scenario7", "json")
    grouped_spans = span.group_spans(spans, "json")
    endpoint_calls = span.get_number_of_endpoint_calls(spans)

    assert scom(grouped_spans, endpoint_calls) == "Undefined (There are too few endpoints to calculate SCOM)"
        
def test_scom_best(): 
    file = open("../test_scenarios/test_data/scenario2.json")
    data = json.load(file)
    file.close()

    spans = span.extract_spans(data, "scenario2", "json")
    grouped_spans = span.group_spans(spans, "json")
    endpoint_calls = span.get_number_of_endpoint_calls(spans)

    assert scom(grouped_spans, endpoint_calls) == 1

def test_scom_worst(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    spans = span.extract_spans(data, "scenario1", "json")
    grouped_spans = span.group_spans(spans, "json")
    endpoint_calls = span.get_number_of_endpoint_calls(spans)

    assert scom(grouped_spans, endpoint_calls) == 0

def test_scom_middle(): 
    file = open("../test_scenarios/test_data/scenario3.json")
    data = json.load(file)
    file.close()

    spans = span.extract_spans(data, "scenario3", "json")
    grouped_spans = span.group_spans(spans, "json")
    endpoint_calls = span.get_number_of_endpoint_calls(spans)

    assert scom(grouped_spans, endpoint_calls) == 0.5

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

def test_retrieve_grouped_spans(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    result = span.get_grouped_spans_from_file(data, "scenario1", "json")
    print(result)

    assert result == {
        'scenario1/employees/': ['customers', 'employees'],
        'scenario1/orders/': ['products', 'orders']
    }

def test_get_number_of_calls():
    spans = [span1, span2, empty_span]

    result = span.get_number_of_calls_per_table(spans)

    assert result == {'service1/products/': {'customers': 1, 'employees': 1, 'products': 1}}


def test_get_number_of_endpoint_calls_from_file(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    result = span.get_number_of_endpoint_calls_from_file(data, "scenario1", "json")

    assert result == {
        'scenario1/orders/': {'orders': 1, 'products': 1},
        'scenario1/employees/': {'employees': 2, 'customers': 2}
    }

def test_get_number_of_endpoint_calls_from_file():
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    result = span.get_number_of_endpoint_calls_from_file(data, "scenario1", "json")

    assert result == {
        'scenario1/orders/': 3, 
        'scenario1/employees/': 5
    }




