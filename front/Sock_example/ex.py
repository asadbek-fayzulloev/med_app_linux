import socket
target_host = "192.168.43.196" 
 
target_port = 9998  # create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
 
# connect the client 
client.connect((target_host,target_port))  
 
# send some data 
request = "OK"
client.send(request.encode())  
 
# receive some data 
response = client.recv(4096)  
http_response = repr(response)
http_response_len = len(http_response)
 
#display the response
print(http_response)