"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 

def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")

    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar elementos a partir de dos listas")

    print("6- Consultar elementos a partir de dos listas (para esta consulta no es necesario elgir la opcion 1 antes de proceder)")
    print("0- Salir")


def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for element in lst:
            if criteria.lower()==element[column].lower(): #filtrar por palabra clave ##se efectuo un cambio por que habia un error en la comparacion
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter
def countElementsByCriteria1(criteria, column, lst)-> None:
    lista2 = []
    promedio = []

    loadCSVFile("Data/AllMoviesCastingRaw.csv", lista2)
    for element in lista2:
            if criteria.lower() in element[column].lower():
                id1 = element["id"]
                for elem in lst:
                    if elem["\ufeffid"] == id1:
                        if float(elem["vote_average"]) >= 6:
                            promedio.append(float(elem["vote_average"]))
    return promedio
   
def countElementsByCriteria2(criteria, lst):
    """
    Retorna la cantidad de elementos que cumplen con un criterio 
    """
    counter=0
    suma=0
    lista1=[]


    loadCSVFile("Data/MoviesCastingRaw-small.csv", lista1)

    for element in lista1:
        if criteria.lower() in element["director_name"]:
            for elemento in lst:
                if elemento[0]==element[0]:
                    if elemento[18]>=6:
                        counter+=1
                        suma+=element[18]

    promedio=suma/counter
    lista=[counter, promedio]
    return lista  


def countElementsByCriteria3(criteria)-> None:
    lista=[] #Lista vacia en donde vamos a tener en memoria nuestra lista del primer archivo
    list_identificadores=[] #Aqui agregaremos los indicadores de las peliculas con el autor especificado (criteria)
    loadCSVFile("Data/AllMoviesCastingRaw.csv", lista)
    if len(lista)==0:
        return (print('La lista esta vacia'))
    else:
        for element in lista:
            if criteria.lower()==element['director_name'].lower():
                list_identificadores.append(element['id'])
    lista=[] #Nueva lista vacia en donde se guardara en memoria la informacion del segundo archivo
    loadCSVFile("Data/AllMoviesDetailsCleaned.csv", lista)
    buenas=0 #numero de pelcilas buenas
    num_votos=0 #Sumatoria de numero de votos
    conteo=0 #contador para revisar la lista
    for elemento in list_identificadores: 
        indicador=False #indicador para finalizar ciclo while
        while indicador==False and conteo<len(lista):
            if lista[conteo]["\ufeffid"]==elemento:
                if float(lista[conteo]['vote_average'])>=6:
                    buenas+=1
                    num_votos+=float(lista[conteo]['vote_average'])
                indicador=True
            conteo+=1

    promedio_votos=num_votos/buenas
    return print('Coinciden ',buenas,' peliculas buenas con un promedio de votacion de: ', promedio_votos)
        
    
    
# La siguiente funcion se creo solo para verificar el tiempo de duracion de la funcion len()
def Duracion_conteo_de_elementos(lista)-> None:
    t1_start= process_time() #inicio de conteo
    longitud_lista=str(len(lista))
    t1_stop= process_time() #tiempo final
    print('Duracion:\n'+str(t1_start-t1_stop))
    print("La lista tiene "+longitud_lista+" elementos")
    
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = [] #instanciar una lista vacia
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
              
                loadCSVFile("Data/AllMoviesDetailsCleaned.csv", lista) #llamar funcion cargar datos

                print("Datos cargados, "+str(len(lista))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(lista)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: Duracion_conteo_de_elementos(lista)
            elif int(inputs[0])==3: #opcion 3
                criteria =input('Ingrese el criterio de búsqueda\n')

                counter=countElementsFilteredByColumn(criteria, "production_countries", lista) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4, Funcion creada por compañero
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter=countElementsByCriteria1(criteria,"director_name",lista)
                print("Se encontaron ",len(counter)," Peliculas buenas para el director: ", criteria)
                print("promedio de evaluación de las peliculas del director ", criteria, " es: ", sum(counter)/len(counter))

            elif int(inputs[0])==5: #opcion 5, Funcion creada por compañero
                criteria =input('Ingrese el criterio de búsqueda\n')
                counter=countElementsByCriteria2(criteria,lista)
                print("Coinciden ",counter[0]," elementos con el crtierio: '", criteria ,"' promedio de votacion:", counter[1])
 
            elif int(inputs[0])==6: #opcion 6, Funcion creada por compañero
                criteria =input('Ingrese el criterio de búsqueda\n')
                countElementsByCriteria3(criteria)

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()
