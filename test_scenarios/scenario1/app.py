from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
from datetime import datetime

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

def create_table(colnames, values): 
    table = '<table border="1"><tr>'
    for colname in colnames:
        table += f'<th>{colname}</th>'
    table += '</tr>'

    for value in values:
        table += '<tr>'
        for item in value:
            table += f'<td>{item}</td>'
        table += '</tr>'
    table += '</table>'
    return table

@app.route('/scenario1/employees')
def get_employees():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    cursor.execute("SELECT * FROM customers")
    cursor.execute("SELECT * FROM employees")
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    table = create_table(colnames, employees)
    return table


@app.route('/scenario1/employees/insert', methods=["POST"])
def insert_employee(): 
    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'position', 'start_date']):
        return jsonify({'error': 'Invalid input'}), 400
    
    startDate = ""
    try:
        startDate = datetime.strptime(data["start_date"], '%d.%m.%Y')
    except ValueError:
        return jsonify({'error': 'Invalid date format, should be DD.MM.YYYY'}), 400

    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    insert_query = '''INSERT INTO employees (name, position, start_date) VALUES (%s, %s, %s)'''
    cursor.execute(insert_query, (data["name"], data["position"], startDate))
    conn.commit()
    cursor.close()
    conn.close()

    return "Employee created"

@app.route('/scenario1/employees/delete', methods=["POST"])
def delete_employee(): 
    id = request.args.get("id")

    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    delete_query = '''DELETE FROM employees WHERE (id=%s)'''
    cursor.execute(delete_query, id)
    conn.commit()
    cursor.close()
    conn.close()

    return "Employee deleted"

@app.route('/scenario1/employees/updatePosition', methods=["POST"])
def update_employee(): 
    data = request.get_json()

    if not data or not all(key in data for key in ['id', 'position']):
        return jsonify({'error': 'Invalid input'}), 400

    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    update_query = '''UPDATE employees SET position = %s WHERE id = %s'''
    
    cursor.execute(update_query, (data["position"], data["id"]))
    conn.commit()
    cursor.close()
    conn.close()

    return "Employee updated"

@app.route('/scenario1/orders')
def get_orders():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    table = create_table(colnames, orders)
    return table

@app.route('/scenario1/')
def hello():
    return "Hello World from szenario1!"