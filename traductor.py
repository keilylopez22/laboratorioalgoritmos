#Elabarar un programa que tenga un archivo de texto
#llamado EN-ES.text el cual contiene las traducciones de palabras 
#del ingles al español 



"""
el programa debe tener la capacidad de :
1. agregar nuevas traducciones
2. traducir el idioma de la sigueinete forma codigo origen, codigo destino y paabra

EN-ES -- dog    perro
EN-ES -- perro   dog

"""
en_es={}
es_en={}


def cargar_diccionario():
    temporalEnEs={}
    temporalEsEn={}
    archivo=open("texto.txt","r")
    for linea in archivo:
        Es, En= linea.strip().split("=") 
        temporalEnEs[En]=Es
        temporalEsEn[Es]=En
    archivo.close()   
    return temporalEnEs, temporalEsEn

def buscarPalabras(diccionario, palabra):
    if palabra in diccionario:
        return diccionario[palabra]
    else:
        return "la palabra no esta"
def guardar_palabra():
    palabraOrigen=input("ingresa la palbra original: ") 
    palabraTraducida= input("ingresa la traduccion: ") 
    archivo= open("texto.txt","a")
    archivo.write("\n"+palabraOrigen+"="+palabraTraducida)
    archivo.close()


en_es, es_en = cargar_diccionario()
#print(en_es)
#print(es_en)
opcion="1"
while opcion !="4":
    palabra =input("que palabras deseas buscar")
    print(" 1. traducir al español")
    print("2. traducir al ingles")
    print("3. agregar palabra.")
    print("4. deseas salir del programa")
    opcion= input("elige una opcion")
    if opcion=="1":
        traduccion= buscarPalabras(en_es, palabra)
        print(traduccion)
        
    elif opcion=="2":
        traduccion= buscarPalabras(es_en, palabra) 
        print(traduccion) 
    elif opcion=="3":
        guardar_palabra()  
        en_es, es_en = cargar_diccionario()   











    
