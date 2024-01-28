import requests


def send_post_request(input_text):
    url = 'http://127.0.0.1:5000/chat'
    data = {'input': input_text}
    print("Giving POST request")
    response = requests.post(url, json=data)
    return response.json()


# Test the function
response = send_post_request('Hello, world!')
print(response)
