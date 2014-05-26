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
    print url2
    response2 = urllib2.urlopen(url2)
    all_tweets = response2.read()

    return all_tweets




def remove_garbage( all_tweets ):
    # remove tweet id, date from the tweets
    
    tweets = ''
    for line in all_tweets:
        try:
            line = line.split('|')
            tweet = line[2]
            tweets += tweet
        except:
            tweets += str(line)


    return tweets




def remove_mentions(filtered_tweets):
    # remove @mentions from the tweets
    tweets = ''
    for line in filtered_tweets:
        if '@' in line:
            a = re.search(r'@sta',  line)
            if a:
                print a.group()
            
    return tweets


def main():
    #all_tweets = get_tweets()
    all_tweets = open('chillaranand.txt')
    filtered_tweets = remove_garbage(all_tweets)
    only_tweets = remove_mentions(filtered_tweets)


if __name__ == '__main__':
    main()
