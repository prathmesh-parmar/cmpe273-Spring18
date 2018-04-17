import grpc
import drone_pb2_grpc
from drone_pb2 import Empty, Response

class DroneClient():
    def __init__(self, host='0.0.0.0', port=3000):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = drone_pb2_grpc.droneStub(self.channel)

    def newCoordinates(self):
        req = Empty()
        for resp in self.stub.newCoordinates(req):
            if(resp._x == -200):
                print("Client ID [2] connected to server")
            elif (resp._x == -100):
                print("Client ID [1] connected to server")
            else:
                print("[received] moving to [{},{},{}]".format(resp._x,resp._y,resp._z))
            

def test():
    client = DroneClient()
    client.newCoordinates()
        
if __name__ == '__main__':
    test()
