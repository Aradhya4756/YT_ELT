import json

import requests

import os

from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

#API_KEY= "AIzaSyCVr1dhQIRbnzj3KRhQM3-9mkA0Gi23Y88"
API_KEY=os.getenv("API_KEY")
CHANNEL_HANDLE="MrBeast"

def get_playlist_id():
    try:
        url=f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response= requests.get(url)
        response.raise_for_status()

        #print(response)

        data=response.json()

        #json.dumps is a python function which used to convert python object into json string format
        #print(json.dumps(data,indent=4))

        #from json visualize tool we can get the root 
        #data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        channel_items=data['items'][0]

        channel_playlistId=channel_items['contentDetails']['relatedPlaylists']['uploads']
        print(channel_playlistId)
        return channel_playlistId
    
    except requests.exceptions.RequestException as e:
        raise e
    
if __name__=="__main__":
    print("get playlist id will be executed ")
    get_playlist_id()
else:
    print("get playlist id woont be executed")


