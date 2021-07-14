import requests
import webbrowser
import time
from playsound import playsound
import json
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database='cowin')
mycursor = mydb.cursor()

url='https://selfregistration.cowin.gov.in/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

print('press 1 for pin \n')
print('press 2 for district')
choice=input('Enter your choice: ')

def findAvailabilitybypin(pin):
    counter = 0

    pincode=pin
    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode,date)
    result = requests.get(URL, headers=header)
    response_json_pin = result.json()

    data = response_json_pin["sessions"]


    for each in data:
        if((each["available_capacity_dose{}".format(dose)] > 0) &(each["vaccine"]=="{}".format(vaccine.upper())) & (each['min_age_limit']==int(age))):
            counter += 1
            print('center name: ',each["name"])
            print('Address: ',each['address'])
            print('Fees: ',each['fee'])
            print('Min Age: ',each['min_age_limit'])
            print('Pincode: ',each["pincode"])
            print('Vaccine: ',each["vaccine"])
            print('Available Capacity: ',each["available_capacity"])
            playsound('/...../..../audio_file.mp3')
            chrome_path=".....//.....//chrome.exe  %s --incognito"
            webbrowser.get(chrome_path).open_new(url)

            return True
    if(counter == 0):
        print("No Available Slots right now")
        return False

''' by district  '''

def findAvailabilitybydist(id_dist):
    counter = 0
    j=id_dist
    URL_single = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(j,date)
    result = requests.get(URL_single, headers=header)

    response_json_dist = result.json()

    data = response_json_dist["sessions"]


    for each in data:
        if((each["available_capacity_dose{}".format(dose)] > 0) &(each["vaccine"]=="{}".format(vaccine.upper()))& (each['min_age_limit']==int(age))):
            counter += 1
            print('center name: ',each["name"])
            print('Address: ',each['address'])
            print('Fees: ',each['fee'])
            print('Min Age: ',each['min_age_limit'])
            print('Pincode: ',each["pincode"])
            print('Vaccine: ',each["vaccine"])
            print('Available Capacity: ',each["available_capacity"])
            playsound('...../..../audio_file.mp3')
            chrome_path="....//....//chrome.exe  %s --incognito"
            webbrowser.get(chrome_path).open_new(url)

            return True
    if(counter == 0):
        print("No Available Slots right now")
        return False

'''  Main code '''
if int(choice)==1:
    pin=input('Enter pin: ')
    vaccine=input('Which vaccine: ')
    dose=input('Which dose? ')
    date=input('enter date: ')
    age=input('Age limit 18 or 45: ')

    while(findAvailabilitybypin(pin) != True):
        time.sleep(5)
        findAvailabilitybypin(pin)

elif int(choice)==2:
    state=input('enter state: ')
    vaccine=input('Which vaccine: ')
    dose=input('Which dose? ')
    date=input('enter date: ')
    age=input('Age limit 18 or 45: ')
    sql = "SELECT state_id FROM state_name WHERE name = %s"
    adr = (state,)
    mycursor.execute(sql,adr)
    myresult = mycursor.fetchone()
    dist_id=myresult[0]
    url_dist = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}'.format(dist_id)
    result_dist = requests.get(url_dist, headers=header)
    dist_json = result_dist.json()
    for a,b in dist_json.items():
        try:
            for i in b:
                print(i['district_name'],' id= ',i['district_id'])
        except:
            continue
    id_dist=input('Enter district_id from above list: ')
    while(findAvailabilitybydist(id_dist) != True):
        time.sleep(5)
        findAvailabilitybydist(id_dist)

else:
    print('wrong input')
