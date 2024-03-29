Deploy a sample 2-tier application on Cloud
I planned to create a simple API. It is useful for gardeners and plant lovers, they will get to know the basic and most recent information about plants. 

First, I created mysql database in AWS RDS Dashboard and I connected the mysql in my system
mysql -h awsmysqlendpoint -u username -p

Then, I create the api code in flask

import pymysql
from flask import Flask, jsonify, request
host = "awsendpoint"
user = ""
password = ""
database = "GreenHouse"
port = 3306
connection = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
cursor = connection.cursor()
app = Flask(__name__)

@app.route('/add', methods=[ 'POST'])
def add():
    try:
        _json = request.json
        _plantname = _json[ 'plantname']
        _plantdescription = _json[ 'plantdescription']
        _plantpriceinrs = _json[ 'plantpriceinrs']
        sqlQuery = "INSERT INTO Plants(PlantName, PlantDescription, PlantPriceInRs) VALUES(%s, %s, %s)"
        bindData = (_plantname, _plantdescription, _plantpriceinrs)
        cursor.execute(sqlQuery, bindData)
        #cursor.execute("insert into login (name password) values (kishori, Sridhar055)")
        connection.commit()
        response = jsonify({ 'response' : 'plant details added successfully!'})
        response.status_code = 200
        #cursor.close()
        #connection.close()
        return response
    except Exception as e:
        print(e)
    
@app.route('/update', methods =[ 'PUT'])
def update():
    try:
        _json = request.json
        _plantname = _json[ 'plantname']
        _plantdescription = _json[ 'plantdescription']
        _plantpriceinrs = _json[ 'plantpriceinrs']
        sqlQuery = "update Plants set PlantPriceInRs=%s, PlantDescription=%s where PlantName=%s"
        bindData = (_plantpriceinrs, _plantdescription, _plantname)
        cursor.execute(sqlQuery, bindData)
        connection.commit()
        response = jsonify({ 'response' : 'plant details updated successfully!'})
        response.status_code = 200
        #cursor.close()
        #connection.close()
        return response
    except Exception as e:
        print(e)

@app.route('/get', methods=['GET'])
def get():
    try:
      _json = request.json
      _plantname = _json[ 'plantname']
      #plant price
      #plant description
      sqlQuery = "select * from Plants where PlantName=%s"
      bindData = (_plantname, )
      cursor.execute(sqlQuery, bindData)
      connection.commit()
      ret = cursor.fetchall()
      response = jsonify({'plantname' : ret[0][0], 'plantdescription': ret[0][1], 'plantpriceinrs' : ret[0][2]})
      return response
    except Exception as e:
        print(e)

@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        _json = request.json
        _plantname = _json[ 'plantname']
        sqlQuery = "delete from Plants where PlantName=%s"
        bindData = ( _plantname)
        cursor.execute(sqlQuery, bindData)
        connection.commit()
        response = jsonify({'response' : 'plant details deleted successfully'})
        return response
    except Exception as e:
        print(e)

@app.route('/')
def home():
    return "Hello World"

if __name__ =="__main__":
    app.run(debug=True,port=8000)

After that, I created an EC2 instance in AWS. And copied my api code using scp command and stored it on my EC2 instance. Then I created a service and ran the api code in my instance.
[Unit]
Description=My API Service

[Service]
WorkingDirectory=/home/ubuntu
User=ubuntu
ExecStart=/usr/bin/python3 /home/ubuntu/api.py

[Install]
WantedBy=multi-user.target


And I Install the caddy server in my EC2 instance. And do the reverse proxy if the request is come from the 80 port it is forward the request to port 8000 in the EC2 instance.

:80 {
        reverse_proxy localhost:8000
}

This is the database I connected to my api. Then, I test the API in curl.

First I tested the GET method in curl

curl -X GET -H 'Content-type: application/json' -d '{"plantname" : "Rose"}' htttp://13.51.106.9/get

Then I tested the POST method in curl

curl -X POST -H 'Content-type: application/json' -d '{"plantname" : "Daisy", "plantdescription" : "sunny springtime blooms", "plantpriceinrs" : "70"}' htttp://13.51.106.9/add

Then I tested the PUT method in curl

curl -X PUT -H 'Content-type: application/json' -d '{"plantname" : "Daisy", "plantdescription" : "blooms", "plantpriceinrs" : "80"}' htttp://13.51.106.9/update

Then I tested the DELETE method in curl

curl -X DELETE -H 'Content-type: application/json' -d '{"plantname" : "Daisy"}' htttp://13.51.106.9/delete



