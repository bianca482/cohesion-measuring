# Simulation test scenarios

This project contains sample microservices which correspond to following test scenarios:

- **Scenario1**: Two endpoints access completely different database tables, which should lead to the worst possible result
- **Scenario2**: Two endpoints access exactly the same database tables, which should lead to the best possible result
- **Scenario3**: Two endpoints access a common database table, but also another, which should lead to a medium cohesion value

## Run application

In the folder `test_data` there are some sample logs available for each scenario. If you want to use your own logs, you have to run the application and create them yourself. Otherwise, continue to the next chapter to find out how to calculate cohesion.

- Install dependencies for each microservice (scenario1, scenario2, scenario3, setup): Run `pip install -r requirements.txt` in each folder
- Run the application using: `docker compose up --build`
- Make some calls (e.g. `{port}/{scenario}/employees` and `{port}/{scenario}/orders`)
- Open JaegerUI at `http://localhost:16686`
- Download results in JSON format for each microservice

## Calculate cohesion

Note, that the `cohesion_calculator` library has to be installed. It is currently only available locally. Follow instructions in `scom\readme.md` to use the library locally.

The file `scom_for_scenarios.py` contains some sample code to retrieve cohesion values as well as additional information like grouped logs and number of calls for each database table per url. Run with `python scom_for_scenarios.py`.

### SCOM Results

- **Scenario1**: Cohesion for Service scenario1: 0.0
- **Scenario2**: Cohesion for Service scenario2: 1.0
- **Scenario3**: Cohesion for Service scenario3: 0.5
