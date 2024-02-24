from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def test_postgres_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="",
            host="webapp-postgres",  # Assuming PostgreSQL container is running with this name
            port="5432"
        )
        conn.close()
        return "Connected successfully"
    except Exception as e:
        return f"Connection failed: {str(e)}"

@app.route('/')
def index():
    return 'Flask App is running!'

@app.route('/api/connection-status')
def test_connection():
    status = test_postgres_connection()
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
