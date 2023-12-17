import ipaddress

def are_networks_in_same_subnet(network1, network2):
    network1 = ipaddress.IPv4Network(network1, strict=False)
    network2 = ipaddress.IPv4Network(network2, strict=False)

    return network1.overlaps(network2)

# Пример использования
subnet1 = "10.0.0.255/32"
subnet2 = "10.0.0.5/8"

if are_networks_in_same_subnet(subnet1, subnet2):
    print(f"Сети {subnet1} и {subnet2} находятся в одной подсети.")
else:
    print(f"Сети {subnet1} и {subnet2} НЕ находятся в одной подсети.")
