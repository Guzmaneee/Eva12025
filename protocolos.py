
# Distancias administrativas por defecto
OSPF = 110
RIP = 120
EIGRP = 90
BGP = 20

protocolo = input("Ingrese el nombre del protocolo (OSPF, RIP, EIGRP o BGP): ").upper()


if protocolo == "OSPF":
    print(f"El protocolo {protocolo} tiene una distancia administrativa de {OSPF}.")
elif protocolo == "RIP":
    print(f"El protocolo {protocolo} tiene una distancia administrativa de {RIP}.")
elif protocolo == "EIGRP":
    print(f"El protocolo {protocolo} tiene una distancia administrativa de {EIGRP}.")
elif protocolo == "BGP":
    print(f"El protocolo {protocolo} tiene una distancia administrativa de {BGP}.")
else:
    print("Protocolo no reconocido. Intente con OSPF, RIP, EIGRP o BGP.")