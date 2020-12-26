import socket

s = socket.socket()
print("Socket created.")

s.bind(('192.168.0.114',9999))

s.listen(4)
print("Listening...")


while True: 
    c, addr = s.accept()
    print(f"Connected with {addr}")

    c.send(bytes("Hey you are connected to my server.",'utf-8'))
    c.close() 
#numpy.array_str(numpydata)