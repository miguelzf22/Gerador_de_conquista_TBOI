#Importando bibliotecas
import random
from colorist import red, green, blue

#Definindo personagens
characters = ["Isaac", "Magdalene", "Cain", "Judas", "???", "Eve", "Samson", "Azazel", "Lazarus", "Eden", "The Lost", "Lilith", "Keeper", "Apollyon", "The Forgotten", "Bethany", "Jacob and Esau"]

#Escolhendo aleatoriamente
number = random.randint(0,30)

green("\nPersonagem:")

#Exibe baseado no ID da lista
if number >= 14:
    print("Tainted " + characters[number-14]) #Adiciona o Tainted
else:
    print(characters[number])

red("\nMarks:")

#Definindo as marks (Marks bem simplificadas)
marks=["???", "The Lamb", "Mega Satan", "Greedier", "Delirium", "Mother", "The Beast"]

#Escolhendo as marks
number=random.randint(0,6)

print(marks[number])

#Aleatoriamente coloca Boss Rush e Hush caso não seja Greedier
if number != 3:
    bossrush=random.choice([True, False])
    if bossrush == True:
        blue("Boss Rush")
    hush=random.choice([True, False])
    if hush == True:
        blue("Hush")

print("")
