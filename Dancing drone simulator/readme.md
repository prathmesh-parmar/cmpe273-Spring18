# About the application
Built a drone dancing simulator in Python using GRPC as a communication protocol.

The simulator has two components:
 - Server
 - Client
 
 ## Server
 
 The server is the main orchestrator to guide directions for all drone in the network. The role of server are:
 - Drone/client membership
 - Getting user inputs for the whole drone cluster movement and sending new coordinate to each drone.
 
 To start the server with a x-axis distance between each drone:
 > python3 server.py {start_coordinate} {peer_distance}
 
 ``
 python3 server.py 0,0,0 10,0,0
 ``
 
 Server log and waits for user input:
 
 ``
 Server started at 3000.
 ``
 
 ``
 Enter New Coordinate[x, y, z] > 
 ``
 
 ## Membership
 When a drone joins to the server, the server will response an unique client/drone id and a coordinate to be moved.
 
 > python3 client.py {server_port}
 
 ``
 python3 client.py 3000
 ``
 
 Client log:
 
 ## First Drone Log
 ``
 Client id [xxxx] connected to the server.
 ``
 
 ``
 [received] moving to [0, 0, 0]
 ``
 ## Second Drone Log
 
 ``
 Client id [xxxx] connected to the server.
 ``
 
 ``
 [received] moving to [10, 0, 0]
 ``
 

## Steps for running the application
1. Clone the repository.
2. Run the proto file using the following command:

  ``
  python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. ping.proto 
  ``
