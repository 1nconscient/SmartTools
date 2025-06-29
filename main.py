from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from colorama import init, Fore, Style
import time, os

init(autoreset=True)

title = """
       ____               __ ______          __  
      / __/_ _  ___ _____/ //_  __/__  ___  / /__
     _\ \/  ' \/ _ `/ __/ __// / / _ \/ _ \/ (_-<
    /___/_/_/_/\_,_/_/  \__//_/  \___/\___/_/___/
                                             """

os.system('cls')
print(title)
print(f"  [{Fore.CYAN}+{Style.RESET_ALL}] You are successfully connected!")

token = input(f"  [{Fore.YELLOW}>{Style.RESET_ALL}] Token: ")

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
chromedriver_path = r"chromedriver.exe"

def lancer():
    if not token:
        return

    options = Options()
    options.binary_location = brave_path
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://discord.com/login")
    time.sleep(5)
    driver.execute_script('console._commandLineAPI = {};') # allow pasting

    # UwU
    driver.execute_script(f'''
        var iframe = document.createElement('iframe');
        document.body.appendChild(iframe);
        iframe.contentWindow.localStorage.setItem('token', '"{token}"');
        location.href = "https://discord.com/app";
    ''')

lancer()