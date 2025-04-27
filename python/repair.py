import subprocess

def reset_gateway():
    print("Resetting gateway...")
    subprocess.run(["systemctl", "restart", "network.service"])

def reset_dns():
    print("Resetting DNS...")
    subprocess.run(["systemctl", "restart", "systemd-resolved"])

def change_dns():
    print("Changing DNS server to fallback...")
    subprocess.run(["nmcli", "dev", "modify", "eth0", "ipv4.dns", "8.8.8.8"])

def reconfigure_routing():
    print("Reconfiguring routing...")
    subprocess.run(["ip", "route", "add", "default", "via", "192.168.1.1"])

if __name__ == "__main__":
    reset_gateway()
    reset_dns()
    change_dns()
    reconfigure_routing()

