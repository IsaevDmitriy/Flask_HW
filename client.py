import requests

HOST = 'http://127.0.0.1:5000'


response1 = requests.post(f'{HOST}/api/post',
                          json={'header': 'Арендую',
                                'definition': 'Мяч',
                                'username': 'Футболист'
                                }).json()
print(response1)


response2 = requests.get(f'{HOST}/api/get/1').json()
print(response2)

response3 = requests.patch(f'{HOST}/api/patch/1',
                                json={'header': 'Куплю',
                                'definition': 'Клюшку',
                                'username': 'Хоккеист'
                                }).json()
print(response3)


response4 = requests.delete(f'{HOST}/api/delete/1').json()
print(response4)