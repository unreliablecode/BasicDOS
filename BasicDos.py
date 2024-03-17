import requests
from threading import Thread

def send_request(ip_address): 
    response = requests.get(f'http://{ip_address}/')
    if response.status_code == 200:
        print("Request successful:", response.text[:100] + '...')  
    else:
        print(f"Request failed. Status code: {response.status_code}")

if __name__ == "__main__":
    ip_address = input("Enter the target IP address: ")
    num_requests = int(input("How many requests would you like to send? "))

    threads = []
    for _ in range(num_requests):
        thread = Thread(target=send_request, args=(ip_address,)) 
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
