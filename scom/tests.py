
from scom.log import extract_table_names

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