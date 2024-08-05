Microservice A Weather Data Communication Contract

This microservice utilizes ZeroMQ to request and receive data. 

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

  reply = socket.recv_pyobj()
  return reply

# Example usage
weather_data = request_weather_data()
print(weather_data)
```

<h1>Complete Example</h1>
The request_weather_data() function will request and return a JSON object containing weather data for a user provided location. When called, the user will be prompted to enter a location like this:

```
Enter city name: 
```
Upon receipt of valid input, and provided the microservice is running and listening on the specified endpoint, the function will then return a JSON object which can be printed in whole, or parsed further within 
the main program depending on end user specifications. 



<h1>UML Diagram</h1>
![image](https://github.com/user-attachments/assets/09fb00fa-49b3-46e0-9cd7-ec54abff5796)

