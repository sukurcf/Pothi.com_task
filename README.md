# Pothi.com Programming Task

Uses the Twitter Streaming API to track a given keyword and generate various reports about the tweets on console.

## This is designed to run on Linux machines with Python 3 installed.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements from `requirements.txt` file as follows:

```bash
pip install -r requirements.txt
```

### Steps to run:
1. Include your credentials in `twitter_credentials.py` file and run the main script using `python get_tweets_data.py`.
2. For first time run, it will download 2 `nltk` sources for parts of speech recognition to remove few words in tweets.
3. As soon as it completes downloading  the sources, you'll be asked to enter the **keyword** that needs to be tracked on twitter.
4. Enter the keyword and hit enter.
5. The script starts running and for every 1 minute it prints the data of last 5 minutes as mentioned in the task criteria in specific format - The format will also be printed console.
6. For stopping the script, KeyboardInterrupt the script using `CTRL + C`. It will kill all the python running processes.
