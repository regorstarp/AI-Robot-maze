# -*- coding: latin-1 -*-
# Eduard Campo Raurich  1390690
# Roger Prats Llivina  1391716

from LinkedList import *

class StackList(object):
    """
    StackList Class
    """
    def __init__(self):
        """
        Inicialitza les variables de la pila com a pila buida
        """
        self.llista = LinkedList() # Initialize value
    def push(self, data):
        """
        Afegeix un element al top de la pila, incrementa el size i deixa current al nou node
        :param data: contingut a afegir al top de la pila
        """
        self.llista.insertBefore(data)

    def pop(self):
        """
        Treu l'element que esta en el top de la pila, decrementa el size i deixa el current al següent node de la pila
        :return: retorna l'element eliminat
        """
        popvalor = self.llista.getHead()
        self.llista.remove()
        return popvalor

    def head(self):
        """
        Retorna el contingut de l'element que es troba en el top de la pila
        :return: element top de la pila
        """
        return self.llista.getHead()
    def purge(self):
        """
        Buida la pila
        """
        self.llista.clear()
    def __len__(self):
        """
        Retorna el nombre d'elements de la pila
        :return: nombre d'elements de la pila
        """
        return self.llista.getSize()
    def __str__(self):
        """
        Retorna els elements de la pila convertits a una cadena de caracters
        :return: elements de la pila en forma de cadena de caracters
        """
        return self.llista.__str__()

