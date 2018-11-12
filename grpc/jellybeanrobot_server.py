#!/usr/bin/env python

# For gRPC magic.
import grpc

# For threading for the server.
from concurrent import futures

# For making the server sleep.
import time

# Our generated files.
import jellybeanrobot_pb2
import jellybeanrobot_pb2_grpc


class Robot():
  """A cute little jellybean-loving robot"""

  def __init__(self, port=8080):
    self.port = port
    self.beans = 0  # How many jellybeans I have!


  def Give(self, request, context):
    """Implement someone giving the robot a jellybean."""
    beans = request.count
    if beans <= 0:
      message = "Fake beans :-("
    else:
      message = "Thank you for the %d new beans!" % beans
      self.beans += beans

    print message
    reply = {
      "message": message,
      "total": self.beans,
    }
    return jellybeanrobot_pb2.Reply(**reply)


  def Take(self, request, context):
    beans = request.count
    if beans <= 0:
      message = "You wanted no beans?"
    elif beans > self.beans:
      message = "I don't have that many beans :-("
    elif beans == self.beans:
      message = "My last bean :-("
      self.beans = 0
    else:
      message = "I am happy to give you %d of my beans!" % beans
      self.beans -= beans

    print message
    reply = {
      "message": message,
      "total": self.beans,
    }
    return jellybeanrobot_pb2.Reply(**reply)


    print "Hi!"


  def start_server(self):
    """Stwrt the gRPC server and listen for connections."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # The two services we added in the proto. You can find these functions in
    # jellybeanrobot_pb2_grpc.py.
    jellybeanrobot_pb2_grpc.add_JellyServicer_to_server(Robot(), server)

    # Start listening on a port.
    server.add_insecure_port("localhost:%d" % self.port)
    print "Listening on localhost:%d!\n" % self.port
    server.start()

    try:
      while True:
        time.sleep(3600) # one hour. 
    except KeyboardInterrupt:
      server.stop(0)

robot = Robot()
print "I'm a robot and I like jellybeans!"
robot.start_server()
