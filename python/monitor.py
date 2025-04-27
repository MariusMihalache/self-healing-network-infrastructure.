import subprocess
import time

def check_ping(host):
    response = subprocess.run(['ping', '-c', '4', host], stdout=subprocess.PIPE)
    return response.returncode == 0

def check_dns(dns_server):
    response = subprocess.run(['nslookup', dns_server], stdout=subprocess.PIPE)
    return response.returncode == 0

def check_gateway(gateway):
    return check_ping(gateway)

def monitor():
    gateway = "192.168.1.1"
    dns_server = "8.8.8.8"

    while True:
        if not check_gateway(gateway):
            print(f"Gateway {gateway} is down!")
        if not check_dns(dns_server):
            print(f"DNS {dns_server} is down!")
        
        time.sleep(60)  # Sleep for 60 seconds before checking again

if __name__ == "__main__":
    monitor()

