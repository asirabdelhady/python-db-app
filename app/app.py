from flask import Flask
import mysql.connector

app = Flask(__name__)

# MySQL Connection Configuration
db_config = {
    'host': '192.168.100.53',  # Replace with your MySQL host IP address or hostname
    'user': 'admin',  # Replace with your MySQL username
    'password': 'pass',  # Replace with your MySQL password
    'database': 'users'  # Replace with your MySQL database name
}

# Establish MySQL connection
cnx = mysql.connector.connect(**db_config)

@app.route('/')
def hello():
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()

    # Format the data into an HTML table
    table_html = '<table border="1"><tr><th>ID</th><th>Name</th><th>Email</th></tr>'
    for row in result:
        table_html += '<tr>'
        table_html += ''.join(f'<td>{str(col)}</td>' for col in row)
        table_html += '</tr>'
    table_html += '</table>'

    return table_html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
