import time
import requests
from datetime import datetime
import smtplib

# My Info
curr_latitude = 40.728226
curr_longitude = -73.794853
my_email = "tszhim_test1@gmail.com"
my_password = "1234"


# Checking if ISS is overhead.
def iss_overhead():
  
    # Retrieving ISS information.
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    # Narrowing data down to ISS coordinates.
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Returns true if ISS overhead, otherwise, false.
    return abs(iss_latitude - curr_latitude) <= 5 and abs(iss_longitude - curr_longitude) <= 5


# Checking if the light levels outside are dark enough to see ISS.
def dark_sky():
    parameters = {
        "lat": curr_latitude,
        "lng": curr_longitude,
        "formatted": 0,
    }

    # Retrieving sunrise and sunset information of current coordinates.
    sun_api_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_api_response.raise_for_status()
    sun_data = sun_api_response.json()

    # Narrowing data down to sunrise and sunset hours.
    sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.now().hour

    # Returns true if dark enough, otherwise, false.
    return current_hour >= sunset_hour or current_hour <= sunrise_hour


# If both conditions are met, send email to self that ISS is directly above and is visible.
while True:
    if iss_overhead() and dark_sky():

        # Establishing connection to email.
        email_connection = smtplib.SMTP("smtp.gmail.com")
        email_connection.starttls()
        email_connection.login(my_email, my_password)

        # Constructing email and sending.
        email_connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: Python ISS Script:\n The ISS is in the sky directly above, and is visible."
        )

        # Allowing main thread to sleep as to reduce resource consumption.
        time.sleep(60)
