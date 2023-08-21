# Pipeline to connect microservice to app

import zmq
from New_Travel_Expenses_Proj import currencyConverter as curr

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5550")

while True:
    msg = socket.recv_string()
    info = [str(val) for val in msg.split(', ')]

    message = curr.convert(info)
    socket.send_string(str(message))
