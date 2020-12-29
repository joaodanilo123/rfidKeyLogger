import requests

host = 'http://localhost/sara/'

def getValidTokens():
    tokens = requests.get(host + 'actions/listar_tags.php')
    return tokens.json()


def updateReserve(token):
    response = requests.post(host + 'actions/atualizar_reserva.php', data = {'rfid': token})
    return response