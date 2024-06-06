import os
import psycopg2
from flask import Flask, request, render_template

app = Flask(__name__)

# Use environment variables to configure the database connection
DATABASE_URL = (
    f"dbname='{os.getenv('DB_NAME')}' "
    f"user='{os.getenv('DB_USER')}' "
    f"password='{os.getenv('DB_PASSWORD')}' "
    f"host='{os.getenv('DB_HOST')}'"
)

# Establish a connection to the database
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# SQL command to create a table named "users" in the "test" schema
create_table_sql = """
CREATE TABLE IF NOT EXISTS test.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255)
);
"""

# Execute the SQL command to create the table
cur.execute(create_table_sql)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    cur.execute("INSERT INTO test.users (username, email) VALUES (%s, %s)", (username, email))
    conn.commit()
    return "Submitted!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
