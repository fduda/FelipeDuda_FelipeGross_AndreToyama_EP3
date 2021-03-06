# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:32:56 2015

@author: André, Felipe Duda, Felipe Gross
"""

############################################## Arquivos e Listas

alimento = open('alimentos.csv','r+')  #abre o arquivo
lista0 = alimento.readlines()
lista=[]

for i in lista0:            #limpa e organiza o arquivo
    lista.append(i.strip().split(';'))    
user1 = open('usuario.csv','r+')
user0 = user1.readlines()
user =[]

for i in user0:
    user.append(i.strip().split(','))       #limpa e organiza a lista

lista_alimentos=[]  
  
for i in range (3, len(user)):
    lista_alimentos.append(user[i])
lista_alimentos.sort()



############################################## Funções

def TMB(idade, peso,sexo, altura):  #Quilogramas, Metros, Anos
    if sexo == 'M':
        return float(88.36 + (13.4*int(peso)) + (4.8*float(altura)) - (5.7*int(idade)))
    if sexo == 'F':
        return float(447.6 + (9.2*int(peso)) + (3.1*float(altura)) - (4.3*int(idade)))
        
tmb = TMB(user[1][1], user[1][2], user[1][3], user[1][4])


def Consumo_diario(tmb, fator):          #cria a função de consumo diário
    if fator == 'mínimo':
        return tmb*1.2 
    if fator == 'baixo':
        return tmb*1.375
    if fator == 'médio':
        return tmb*1.55
    if fator == 'alto':
        return tmb*1.725
    if fator == 'muito alto':
        return tmb*1.9
        
consumo_diario = Consumo_diario(tmb, user[1][5])

def IMC(peso, altura):              #cria a função de IMC
    if float(altura) >= 1.80:        
        return ((1.3*int(peso))/(float(altura)**2.5)) - 1
    elif float(altura) <= 1.50:
        return ((1.3*int(peso))/(float(altura)**2.5)) + 1 
    else:
        return ((1.3*int(peso))/(float(altura)**2.5))
        
        
imc = IMC(user[1][2], user[1][4])


def Condição(imc):          #Cria a função de Condição
    if imc < 18.5:
        return 'abaixo do peso'
    elif 18.5<imc<24.9:
        return 'normal'
    elif 25<imc<29.9:
        return 'sobrepeso'
    elif imc >= 30:
        return 'obeso'
        
condição_fisica = Condição(imc)


#################################################### dicionário

dias = {}

for i in range (len(lista_alimentos)):
    
    if not lista_alimentos[i][0] in dias:
        dias[lista_alimentos[i][0]] = []
    dias[lista_alimentos[i][0]].append(lista_alimentos[i])    

dicionario = {}

for i in range (len(lista)):
    dicionario[lista[i][0]] = []
    dicionario[lista[i][0]].append(lista[i])

#################################################### dicionário

dias = {}                                #Dicionário com os alimentos ingeridos pelo usuário, organizado por dia

for i in range (len(lista_alimentos)):
    
    if not lista_alimentos[i][0] in dias:
        dias[lista_alimentos[i][0]] = []
    dias[lista_alimentos[i][0]].append(lista_alimentos[i])    

dicionario = {}                         #dicionário com os dados dos alkimentos, nome, quantidade, calorias, proteinas, carboidratos e ggorduras

for i in range (len(lista)):
    dicionario[lista[i][0]] = []
    dicionario[lista[i][0]].append(lista[i])



############# Calorias, Proteinas, Carboidratos e Gorduras 



def calorias_consumidas(data):                                  #função para calcular o quanto de calorias foi consumido no respectivo dia
    cals = 0    
    for i in range ((len(dias[data])) - 1):
        cals += (float(dicionario[dias[data][i][1]][2])*(float(dias[data][i][2])*0.01))

def proteinas_consumidas(data):                                 #função para calcular o quanto de proteínas foi consumido no respectivo dia
    prot = 0    
    for i in range ((len(dias[data])) - 1):
        prot += (float(dicionario[dias[data][i][1]][3])*(float(dias[data][i][2])*0.01))

def carboidratos_consumidos(data):                              #função para calcular o quanto de carboidratos foi consumido no respectivo dia
    carb = 0    
    for i in range ((len(dias[data])) - 1):
        carb += (float(dicionario[dias[data][i][1]][4])*(float(dias[data][i][2])*0.01))


def gorduras_comnsumidas(data):                                #função para calcular o quanto de gordura foi consumido no respectivo dia
    gord = 0
    for i in range ((len(dias[data])) - 1):
        gord += (float(dicionario[dias[data][i][1]][5])*(float(dias[data][i][2])*0.0

################################################## Exercício

exercicio = open("exercicio.csv","r+")
dicionario1=exercicio.readlines()
dicionario1={}


met={"Squash": 12.0,"Boxe": 12.0,"Tenis": 7.0,"Futebol": 7.0,"Nadar": 10.0,"Rugby": 10.0,"Correr": 7.0}
t=[45,60,90,30,50,45,50]
x=t[]/60  # X = tempo de atividade fisica (em horas)

{met[exercicio]}*(70)*t   #Equivalência Metabólica. Calcula a quantidade de calorias gasta por exercício
