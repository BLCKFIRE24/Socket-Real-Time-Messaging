import socketserver
import socket
import logging
import sys


class MyTCPHandler(socketserver.StreamRequestHandler):

       def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        #send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9000

    #create the server and bind it to port 9000
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
    #server will run forever. Ctrl-C to quit server
        server.serve_forever()

        HOST, PORT = "127.0.0.1", 9000
        data = " ".join(sys.argv[1:])

        #create socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect((HOST, PORT))
            s.sendall(bytes(data + "\n", "utf-8"))

            #shutdown server after data is received
            received = str(s.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
