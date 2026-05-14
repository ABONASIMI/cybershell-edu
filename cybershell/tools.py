import subprocess
import shutil

def command_exists(command):
    return shutil.which(command) is not None

def run_command(command_list, timeout=30):
    try:
        result = subprocess.run(
            command_list,
            text=True,
            capture_output=True,
            timeout=timeout
        )

        if result.stdout:
            print(result.stdout)

        if result.stderr:
            print(result.stderr)

    except subprocess.TimeoutExpired:
        print("Error: command timed out.")
    except FileNotFoundError:
        print("Error: command not found.")
    except Exception as error:
        print(f"Error: {error}")

def run_ping(host):
    if not command_exists("ping"):
        print("ping is not installed.")
        return
    run_command(["ping", "-c", "4", host])

def run_nmap_basic(host):
    if not command_exists("nmap"):
        print("nmap is not installed.")
        return
    run_command(["nmap", "-sV", host], timeout=60)

def run_whois(target):
    if not command_exists("whois"):
        print("whois is not installed.")
        return
    run_command(["whois", target])

def run_dig(domain):
    if not command_exists("dig"):
        print("dig is not installed.")
        return
    run_command(["dig", domain])

def run_traceroute(host):
    if command_exists("traceroute"):
        run_command(["traceroute", host])
    elif command_exists("tracepath"):
        run_command(["tracepath", host])
    else:
        print("traceroute or tracepath is not installed.")

def run_curl_headers(url):
    if not command_exists("curl"):
        print("curl is not installed.")
        return
    run_command(["curl", "-I", url])

def run_nc_connect(host, port):
    if command_exists("nc"):
        run_command(["nc", "-vz", host, port])
    elif command_exists("netcat"):
        run_command(["netcat", "-vz", host, port])
    else:
        print("netcat/nc is not installed.")
