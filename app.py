import spotipy, os, pyaudio, json
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from vosk import Model, KaldiRecognizer, SetLogLevel

SetLogLevel(-1)
load_dotenv()

model_path = os.getenv("MODEL_PATH")
keyword = os.getenv("KEYWORD")
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope= "user-read-playback-state user-modify-playback-state"
))

def get_track_uri(clean_text):
    if " by " in clean_text.lower():
        parts = clean_text.lower().split(" by ")
        song_name = parts[0].strip()
        artist_name = parts[1].strip()
    else:
        song_name = clean_text.strip()
        artist_name = None
    
    query = f"track:{song_name}"
    if artist_name:
        query += f" artist:{artist_name}"
    
    results = sp.search(q=query, type="track", limit=20)
    
    if not results['tracks']['items']:
        return None
    
    for track in results['tracks']['items']:
        track_name = track['name'].lower()
        is_original_version = all(
            term not in track_name 
            for term in ['acoustic', 'live', 'remix', 'version', 'cover', 'audio', '8d']
        )
        
        if artist_name:
            artist_match = any(
                artist_name in artist['name'].lower() 
                for artist in track['artists']
            )
        else:
            artist_match = True
            
        if is_original_version and artist_match:
            return track['uri']
    
    return results['tracks']['items'][0]['uri']

def voice_listener():
    while True:
        data = mic.read(4096)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = json.loads(result)
            text = result_dict["text"]
            if keyword in text:
                if "play" in text:
                    clean_text = text.replace(keyword, "").replace("play", "").strip()
                    uri = get_track_uri(clean_text)
                    if uri:
                        sp.start_playback(uris=[str(uri)])
                        print("Playing: ",clean_text)
                    else:
                        print("track not found")
                        print(clean_text)
                elif "que" in text:
                    clean_text = text.replace(keyword, "").replace("que", "").strip()
                    uri = get_track_uri(clean_text)
                    if uri:
                        sp.add_to_queue(uris=[str(uri)])
                        print("Playing: ",clean_text)
                    else:
                        print("track not found")
                        print(clean_text)
                elif "next" in text:
                    sp.next_track
                elif "pause" in text or "wait" in text:
                    sp.pause_playback()
                    print("Pausing")
                elif "continue" in text:
                    sp.start_playback()
                    print("contiuning")
                elif "stop" in text:
                    os.system('cls')
                    print("Exiting...")
                    sp.pause_playback()
                    break
                else:
                    print(keyword, "did not understand: ",text)
            elif "test" in text:
                print("successful")
            elif text != "":
                print("captured but not used:",text)

mic = pyaudio.PyAudio().open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
mic.start_stream()
print("Listening begun")

if __name__ == "__main__":
    voice_listener()