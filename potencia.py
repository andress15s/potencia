"""parograma para calcular una potencia 
x^y  """



print("-------------------------------")
print("------potencia: x ^ y----------")
print("-------------------------------")

#input
x = input("digite el valor de x: ")
x = int(x)
y = input("digite el valor de la potencia: ")
y = int(y)


#processing
z = x**y



#output
print(str(x) + " elevado a la "+ str(y) + " es igual a "+ str(z))
