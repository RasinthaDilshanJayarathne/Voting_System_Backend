from werkzeug.utils import redirect
import mysql.connector

conn = mysql.connector.connect(
  host="electionvoting.cx7qj2rz3vn4.us-east-2.rds.amazonaws.com",
  user="Admin",
  password="Admin1234",
  database="election_voting"
)

mycursor = conn.cursor()
# mycursor.execute("DROP TABLE IF EXISTS candidate")
# mycursor.execute("CREATE TABLE candidate (first_name VARCHAR(255), last_name VARCHAR(255), nic VARCHAR(64) PRIMARY KEY, email VARCHAR(255), gender VARCHAR(12), age int, election_party VARCHAR(255), vote_no int, password VARCHAR(255), conform_password VARCHAR(255))")
# mycursor.execute("DROP TABLE IF EXISTS voter")
# mycursor.execute("CREATE TABLE voter (first_name VARCHAR(255), last_name VARCHAR(255), nic VARCHAR(64) PRIMARY KEY, email VARCHAR(255), gender VARCHAR(12), age int, password VARCHAR(255), conform_password VARCHAR(255))")
# mycursor.execute("DROP TABLE IF EXISTS quota")
# mycursor.execute("CREATE TABLE quota (quota_name VARCHAR(255), quota_reg_no VARCHAR(64) PRIMARY KEY, no_of_people int, registerd_voters int)")
# mycursor.execute("CREATE TABLE students (id int(11) PRIMARY KEY, name varchar(255), email varchar(255), phone varchar(255))")
