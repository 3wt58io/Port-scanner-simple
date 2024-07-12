import socket
from art import *
import signal
def handler(signum, frame):
  raise TimeoutError("ranout of time")
signal.signal(signal.SIGALRM, handler)
signal.alarm(2)
# Generate ASCII art text
maintext = text2art("Port scanner")
print(maintext)
print("***************************")
print("Made by Sai")
print("****************************")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter host here:  ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))
port = 0
def portscanner(port):
  try:
   if s.connect_ex((host, port)):
     print(f"Port is closed port number: {port}")
   else:
     print(f"Port is open port number: {port}")
  except TimeoutError:
    print("couldnt scan port in time!")
for port in range(start_port, end_port + 1):
  signal.alarm(5)
  portscanner(port)
s.close()
