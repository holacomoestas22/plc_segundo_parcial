#cafeteria de Ana 
print("Hola soy la cafeteria Ana y te ayudare")
print("")
tem_beb = float(input("Dame la temperatura de tu bebida en grados celcius, solo el entero "))
print("")
hora_dia = float(input("Dame la hora actual en formato de horas, es decir enteros de 1 a 24 "))
print("")
tipo_bebida = str(input("Elige una bebida a=cafe  b=te  c=chocolate calientito ")) 
print("")


if tem_beb < 50:
  print("Debe esperar a que se caliente la bebida")

elif tem_beb >= 50 and tem_beb <= 70:
  print("Se puede servir de inmediato")

elif tem_beb > 70 :
  print("Bebida muy caliente debe esperar a que se enfrie")



if hora_dia >= 6 and hora_dia <= 11:
  print("Las bebidas calientes se sirven mas rapido")

else:
  print("Espera el turno")
