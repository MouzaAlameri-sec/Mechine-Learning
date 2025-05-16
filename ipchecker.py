
__Author__ = "Mouza Alameri"
__Date__ = "16/05/2025"

def log_event(user, ip="192.168.1.1"):
    print(f"Logging: {user} accessed from IP {ip}")
    
    if ip != "192.168.1.1":
        print(f" Suspicious IP detected: {ip}")
    else:
        print(f" IP {ip} is from the internal network.")


username = input("Username: ")
ipaddy = input("IP Address (press enter for default): ")

if ipaddy.strip() == "":
    log_event(username)
else:
    log_event(username, ipaddy)

