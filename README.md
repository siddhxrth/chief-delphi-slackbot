# chief delphi slack bot

[![python application](https://github.com/siddhxrth/chief-delphi-slackbot/actions/workflows/python-app.yml/badge.svg)](https://github.com/siddhxrth/chief-delphi-slackbot/actions/workflows/python-app.yml)

#### sends all new chief delphi posts marked as technical into a conversation of your choice using webhooks

#### setup:
1) create a  new slack application and enable webhook functionality into a channel/dm of your choice
    1) **make sure to copy the webhook url, you will need it**
2) the only changes you will need to make in the code are to the [setup.py](setup.py) file:
    1) update the ```WEBHOOK URL``` field with the webhook that slack provided - this is where the application will make requests to post messages, so be sure that the webhook is for the channel in which you would like to post updates 
    2) update the ```REFRESH_INTERVAL``` field with how often you want the bot to check for new posts on chief delphi (**in seconds**)
    
#### about:
hi! i'm sid, a full stack dev from new jersey currently in highschool. i love making little scripts like this that make life more convenient :grin: if you liked this or used it for your frc slack workspace, star the repo or open and issue and let me know! PRs are open for this so if you would like to add a new feature, be sure to add it and open a PR.
 you can see some of the other projects i've created on my [website](https://siddharthlohani.dev) or check out my [Twitter](https://twitter.com/sidlohani)!
