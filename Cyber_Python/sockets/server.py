# Socket Programming
# Server file
import socket
import subprocess

host = "127.0.0.1"
port = 50002

server_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM ) # socket nesnesi oluşturuldu

server_socket.bind((host,port))  # nesneyi bind ediyoruz, bağlıyoruz
server_socket.listen()

conn , addr = server_socket.accept()   # connection nesnesi ve adress nesnesi
# adress nesnesi hangi ipden ve porttan bağlandığını gösterir
# connection nesnesi bağlantı olup olmadığını gösterir

print ( "Connected from " + str(addr))

while True :

    #CALISMA 1
    #data = conn.recv(1024).decode()
    #print (data)
    #response_data = "Mesajınız Alındı..."
    #conn.send (response_data.encode())


    #CALISMA 2
    data = conn.recv(1024).decode()
    print (data)
    result = subprocess.run(data, stdout=subprocess.PIPE , shell=True)
    response_data = result.stdout    # stdout da byte array şeklindedir, gönderirken encode edilmesi gerekmez

    if (result.stdout.decode() != "" ):
        response_data = result.stdout
    else:
        response_data =("Command Executed").encode()    


    conn.send (response_data)


conn.close()
