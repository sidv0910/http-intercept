import pyshark
import socket

# ip address of the vulnerable website
ip_address = socket.gethostbyname("testhtml5.vulnweb.com")

# port on which the vulnerable website is running
tcp_port = "80"

http_filter = "http and tcp.port == {port} and ip.addr == {ip}".format(port = tcp_port, ip = ip_address)

output_file = "C:/Users/Administrator/Desktop/output-file.txt"
