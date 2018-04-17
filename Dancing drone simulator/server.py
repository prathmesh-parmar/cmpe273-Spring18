import time
import grpc
import sys
import drone_pb2
import drone_pb2_grpc
import queue
from concurrent import futures

client_1 = queue.Queue()
client_2 = queue.Queue()
client_id = 1
x,y,z = 0,0,0
class DroneServer(drone_pb2_grpc.droneServicer):
    def newCoordinates(self,request,context):
        global client_id
        if client_id == 2:
            yield drone_pb2.Response(_x = -200,_y=-200,_z=-200)
            while 1:
                if not client_2.empty():
                    yield drone_pb2.Response(_x = int(client_2.get()), _y =int(y), _z = int(z))
        
        elif client_id == 1:
            yield drone_pb2.Response(_x = -100,_y=-100,_z=-100)
            client_id = client_id + 1
            while 1:
                if not client_1.empty():
                    yield drone_pb2.Response(_x = int(client_1.get()), _y = int(y), _z = int(z))
        
def get():
    global x,y,z
    i = input("Enter the New coordinate[x,y,z] >")
    x, y, z = i.split(",")

def run(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    drone_pb2_grpc.add_droneServicer_to_server(DroneServer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        firstCoordinate = sys.argv[1]
        secondCoordinate = sys.argv[2]
        x1 , y1, z1  = firstCoordinate.split(",")
        x2 , y2, z2  = secondCoordinate.split(",")
        print("Server started at...%d" % port)
        while True:
            get()
            client_1.put(int(x))
            client_2.put(int(x2) + int(x) - int(x1))
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run('0.0.0.0', 3000)
