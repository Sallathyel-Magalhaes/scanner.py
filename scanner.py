import requests
import socket

def check_headers(url):
    """Verifica cabeçalhos de segurança do site"""
    try:
        response = requests.get(url)
        headers = response.headers
        security_headers = [
            "Content-Security-Policy", "Strict-Transport-Security", "X-Frame-Options",
            "X-XSS-Protection", "X-Content-Type-Options", "Referrer-Policy"
        ]
        
        print("\n[+] Verificando cabeçalhos de segurança:")
        for header in security_headers:
            if header in headers:
                print(f"✔ {header}: {headers[header]}")
            else:
                print(f"❌ {header} não encontrado!")
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")

def scan_ports(host, ports=[80, 443, 21, 22, 25, 3306]):
    """Verifica se portas críticas estão abertas"""
    print("\n[+] Escaneando portas abertas:")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"⚠ Porta {port} aberta!")
        else:
            print(f"✔ Porta {port} fechada.")
        sock.close()

if __name__ == "__main__":
    target_url = input("Digite a URL do site (ex: https://exemplo.com): ")
    domain = target_url.replace("https://", "").replace("http://", "").split('/')[0]
    
    check_headers(target_url)
    scan_ports(domain)
