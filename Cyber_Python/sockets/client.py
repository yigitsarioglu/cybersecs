# Socket Programming
# Client file

import socket

# host ve port değerleri verildi
host = "127.0.0.1"
port = 50002

# AF.INET IP4 bağlantı yapmak istediğimizi belirtir, 
#Sock_stream ise tcp bağlantıyı belirtir
client_socket = socket.socket( socket.AF_INET ,socket.SOCK_STREAM) # socket nesnesi oluşturuyoruz

client_socket.connect((host,port))   # tuple olarak değer veriliyor

message = input(">> ")



while message.lower().strip() != "quit":

    if (message !="") :
        #Gönderilecek mesaj byte arrray olmalıdır, bu yüzden mesaj encode edip gönderilir
        client_socket.send(message.encode() )

        # receive edilen mesaj byte array olarak alınıyor sonra string haline decode ediliyor
        data = client_socket.recv(1024).decode()
        print ("Response from server : " + str(data) )

    elif message == "" :
        print("Please write valid command!")
    
    message = input(">> ")


client_socket.close()