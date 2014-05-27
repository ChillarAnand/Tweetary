
import subprocess
import re
import sys
import urllib2



def get_tweets():
    # get tweets for the given username form greptweet
    username = sys.argv[1]
    url1 = 'http://greptweet.com/create.cgi?id=' + username 

    response1 = urllib2.urlopen(url1)
    page = response1.read()

    url2 = 'http://greptweet.com/u/' + username + '/' + username + '.txt'
    response2 = urllib2.urlopen(url2)
    all_tweets = response2.read()

    return all_tweets


def main():
    all_tweets = get_tweets()
    file = open("tweets.txt", "w")
    file.write(all_tweets)
    file.close()

    output = subprocess.check_output('python get_top_keywords.py tweets.txt')


if __name__ == '__main__':
    main()
