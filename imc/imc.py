peso = float(input('Qual é seu peso?'))
print('-=-'*10)
altura = float(input('Qual é a sua altura?'))
imc = peso / (altura ** 2 )
print('-=-'*10)
print('Seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta a baixo do peso !!!')
elif imc >= 18.5 and imc < 25:
    print('Você esta no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você esta com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você esta obeso.')
else:
    print('VocÊ esta com obsidade morbida.')