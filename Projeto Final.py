# Trabalho Realizado no ambito da Disciplina de PSI
# Realizado por Afonso Pereira

import time
import random

total1 = 0
total2 = 0
ronda = 0

print(" 👋 Bem Vindo ao jogo de dados 👋 ")
print()
time.sleep(3)
print("Objetivo de jogo, quem ultrapassar os 20 , 70 ou 150 pontos ira vencer 🏆 ")
time.sleep(2)
print()
print("Regras do Jogo 📜 :")
time.sleep(0.5)
print("Cada jogador ira poder lançar 2 dados por ronda, Caso num lançamento saia um par de números ímpares a pontuação ira ser descontada ao Score Total")
print()
print("Existe 3 modos de jogo O curto o médio e o longo")
time.sleep(0.5)
print()
print("---------------------- Inicio ----------------------")
print()      
jogador1 = input("Insira o seu Primeiro e ultimo nome: ")
jogador2 = input("Insira o seu Primeiro e ultimo nome: ")
print()

print("1 -> Jogo Curto")
print("2 -> Jogo Médio")
print("3 -> Jogo Longo")
modo = int(input("Escolhe o tipo de Jogo que quer jogar "))
print()

match modo:
    case 1:
        print("Jogo Curto foi selecionado , Boa sorte !!!")
        print()
        print("---------------------- Jogador 1  - ",jogador1,"----------------------")
        print()
        enter = input("Pressiona a tecla Enter para lançar os dados ↵ ")
        print()

        while total1 <=20 and total2 <=20:
            print("Jogador 1 -",jogador1)
            print()
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            print("Os dados rolam 🎲... é sai o valor : ",dado1)
            print("Os dados rolam 🎲... é sai o valor : ",dado2)
            ronda = ronda + 1
            res = dado1 + dado2
            print("Pontuação da ronda:",res)
            if dado1 % 2 == 1 and dado2 % 2 == 1:
                total1 = total1 - res
                print()
                print("TIVESTE AZAR ⚠ !!! SAIU UM PAR DE NÚMEROS ÍMPARES. O RESULTADO DESTA RONDA SERÁ DESCONTADO DO SCORE TOTAL !!! ")
            else:
                total1 = total1 + res
        
            print("O score total é de",total1)
            print()
            enter = input ("Para continuar a lançar do dados carregue na tecla Enter ↵ ")
            print()
            print("---------------------- Jogador 2  - ",jogador2,"----------------------")
            print()
            enter = input ("Pressiona a tecla Enter para lançar os dados ↵ ")
            print()
            print("Jogador 2 -",jogador2)
            print()
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            print("Os dados rolam 🎲... é sai o valor : ",dado1)
            print("Os dados rolam 🎲... é sai o valor : ",dado2)
            res = dado1 + dado2
            print("Pontuação da ronda:",res)
            if dado1 % 2 == 1 and dado2 % 2 == 1:
                total2 = total2 - res
                print()
                print("TIVESTE AZAR ⚠ !!! SAIU UM PAR DE NÚMEROS ÍMPARES. O RESULTADO DESTA RONDA SERÁ DESCONTADO DO SCORE TOTAL !!! ")
            else:
                total2 = total2 + res
            print("O score total é de",total2)
            print()
            enter = input ("Para continuar a lançar do dados carregue na tecla Enter ↵ ")
            print()
            print("---------------------- Jogador 1  - ",jogador1,"----------------------")
    
            print()
        print("---------------------- 👑 Ranking 👑 ----------------------")
        print()
        print("Jogador 1  - ",jogador1,)
        print("Acabou o jogo ! A tua pontuação foi de",total1)
        print()
        print("Jogador 2  - ",jogador2,)
        print("Acabou o jogo ! A tua pontuação foi de",total2)
        print("Espero que te tenhas divertido e gostado !!!")

        print()

    case 2:
        print("Jogo Médio foi selecionado , Boa sorte !!!")
        print("---------------------- Jogador 1  - ",jogador1,"----------------------")
        print()
        enter = input("Pressiona a tecla Enter para lançar os dados ↵ ")
        print()

        while total1 <=70 and total2 <=70:
            print("Jogador 1 -",jogador1)
            print()
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            print("Os dados rolam 🎲... é sai o valor : ",dado1)
            print("Os dados rolam 🎲... é sai o valor : ",dado2)
            ronda = ronda + 1
            res = dado1 + dado2
            print("Pontuação da ronda:",res)
            if dado1 % 2 == 1 and dado2 % 2 == 1:
                total1 = total1 - res
                print()
                print("TIVESTE AZAR ⚠ !!! SAIU UM PAR DE NÚMEROS ÍMPARES. O RESULTADO DESTA RONDA SERÁ DESCONTADO DO SCORE TOTAL !!! ")
            else:
                total1 = total1 + res
        
            print("O score total é de",total1)
            print()
            enter = input ("Para continuar a lançar do dados carregue na tecla Enter ↵ ")
            print()
            print("---------------------- Jogador 2  - ",jogador2,"----------------------")
            print()
            enter = input ("Pressiona a tecla Enter para lançar os dados ↵ ")
            print()
            print("Jogador 2 -",jogador2)
            print()
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            print("Os dados rolam 🎲... é sai o valor : ",dado1)
            print("Os dados rolam 🎲... é sai o valor : ",dado2)
            res = dado1 + dado2
            print("Pontuação da ronda:",res)
            if dado1 % 2 == 1 and dado2 % 2 == 1:
                total2 = total2 - res
                print()
                print("TIVESTE AZAR ⚠ !!! SAIU UM PAR DE NÚMEROS ÍMPARES. O RESULTADO DESTA RONDA SERÁ DESCONTADO DO SCORE TOTAL !!! ")
            else:
                total2 = total2 + res
            print("O score total é de",total2)
            print()
            enter = input ("Para continuar a lançar do dados carregue na tecla Enter ↵ ")
            print()
            print("---------------------- Jogador 1  - ",jogador1,"----------------------")
    
        print()
        print("---------------------- 👑 Ranking 👑 ----------------------")
        print()
        print("Jogador 1  - ",jogador1,)
        print("Acabou o jogo ! A tua pontuação foi de",total1)
        print()
        print("Jogador 2  - ",jogador2,)
        print("Acabou o jogo ! A tua pontuação foi de",total2)
        print("Espero que te tenhas divertido e gostado !!!")

        print()
            
    case 3:
        print("Jogo Longo foi selecionado , Boa sorte !!!")
        print("---------------------- Jogador 1  - ",jogador1,"----------------------")
        print()
        enter = input("Pressiona a tecla Enter para lançar os dados ↵ ")
        print()

        while total1 <=150 and total2 <=150:
            print("Jogador 1 -",jogador1)
            print()
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            print("Os dados rolam 🎲... é sai o valor : ",dado1)
            print("Os dados rolam 🎲... é sai o valor : ",dado2)
            ronda = ronda + 1
            res = dado1 + dado2
            print("Pontuação da ronda:",res)
            print()
            if dado1 % 2 == 1 and dado2 % 2 == 1:
                total1 = total1 - res
                print()
                print("TIVESTE AZAR ⚠ !!! SAIU UM PAR DE NÚMEROS ÍMPARES. O RESULTADO DESTA RONDA SERÁ DESCONTADO DO SCORE TOTAL !!! ")
            else:
                total1 = total1 + res
            if dado1 >= 3 and dado2 >= 3:
                res * 2
                total1 = total1 + res
                print("TIVESTE SORTE ⚠ !!! SAIU UM PAR DE NÚMEROS MAIOR QUE 3 . O RESULTADO DESTA RONDA SERÁ DUPLICADO !!! ")
                
            print("O score total é de",total1)
            print()
            enter = input ("Para continuar a lançar do dados carregue na tecla Enter ↵ ")
            print()
            print("---------------------- Jogador 2  - ",jogador2,"----------------------")
            print()
            enter = input ("Pressiona a tecla Enter para lançar os dados ↵ ")
            print()
            print("Jogador 2 -",jogador2)
            print()
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            print("Os dados rolam 🎲... é sai o valor : ",dado1)
            print("Os dados rolam 🎲... é sai o valor : ",dado2)
            res = dado1 + dado2
            print("Pontuação da ronda:",res)
            if dado1 % 2 == 1 and dado2 % 2 == 1:
                total2 = total2 - res
                print()
                print("TIVESTE AZAR ⚠ !!! SAIU UM PAR DE NÚMEROS ÍMPARES. O RESULTADO DESTA RONDA SERÁ DESCONTADO DO SCORE TOTAL !!! ")
            else:
                total2 = total2 + res
            print("O score total é de",total2)
            print()
            enter = input ("Para continuar a lançar do dados carregue na tecla Enter ↵ ")
            print()
            """print("---------------------- Jogador 1  - ",jogador1,"----------------------")"""
    
        print()
        print("---------------------- 👑 Ranking 👑 ----------------------")
        print()
        print("Jogador 1  - ",jogador1,)
        print("Acabou o jogo ! A tua pontuação foi de",total1)
        print()
        print("Jogador 2  - ",jogador2,)
        print("Acabou o jogo ! A tua pontuação foi de",total2)
        print("Espero que te tenhas divertido e gostado !!!")

        print()

if total1 > total2:
    print("---------------------- 🥇 Vencedor 🥇 ----------------------")
    print()
    print("PAREBÉNS Jogador 1  - ",jogador1,"Ganhas te o jogo e realizaste",ronda,"rondas 🏁 !!!. Foste Incrivel")
    print("Obrigado por teres jogado 🙏")
else:
    print("---------------------- 🥇 Vencedor 🥇 ----------------------")
    print()
    print("PAREBÉNS Jogador 2  - ",jogador2,"Ganhas te o jogo e realizaste",ronda,"rondas 🏁 !!!. Foste Incrivel")
    print("Obrigado por teres jogado 🙏")

