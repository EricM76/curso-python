
resultado1 = 2 + 5 > 9 * (2 - 3) + 5 and "hola" == "Chau" or 5 == 8 and "hola" != "Chau"

resultado2 =  2 + 5 > 9 * (2 - 3) + 5 and not ("hola" == "Hola") or 5 == 8 and "hola" != "Chau"

# resultado3 =  5*9 == 45 and "1978" < 4 * 6 
'''
45 == 45 and "1978" < 24
T and ERROR

'''

resultado4 =  not 2 + 5 > 9 * (2 - 3) + 5 and True or "hola" == "Hola" or 5 == 8 and "hola" != "Chau"

print(resultado1)
print(resultado2)
# print(resultado3)
print(resultado4)



resultado2 =  2 + 5 > 9 * (2 - 3) + 5 and not ("hola" == "Hola") or 5 == 8 and "hola" != "Chau"

'''
2 + 5 > 9 * (2 - 3) + 5 and not ("hola" == "Hola") or 5 == 8 and "hola" != "Chau"
2 + 5 > 9 * (-1) + 5 and not False or 5 == 8 and "hola" != "Chau"
7 > -9 + 5 and not False or 5 == 8 and "hola" != "Chau"
7 > -4 and not False or 5 == 8 and "hola" != "Chau"
True and not False or False and True
True and True or False and True
True or False
True


'''