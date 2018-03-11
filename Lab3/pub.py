import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
pub = context.socket(zmq.PUB)
pull = context.socket(zmq.PULL)
pull.bind("tcp://127.0.0.1:5680")

pub.bind("tcp://127.0.0.1:5681")

while True:
    time.sleep(1)
    data=pull.recv_string()
    data_1 = data.split(",")
    print(data_1)
    pub.send_string(data)
    print("sent")
