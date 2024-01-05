import requests, sys
from requests.exceptions import ConnectTimeout, ReadTimeout

url = 'https://aaio.io/api/balance'
api_key = 'MGU2OTliOWMtMDgxMi00Zjc0LWI2MmEtNjI4NzNlYzY2N2ZhOiR3c01WWl4zMWZ6T0ZEcGQhelduQSV0QkV1I2xeSmxq' # Ключ API из раздела https://aaio.io/cabinet/api

headers = {
    'Accept': 'application/json',
    'X-Api-Key': api_key
}

try:
    response = requests.post(url, headers=headers, timeout=(15, 60))
except ConnectTimeout:
    print('ConnectTimeout') # Не хватило времени на подключение к сайту
    sys.exit()
except ReadTimeout:
    print('ReadTimeout') # Не хватило времени на выполнение запроса
    sys.exit()

if(response.status_code in [200, 400, 401]):
    try:
        response_json = response.json() # Парсинг результата
    except:
        print('Не удалось пропарсить ответ')
        sys.exit()

    if(response_json['type'] == 'success'):
        print(response_json) # Вывод результата
    else:
        print('Ошибка: ' + response_json['message']) # Вывод ошибки
else:
    print('Response code: ' + str(response.status_code)) # Вывод неизвестного кода ответа
