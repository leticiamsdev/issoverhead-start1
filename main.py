import time

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.
def function():
    if iss_latitude+5 <= MY_LAT <= iss_latitude-5:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hours_now = time_now.hour

#If the ISS is close to my current position

# and it is currently dark
while True:
    time.sleep(60)
    if  function() and sunset <= hours_now <= sunrise:
        my_email = "leticiatestesmtp@gmail.com"
        password = PASSWORD
        connection = smtplib.SMTP("smtp.gmail.com", 587)  # connection with server
        connection.starttls()  # proteger os dados
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="leticiamari2004@yahoo.com", msg="Look for sky")
        connection.close()

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



