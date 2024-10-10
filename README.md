# Weather Forecast API Documentation

## Purpose of the API

The purpose of this API is to provide weather information for any specified city by interacting with the [OpenWeatherMap](www.openweathermap.org) API to fetch real-time weather data. This weather forecasting API is built using Flask as the backend and serves current weather information, including temperature, humidity, wind speed, and weather description.

### Key Features:

* Retrieves current weather information for a city.
* Provides weather details such as temperature, humidity, wind speed, and a weather description.
* Implements error handling to return appropriate messages when a city is not found or if the city parameter is missing.
* Built using Flask (a lightweight Python web framework) to handle requests and responses.
* Simple, responsive frontend for user interaction.


## Installation and Setup

### Prerequisites

Ensure you have installed:
+ Python 3.x

### 1. Clone the Repository
First, clone the repository to your local machine and navigate to it:

    git clone <repository_url>
    cd <repository_directory>


***OR*** 

### Download the files from Github
Copy the downloaded files to a directory on your local machine

### 2. Create a Virtual Environment (Optional but recommended)
It's a good practice to create a virtual environment to isolate the dependencies. To do this, Open **Command Prompt** on your machine and  navigate to the cloned repository or the directory on your local machine where you copied the downloaded files.

*Run the following commands:*

**On Windows:**

    python -m venv venv

    venv\Scripts\activate

**On macOS/Linux:**

    python3 -m venv venv

    source venv/bin/activate

This step ensures that the dependencies are isolated from your global Python environment

### 3. Install Dependencies
Once your virtual environment is activated, install the required Python dependencies:
    
    pip install -r requirements.txt

Note: You can install the necessary dependencies manually also:

    pip install Flask requests flask-cors


### 4. Run the API 
To start the Flask server, inside the activated virtual environment use the following command:

    python api.py

`Once the server is running, the API will be available at http://127.0.0.1:5000.`

Open your browser and enter the below url in the address bar;
    
    http://localhost:5000/api/weather?city=London
    
    OR
    
    http://127.0.0.1:5000/api/weather?city=London

This will provide the weather data for London in JSON format i.e in the format shown below:

    {
    "city": "London",
    "description": "few clouds",
    "humidity": 71,
    "temperature": 10.49,
    "wind_speed": 4.12
    }

Open another **Command Prompt** Window and activate the virtual environment by navigating to the directory and running the command:

    venv\Scripts\activate

Once activated run the following command:

    python server.py

This will start serving the index.html `(frontend)` file at http://127.0.0.1:5001. 

### 5. Using the Frontend
To check weather information for any city, first, ensure the API server is running (see step 4). 
After that open your web browser and type in the URL below: 

    http://localhost:5001

or directly open the ***index.html*** file from the directory.

`Enter a city name in the input field.
Click the "Get Weather" button to retrieve the weather forecast.
The frontend will send a request to the running API and display the weather data including temperature, humidity, wind speed, and description.`


## API Endpoints

| HTTP Method | Endpoint      | Parameters        | Description                         |
|-------------|---------------|-------------------|-------------------------------------|
| GET         | /api/weather  | city=<city_name>  | Fetches the weather data for the city |

## Additional Notes

- Ensure that the API server is running before using the frontend or making API requests.
- The API provides weather data in JSON format.
- Use the frontend (`index.html`) for a user-friendly interface to interact with the API.
- The API depends on external services to fetch weather information, so ensure an active internet connection.






