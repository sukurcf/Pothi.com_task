import glob
import json
import os
import time

os.chdir(os.path.dirname(os.path.realpath(__file__)))

while True:
    try:
        time.sleep(60)
        content = ''
        # for i in glob.glob('log*'):
        #     with open(i) as file:
        #         content += file.read()
        for i in glob.glob('log*'):
            content += json.load(i)
        print(content)
    except:
        os.system('pkill -9 python')
