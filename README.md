# limeduck-simple-twitter-bot

![](http://i.imgur.com/D3jbPiN.png)
![](http://i.imgur.com/tCqz2eH.png)

## Development

#### Requirements

- Python 3.6+
	- Mac: `brew install python3`
- virtualenvwrapper
	- https://virtualenvwrapper.readthedocs.io/en/latest/
- Twitter API Credentials (https://apps.twitter.com/)
	- Create New Twitter App: https://apps.twitter.com/app/new

#### Setup
```
mkvirtualenv -p python3 limeduck-simple-twitter-bot -r requirements.txt
cp .env.example .env
# edit .env file to add twitter credentials
```

#### Usage
```
workon limeduck-simple-twitter-bot
./app.py
```

#### Test
```
workon limeduck-simple-twitter-bot
py.test
```