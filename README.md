# Setup:

Copy the microservice file combatserver.py to your project folder. Install the ZeroMQ library by running 
"pip3 install pyzmq" in your terminal.

To use the microservice, run combatserver.py in a terminal, then run your project in a separate terminal.
Your project should connect to the microservice via TCP port 5555. The file gameclient.py shows a sample
implementation of the connection in Lines 22 and 23.

# How to Request Data:

Your project should send the string "Fight" to combatserver.py via the TCP connection. Line 27 of
gameclient.py shows a sample implementation of how to send the string "Fight" through the port.

# How to Receive Data:

Your project should receive a string from combatserver.py via the TCP connection. The string has the following
format:

{"enemy": "Goblin", "damage": 1, "gold": 4}

Line 30 of gameclient.py shows a sample implementation of how to receive the string from the port. 
Line 32 of gameclient.py shows how the received string can be converted to dictionary format for use in your
project.