# secret API key, load from WOLFRAM_API_KEY.txt

import os

import requests

PATH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(PATH, 'WOLFRAM_API_KEY.txt'), 'r') as f:
    WOLFRAM_API_KEY = f.read().strip()


# Wolfram API format:
# https://www.wolframalpha.com/api/v1/llm-api?input=<input>&appid=<API key>&maxchars=<maxchars>

def wolfram_api(input_, maxchars=1000):
    url = f"https://www.wolframalpha.com/api/v1/llm-api?input={input_}&appid={WOLFRAM_API_KEY}&maxchars={maxchars}"
    r = requests.get(url)
    return r.text.strip()


def parse_input_from_response(text):
    x = text.split('wolfram_api')[1]
    return x


def give_response(text):
    input_ = parse_input_from_response(text)
    response = wolfram_api(input_)
    return "wolfram_response " + response
