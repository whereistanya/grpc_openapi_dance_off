pip install grpcio grpcio-tools

1. Make a proto.
jellybeanrobot.proto

2. Generate stubs. 
$ python -m grpc_tools.protoc --proto_path=. ./jellybeanrobot.proto --python_out=. --grpc_python_out=.

It created jellybeanrobot_pb2.py and jellybeanrobot_pb2_grpc.py. These are valid
python you can read but shouldn't edit.

3. Make a server.

jellybeanrobot_server.py.

Most of it is boilerplate, but we'll need to implement Give and Take from the
proto. It runs on a port and listens for jellybean requests.

4. Make a client.

jellybeanrobot_client.py. It runs on the commandline and calls 'Give' and 'Take'
to talk to the robot server.


Mistakes I made
- I did python -m jellybeanrobot.protoc; it's supposed to be the python module,
  grpc_tools.protoc
- I left off the --gprc_python_out=. and it didn't generate
  jellybeanrobot_pb2_grpc.py
