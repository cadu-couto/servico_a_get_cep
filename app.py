from flask_openapi3 import OpenAPI, Info, Tag
from schemas import *
from search_address import search_address
from flask_cors import CORS


info = Info(title="MVP - Consulta CEP", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

cep_tag = Tag(name="Consulta CEP", description="Documentação da consulta de API viaCEP")


@app.post('/address_by_cep', summary="Retorna o Endereço de um determinado CEP", tags=[cep_tag])
def search_address_by_cep(form: cepSchema):
    res = search_address(form.cep)
    if res['sucess'] == True:
        return res, 200
    else:
        return res, 404






