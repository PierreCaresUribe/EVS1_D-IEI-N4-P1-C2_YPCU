from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista3(request):
    html="""
    <h1 style="color: red;">Vista 3</h1>
    <br>
    <p>Texto de ejemplo para completar</p>
    <br>
    <a href="www.reddit.com">Reddit</a>
    <img src="https://play-lh.googleusercontent.com/i_ZabizifODPnMgIMkyi_nIirJp73q6BbZWLkkUEiTIuHnQkuADH5xdEl2S-2LZubTA" alt="logo de reddit" width="200px" height="200px">
    """
    return HttpResponse(html)
def vista4(request):
    html="""
    <h1 style="color: green;">Vista 4</h1>
    <br>
    <p>Texto de ejemplo para completar</p>
    <br>
    <a href="www.twitch.tv">Twitch</a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Twitch.jpg/640px-Twitch.jpg" alt="logo de twitch" width="200px" height="200px">
    """
    return HttpResponse(html)