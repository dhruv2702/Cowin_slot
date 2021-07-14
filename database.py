import json
import requests
import webbrowser
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database='cowin'
)
mycursor = mydb.cursor()
mycursor.execute('DROP TABLE IF EXISTS state_name')

mycursor.execute("CREATE TABLE state_name (name VARCHAR(255), state_id int(10) )")
url='https://selfregistration.cowin.gov.in/'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
URL = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'
result = requests.get(URL, headers=header)
state_json = result.json()
lst=[]
id=1

for a,b in state_json.items():
    try:
        for i in b:
            value=i['state_name']
            query="INSERT INTO state_name (name,state_id) VALUES (%s,%s)"
            mycursor.execute(query,(value,id))
            id=id+1

    except:
        continue
mydb.commit()
