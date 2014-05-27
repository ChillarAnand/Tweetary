import os
import subprocess
import re
import sys
import urllib2



def get_tweets(username):
    # get tweets for the given username form greptweet
    url1 = 'http://greptweet.com/create.cgi?id=' + username 

    response1 = urllib2.urlopen(url1)
    page = response1.read()

    url2 = 'http://greptweet.com/u/' + username + '/' + username + '.txt'
    response2 = urllib2.urlopen(url2)
    all_tweets = response2.read()

    return all_tweets


def main():
    username = sys.argv[1]
    print username
    all_tweets = get_tweets(username)
    file = open("tweets.txt", "w")
    file.write(all_tweets)
    file.close()
    
    current_directory = os.getcwd()
    os.chdir(current_directory)
    output = subprocess.check_output('python get_top_keywords.py tweets.txt', shell=True)
    print '\nTop 25 words used by @' + username + '\n'
    print output


if __name__ == '__main__':
    main()
