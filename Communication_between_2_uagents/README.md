# Temperature Monitoring Agent Notifying Another Agent 🌡️📢

This repository contains a Temperature Monitoring Agent that monitors the temperature in a selected location and notifies another agent, Bob, remotely when the temperature changes. The project demonstrates remote agent communication and was developed using the [uAgents](https://github.com/fetchai/uAgents) framework.

## Getting Started 🚀

To use the Temperature Monitoring Agent to notify Bob when the temperature changes, follow these steps:

### Step 1: Set Up the Environment

1. Install the required dependencies by running the following command:

```shell
 pip install uagents requests
```

### Step 2: Configure the Agents

- **Configure the Temperature Monitoring Agent:**

    - **Define the temperature readings for the selected location.**
    - **Define your desired minimum and maximum temperature range.**
- **Configure the Bob Agent (not shown in this code snippet):**
  - **Ensure that Bob is running and accessible remotely.**

### Step 3: Run the Agents 🏃

- **Run the Temperature Monitoring Agent:**

  ```shell
  python temperature_agent.py
  python agent-bob.py
  ```
-**Ensure that Bob is running and ready to receive notifications.**

### Step 4: Monitoring and Notification

- **The Temperature Monitoring Agent will periodically check the temperature in the selected location.**

- **If the temperature falls below or rises above your desired range, the agent will notify Bob remotely.**

- **Bob will receive the temperature change notification and can take appropriate actions.**

### Example Usage

Here's an example of how to use the Temperature Monitoring Agent to notify Bob when the temperature changes:

- **Run the Temperature Monitoring Agent as described above.**
- **Ensure that Bob's agent is running and ready to receive notifications.**
- **Enter the city name you want to monitor (e.g., "London").**
- **Enter your desired minimum temperature (e.g., 15°C).**
- **Enter your desired maximum temperature (e.g., 25°C).**
- **The agent will periodically check the temperature, and Bob will be notified remotely if the temperature falls below or rises above your desired range.**

Now you can monitor temperature changes and notify other agents remotely with ease!

Enjoy temperature monitoring and agent communication! 🌡️📢

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
