import requests

def hello_tea_func():
    response = requests.get('https://app.tea.xyz/')
    print("Hello tea!!!!")
    print("Statusss:", response.url, response.ok)
