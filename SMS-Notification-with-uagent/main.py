from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import requests

class Message(Model):
    message: str

temperature_agent = Agent(
    name="temperature_agent",
    port=8000,
    seed="temperature_secret_phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(temperature_agent.wallet.address())

# Define the temperature readings for the selected location
selected_location = input("Enter the city you want to put in surveillance: ")

# Define the user's desired temperature range
desired_min_temp = int(input("Enter your desired minimum temperature: "))
desired_max_temp = int(input("Enter your desired maximum temperature: "))

url = f'https://api.openweathermap.org/data/2.5/weather?q={selected_location}&appid="INSERT_YOUR_API_KEY_HERE"'

try:
    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print relevant weather information
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15  # Convert to Celsius

    else:
        print(f"Request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")

current_temperature = temperature_celsius

def monitor_temperature():
    if current_temperature < desired_min_temp:
        return (f"Temperature in {selected_location} is below the desired minimum ({desired_min_temp}°C).")
    elif current_temperature > desired_max_temp:
        return (f"Temperature in {selected_location} is above the desired maximum ({desired_max_temp}°C).")
    else:
        return (f"Temperature in {selected_location} is within the desired range ({desired_min_temp}-{desired_max_temp}°C).")

async def notify_user(message):
    servicePlanId = "INSERT_YOUR_SERVICE_PLAN_ID_HERE"
    apiToken = "INSERT_YOUR_API_TOKEN_HERE"
    sinchNumber = "INSERT_YOUR_SINCH_NUMBER_HERE_WITH_COUNTRY_CODE"
    toNumber = "INSERT_USERS_NUMBER_HERE_WITH_COUNTRY_CODE"
    url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

    payload = {
    "from": sinchNumber,
    "to": [
        toNumber
    ],
    "body": message
    }
    headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + apiToken
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

@temperature_agent.on_interval(period=3600.0)  # Check every hour
async def temperature_monitor(ctx: Context):
    temperature_status = monitor_temperature()
    ctx.logger.info(temperature_status)
    if "below" in temperature_status or "above" in temperature_status:
        await notify_user(temperature_status)

if __name__ == "__main__":
    temperature_agent.run()
