compra = float(input('Digite o valor de sua compra: R$'))
print('''Escolha a opção de pagamento.
[1] - A vista/Pix (desconto de 10%)
[2] - Cartão de crédito em 3x (desconto de 5%)
[3] - Cartão de crédito em 4x ou mais (juros de 3%)''')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print('Você escolheu A vista/Pix\n sua compra de R${:.2f} sairá por R${}'.format(compra, compra - (compra * 10/100)))
elif opcao == 2:
    print('Você escolheu Cartão de crédito em 3x\n sua compra de R${} sairá por R${:.2f}'.format(compra, compra - (compra * 5/100)))
elif opcao == 3:
    print('Você escolheu Cartão de crédito em 4x ou mais\n essa opção terá juros de 3%\n sua compra de R${} sairá por R${:.2f}'.format(compra, compra + (compra * 3/100)))

print('Obrigado por utilizar nosso sistema')