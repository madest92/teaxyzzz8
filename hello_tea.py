import requests

def hello_tea_func():
    response = requests.get('https://app.tea.xyz/')
    print("Hello teaxyzzz2!")
    print("Status teaxyzzz2:", response.url, response.ok)
