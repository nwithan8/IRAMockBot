# IRAMockBot
Uses Markov chains and Twitter data to produce fake IRA tweets.

Using Markovify (https://github.com/jsvine/markovify), the bot analyzes the dataset of IRA-associated tweets provided by Twitter (https://about.twitter.com/en_us/values/elections-integrity.html#data), creating a fake IRA tweet and posting it, using Tweepy (https://github.com/tweepy/tweepy) every 15 minutes.

For readability, Twitter's data has been narrowed down to only English language tweets, and only original tweets (no retweets or replies). Instances of hyperlinks, @mentions and "RT <username>" have also been removed from the dataset. Original #hashtags are still included in the data. Overall, the bot pulls from the text of 239,764 of the original 1,048,575 tweets included in Twitter's original provided data.
