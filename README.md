# Info
Simple python script for switching songs using spotify API and voice recognition VOSK

## Setup - WILL BE UPDATED
Clone repositary
On spotify developer dashboard, create an app, put SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET and SPOTIFY_CLIENT_URI into .env file  
Download voskmodel (configured for vosk-model-small-en-us-0.15) and link its directory as model  
**optional** - change keyword for desired one  

## Usage
Activate by saying keyword
Commands:
- play [songname] **optional** (by [artist]) - plays song you selected if found
- wait or pause (pause recognition doesnt work consistantly) - pauses current song
- continue - continues current song
- stop - pauses current songs and exits script
Other commands:
- test - outputs "successful" if listening works properly

### Bugs
Program fails if already running action is performed  
Keyword capturing works pretty bad (probably caused by pronunciation)

### Todo
support pro češtinu  
move to docker  
init git repo  
volume management  
support for numbers  
support for common songs  
update speech recognition  
update readme  
comment code