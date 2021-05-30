import requests
from twilio.rest import Client

# My information
api_key = "3663abd9b2e5bdcf0adc34e4c1bfa8e1"
my_latitude = 40.728226
my_longitude = -73.794853
twilio_sid = "not included for privacy"
auth_token = "not included for privacy"

# Handling open weather map API request.
weather_status = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=" + str(my_latitude) +
                                  "&lon=" + str(my_longitude) + "&appid=" + api_key)
weather_status.raise_for_status()
if not 200 <= weather_status.status_code < 300:
    raise ConnectionError("Request failed.")

# Retrieving data.
weather_status_data = weather_status.json()

# Manipulating data to narrow it down precipitation status of next 48 hours.
weather_twelve_hr = weather_status_data["hourly"][:12]

# Storing precipitation status.
thunderstorm = False
drizzle = False
rain = False
snow = False
clear = False
cloudy = False

for hour in weather_twelve_hr:
    weather_code = int(hour["weather"][0]["id"])

    if 200 <= weather_code <= 232:
        thunderstorm = True
    elif 300 <= weather_code <= 321:
        drizzle = True
    elif 500 <= weather_code <= 531:
        rain = True
    elif 600 <= weather_code <= 622:
        snow = True
    elif weather_code == 800:
        clear = True
    elif 800 <= weather_code <= 804:
        cloudy = True

# Constructing SMS message.
if thunderstorm or drizzle or rain or snow or clear or cloudy:
    sms_msg = ""

    if thunderstorm:
        sms_msg = sms_msg + "It will be stormy. ⛈"
    if drizzle:
        sms_msg = sms_msg + "It will be slightly rainy. ☂"
    if rain:
        sms_msg = sms_msg + "It will be very rainy. ☂"
    if snow:
        sms_msg = sms_msg + "It will be snowy. ❄"
    if clear:
        sms_msg = sms_msg + "It will be clear. ☀"
    if cloudy:
        sms_msg = sms_msg + "It will be cloudy. 🌥"

    # Sending message.
    client = Client(twilio_sid, auth_token)
    message = client.messages.create(
        body=sms_msg,
        from_="not included for privacy",
        to="not included for privacy"
    )
    print(message.status)
