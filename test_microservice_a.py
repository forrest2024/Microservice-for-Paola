import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

data = input("Enter city name: ")
socket.send_string(data)

reply = socket.recv_pyobj()
print(reply)