import requests
import datetime

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

#print(data)

rate = data["rates"]["INR"]
timestamp = datetime.datetime.now().strftime("%d %b %Y, %I:%M %p")

print("USD to INR Rate: ", rate)
print("Fetched at: ", timestamp)