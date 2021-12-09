# Programa que transforma um texto digitado pelo usuário em áudio e o executa.

from utilidades import *
from pyttsx3 import *
from time import sleep
from os import system

try:
    arquivo_de_texto = open('arquivo_de_texto.txt', 'r')
    arquivo_de_texto.close()
except FileNotFoundError:
    arquivo_de_texto = open('arquivo_de_texto.txt', 'w+')
    arquivo_de_texto.close()

while True:
    cabeçalho('LEITOR DE TEXTO EM ÁUDIO')

    texto_digitado = input('Por favor, digite o texto que deseja ouvir: \n')

    escrever_arquivo_texto(texto_digitado, arquivo_de_texto)

    arquivo_de_texto = open('arquivo_de_texto.txt', 'r')
    for l in arquivo_de_texto:
        ouvir_arquivo = l
    arquivo_de_texto.close()

    ler_audio(ouvir_arquivo)
    
    opção = input('Continuar? [S/N]').strip().upper()[0]
    if opção == 'N':
        break
    system('cls')
    
print()
print('Encerrando programa...')
sleep(1)
print()