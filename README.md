# Gerador de conquista TBOI
Um programa simples que foi usado para praticar a linguagem Python e a biblioteca da steam_api_web 

Gera uma conquista não obtida do The Binding Of Isaac para você tentar desbloquear :)

No momento, o código não é adaptado para as DLCs, então ele vai ler todas as conquistas.

# Gerador de run básico TBOI "Dinâmico"
Um gerador de run aleatória baseado no projeto do TRPG0, só que mais feio

O código se adapta mais ou menos à sua progressão no jogo.

O código checa os personagens e as marks desbloquadas, mas não as marks específicas de cada personagem, então pode acontecer que gere marks que você já obteve.

Possivelmente não terá uma opção para se adaptadar às marks específicas do seu personagem pelo fato de que seria chato, trabalhoso e um pouco comlexo de programar.

# Requisitos

## Bilbiotecas externas

### **colorist**

Utilizada para cores no terminal, no código é apenas cosmético para deixar mais agradável aos olhos.

### **steam_web_api**

Utilizado para obter as conquistas e outras informações do usuário.

### Comandos para instalar

Utilize `pip install steam_web_api` e `pip install colorist` para instlar as bibliotecas, sem elas o código não funciona.

## Outros

**Chave API da Steam:** 

Crie uma váriavel do ambiente chamada "STEAM_API_KEY" e insira sua chave.

Insira o comando `getx STEAM_API_KEY "sua_key"` no terminal do Windows (Substitua o sua_key pela sua chave API da Steam).

**The Binding of Isaac:** 

Necessário ter jogado o jogo, não necessariamente possuir (Biblioteca steam, etc.)

**DLCs:** 

Altamente recomendado ter a DLC do Repentance. 

**Perfil Público:** 

Seu perfil e suas conquistas precisam ser públicos.
