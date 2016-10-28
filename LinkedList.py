# -*- coding: utf-8 -*-
class LinkedList(object):
    
    class Node(object):
        def __init__(self, data, next = None):
            """ Constructor de la classe.
                Parametres:
                -data guarda la dada que es vol emmagatzemar en el node
                -next apuntador al node seguent
            """
            self.data = data
            self.next = next

        def getData(self):
            """ Retorna les dades del node """
            return self.data

        def getNext(self):
            """ Retorna la referencia al seguent node """
            return self.next

        def setData(self, data):
            """ Instancia la variable data amb un nou valor """
            self.data = data

        def setNext(self, next):
            """ Instancia la variable next amb un nou valor """
            self.next = next

        def __str__(self):
            """ Retorna el contingut de la variable data convertit a cadena de caracters """
            return str(self.data)

    def __init__(self):
        """ Constructor de la classe.
            Parametres:
            -self.head apuntador al primer node de la llista
            -self.tail apuntador a l'ultim node de la llista
            -self.current apuntador al node actual de la llista, utilitzat per consultar, afegir i eliminar nodes d'alla on desitgem
            -self.size guarda quants elements hi ha a la llista
        """

        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def getHead(self):
        """ Retorna les dades guardades al primer node de la llista, mostra excepcio de tipus IndexError si la llista es buida """
        if self.isEmpty():
            raise IndexError
        else:
            return self.head.getData()
    
    def getTail(self):
        """ Retorna les dades guardades a l'ultim node de la llista, mostra excepcio de tipus IndexError si la llista es buida """
        if self.isEmpty():
            raise IndexError
        else:
            return self.tail.getData()
    
    def getCurrent(self):
        """ Retorna les dades guardades en el node actual, es a dir, les dades del node al que apunta current, mostra excepcio de tipus IndexError si la llista es buida """
        if self.isEmpty():
            raise IndexError
        else:
            return self.current.getData()
    
    def moveNext(self):
        """ Mou current al node seguent, mostra excepcio de tipus IndexError si current no es pot moure, es a dir si la llista es buida o current apunta a l'ultim node de la llista """
        if self.isEmpty() or self.current == self.tail:
            raise IndexError
        else:
            self.current = self.current.getNext()
    
    def moveHead(self):
        """ Mou current al primer node de la llista, mostra excepcio de tipus IndexError si la llista es buida """
        if self.isEmpty():
            raise IndexError
        else:
            self.current = self.head
    
    def isEmpty(self):
        """ Retorna un boolea que es True si la llista es buida i False en cas contrari """
        if self.head == None:
            return True
        else:
            return False
    
    def getSize(self):
        """ Retorna el numero d'elements a la llista """
        return self.size 
    
    def clear(self):
        """ Esborra la llista sencera """
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0
    
    def insertBefore(self, data):
        """ Afegeix dades a un nou node abans del current, incrementa size i mou current al nou node """
        if self.head == None:
            aux = self.Node(data)
            self.head = aux
            self.size = self.size + 1
            self.current = aux
            self.tail = aux
        elif self.current == self.head:
            self.size = self.size + 1
            aux = self.Node(data,self.head)
            self.head = aux
            self.current = aux    
        else:
            aux1 = self.Node(None,self.head) 
            while aux1.getNext() != self.current:
                aux1 = aux1.getNext()
            aux2 = self.Node(data,self.current)
            aux1.setNext(aux2)
            self.current = aux2
            self.size = self.size + 1
    
    def insertAfter(self, data):
        """ Afegeix dades a un nou node despres del current, incrementa size i mou current al nou node """
        if self.head == None:
            aux = self.Node(data)
            self.head = aux
            self.tail = aux
            self.current = aux
            self.size = self.size + 1
        elif self.current == self.tail:
            self.size = self.size + 1
            aux = self.Node(data)
            self.tail.setNext(aux)
            self.tail = aux
            self.current = aux 
        else:
            self.size = self.size + 1
            aux = self.Node(data,self.current.getNext())
            self.current.setNext(aux)
            self.current = aux
            
    def remove(self):
        """ Esborra el node actual, decrementa size i mou el current al node anterior sempre que sigui possible """
        if self.isEmpty():
            raise IndexError
        elif self.size == 1:
            self.clear()
        elif self.current == self.head: 
            aux = self.head.getNext()
            self.head.setNext(None)
            self.head = aux
            self.current = aux
            self.size = self.size - 1
        elif self.current == self.tail: 
            aux = self.Node(None,self.head)
            while (aux.getNext() != self.tail):
                aux = aux.getNext()
            aux.setNext(None)
            self.tail = aux
            self.current = aux
            self.size = self.size - 1
        else: 
            aux = self.Node(None,self.head)
            while (aux.getNext() != self.current):
                aux = aux.getNext()
            aux.setNext(self.current.getNext())
            self.current = aux
            self.size = self.size - 1
    def __str__(self):
        """ Retorna la llista convertida a una cadena de caracters """
        L=[]
        aux = self.Node(None,self.head)
        while (aux != self.tail):
            aux = aux.getNext()
            L.append(aux.__str__())
        return str(L)

        
