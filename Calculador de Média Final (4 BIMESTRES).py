P = float (input ("Digite sua média no primeiro bimestre: "))
S = float (input ("Digite sua média no segundo bimestre: "))
T = float (input ("Digite sua média no terceiro bimestre: "))
Q = float (input ("Digite sua média no quarto bimestre: "))
somaNotas= (P+S+T+Q)
media= somaNotas/4
if media >= 6: 
    print ("Sua média final é: ", media)
    print ("Você foi aprovado")
#encerrar
    input()
else:
    print ("Sua média final é: ", media)
    print ("Você não foi aprovado")
#encerrar
    input()
