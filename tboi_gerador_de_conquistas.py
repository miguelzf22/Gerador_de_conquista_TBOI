#Importando bibliotecas
import os
import random
import steam_web_api
from steam_web_api import Steam
from colorist import green, red

#Pega a Chave API da Steam pela as variáveis do ambiente
KEY = os.environ.get("STEAM_API_KEY")
steam = Steam(KEY)

green("Gerador de conquista para obter do TBOI REP+")

#Preparando as variáveis e as conquistas
user = steam.apps.get_user_achievements("<seu_id_da_steam>","250900") #Coloque o seu ID da Steam
user = user["playerstats"]["achievements"]

#Gera e escolhe outra conquista caso ela já tenha sido obtida
number = random.choice(user)
while number["achieved"] == 1: 
    number = random.choice(user)

print("Tente pegar a conquista: " + number["name"])

#Transfere os IDs das conquistas de string para inteiro
ach_id = int(number["apiname"])

#Define qual DLC a conquista pertence pelo ID da conquista
if ach_id<179:
    red("Não é necessário DLCs!!")
elif ach_id>=179 and ach_id<277:
    red("Necessário DLC do Afterbirth")
elif ach_id>=277 and ach_id<404:
    red("Necessário DLC do Afterbirth+")
elif ach_id>=404 and ach_id<638:
    red("Necessário DLC do Repetance")
else:
    red("Necessário DLC do Repetance+")
