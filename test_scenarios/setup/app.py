from flask import Flask
import psycopg2

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor

app = Flask(__name__)

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
Psycopg2Instrumentor().instrument(enable_commenter=True, commenter_options={})

db_params = {
    'dbname': 'scenariodb',  
    'user': 'postgres',
    'password': 'postgres',
    'host': 'scenario_db', 
    'port': '5432'      
}

@app.route('/setup/init')
def init():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        price NUMERIC(10, 2) NOT NULL,
        stock INT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        position VARCHAR(100) NOT NULL,
        start_date DATE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS customers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        date_of_birth DATE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        customer_id INT NOT NULL,
        product_id INT NOT NULL,
        timestamp TIMESTAMP NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (product_id) REFERENCES products(id)
    );
    '''

    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

    products_sample_data = [
        ('Elegant Oak Table', 'A beautifully crafted oak table.', 150.99, 20),
        ('Modern Leather Sofa', 'A comfortable and stylish leather sofa.', 899.99, 10),
        ('Rustic Bookshelf', 'A rustic bookshelf made from reclaimed wood.', 120.49, 15),
        ('Vintage Armchair', 'A cozy vintage armchair with a modern twist.', 350.75, 5),
        ('Glass Coffee Table', 'A sleek glass coffee table with metal legs.', 180.20, 25),
        ('Ergonomic Office Chair', 'An ergonomic chair for comfortable working.', 220.00, 30),
        ('Classic Wooden Bedframe', 'A classic wooden bedframe with a sturdy design.', 450.50, 8),
        ('Marble Dining Table', 'A luxurious marble dining table for elegant meals.', 1200.00, 2),
        ('Industrial TV Stand', 'A modern TV stand with an industrial look.', 299.99, 12),
        ('Outdoor Patio Set', 'A complete patio set for outdoor relaxation.', 750.99, 7)
    ]

    employees_sample_data = [
        ('Alice Johnson', 'Software Engineer', '2020-05-14'),
        ('Bob Smith', 'Project Manager', '2018-03-22'),
        ('Carol White', 'UX Designer', '2019-07-01'),
        ('David Brown', 'Data Scientist', '2021-01-15'),
        ('Eva Green', 'Marketing Specialist', '2017-11-05'),
        ('Frank Wilson', 'Sales Manager', '2016-09-30'),
        ('Grace Lee', 'HR Manager', '2022-02-28'),
        ('Henry Adams', 'DevOps Engineer', '2020-08-20'),
        ('Ivy Baker', 'Content Writer', '2019-04-25'),
        ('Jack Turner', 'Customer Support', '2021-06-10')
    ]

    customers_sample_data = [
        ('John Doe', 'john.doe@example.com', '1985-02-15'),
        ('Jane Smith', 'jane.smith@example.com', '1990-06-25'),
        ('Robert Johnson', 'robert.johnson@example.com', '1978-11-30'),
        ('Emily Davis', 'emily.davis@example.com', '1983-05-22'),
        ('Michael Brown', 'michael.brown@example.com', '1995-08-14'),
        ('Sarah Wilson', 'sarah.wilson@example.com', '1987-12-03'),
        ('David Taylor', 'david.taylor@example.com', '1975-03-18'),
        ('Laura Moore', 'laura.moore@example.com', '1992-09-10'),
        ('James Anderson', 'james.anderson@example.com', '1989-01-29'),
        ('Emma Thomas', 'emma.thomas@example.com', '1981-07-19')
    ]

    orders_sample_data = [
        (1, 2, '2023-05-15 14:30:00'),
        (2, 4, '2023-05-16 09:20:00'),
        (3, 1, '2023-05-17 17:45:00'),
        (4, 3, '2023-05-18 11:10:00'),
        (5, 5, '2023-05-19 13:50:00'),
        (6, 2, '2023-05-20 16:30:00'),
        (7, 1, '2023-05-21 10:05:00'),
        (8, 4, '2023-05-22 15:20:00'),
        (9, 3, '2023-05-23 12:40:00'),
        (10, 5, '2023-05-24 08:55:00')
    ]

    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    
    # Create the products table
    cursor.execute(create_table_query)
    
    # Insert sample data
    for item in products_sample_data:
        cursor.execute('''INSERT INTO products (name, description, price, stock) VALUES (%s, %s, %s, %s)''', item)

    for item in employees_sample_data:
        cursor.execute('''INSERT INTO employees (name, position, start_date) VALUES (%s, %s, %s)''', item)

    for item in customers_sample_data:
        cursor.execute('''INSERT INTO customers (name, email, date_of_birth) VALUES (%s, %s, %s)''', item)

    for item in orders_sample_data:
        cursor.execute('''INSERT INTO orders (customer_id, product_id, timestamp) VALUES (%s, %s, %s)''', item)

    # Committing the transaction
    conn.commit()

    # Closing the cursor and connection
    cursor.close()
    conn.close()

    return "done!"

@app.route('/setup/')
def hello():
    return "Hello World from setup!"