import requests


def search_address(cep):
    r = requests.get(url=f"https://viacep.com.br/ws/{cep}/json/")
    res = {"sucess": True,
           "msg": "ok",
           "address": ""}
    if r.status_code != 200:
        res = {"sucess": False,
               "msg": f"Erro: {r.status_code}",
               "address": ""}
        return res

    try:
        data = r.json()
        address = { 'cep': data['cep'],
                    'street': data['logradouro'],
                    'neighborhood': data['bairro'],
                    'city': data['localidade'],
                    'state': data['uf'],
                    }
        res = {"sucess": True,
               "msg": "ok",
               "address": address}
    except Exception as ex:
        res = {"sucess": False,
               "msg": f"Erro: {ex}",
               "address": ""}
    return res


