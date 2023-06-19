from flask import Flask, request, jsonify, json
import mysql.connector

url = "http://localhost:5000/candidate"

headers = {
    'Content-Type': 'application/json'
}

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="electionvoting.cx7qj2rz3vn4.us-east-2.rds.amazonaws.com",
            user="Admin",
            password="Admin1234",
            database="election_voting"
        )
        if conn.is_connected():
            print("Connected to the database")
    except mysql.connector.Error as e:
        print(e)
    return conn


@app.route('/candidate', methods=['GET', 'POST'])
def candidates():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        cursor.execute("SELECT * FROM candidate")
        candidates = cursor.fetchall()
        if candidates:
            return jsonify(candidates), 200
        else:
            return "No candidates found", 404

    if request.method == 'POST':
        candidate_data = request.get_json()
    try:
        sql = "INSERT INTO candidate (first_name, last_name, nic, email, gender, age, election_party, vote_no, password, conform_password) VALUES (%(first_name)s, %(last_name)s, %(nic)s, %(email)s, %(gender)s, %(age)s, %(election_party)s, %(vote_no)s, %(password)s, %(conform_password)s)"
        cursor.execute(sql, candidate_data)
        conn.commit()
        return "Candidate created successfully", 201
    except mysql.connector.Error as e:
        print(f"Error creating candidate: {e}")
        return "Failed to create candidate", 500


@app.route('/candidate/<string:nic>', methods=['GET', 'PUT', 'DELETE'])
def single_candidate(nic):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        try:
            cursor.execute(
                "SELECT * FROM candidate WHERE nic = %(nic)s", {'nic': nic})
            candidate = cursor.fetchone()
            if candidate:
                return jsonify(candidate), 200
            else:
                return "Candidate not found", 404
        except mysql.connector.Error as e:
            print(f"Error creating candidate: {e}")
            return "Failed to create candidate", 500


    if request.method == 'PUT':
        candidate_data = request.get_json()

        try:
            sql = "UPDATE candidate SET first_name = %(first_name)s, last_name = %(last_name)s, nic = %(nic)s, email = %(email)s, gender = %(gender)s, age = %(age)s, election_party = %(election_party)s, vote_no = %(vote_no)s, password = %(password)s, conform_password = %(conform_password)s WHERE nic = %(nic)s"
            candidate_data['nic'] = nic
            cursor.execute(sql, candidate_data)
            conn.commit()
            return "Candidate updated successfully", 200
        except mysql.connector.Error as e:
            print(f"Error creating candidate: {e}")
            return "Failed to create candidate", 500

    if request.method == 'DELETE':
        try:
            sql = "DELETE FROM candidate WHERE nic = %(nic)s"
            cursor.execute(sql, {'nic': nic})
            conn.commit()
            return "Candidate deleted successfully", 200
        except mysql.connector.Error as e:
            print(f"Error creating candidate: {e}")
            return "Failed to create candidate", 500


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
