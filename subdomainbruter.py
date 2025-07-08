import socket
import argparse

def resolve_subdomains(domain, wordlist):
    with open(wordlist, 'r') as f:
        prefixes = [line.strip() for line in f if line.strip()]

    print(f"[*] Resolving subdomains for: {domain}")
    for prefix in prefixes:
        subdomain = f"{prefix}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            print(f"[+] {subdomain} resolves to {ip}")
        except socket.gaierror:
            pass  # Silently skip unresolved domains

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Resolver")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g. example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file with subdomain prefixes")

    args = parser.parse_args()
    resolve_subdomains(args.domain, args.wordlist)
