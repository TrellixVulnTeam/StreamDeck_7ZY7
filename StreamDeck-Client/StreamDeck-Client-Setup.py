import os
import subprocess
from sys import exit, stderr, stdout
import threading
import time
from functools import wraps
from platform import *
from traceback import print_exc
import urllib.request


class Colors:
    END = '\33[0m'
    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    URL = '\33[4m'
    BLINK = '\33[5m'
    BLINK2 = '\33[6m'
    SELECTED = '\33[7m'
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'
    BLACKBG = '\33[40m'
    REDBG = '\33[41m'
    GREENBG = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG = '\33[46m'
    WHITEBG = '\33[47m'
    GREY = '\33[90m'
    RED2 = '\33[91m'
    GREEN2 = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2 = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2 = '\33[96m'
    WHITE2 = '\33[97m'
    GREYBG = '\33[100m'
    REDBG2 = '\33[101m'
    GREENBG2 = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2 = '\33[104m'
    VIOLETBG2 = '\33[105m'
    BEIGEBG2 = '\33[106m'
    WHITEBG2 = '\33[107m'


def animated_loading(text):
    """
    Loading Animation

    :param text:
    :return:
    """
    chars = "|/-\\"
    for char in chars:
        sys.stdout.write('\r' + text + char)
        time.sleep(0.1)
        sys.stdout.flush()


def title():
    return f'{Colors.BLUE2}   _____ {Colors.GREEN}__ {Colors.VIOLET}     {Colors.BLUE}     {Colors.YELLOW}     {Colors.RED}            {Colors.WHITE}____            __  \n{Colors.BLUE2}  / ___/{Colors.GREEN}/ /_{Colors.VIOLET}_____{Colors.BLUE}___  {Colors.YELLOW}____ {Colors.RED}_____ ___  {Colors.WHITE}/ __ \___  _____/ /__\n{Colors.BLUE2}  \__ \{Colors.GREEN}/ __/{Colors.VIOLET} ___{Colors.BLUE}/ _ \{Colors.YELLOW}/ __ `{Colors.RED}/ __ `__ \{Colors.WHITE}/ / / / _ \/ ___/ //_/\n{Colors.BLUE2} ___/ /{Colors.GREEN} /_{Colors.VIOLET}/ /  {Colors.BLUE}/  __{Colors.YELLOW}/ /_/ /{Colors.RED} / / / / /{Colors.WHITE} /_/ /  __/ /__/ ,<   \n{Colors.BLUE2}/____/{Colors.GREEN}\__/{Colors.VIOLET}_/   {Colors.BLUE}\___/{Colors.YELLOW}\__,_/{Colors.RED}_/ /_/ /_/{Colors.WHITE}_____/\___/\___/_/|_|  \n'


def check_python_version():
    if '3.9' in python_version():
        pass
    else:
        print(
            Colors.RED + f'Your Python version is outdated (required: 3.9 or newer / your version: {python_version()})' + Colors.WHITE)
        time.sleep(100)
        exit()


def install_packages():
    subprocess.call('pip --disable-pip-version-check install dearpygui', stdout=subprocess.DEVNULL)
    subprocess.call('pip --disable-pip-version-check install requests', stdout=subprocess.DEVNULL)


def check_internet():
    try:
        urllib.request.urlopen('https://github.com')
        return True
    except:
        return False


def add_to_startup():
    with open('/etc/rc.local', 'a') as s:
        s.write('\npython3 /etc/StreamDeck/StreamDeck-Client/StreamDeck-Client.py')
        s.close()


def download_sdclient():
    subprocess.call('cd /etc/', stdout=subprocess.DEVNULL)
    subprocess.call('git clone https://github.com/philliphqs/StreamDeck', stdout=subprocess.DEVNULL)


def check_platform():
    if sys.platform == "linux" or sys.platform == "linux2":
        pass
    else:
        print(Colors.RED + f'You are using an incompatible OS for StreamDeck-Client (required: Linux / your os: {sys.platform})' + Colors.White)
        time.sleep(100)
        exit()


