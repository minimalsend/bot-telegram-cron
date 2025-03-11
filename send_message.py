import requests
import os

def enviar_mensagem():
    bot_token = os.environ['BOT_TOKEN']
    chat_id = os.environ['CHAT_ID']
    mensagem = 'Mensagem protegida via Secrets!'

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': mensagem}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print('Mensagem enviada!')
    else:
        print('Erro:', response.text)

if __name__ == '__main__':
    enviar_mensagem()
