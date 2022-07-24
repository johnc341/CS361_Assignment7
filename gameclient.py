#
#   Game client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Fight" to server, expects back a JSON of the randomly selected enemy
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to combatserver…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Request a fight
print("Sending request for a fight")
socket.send_string("Fight")

#  Get the reply.
message = socket.recv()
print("Received reply [ %s ]" % (message))