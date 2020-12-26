import socket

s = socket.socket()
print("Socket created.")

s.bind(('https://git.heroku.com/server-socket-io-simple.git',80))

s.listen(4)
print("Listening...")


while True: 
    c, addr = s.accept()
    print(f"Connected with {addr}")

    c.send(bytes("Hey you are connected to my server.",'utf-8'))
    c.close() 
