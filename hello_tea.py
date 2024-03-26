import requests

def hello_tea_func():
    response = requests.get('https://app.tea.xyz/')
    print("Hello teaxyzzz8!")
    print("Status teaxyzzz8:", response.url, response.ok)
