from collections import defaultdict
diccionario_dogs = ['Sparky','Hunter','Loki','Astro','Sparky','Rocky','Toby','Chelsea',
                    'Maple','Maya','Loki','Sparky','Toby','Sparky','Dexter','Fido','Sparky']


dog_dic = defaultdict (int)
for dog in diccionario_dogs:
    dog_dic[dog] +=1
print('Rocky', dog_dic['Rocky'])
print('Sparky', dog_dic['Sparky'])
print(f"Los nombrs son: ", list(dog_dic.keys()))

#Comentario nuevooo
#Nuevo comentario
#Subiendo cambios para empezar a ver que ondagit
#nuevo
#Otro intento