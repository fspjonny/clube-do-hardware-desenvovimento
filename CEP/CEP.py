from urllib.parse import urlencode
from urllib.request import urlopen,Request
import re
import webbrowser


cep = input("\033[0;33mDigite o CEP de consulta: ")

url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm"
dados = {"relaxation":cep,"tipoCEP":"ALL","semelhante":"N"}

request = Request(url, urlencode(dados).encode())
retorno = urlopen(request).read()

resultadoBruto = str(retorno)

decodifica = bytes(resultadoBruto,"iso-8859-1").decode("unicode_escape")

expressaoRegular = r"(?:<td.*?>)(.*?)(?:</td>)"

resultadoFinal = re.findall(expressaoRegular,decodifica)

if not resultadoFinal:
    print("O CEP informado %s é inválido!!!" %cep)
    exit()

else:

    arq_html = resultadoFinal
    try:
        arq_html = open("resultado.html", "r+")
        arq_html.writelines("<!doctype html><html><head><meta charset='latin-1'><title>Python consulta CEP</title></head><body><h3>Retorno da consulta do CEP: "+resultadoFinal[3]+"</h3><p>Endereço: <b>"+resultadoFinal[0]+"</b></p><p>Bairro: <b>"+resultadoFinal[1]+"</b></p><p>Estado: <b>"+resultadoFinal[2]+"</b></p></body></html>")
        arq_html.close()
        webbrowser.open_new("resultado.html")
        exit()

    except FileNotFoundError:
        arq_html = open("resultado.html", "w+")
        arq_html.writelines("<!doctype html><html><head><meta charset='latin-1'><title>Python consulta CEP</title></head><body><h3>Retorno da consulta do CEP: "+resultadoFinal[3]+"</h3><p>Endereço: <b>"+resultadoFinal[0]+"</b></p><p>Bairro: <b>"+resultadoFinal[1]+"</b></p><p>Estado: <b>"+resultadoFinal[2]+"</b></p></body></html>")
        arq_html.close()
        webbrowser.open_new("resultado.html")

print("\033[0;34mArquivo pronto!\n\033[0;30mAguarde exibição HTML...")
exit()