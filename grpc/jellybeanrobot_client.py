#!/usr/bin/env python

# For gRPC magic.
import grpc

# Our generated files.
import jellybeanrobot_pb2
import jellybeanrobot_pb2_grpc


channel = grpc.insecure_channel("localhost:8080")
stub = jellybeanrobot_pb2_grpc.JellyStub(channel)

# Two jellybeans to send to the robot with a friendly message.
jellybeans = jellybeanrobot_pb2.Jellybeans(
    count=2, message="For you, robot friend!")

# Send them.
response = stub.Give(jellybeans)

# What did the robot tell us?
print "The robot said '%s'. It has %d jellybeans." % (response.message, response.total)


# A request for a jellybean!
jellybeans = jellybeanrobot_pb2.Jellybeans(
    count=1, message="May I have a jellybean?")

# Take them.
response = stub.Take(jellybeans)

# What did the robot tell us?
print "The robot said '%s'. It has %d jellybeans." % (response.message, response.total)

