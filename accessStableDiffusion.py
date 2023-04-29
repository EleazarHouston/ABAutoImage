import urllib.request
import requests
import json
from PIL import Image
import io
import base64
import random


existsStableDiffusion = False

try:
    print("Checking URL...")
    if urllib.request.urlopen("http://127.0.0.1:7860").getcode() == 200:
        existsStableDiffusion = True
        print("Stable Diffusion Online")
except Exception as e:
    print(f"Exception: {e}")

def getSDiffImage():
    if existsStableDiffusion == False:
        print("Stable Diffusion not found. Exiting...")
        return False

    result = []
    imageCategories = json.load(open("private/imageCategories.json", "r"))
    for category in imageCategories:
        result.append(random.choice(imageCategories[category]))
    prompt = ", ".join(result)
    print("Debug1")
    promptAddon = str(open("private/promptAddon.txt", "r").readlines()[0])
    print("Debug2")
    payload = {
        "prompt": prompt + promptAddon,
        "steps": 30,
        "sampler_index": "Euler a",
        "restore_faces": True,
        "eta": 0.75,
        "cfg_scale": 15
    }
    print("Retrieving image...")
    response = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/txt2img', json=payload)
    r = response.json()
    print("Debug0")
    index = 1
    for i in r['images']:
        print("Debug3")
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
        image.save(f'generatedImages/{prompt}.png')
        print("Image saved")
    return

#getSDiffImage()