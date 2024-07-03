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

@app.route('/scenario3/employees')
def get_employees():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    cursor.execute("SELECT * FROM orders")
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    table = create_table(colnames, employees)
    return table

@app.route('/scenario3/orders')
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

@app.route('/scenario3/')
def hello():
    return "Hello World from szenario3!"