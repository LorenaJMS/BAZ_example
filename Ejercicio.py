
#Crear un diccionario donde cuentes las veces que aparece cada nombre en 'dogs
#Imprime la cantidad de perros que se llaman 'Rocky" y 'Sparky'
#Imprime la lista con los diferentes nombres de perros


diccionario_dogs = ['Sparky','Hunter','Loki','Astro','Sparky','Rocky','Toby','Chelsea',
                    'Maple','Maya','Loki','Sparky','Toby','Sparky','Dexter','Fido','Sparky']

contador_rocky = diccionario_dogs.count('Rocky')
contador_sparky = diccionario_dogs.count('Sparky')



print(f"Rocky son:{contador_rocky}")
print(f"Sparky son: {contador_sparky}")

lista_nombres =set(diccionario_dogs)
print("Los nombres son" , diccionario_dogs)

repeticiones = {}

for n in diccionario_dogs:
      if n in repeticiones :
        repeticiones[n] +=1
      else:
         repeticiones[n] =1

print(repeticiones)

print(len(repeticiones))