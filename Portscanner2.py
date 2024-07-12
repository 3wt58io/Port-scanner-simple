import socket
import signal

def handler(signum, frame):
    raise TimeoutError("Timeout: Operation took too long")

signal.signal(signal.SIGALRM, handler)

# Generate ASCII art text
font = """
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓                              
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒                              
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░                              
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░                               
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░                               
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░                                 
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░                                  
░░       ░ ░ ░ ▒    ░░   ░   ░                                    
             ░ ░     ░                                            
                                                                  
  ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
      ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
         ░                                                        
"""

print(font)
print("***************************")
print("Made by Sai")
print("****************************")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter host here: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

def portscanner(port):
    try:
        signal.alarm(5)  # Set a timeout of 5 seconds for each port scan
        if s.connect_ex((host, port)) == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        signal.alarm(0)  # Cancel the alarm after successful port check
    except TimeoutError:
        print(f"Timeout: Could not scan port {port} in time")
    except Exception as e:
        print(f"Error occurred: {e}")

try:
    for port in range(start_port, end_port + 1):
        portscanner(port)
finally:
    s.close()
