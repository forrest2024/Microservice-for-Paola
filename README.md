<h1>Microservice A Weather Data Communication Contract</h1>

This microservice utilizes ZeroMQ to request and receive data. The connection is set to tcp://localhost:5555 so be sure to keep that port open or change the port and IP as needed in the source code. The microservice queries the OpenWeatherMap API using a privately generated API key from my personal OpenWeatherMap API account. Please keep API calls to under 100,000 per day in order to avoid incurring cost. Please reference the UML diagram below for specifics on how the microservice interacts with the API. I am using the zmq and requests libs to 

<h1> How to programatically request and receive data: </h1>

1. First, install ZeroMQ: 
```
pip install zmq
```
Utilize the following code within your main program to request weather data from the API and connect to the microservice, and to receive a response from the microservice. 

```python
import zmq

def request_weather_data():
  # Establish communication pipeline
  context = zmq.Context()
  socket = context.socket(zmq.REQ)
  socket.connect("tcp://localhost:5555")

  # Get user input for location and send string to microservice
  data = input("Enter city name: ")
  socket.send_string(data)

  # Receive JSON object from microservice and return object to calling procedure/variable.
  reply = socket.recv_pyobj()
  return reply

# Example usage
weather_data = request_weather_data()
print(weather_data)
```

<h1>Usage Example</h1>
The request_weather_data() function will request and return a JSON object containing weather data for a user provided location. When called, the user will be prompted to enter a location like this:

```
Enter city name: 
```
Upon receipt of valid input, and provided the microservice is running and listening on the specified endpoint, the function will then return a JSON object which can be printed in whole, or parsed further within 
the main program depending on end user specifications. 

Example output of the JSON object from the use of request_weather_data() above:
```
{'coord': {'lon': -122.6762, 'lat': 45.5234}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 81.37, 'feels_like': 81.5, 'temp_min': 77.58, 'temp_max': 83.98, 'pressure': 1015, 'humidity': 45, 'sea_level': 1015, 'grnd_level': 1005}, 'visibility': 10000, 'wind': {'speed': 3, 'deg': 315, 'gust': 5.01}, 'clouds': {'all': 0}, 'dt': 1722887412, 'sys': {'type': 2, 'id': 2005350, 'country': 'US', 'sunrise': 1722862798, 'sunset': 1722915198}, 'timezone': -25200, 'id': 5746545, 'name': 'Portland', 'cod': 200}
```
Once this JSON object is returned to the main program, it can be manipulated and displayed however the end user desires. 


<h1>UML Diagram</h1>
![image](https://github.com/user-attachments/assets/09fb00fa-49b3-46e0-9cd7-ec54abff5796)

