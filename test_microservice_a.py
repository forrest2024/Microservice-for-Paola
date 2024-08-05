import zmq

def request_weather_data():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    data = input("Enter city name: ")
    socket.send_string(data)

    reply = socket.recv_pyobj()
    return reply

weather_data = request_weather_data()
print(weather_data)

