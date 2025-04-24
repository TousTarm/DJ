A simple Python script for switching songs using the Spotify API and voice recognition with VOSK.
### Setup
##### Dependencies
```bash
pip install spotipy python-dotenv vosk pyaudio
```
##### Instalation - windows
```powershell
git clone https://github.com/TousTarm/DJ.git
cd DJ
(
  echo MODEL_PATH='vosk-model-small-en-us-0.15'
  echo KEYWORD="spotify"
  echo SPOTIFY_CLIENT_ID="your_client_id"
  echo SPOTIFY_CLIENT_SECRET="your_client_secret"
  echo SPOTIFY_REDIRECT_URI="http://localhost:8888/callback"
) > .env
powershell -command "Invoke-WebRequest -Uri 'https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip' -OutFile 'vosk-model-small-en-us-0.15.zip'"
powershell -command "Expand-Archive -Path 'vosk-model-small-en-us-0.15.zip' -DestinationPath ."
```
##### Instalation - linux
```bash
git clone https://github.com/TousTarm/DJ.git
cd DJ
echo -e 'MODEL_PATH="vosk-model-small-en-us-0.15"\nKEYWORD="spotify"\nSPOTIFY_CLIENT_ID=""\nSPOTIFY_CLIENT_SECRET=""\nSPOTIFY_REDIRECT_URI=""' > .env && chmod 600 .env
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
```
##### Instalation - shared
On the Spotify Developer Dashboard (https://developer.spotify.com/dashboard), create a new app and paste the SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, and SPOTIFY_REDIRECT_URI into the .env file.
> Note: Installation has not been tested yet and might not work as intended
#### Usage
run the app using:
```python
python app.py
```

Commands:
- play [songname] (optional: by [artist]) - Plays the selected song if found
- queue [songname] (optional: by [artist]) - Adds the selected song to the queue if found
- next - Plays the next song in the queue
- wait or pause - Pauses the current song
- continue - Resumes the current song
- stop - Pauses the current song and terminates he script

#### Known bugs
program fails if already running action is performed  
keyword capturing works pretty bad (probably caused by pronunciation)

#### Todo
support pro češtinu  
move to docker  
volume management  
support for numbers    
comment code  
better filter algorythm
fix bugs :q