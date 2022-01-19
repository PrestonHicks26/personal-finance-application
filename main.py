import zmq
import PersonalFinance as pf
import threading

def dateListener():
    context = zmq.Context()
    sock = context.socket(zmq.PAIR)
    sock.connect("tcp://127.0.0.1:1234")
    message = sock.recv()
    if message == '':
        pass
    if message == '':
        pass

global pf
pf = pf.Finance()
t = threading.Thread(target=dateListener())
t.start()





