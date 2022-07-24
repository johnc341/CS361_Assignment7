#
#   Game client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Fight" to server, expects back a JSON of the randomly selected enemy
#

import zmq

def gameclient():

    while True:
        context = zmq.Context()

        user_input = input("What would you like to do? ")

        if user_input == "Fight":

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
    
        else:
            print("unknown option")
            return False

gameclient()