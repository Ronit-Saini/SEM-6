import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = socket.gethostname()
udp_port = 9994
msg = 'hi'
s.sendto(msg.encode(),(udp_host,udp_port))
tm = s.recvfrom(1024)
print(' Current time from Sever :', tm.decode())
s.close()