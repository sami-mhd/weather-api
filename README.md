# Weather Forecast API Documentation

## Team Collaboration Overview
In our recent work on the project, we’ve all contributed to different aspects, making progress together.

### 221086-Sami / Github sami-mhd

    On the feature-api-development branch, I created the api.py file, which contains the main logic for our weather API, including the endpoints that connect to the OpenWeatherMap service. I also put together the complete documentation to ensure that everything is well-explained and easy to understand for anyone working on the project.

### 221060-Huzaifa / Github Uzaifa123

    Over on the feature-test branch, Huzaifa worked on the index.html file, which serves as the main user interface. He also focused on writing unit tests to ensure everything is functioning as expected. These tests are crucial for catching any issues early and maintaining code quality.

### 221094-Zulkha / Github zulkha-tariq

    On the feature-server branch, Zulkha developed the server.py application, which handles our server setup. She also updated the index.html file to make the frontend more elegant and user-friendly, enhancing the overall experience for our users.

Our collaboration has led to a solid foundation for the project, with a well-functioning API, thorough testing, an attractive interface, and comprehensive documentation. 




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

Once the server is running, the API will be available at http://127.0.0.1:5000.

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

<br>
<br>

# Explanation of the Weather API Code

The code includes two Flask applications. The first one sets up a weather API that retrieves data from the OpenWeatherMap service, while the second one is a basic Flask app that serves an HTML template.

## First Flask Application (Weather API - [api.py])
### Imports

***Flask:***  *This is the core of the web application framework. It provides the tools needed to create the app.*

***jsonify:*** *This function converts Python dictionaries into JSON format, which is what APIs typically return.*

***request:*** *This allows the app to access incoming request data, such as query parameters.*

***requests:*** *A library used to make HTTP requests to external APIs.*

***CORS:*** *This module enables Cross-Origin Resource Sharing, which allows your API to be accessed from other domains.*

### Application Setup

    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes

Here, a new Flask application is created. CORS is enabled for all routes, meaning that requests from different origins (like a frontend app hosted elsewhere, in this case the server is at `localhost:5000` and the frontend i-e index.html is at `localhost:5001`) can access this API.

### Constants

    API_KEY = 'SECRET_API_KEY' 
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

These are constants that store the API key and the base URL for making requests to the OpenWeatherMap API.

### API Route

    @app.route('/api/weather', methods=['GET'])

This line defines a new route for the application. When a GET request is made to /api/weather, the get_weather function will handle it.

### Fetching the City Parameter

    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400

This section retrieves the city name from the query parameters of the request. If the city is not provided, it returns a `400 error` with a message indicating that the city is required.

### Constructing the API Request

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

Here, the code builds the URL for the OpenWeatherMap API using the city name and the API key. It then sends a GET request to this URL to fetch the weather data.

### Handling the Response

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data['name'],
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed'],
        }
        return jsonify(weather_info), 200
    else:
        return jsonify({"error": "City not found"}), 404

If the request to the weather API is successful `(indicated by a 200 status code)`, it processes the JSON response and extracts relevant weather details like the city `name`, `temperature`, `weather` `description`, `humidity`, and `wind speed`. This information is then returned as a JSON response. If the city is not found, it returns a `404 error`.

### Running the Application

    if __name__ == '__main__':
        app.run(port=5000, debug=True)

This line starts the Flask application on port 5000. The `debug=True` option enables debug mode, which provides helpful error messages and automatic reloading during development.

## Second Flask Application (HTML Template)

### Imports

Similar to the first app, it `imports Flask` and `render_template`, which is used to render HTML files.

### Application Setup

    app = Flask(__name__)

A new Flask application instance is created.

### Home Route

    @app.route('/')
    def index():
        return render_template('index.html')

This defines a route for the root URL (/). When someone accesses this URL, the index function is called, which renders an HTML template called index.html.

### Running the Application

    if __name__ == '__main__':
        app.run(port=5001, debug=True)

This starts the second Flask application on port 5001, also in debug mode.


## Additional Notes

- Ensure that the API server is running before using the frontend or making API requests.
- The API provides weather data in JSON format.
- Use the frontend (`index.html`) for a user-friendly interface to interact with the API.
- The API depends on external services to fetch weather information, so ensure an active internet connection.






