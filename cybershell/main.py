import shlex

from cybershell.tools import (
    run_ping,
    run_nmap_basic,
    run_whois,
    run_dig,
    run_traceroute,
    run_curl_headers,
    run_nc_connect,
)

def show_help():
    print("""
CyberShell EDU commands:

  ping <host>
  nmap-basic <host>
  whois <domain_or_ip>
  dig <domain>
  traceroute <host>
  curl-headers <url>
  nc-connect <host> <port>
  help
  exit

Safety:
  Only test systems you own or have explicit permission to test.
""")

def main():
    print(r"""
       ______      __              _____ __         ____     __________  __  __
      / ____/_  __/ /_  ___  _____/ ___// /_  ___  / / /    / ____/ __ \/ / / /
     / /   / / / / __ \/ _ \/ ___/\__ \/ __ \/ _ \/ / /    / __/ / / / / / / 
    / /___/ /_/ / /_/ /  __/ /   ___/ / / / /  __/ / /___ / /___/ /_/ / /_/ /  
    \____/\__, /_.___/\___/_/   /____/_/ /_/\___/_/_____(_)_____/\____/\____/   
         /____/                                                                  
    
            CyberShell EDU — Security Lab Assistant
    """)
    print("=" * 75)
    print("  Educational cybersecurity toolkit for authorized security testing.")
    print("  Run network diagnostics, DNS checks, Nmap scans, and header analysis.")
    print("  Type 'help' to see commands. Type 'exit' to quit.")
    print("=" * 75)
    
    while True:
        try:
            user_input = input("cybershell> ").strip()
        except KeyboardInterrupt:
            print("\nExiting.")
            break

        if not user_input:
            continue

        parts = shlex.split(user_input)
        command = parts[0]
        args = parts[1:]

        if command == "exit":
            break
        elif command == "help":
            show_help()
        elif command == "ping":
            run_ping(args[0]) if len(args) == 1 else print("Usage: ping <host>")
        elif command == "nmap-basic":
            run_nmap_basic(args[0]) if len(args) == 1 else print("Usage: nmap-basic <host>")
        elif command == "whois":
            run_whois(args[0]) if len(args) == 1 else print("Usage: whois <domain_or_ip>")
        elif command == "dig":
            run_dig(args[0]) if len(args) == 1 else print("Usage: dig <domain>")
        elif command == "traceroute":
            run_traceroute(args[0]) if len(args) == 1 else print("Usage: traceroute <host>")
        elif command == "curl-headers":
            run_curl_headers(args[0]) if len(args) == 1 else print("Usage: curl-headers <url>")
        elif command == "nc-connect":
            run_nc_connect(args[0], args[1]) if len(args) == 2 else print("Usage: nc-connect <host> <port>")
        else:
            print(f"Unknown command: {command}")
            print("Type 'help' to see commands.")

if __name__ == "__main__":
    main()
