Microservice A Weather Data Communication Contract

This microservice utilizes ZeroMQ to request and receive data. 

How to programatically request and receive data: 

1. First, install ZeroMQ: 
```
pip install zmq
```
Utilize the following code within your main program to request weather data from the API and connect to the microservice, and to receive a response from the microservice. 

```
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

UML Diagram
![image](https://github.com/user-attachments/assets/09fb00fa-49b3-46e0-9cd7-ec54abff5796)

