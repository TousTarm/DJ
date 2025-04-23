# Info
Simple python script for switching songs using spotify API and voice recognition VOSK

## Setup - WILL BE UPDATED
##### Dependencies
```python
pip install spotipy python-dotenv vosk pyaudio
```
##### Instalation
```bash
git clone https://github.com/TousTarm/DJ.git
cd DJ
echo -e 'MODEL_PATH="vosk-model-small-en-us-0"\nKEYWORD="spotify"\nSPOTIFY_CLIENT_ID=""\nSPOTIFY_CLIENT_SECRET=""\nSPOTIFY_REDIRECT_URI=""' > .env && chmod 600 .env
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
```
On spotify developer dashboard (https://developer.spotify.com/dashboard) create new app and paste SPOTIFI_CLIENT_ID, SPOTIFY_CLIENT_SECRET and SPOTIFI_CLIENT_URI into .env file

## Usage
run app by:
```python
python app.py
```

Commands:
- play [songname] **optional (by [artist])** - plays song you selected if found
- que [songname] **optional (by [artist])** - add song you selected to que if found
- next - plays next song in que
- wait or pause - pauses current song
- continue - continues current song
- stop - pauses current songs and kills script
Other commands:
- test - outputs "successful" if listening works properly

### Bugs
program fails if already running action is performed  
keyword capturing works pretty bad (probably caused by pronunciation)

### Todo
support pro češtinu  # Info
move to docker  
init git repo  
volume management  
support for numbers  
support for common songs  
update speech recognition  
update readme  
comment code
parametrs for terminal run
linux support
model path přepsat do enviroment variable
better filter algorythm