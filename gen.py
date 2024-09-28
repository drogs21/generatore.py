## GENERATORE DI IP ##
## CODE bY kOrOIRC@koro.eu
## CAMBIA LINEA 24 - 25
## FILE SALVATI SU ips.txt

def ip_to_int(ip):
    """Converte un indirizzo IP in un numero intero."""
    parts = list(map(int, ip.split('.')))
    return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

def int_to_ip(ip_int):
    """Converte un numero intero in un indirizzo IP."""
    return f"{(ip_int >> 24) & 255}.{(ip_int >> 16) & 255}.{(ip_int >> 8) & 255}.{ip_int & 255}"

def generate_ips(start_ip, end_ip, filename):
    """Genera una lista di IP dall'indirizzo start_ip a end_ip e li scrive in un file."""
    start = ip_to_int(start_ip)
    end = ip_to_int(end_ip)
    
    with open(filename, 'w') as file:
        for ip_int in range(start, end + 1):
            file.write(int_to_ip(ip_int) + '\n')

# Imposta l'intervallo di IP e il nome del file
start_ip = "1.1.1.1"  # Cambia questo con l'indirizzo IP di inizio
end_ip = "20.255.255.255"  # Cambia questo con l'indirizzo IP di fine
output_file = "ips.txt"

# Genera gli IP e scrivili nel file
generate_ips(start_ip, end_ip, output_file)
print(f"IP da {start_ip} a {end_ip} salvati nel file {output_file}")
