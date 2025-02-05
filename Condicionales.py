#coding=utf-8

#Prgorama que lee un dato de hora y lo convierte a segundos
#entrada: El Valor de la hora
#salida: El valor de la hora en minutos



print( 'Programa que lee una hora y lo convierte a segundos')
dato_hora= input('ingrese la hora')
print('El tipo de dato de la variable horas es:', type(dato_hora))

#identificamos si en la cadena hay el caracter "."
if '.' in dato_hora:
  #si la cadena contiene el caracter "." entonces se convierte a float
  dato_hora = float(dato_hora)
else: 
  #si la cadena no contiene el caracter "." entonces se convierte a entero
  dato_hora = int(dato_hora)

#se caulcula la hora en minutos
minutos = dato_hora * 60

print(f'las horas {dato_hora} convertidas en minutos son ' , {minutos}) 

print('el tipo de dato de la variable hora_en_minutos es:', type(minutos))

muchos_minutos = 120

if minutos > muchos_minutos:
  print('los minutos son mayores a 120, son muchos minutos')

elif minutos == muchos_minutos:
 print(f'los minutos son iguales a {muchos_minutos}')

else: 
  print('los minutos son menores a 120, son pocos minutos')

if minutos > muchos_minutos:
 print (f'los minutos son mayores a {muchos_minutos},son muchos minutos')
else:
 if minutos == muchos_minutos:
  print(f'los minutos son iguales a {muchos_minutos}, son apenas {muchos_minutos}')
 else:
   print (f'los minutos son menores a {muchos_minutos}, son pocos minutos')



#programa ora identificar si una oersina puede votar
#deoendiendo de la edad y nacionalidad


#tabla de verdad
#P  Q   P and Q   P or Q
#V  V   V         V
#V  F   F         V
#F  V   F         V
#F  F   F         F

print('programa que identifica si una persona puede votar')
print('dependiendo de su edad y nacionalidad')

edad = int(input('Ingrese su edad: '))
nacionalidad = input('Ingrese su nacionalidad: ')

if edad >= 18 and nacionalidad.lower() == 'colombiano':
  print('Usted puede votar por petro')
elif edad >= 21 and nacionalidad == 'extranjero':
  print('Usted no puede votar por petro, vote por maduro')
else:
  print('paila, no puede votar en este planeta')