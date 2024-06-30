import json
from cohesion_calculator.cohesion import calculate_connection_intensity, scom, calculate_scom, filter_empty_apis
from cohesion_calculator.log import Log, extract_logs, group_logs, get_grouped_logs_from_file, set_parent_endpoints, get_number_of_endpoint_calls, get_number_of_calls_per_table, get_number_of_endpoint_calls_from_file, get_number_of_calls_from_file


log = Log("span1", "trace1", ["products"], "/service1/products", 1)
log2 = Log("span2", "trace1", ["employees", "customers"], "/service1/employees?id=10", 2)
empty_log = Log("span3", "trace2", [], "", 3)

span1 = Log("span1", "trace1", ["products"], "/service1/products", 10)
span2 = Log("span2", "trace1", ["employees", "customers"], "/service1/employees?id=10", 20)
span3 = Log("span3", "trace2", [], "/service2/test", 5)
span4 = Log("span4", "trace2", [], "/service1/test", 30)
span5 = Log("span5", "trace2", ["orders"], "/service1/orders", 45)


def test_get_endpoint_name():
    assert log.get_endpoint_name() == "service1/products/"
    assert log2.get_endpoint_name() == "service1/employees/"
    assert empty_log.get_endpoint_name() == None

def test_get_table_names():
    assert log.get_table_names() == ["products"]
    assert log2.get_table_names() == ["employees", "customers"]
    assert empty_log.get_table_names() == None

def test_is_number(): 
    assert log.is_number(1) == True
    assert log.is_number("34") == True
    assert log.is_number("kjdfh") == False
    assert log.is_number("+") == False

def test_group_traces_by_trace_id():
    result = log.group_traces_by_trace_id([span1, span2, span3, span4, span5])
    assert result == {"trace1": [span1, span2], "trace2": [span3, span4, span5]}

def test_set_parent_endpoints(): 
    assert span1.parent_endpoint == None
    assert span2.parent_endpoint == None
    assert span3.parent_endpoint == None
    assert span4.parent_endpoint == None
    assert span5.parent_endpoint == None

    logs = [span1, span2, span3, span4, span5]
    set_parent_endpoints(logs, "service1")

    assert span1.parent_endpoint == "service1/products/"
    assert span2.parent_endpoint == "service1/products/"
    assert span3.parent_endpoint == "service1/test/"
    assert span4.parent_endpoint == "service1/test/"
    assert span5.parent_endpoint == "service1/test/"

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

def test_extract_logs_with_nested_url(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    result = json.load(file)
    file.close()

    logs = extract_logs(result, "scenario1")

    assert logs[0].span_id == "186e4c8f97c57c94"
    assert logs[0].get_endpoint_name() == "scenario1/orders/"
    assert logs[0].get_table_names() == None

    assert logs[1].span_id == "9eb9be13e922fc0e"
    assert logs[1].get_endpoint_name() == "scenario1/orders/"
    assert logs[1].get_table_names() == ["orders"]


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
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    logs = extract_logs(data, "scenario7")
    grouped_logs = group_logs(logs)
    endpoint_calls = get_number_of_endpoint_calls(logs)

    assert scom(grouped_logs, endpoint_calls) == "Too few endpoints"
        
def test_scom_best(): 
    file = open("../test_scenarios/test_data/scenario2.json")
    data = json.load(file)
    file.close()

    logs = extract_logs(data, "scenario2")
    grouped_logs = group_logs(logs)
    endpoint_calls = get_number_of_endpoint_calls(logs)

    assert scom(grouped_logs, endpoint_calls) == 1

def test_scom_worst(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    logs = extract_logs(data, "scenario1")
    grouped_logs = group_logs(logs)
    endpoint_calls = get_number_of_endpoint_calls(logs)

    assert scom(grouped_logs, endpoint_calls) == 0

def test_scom_middle(): 
    file = open("../test_scenarios/test_data/scenario3.json")
    data = json.load(file)
    file.close()

    logs = extract_logs(data, "scenario3")
    grouped_logs = group_logs(logs)
    endpoint_calls = get_number_of_endpoint_calls(logs)

    assert scom(grouped_logs, endpoint_calls) == 0.5

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

    result = get_grouped_logs_from_file(data, "scenario1")

    assert result == {
        'scenario1/employees/': ['customers', 'employees'],
        'scenario1/orders/': ['orders', 'products']
    }

def test_get_number_of_calls():
    logs = [log, log2, empty_log]

    result = get_number_of_calls_per_table(logs)

    assert result == {'service1/products/': {'customers': 1, 'employees': 1, 'products': 1}}


def test_get_number_of_calls_from_file(): 
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    result = get_number_of_calls_from_file(data, "scenario1")

    assert result == {
        'scenario1/orders/': {'orders': 1, 'products': 1},
        'scenario1/employees/': {'employees': 2, 'customers': 2}
    }

def test_get_number_of_endpoint_calls_from_file():
    file = open("../test_scenarios/test_data/scenario1.json")
    data = json.load(file)
    file.close()

    result = get_number_of_endpoint_calls_from_file(data, "scenario1")

    assert result == {
        'scenario1/orders/': 3, 
        'scenario1/employees/': 5
    }




