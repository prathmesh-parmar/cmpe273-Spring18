import zmq
import threading
import sys
import time

# ZeroMQ Context
context = zmq.Context()
poller = zmq.Poller()

# Define the socket using the "Context"
sub = context.socket(zmq.SUB)
push = context.socket(zmq.PUSH)

# Define subscription and messages with prefix to accept.
sub.setsockopt_string(zmq.SUBSCRIBE, "")
sub.connect("tcp://127.0.0.1:5681")

push.connect("tcp://127.0.0.1:5680")

class messageDisplay(threading.Thread):
    def __init__(self):
      threading.Thread.__init__(self)
    
    def run(self):
        while(True):
            data=str(sub.recv())
            data = data.split(',')
            name = str(data[0])
            message = str(data[1])
            name = name[2:]
            i = len(message)
            message = message[:(i-1)]
            print ("[" + name+"]"+" "+ message)
            time.sleep(1)
thread=messageDisplay()
thread.start()

name=sys.argv[1]

while (True):
    message=input("["+name+"]>")
    full_message = name +"," +message
    push.send_string(full_message)
