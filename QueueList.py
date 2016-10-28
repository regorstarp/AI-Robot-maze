# -*- coding: utf-8 -*-
# LLenar con NIUs de los integrantes del grupo
# NIU_1:1390690
# NIU_2:1391716

from LinkedList import *


class QueueList(LinkedList):
    """
    QueueList Class
    """
    def __init__(self):
        """
        Inicialitza les variables de la cua com a cua buida
        """
        LinkedList.__init__(self)

    def push(self, data):
        """
        Afegeix un element al final de la cua, incrementa el size i deixa current al nou node
        :param data: contingut a afegir a la cua
        """
        self.current = self.tail
        LinkedList.insertAfter(self, data)

    def pop(self):
        """
        Treu el primer element de la cua, decrementa el size i deixa el current al següent node de la cua
        :return: retorna l'element eliminat
        """
        
        LinkedList.moveHead(self)
        aux = LinkedList.getHead(self)
        LinkedList.remove(self)
        return aux
    

    def queueHead(self):
        """
        Retorna el contingut del primer element que sortirà de la cua
        :return: primer element de la cua
        """
        return LinkedList.getHead(self)

    def purge(self):
        """
        Buida la cua
        """
        LinkedList.clear(self)

    def __len__(self):
        """
        Retorna el nombre d'elements de la cua
        :return: nombre d'elements de la cua
        """
        return self.size
