# articles_from_twitter_timeline
extract articles from your twitter timeline and post them to a new twitter account

1) Get API keys for your primary account and twitter bot account
2) put the keys in a separate file called twitter_bot_credentials.json. for instance:

{
    "APP_KEY": "",
    "APP_SECRET": "",
    "OAUTH_TOKEN": "",
    "OAUTH_TOKEN_SECRET": "",
    "APP_KEYbot": "",
    "APP_SECRETbot": "",
    "OAUTH_TOKENbot": "",
    "OAUTH_TOKEN_SECRETbot": ""
}

3) pip install your python dependencies in the directory of your python bot (main script and the json credential file). eg: pip install twython -t C:/twitterbot

4) put the twython files, main bot script and creds into a zip file
5) upload the zip file to Amazon AWS Lambda. Eg:  Code Entry Type: Use a .ZIP file
6) Your "Handler" is the equivalent of calling the main() function in your script. Your telling Lambda what to execute. For my bot , it was cmhbot2.handler
7) test it , make it run on a recurring basis using the Triggers tab and setting up a recurring CloudWatch Events rule 

