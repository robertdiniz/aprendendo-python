from math import sqrt
catetoAd = float(input("Digite o valor do cateto adjentacente: "))
catetoOp = float(input("Digite o valor do cateto oposto: "))

hipotenusa = sqrt((pow(catetoAd, 2) + pow(catetoOp, 2)))

print(f'A soma dos lados cateto adjentacente {catetoAd}, '
      f'e cateto oposto {catetoOp}, '
      f'a hipotenusa é igual a: {hipotenusa:.2f}')

'''Outra forma era (((catetoAd ** 2) + (catetoOp ** 2)) ** (1/2)), ou
   usando a função math.hypo(catetoOp, catetoAd)'''