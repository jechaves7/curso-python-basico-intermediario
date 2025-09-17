#Crie um código python que teste se o site pudim está acessivel pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site pudim com sucesso!')
    print(site.read())