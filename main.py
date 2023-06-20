from flask import Flask, request, jsonify, json
import mysql.connector

url = "http://localhost:5000/candidate"

headers = {
    'Content-Type': 'application/json'
}

app = Flask(__name__)

# DB CONNECTION


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


# CANDIDATE
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

# VOTER
@app.route('/voter', methods=['GET', 'POST'])
def voters():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        cursor.execute("SELECT * FROM voter")
        voters = cursor.fetchall()
        if voters:
            return jsonify(voters), 200
        else:
            return "No voter found", 404

    if request.method == 'POST':
        voter_data = request.get_json()
    try:
        sql = "INSERT INTO voter (first_name, last_name, nic, email, gender, age, password, conform_password) VALUES (%(first_name)s, %(last_name)s, %(nic)s, %(email)s, %(gender)s, %(age)s, %(password)s, %(conform_password)s)"
        cursor.execute(sql, voter_data)
        conn.commit()
        return "Voter created successfully", 201
    except mysql.connector.Error as e:
        print(f"Error creating voter: {e}")
        return "Failed to create voter", 500


@app.route('/voter/<string:nic>', methods=['GET', 'PUT', 'DELETE'])
def single_voter(nic):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        try:
            cursor.execute(
                "SELECT * FROM voter WHERE nic = %(nic)s", {'nic': nic})
            voter = cursor.fetchone()
            if voter:
                return jsonify(voter), 200
            else:
                return "Voter not found", 404
        except mysql.connector.Error as e:
            print(f"Error creating voter: {e}")
            return "Failed to create voter", 500

    if request.method == 'PUT':
        voter_data = request.get_json()
        try:
            sql = "UPDATE voter SET first_name = %(first_name)s, last_name = %(last_name)s, nic = %(nic)s, email = %(email)s, gender = %(gender)s, age = %(age)s, password = %(password)s, conform_password = %(conform_password)s WHERE nic = %(nic)s"
            voter_data['nic'] = nic
            cursor.execute(sql, voter_data)
            conn.commit()
            return "Voter updated successfully", 200
        except mysql.connector.Error as e:
            print(f"Error creating voter: {e}")
            return "Failed to create voter", 500

    if request.method == 'DELETE':
        try:
            sql = "DELETE FROM voter WHERE nic = %(nic)s"
            cursor.execute(sql, {'nic': nic})
            conn.commit()
            return "Voter deleted successfully", 200
        except mysql.connector.Error as e:
            print(f"Error creating voter: {e}")
            return "Failed to create voter", 500

#QUOTA
@app.route('/quota', methods=['GET', 'POST'])
def quotas():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        cursor.execute("SELECT * FROM quota")
        quotas = cursor.fetchall()
        if quotas:
            return jsonify(quotas), 200
        else:
            return "No quota found", 404

    if request.method == 'POST':
        quota_data = request.get_json()
    try:
        sql = "INSERT INTO quota (quota_name,quota_reg_no,no_of_people,registerd_voters) VALUES (%(quota_name)s, %(quota_reg_no)s, %(no_of_people)s, %(registerd_voters)s)"
        cursor.execute(sql, quota_data)
        conn.commit()
        return "Quota created successfully", 201
    except mysql.connector.Error as e:
        print(f"Error creating quota: {e}")
        return "Failed to create quota", 500


@app.route('/quota/<string:quota_reg_no>', methods=['GET', 'PUT', 'DELETE'])
def single_quota(quota_reg_no):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        try:
            cursor.execute(
                "SELECT * FROM quota WHERE quota_reg_no = %(quota_reg_no)s", {'quota_reg_no': quota_reg_no})
            quota = cursor.fetchone()
            if quota:
                return jsonify(quota), 200
            else:
                return "Quota not found", 404
        except mysql.connector.Error as e:
            print(f"Error creating quota: {e}")
            return "Failed to create quota", 500

    if request.method == 'PUT':
        quota_data = request.get_json()
        try:
            sql = "UPDATE quota SET quota_name = %(quota_name)s, no_of_people = %(no_of_people)s, registerd_voters = %(registerd_voters)s WHERE quota_reg_no = %(quota_reg_no)s"
            quota_data['quota_reg_no'] = quota_reg_no
            cursor.execute(sql, quota_data)
            conn.commit()
            return "Voter updated successfully", 200
        except mysql.connector.Error as e:
            print(f"Error creating quota: {e}")
            return "Failed to create quota", 500

    if request.method == 'DELETE':
        try:
            sql = "DELETE FROM quota WHERE quota_reg_no = %(quota_reg_no)s"
            cursor.execute(sql, {'quota_reg_no': quota_reg_no})
            conn.commit()
            return "Quota deleted successfully", 200
        except mysql.connector.Error as e:
            print(f"Error creating quota: {e}")
            return "Failed to create quota", 500


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
