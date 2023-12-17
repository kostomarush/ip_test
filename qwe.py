import ipaddress
import json
from random import randint, choice

def generate_ip_pairs(num_pairs):
    ip_pairs = []

    for _ in range(num_pairs):
        pair = []
        for _ in range(5):
            ip1 = generate_random_ip()
            ip2 = generate_random_ip()
            pair.append({"ip1": ip1, "ip2": ip2})
        
        ip_pairs.append(pair)

    return ip_pairs

def generate_random_ip():
    ip = ipaddress.IPv4Address(randint(0, 2**32 - 1))
    subnet_mask = choice([16, 20, 24, 25, 30])
    return f"{ip}/{subnet_mask}"

def generate_algorithm():
    algorithm = {"ip_pairs": generate_ip_pairs(10)}
    return algorithm

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    generated_algorithm = generate_algorithm()
    save_to_json(generated_algorithm, "generated_algorithm.json")
