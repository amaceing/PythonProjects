import praw

redditUser = 'codeycoderson'
userSubreddit = 'learnprogramming'
subredditSubmissionLimit = 10

response = praw.Reddit(user_agent=redditUser)
submissions = r.get_subreddit(userSubreddit).get_hot(limit=subredditSubmissionLimit)
[str(x) for x in submissions]