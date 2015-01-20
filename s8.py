import socket
import sys
try:
    import thread
except ImportError:
    import _thread as thread

def clientthread(conn):
    #your code here ...
    while 1:

        #print('connection with ' + addr[0] + ':' +  str(addr[1]))
        data = conn.recv(1024)
        if not data:
            break
        data2 = str(data)
        #data2 = data2[2:len(data2)-5]
        reply = '<Hello ' + data2 + ' >'
        conn.sendall(reply.encode("UTF-8"))

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

except socket.error as msg:
    print("failed to create socket")
    print('Error code: ' + str(msg[0]) + ' , Error message: ' + msg[1])
    sys.exit()

print("socket created.")
host = ''
port = 8887

try:
    s.bind((host,port))
except socket.error as msg:
    print ('Bind failed. error code: ' + str(msg[0]) + ', message: ' + str(msg[1]))
    sys.exit()
print('Socket bind is complete')
s.listen(2)
print('port is now listening')

while 1:

    conn, addr = s.accept()
    thread.start_new_thread(clientthread,(conn,))

conn.close()
s.close()

