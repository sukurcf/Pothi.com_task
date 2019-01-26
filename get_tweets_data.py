import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
keyword = input('Enter keyword: ')
try:
    os.system(
        'python tweets_metrics.py & python tweepy_streamer.py {}'.format(keyword))
except:
    os.system('pkill -9 python')
