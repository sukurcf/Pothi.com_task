import json
import os
import subprocess
import time
from collections import Counter

os.chdir(os.path.dirname(os.path.realpath(__file__)))

while True:
    try:
        users = []
        time.sleep(30)
        content = subprocess.getoutput('cat log*').splitlines()
        content = [json.loads(i) for i in content if len(i) != 0]
        for i in content:
            user = i['user']
            users.append(user['screen_name'])
        users_tweets_count = Counter(users)
        for i, j in users_tweets_count.items():
            print(i.ljust(15), j, sep=' - ')
        print('='*100)
    except:
        os.system('pkill -9 python')
