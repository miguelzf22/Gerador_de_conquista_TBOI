#Importando bibliotecas
import random
import os
import steam_web_api
from steam_web_api import Steam
from colorist import red, green, blue

#Pegando a Chave da Steam
KEY = os.environ.get("STEAM_API_KEY")
steam = Steam(KEY)

#Preparando as variáveis e as conquistas
user = steam.apps.get_user_achievements("<seu_id_da_steam>","250900") #Coloque o seu ID da Steam
user = user["playerstats"]["achievements"]

#Definindo funções para verificar se o personagem está desbloqueado (baseado nas conquistas)
def ach_get(n):
    for conquista in user:
        if int(conquista["apiname"]) == n:
            if conquista["achieved"] == 1:
                return True
            else:
                return False

def char_check(n):
    match n:
        case 0:
            return True
        
        case 1:
            if ach_get(1):
                return True
            else:
                return False

        case 2:
            if ach_get(2):
                return True
            else:
                return False

        case 3:
            if ach_get(3):
                return True
            else:
                return False
        
        case 4:
            if ach_get(32):
                return True
            else:
                return False

        case 5:
            if ach_get(42):
                return True
            else:
                return False

        case 6:
            if ach_get(67):
                return True
            else:
                return False

        case 7:
            if ach_get(79):
                return True
            else:
                return False

        case 8:
            if ach_get(80):
                return True
            else:
                return False

        case 9:
            if ach_get(81):
                return True
            else:
                return False

        case 10:
            if ach_get(82):
                return True
            else:
                return False

        case 11:
            if ach_get(199):
                return True
            else:
                return False

        case 12:
            if ach_get(251):
                return True
            else:
                return False

        case 13:
            if ach_get(340):
                return True
            else:
                return False

        case 14:
            if ach_get(390):
                return True
            else:
                return False

        case 15:
            if ach_get(404):
                return True
            else:
                return False

        case 16:
            if ach_get(405):
                return True
            else:
                return False

        case 17:
            if ach_get(474):
                return True
            else:
                return False
        
        case 18:
            if ach_get(475):
                return True
            else:
                return False
        
        case 19:
            if ach_get(476):
                return True
            else:
                return False
        
        case 20:
            if ach_get(477):
                return True
            else:
                return False
        
        case 21:
            if ach_get(478):
                return True
            else:
                return False
        
        case 22:
            if ach_get(479):
                return True
            else:
                return False
        
        case 23:
            if ach_get(480):
                return True
            else:
                return False
        
        case 24:
            if ach_get(481):
                return True
            else:
                return False
        
        case 25:
            if ach_get(482):
                return True
            else:
                return False
        
        case 26:
            if ach_get(483):
                return True
            else:
                return False
        
        case 27:
            if ach_get(484):
                return True
            else:
                return False
        
        case 28:
            if ach_get(485):
                return True
            else:
                return False
        
        case 29:
            if ach_get(486):
                return True
            else:
                return False
        
        case 30:
            if ach_get(487):
                return True
            else:
                return False
        
        case 31:
            if ach_get(488):
                return True
            else:
                return False
        
        case 32:
            if ach_get(489):
                return True
            else:
                return False
        
        case 33:
            if ach_get(490):
                return True
            else:
                return False

        case _:
            return False
                
#Definindo personagens
characters = ["Isaac", "Magdalene", "Cain", "Judas", "???", "Eve", "Samson", "Azazel", "Lazarus", "Eden", "The Lost", "Lilith", "Keeper", "Apollyon", "The Forgotten", "Bethany", "Jacob and Esau"]

#Escolhendo aleatoriamente
number = random.randint(0,33)

#Escolhe novamente se o personagem não estiver desbloqueado
while not char_check(number):
    number = random.randint(0,33)

green("\nPersonagem:")

#Exibe baseado no ID da lista
if number >= 17:
    print("Tainted " + characters[number-17]) #Adiciona o Tainted
else:
    print(characters[number])

#Checa as Marks baseado nas conquistas
def mark_check(n):
    match n:
        case 0:
            if ach_get(57):
                return "???"
            elif ach_get(33) or ach_get(34):
                return "Isaac"
            elif ach_get(4):
                return "Mom's Heart"
            else:
                return "Mom"

        case 1:
            if ach_get(78):
                return "The Lamb"
            elif ach_get(33) or ach_get(34):
                return "Satan"
            elif ach_get(4):
                return "Mom's Heart"
            else:
                return "Mom"

        case 2:
            if ach_get(155):
                return "Mega Satan"
            else:
                n = random.randint(1,2)
        
        case 3:
            if ach_get(341):
                return "Greedier"
            else:
                return "Greed"

        case 4:
            if ach_get(348):
                return "Delirium"
            elif ach_get(234):
                return "Hush"
            elif ach_get(4):
                return "Mom's Heart"
            else:
                return "Mom"
        
        case 5:
            if ach_get(407):
                return "Mother"
            elif ach_get(234):
                return "Hush"
            elif ach_get(4):
                return "Mom's Heart"
            else:
                return "Mom"
        
        case 6:
            if ach_get(635):
                return "The Beast"
            elif ach_get(407):
                return "Mother"
            elif ach_get(234):
                return "Hush"
            elif ach_get(4):
                return "Mom's Heart"
            else:
                return "Mom"
                
red("\nMarks:")

#Definindo as marks (Marks bem simplificadas)
marks=["???", "The Lamb", "Mega Satan", "Greedier", "Delirium", "Mother", "The Beast"]

#Escolhendo as marks
number=random.randint(0,6)
print(mark_check(number))

#Aleatoriamente coloca Boss Rush e Hush caso não seja Greedier
if number != 3 and number!=5:
    bossrush=random.choice([True, False])
    if bossrush == True:
        blue("Boss Rush")
    hush=random.choice([True, False])
    if hush == True and mark_check(number)!="Hush" and mark_check(number)!="The Beast":
        blue("Hush")
        
#Sei lá também
print("")
