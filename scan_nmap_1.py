import os

filename = "result.txt"

with open(filename, "r") as f:
    lines = list(set([ip.strip() for ip in f]))

    subnet_list = list(set(['.'.join(ip.split('.')[0:2]) + '.0/24' for ip in lines]))

    print('Please select the IP addresses to scan (separated by commas):')
    for i, subnet in enumerate(sorted(subnet_list)):
        print(f'{i+1}. {subnet}')
    subnet_choice = int(input()) - 1
    selected_ips = [ip for ip in lines if ip.startswith(subnet_list[subnet_choice][:-4])]

command = "sudo nmap -sS -Pn -v -O -sU --script vuln -oN"

for line in lines:
    data = line.strip().split("\t")
    ip = data[0]
    port_str = data[1] if len(data) > 1 else None

    if port_str is not None and "," in port_str:
        ports = port_str.split(",")
    elif port_str is not None:
        ports = [port_str]
    else:
        ports = []

    filename = f"scan_results_{ip}.txt"

    if len(ports) > 0:
        command_with_port = f"{command} {filename} -p {','.join(ports)} {ip}"
    else:
        command_with_port = f"{command} {filename} {ip}"

    with open(filename, "a") as f:
        os.system(f"{command_with_port} >> {filename}")

print("Scan results saved to files with names like scan_results_<IP address>.txt")
