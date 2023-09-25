from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    html="""
    <h1 style="color: black;">Vista 1</h1>
    <br>
    <p>Texto de ejemplo para completar</p>
    <br>
    <a href="www.google.com">Google</a>
    <img src="https://pbs.twimg.com/profile_images/1313547461512880128/XpnRuLqK_400x400.jpg" alt="logo de google" width="200px" height="200px">
    """
    return HttpResponse(html)
def vista2(request):
    html="""
    <h1 style="color: blue;">Vista 2</h1>
    <br>
    <p>Texto de ejemplo para completar</p>
    <br>
    <a href="www.facebook.com">Facebook</a>
    <img src="https://www.facebook.com/images/fb_icon_325x325.png" alt="logo de facebook" width="200px" height="200px">
    """
    return HttpResponse(html)