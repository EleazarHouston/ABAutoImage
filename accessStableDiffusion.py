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
except Exception as e:
    print(f"Exception: {e}")