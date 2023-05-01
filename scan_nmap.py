import os

# Открываем файл с IP-адресами для чтения
with open('ip_scan.txt', 'r') as f:
    # Читаем файл построчно и сохраняем каждый уникальный IP-адрес в переменной ip_list
    ip_list = list(set([ip.strip() for ip in f]))

    # Получаем список уникальных сетей, по которым можно проводить сканирование
    subnet_list = list(set(['.'.join(ip.split('.')[0:2]) + '.0/24' for ip in ip_list]))

    # Предлагаем пользователю выбрать IP-адреса для сканирования
    print('Please select the IP addresses to scan (separated by commas):')
    for i, subnet in enumerate(sorted(subnet_list)):
        print(f'{i+1}. {subnet}')
    subnet_choice = int(input()) - 1
    selected_ips = [ip for ip in ip_list if ip.startswith(subnet_list[subnet_choice][:-4])]

    # Запрашиваем порт для сканирования
    print('Please enter the port to scan (Press enter to scan all ports):')
    port = input()

    # Предлагаем пользователю выбрать флаги для сканирования
    print('Please enter the nmap flags:')
    flags = "-sS -Pn -v -O"

    # Строка с командой Nmap
    command = f"sudo nmap {flags} -p {port} {' '.join(selected_ips)}"

    # Запускаем сканирование Nmap
    os.system(command)
