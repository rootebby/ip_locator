import socket
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(f"""
My IP Address is : {ip}
""")