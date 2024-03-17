import socket
import random
import string
from threading import Thread

def generate_random_string(length=10):
    """Generates a random string of the specified length."""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def send_tcp(ip_address, port):
    """Sends a random string over TCP."""
    random_string = generate_random_string()
    data = random_string.encode()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        s.sendall(data)
        print(f"TCP: Sent random string: {random_string}")

def send_udp(ip_address, port):
    """Sends a random string over UDP."""
    random_string = generate_random_string()
    data = random_string.encode()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(data, (ip_address, port))
        print(f"UDP: Sent random string: {random_string}")

if __name__ == "__main__":
    ip_address = input("Enter the target IP address: ")
    port = int(input("Enter the port number: "))
    protocol = input("Select protocol (TCP/UDP): ").upper()
    num_requests = int(input("How many requests would you like to send? "))

    if protocol == "TCP":
        send_func = send_tcp
    elif protocol == "UDP":
        send_func = send_udp
    else:
        print("Invalid protocol. Please choose TCP or UDP.")
        exit()

    threads = []
    for _ in range(num_requests):
        thread = Thread(target=send_func, args=(ip_address, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
