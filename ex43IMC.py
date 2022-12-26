peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura*altura)

print('Seu imc é {}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif imc <= 25:
    print('Você está com o peso ideal')
elif imc <= 30:
    print('Você está com o com o peso acima do ideal')
elif imc <= 40:
    print('Você está obeso(a)')
else:
    print('Você está com grau de obesidade mórbida')


