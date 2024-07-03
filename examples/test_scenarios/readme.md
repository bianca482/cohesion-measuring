# Simulation test scenarios

This project contains sample microservices which correspond to following test scenarios:

- Scenario1: Two endpoints access completely different database tables, which should lead to the worst possible result
- Scenario2: Two endpoints access exactly the same database tables, which should lead to the best possible result
- Scenario3: Two endpoints access a common database table, but also another, which should lead to a medium cohesion value

## Run application

In the folder `test_data` there are some sample logs available for each scenario. If you want to use your own logs, you have to run the application and create them yourself. Otherwise, continue to the next chapter to find out how to calculate cohesion.

- Install dependencies for each microservice (scenario1, scenario2, scenario3, setup): Run `pip install -r requirements.txt` in each folder
- Run the application using: `docker compose up --build`
- Make some calls
- Open JaegerUI at `http://localhost:16686`
- Download results in JSON format for each microservice

## Calculate cohesion

Note, that the `cohesion_calculator` library has to be installed - currently only available locally. Follow instructions in `scom\readme.md` to use the library locally.

The file `scom_for_scenarios.py` contains some sample code to retrieve cohesion values as well as additional information like grouped logs and number of calls for each database table per url. Run with `python scom_for_scenarios.py`.

There is also a Jupyer Notebook `cohesion_scenarios.ipynb` available to play around with the logs and cohesion calculation.

### SCOM Results

#### Scenario1

Cohesion for Service scenario1: 0.0

Grouped logs for scenario1.json: {'scenario1/orders/': ['orders', 'products'], 'scenario1/employees/': ['customers', 'employees']}

Number of calls for scenario1.json: {'scenario1/orders/': {'orders': 1, 'products': 1}, 'scenario1/employees/': {'customers': 2, 'employees': 2}}

#### Scenario2

Cohesion for Service scenario2: 1.0

Grouped logs for scenario2.json: {'scenario2/employees/': ['customers', 'orders', 'products', 'employees'], 'scenario2/orders/': ['products', 'employees', 'customers', 'orders']}

Number of calls for scenario2.json: {'scenario2/employees/': {'customers': 1, 'orders': 1, 'products': 1, 'employees': 1}, 'scenario2/orders/': {'products': 1, 'employees': 1, 'customers': 1, 'orders': 1}}

#### Scenario3

Cohesion for Service scenario3: 0.5

Grouped logs for scenario3.json: {'scenario3/orders/': ['products', 'orders'], 'scenario3/employees/': ['customers', 'orders', 'employees']}

Number of calls for scenario3.json: {'scenario3/orders/': {'products': 1, 'orders': 1}, 'scenario3/employees/': {'customers': 1, 'orders': 1, 'employees': 1}}

### LSCC Cohesion

LSCC Cohesion for Service scenario1: 0.0

LSCC Cohesion for Service scenario2: 1.0

LSCC Cohesion for Service scenario3: 0.25
