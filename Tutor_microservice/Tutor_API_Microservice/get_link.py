import zmq
import db_imp as db

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    msg = socket.recv_string()
    info = [str(val) for val in msg.split(', ')]
    task = int(info[0])
    del info[0]
    message = ""

    if task == 1:
        message = db.get_link(info)

    elif task == 2:
        message = db.add_link(info)

    elif task == 3:
        message = db.edit_link(info)

    elif task == 4:
        db.deleteAll()

    socket.send_string(str(message))
