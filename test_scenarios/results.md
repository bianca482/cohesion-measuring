### Scenario1

Cohesion for Service scenario1: 0.0

Grouped logs for scenario1.json: {'scenario1/orders/': ['orders', 'products'], 'scenario1/employees/': ['customers', 'employees']}

Number of calls for scenario1.json: {'scenario1/orders/': {'orders': 1, 'products': 1}, 'scenario1/employees/': {'customers': 2, 'employees': 2}}

### Scenario2

Cohesion for Service scenario2: 1.0

Grouped logs for scenario2.json: {'scenario2/employees/': ['customers', 'orders', 'products', 'employees'], 'scenario2/orders/': ['products', 'employees', 'customers', 'orders']}

Number of calls for scenario2.json: {'scenario2/employees/': {'customers': 1, 'orders': 1, 'products': 1, 'employees': 1}, 'scenario2/orders/': {'products': 1, 'employees': 1, 'customers': 1, 'orders': 1}}

### Scenario3

Cohesion for Service scenario3: 0.5

Grouped logs for scenario3.json: {'scenario3/orders/': ['products', 'orders'], 'scenario3/employees/': ['customers', 'orders', 'employees']}

Number of calls for scenario3.json: {'scenario3/orders/': {'products': 1, 'orders': 1}, 'scenario3/employees/': {'customers': 1, 'orders': 1, 'employees': 1}}
