import requests
import sys
from bs4 import BeautifulSoup

username = sys.argv[1]
password = sys.argv[2]
plate = sys.argv[3]

url_login = "http://localhost:3000/login"
url_park = "http://localhost:3000/park"

#Login
s = requests.Session()
logged_in_page = s.post(url_login,data={"username":username,"password":password})
#Grab parking place ID:s
soup = BeautifulSoup(logged_in_page.text, 'html.parser')
locations = soup.select("select[name='location'] option")

for location in locations:
    response = s.post(url_park,data={"licensePlate":plate,"mintime":"0","location":location.get("id")})
    if "This car is already parked in the selected location. Do not waste your money !" in response.text:
        print(f"Car: {plate} is parked at {location.text}")

