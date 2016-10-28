#-*- coding: latin-1 -*- # Comentari per permetre que s'utilitzin accents i caràcters especials als comentaris i les cadenes de text.
from QueueList import *
class Pilot(object):
    __slots__ = ['__previous', '__sonar', '__inverse', '__culdesac']
    def __init__(self):
        """ Constructor de la classe.
            Paràmatres:
            __previous guarda l'últim moviment que ha fet el robot
            __sonar guarda un diccionari amb informació de quines posicions contigües a la que es troba el robot estan lliures
            __inverse diccionari que guarda informacio de quin es el moviment contrari a una direcció donada
            __culdesac booleà que guarda informació sobre si ens hem trobat en cul de sac o no
        """
        self.__previous = None
        self.__sonar = {}
        self.__inverse = {'left' : 'right', 'right' : 'left', 'up' : 'down', 'down' : 'up'}
        self.__culdesac = False
    def getPrevious(self): return self.__previous
    def setSonar(self, sonar): self.__sonar = dict(sonar) # Fa una copia del diccionari, no una referència.
    def isCrossRoad(self): return sum(self.__sonar.values()) > 2
    def getCulDeSac(self): return self.__culdesac
    def setCulDeSac(self, culdesac): self.__culdesac = culdesac

    def moveTo(self, action):
        """ Funció que comprova si el robot es pot moure seguint la direcció que indica el paràmetre action """
        if action == 'up' or action == 'down' or action == 'right' or action == 'left':
            if self.__sonar[action]:
                self.__previous = self.__inverse[action]
                return action
            else:
                raise ValueError ('No es pot moure')
        else:
            raise ValueError ('Direccio incorrecte')
        
    def nextMove(self):
        """ Funció que retorna la direcció que ha de seguir el robot per anar a la següent casella sense tornar enrere """
        sonar2 = dict(self.__sonar)
        sonar2[self.__previous] = False
        if sonar2.values().count(True) == 0:
            self.__culdesac = True
            return self.__previous
        else:
            for key in sonar2:
                if sonar2[key] :
                    self.__previous = key
                    return key
        
    def possibleActions(self):
        """ Funcio que retorna tots els moviments que pot realitzar el robot en un determinat punt """
        cua_actions = QueueList()
        tupla = (True, self.__previous)
        cua_actions.push(tupla) #head

        for key in self.__sonar:
            if key != self.__previous and self.__sonar[key]: #posar a fals tots els possibles moviments menys el previ
                tupla = (False, key)
                cua_actions.push(tupla)
        
        return cua_actions

        
