from PIL import Image, ImageFont, ImageDraw, GifImagePlugin
import io, requests, random

def compile(data):
    array = io.BytesIO()
    data.save(array, format='PNG')
    array.seek(0)
    return array

def imagefromURL(url):
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    return image
    return data

def imgs(url):
    image = imagefromURL(url)
    data = compile(image)
    return data