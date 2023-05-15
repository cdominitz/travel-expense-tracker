import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


while True:
    task = int(input("Enter 1 for get link, 2 for add link, 3 for edit link\n"))
    row = input("enter: subject, outcome, link(if applicable)\n")
    user_input = str(task) + ', ' + row
    socket.send_string(user_input)
    message = socket.recv_string()
    print(message)

    #  Do some 'work'
    time.sleep(1)

