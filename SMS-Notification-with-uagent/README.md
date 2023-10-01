# Temperature Monitoring Agent with SMS Notification 🌡️📲

This repository contains a Temperature Monitoring Agent that checks the temperature in a selected location and sends a text message notification to the user if the temperature falls below or rises above the user's desired temperature range. This project was developed for the [Fetch.ai Hackathon](https://lu.ma/fetchai-hackathon) organized by [Fetch.ai](https://fetch.ai/).

## Getting Started 🚀

To use the Temperature Monitoring Agent with SMS notification, follow these steps:

### Step 1: Obtain API Keys 🔑

Before running the agent, you need to obtain the required API keys:

- **OpenWeatherMap API Key:** Get an API key from OpenWeatherMap by signing up at [OpenWeatherMap API](https://openweathermap.org/api).

- **Sinch SMS API Key:** Sign up for an account on [Sinch](https://www.sinch.com/). After logging in, navigate to the "API" section to create an API token. Ensure you have a Sinch number to send SMS notifications from.

### Step 2: Set Environment Variables 🌐

Create a `.env` file in the project directory and export the obtained API keys as environment variables:

```shell
export OPENWEATHERMAP_API_KEY="YOUR_OPENWEATHERMAP_API_KEY"
export SINCH_API_TOKEN="YOUR_SINCH_API_TOKEN"
```

### Step 3: Install Dependencies ⚙️

To use the environment variables from the .env file and install the project dependencies, run the following commands:

```shell
source .env
poetry install
```

### Step 4: Run the Agent 🏃

To run the Temperature Monitoring Agent:

```shell 
python main.py
```

- **Enter the city you want to monitor for temperature.**
- **Enter your desired minimum and maximum temperatures.**
- **Now, the agent will periodically check the temperature in the selected location and send you a text message notification if it falls below or rises above your desired temperature range.**

### Example Usage

Here's an example of how to use the Temperature Monitoring Agent:

- **Run the agent using the provided instructions.**
- **Enter the city name you want to monitor (e.g., "London").**
- **Enter your desired minimum temperature (e.g., 15°C).**
- **Enter your desired maximum temperature (e.g., 25°C).**
- **The agent will periodically check the temperature in the selected city.**
- **If the temperature falls below or rises above your desired range, you will receive a text message notification.**

Now you can stay informed about temperature changes in your selected location!

Enjoy monitoring temperatures with SMS notifications! 🌡️📲

## Video Explanation 🎥

For a more detailed overview and step-by-step walkthrough of the projects included in this repository, watch our video explanation below:

Youtube Link: https://youtu.be/SKqWiv3K6IM

Gdrive Link: https://drive.google.com/file/d/1GOmE0o4lgdCpiaaAMgimHn6XrsCokBrJ/view?usp=sharing

## Licence

Copyright (c) 2023 Raj Bhatt

 Permission is hereby granted, free of charge, to any person obtaining 
 a copy of this software and associated documentation files (the 
 "Software"), to deal in the Software without restriction, including 
 without limitation the rights to use, copy, modify, merge, publish, 
 distribute, sublicense, and/or sell copies of the Software, and to 
 permit persons to whom the Software is furnished to do so, subject to 
 the following conditions: 
  
 The above copyright notice and this permission notice shall be 
 included in all copies or substantial portions of the Software. 
  
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
 LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
 WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
