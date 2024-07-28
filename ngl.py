import random
import string
import requests
import threading
def deviceId():
    characters = string.ascii_lowercase + string.digits
    part1 = ''.join(random.choices(characters, k=8))
    part2 = ''.join(random.choices(characters, k=4))
    part3 = ''.join(random.choices(characters, k=4))
    part4 = ''.join(random.choices(characters, k=4))
    part5 = ''.join(random.choices(characters, k=12))
    device_id = f"{part1}-{part2}-{part3}-{part4}-{part5}"
    return device_id
def UserAgent():
    with open('user-agents.txt', 'r') as file:
        user_agents = file.readlines()
        random_user_agent = random.choice(user_agents).strip()
        return random_user_agent
def random_message():
    with open("words.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    return random.choice(content).strip()
username = input("Target: ")
threadz = int(input("Threads: "))
message = random_message()
headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': f'{UserAgent()}',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{username}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }
data = {
            'username': f'{username}',
            'question': f'{message}',
            'deviceId': f'{deviceId()}',
            'gameSlug': '',
            'referrer': '',
        }
# threading is a real power to make it go a few times faster.
def send(thread_id):
    response = requests.post('https://ngl.link/api/submit', headers=headers, data=data)
threads = []
for i in range(threadz):
    thread = threading.Thread(target=send, args=(i,))
    thread.start()
    threads.append(thread)
    print(f"Started thread: < {i+1} >")
for thread in threads:
    thread.join()
    print(f"Thread Finished")