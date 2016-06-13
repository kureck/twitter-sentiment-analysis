import sys
import json

def hw():
    print 'Hello, world!'

def tweet_texts(jf):
    twitter_texts_list = []
    with open(jf) as f:
        for line in f:
            try:
                e = extracted_tweets(line)
                twitter_texts_list.append(e)
            except:
                continue

    return twitter_texts_list

def sentiment_hash(sent_file):
    with open(sent_file) as f:
        sent_hash = {word: int(score.strip()) for (word, score) in
                     [x.split('\t') for x in f]}

    return sent_hash

def extracted_tweets(tweet):
    tweet_id = json.loads(tweet).get('id', None)
    text = json.loads(tweet).get('text', None)
    splited_tweet = text.split()
    full_tweet = json.loads(tweet)
    score = 0
    tweet = {'tweet_id': tweet_id, 'text': text,
            'splited_tweet': splited_tweet,
            'full_tweet': full_tweet, 'score': score}
    return tweet

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]

    print(tweet_texts(tweet_file))

if __name__ == '__main__':
    main()