def create_run():
    with open('home/StreamDeck.sh', 'w') as r:
        r.write('cd etc/StreamDeck/StreamDeck-Client\n'
                'python3 -m StreamDeck-Client.py')
        r.close()
    subprocess.call('chmod +x ./StreamDeck.sh', stdout=subprocess.DEVNULL)


print(title() + '---Client-Setup----------------------------------------------')

# PreStep 1 - Checking Python version
check_python_version_thread = threading.Thread(name='check_python_version', target=check_python_version)
check_python_version_thread.start()

while check_python_version_thread.is_alive():
    animated_loading('Checking Python version: ')

print(f'\rChecking Python Version: {Colors.GREEN}Checked!{Colors.WHITE}')

# PreStep 2 - Check internet connection
check_internet_connection_thread = threading.Thread(name='check_internet_connection', target=check_internet)
check_internet_connection_thread.start()

while check_internet_connection_thread.is_alive():
    animated_loading('Checking Internet connection: ')

print(f'\rChecking Internet connection: {Colors.GREEN}Connected!{Colors.WHITE}')

# PreStep 3 - Check platform compatibility
check_platform_thread = threading.Thread(name='check_platform', target=check_platform)
check_platform_thread.start()

while check_platform_thread.is_alive():
    animated_loading('Checking platform compatibility: ')

print(f'\rChecking platform compatibility: {Colors.GREEN}Compatible!{Colors.WHITE}')

# Step 1 - Installing Packages
install_packages_thread = threading.Thread(name='install_packages', target=install_packages)
install_packages_thread.start()

while install_packages_thread.is_alive():
    animated_loading('Installing Packages: ')

print(f'\rInstalling Packages: {Colors.GREEN}Done!{Colors.WHITE}')

# Step 2 - Downloading StreamDeck-Client
download_sdclient_thread = threading.Thread(name='download_sdclient', target=download_sdclient)
download_sdclient_thread.start()

while download_sdclient_thread.is_alive():
    animated_loading('Cloning StreamDeck: ')

print(f'\rCloning StreamDeck: {Colors.GREEN}Cloned!{Colors.WHITE}')

# Step 3 - Creating StreamDeck run file at home dir
create_run_thread = threading.Thread(name='create_run', target=create_run)
create_run_thread.start()

while create_run_thread.is_alive():
    animated_loading('Creating run command: ')

print(f'\rCreating run command: {Colors.GREEN}Created!{Colors.WHITE}')

# Info 1
print('Finished with the main installation.')

# Extra Step 1 - Add to startup
add_to_startup_thread = threading.Thread(name='add_to_startup', target=add_to_startup)

ask_step1 = input('Do you want to add StreamDeck on startup? (y/n)')
if ask_step1.startswith('y'):
    add_to_startup_thread.start()

    while add_to_startup_thread.is_alive():
        animated_loading('Adding StreamDeck to startup: ')

    print(f'\rAdding StreamDeck to startup: {Colors.GREEN}Added!{Colors.WHITE}')
    pass
elif ask_step1.startswith('n'):
    pass
else:
    print(Colors.RED + ask_step1 + ' is not an valid answer!' + Colors.WHITE)

# Info 2
print('StreamDeck is now on your device if you need help go to GitHub and create an issue\n'
      '---------------------------\n'
      f'StreamDeck related {Colors.BLUE}links{Colors.WHITE}\n'
      'Repo: https://github.com/philliphqs/StreamDeck\n'
      'Website: https://philliphqs.github.io/StreamDeck\n'
      '---------------------------\n'
      'About me\n'
      'Author: philliphqs\n'
      'GitHub: https://github.com/philliphqs\n'
      'Website: https://philliphqs.github.io\n'
      '---------------------------\n'
      f'{Colors.BLUE2}Discord\n'
      f'{Colors.VIOLET}hqsartworks{Colors.WHITE}: https://discord.gg/ZrbW2FHdjH\n'
      f'alphaclan Community: https://discord.gg/faM2eWpK8m\n'
      f'--------------------------\n'
      f'{Colors.BLINK}Click CTRL+C or CTRL+Z to quit\n')