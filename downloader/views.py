from django.shortcuts import render
from django.http import JsonResponse
from .helpers import (file_zipper,playlist_id_maker,
                    playlist_downloader,single_download)
from django.views.decorators.csrf import csrf_exempt

from pytube import YouTube
import json
# playlist=pytube.Playlist('https://www.youtube.com/watch?v=sakQbeRjgwg&list=PL4cUxeGkcC9jdm7QX143aMLAqyM-jTZ2x&index=1')
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
# print(playlist)
# for url in playlist.video_urls:
#     youtube = pytube.YouTube(url)
#     print(youtube.streams.first())
    

# playlist=pytube.Playlist('https://www.youtube.com/playlist?list=PL4cUxeGkcC9hKBg2mU8Hat4-NedlubC3C')
# # playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
# for url in playlist.video_urls:
#     youtube = pytube.YouTube(url)
#     video = youtube.streams.first()
#     video.download('media/screen')
# python -m pip install git+https://github.com/nficano/pytube  correct pytube-plugin

def home(request):

    return render(request,'downloader/index.html')

@csrf_exempt
def downloader(request):
    

    if request.method=='POST':
        body=json.loads(request.body)
        
        if body['playlist']:           
            media_link = playlist_downloader(body)

        else:
            media_link = single_download(body)

        return JsonResponse({'message':'it worked','media':media_link})   



# main()