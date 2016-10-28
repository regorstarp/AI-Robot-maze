# -*- coding: latin-1 -*- # Comentari per permetre que s'utilitzin accents i carÃ cters especials als comentaris i les cadenes de text.
# Eduard Campo Raurich  1390690
# Roger Prats Llivina  1391716

from pyrobot.brain import Brain

from LinkedList import * # Es suposa que LinkedList estÃ  implementada correctament.
import StackList
reload(StackList) # 'reload' serveix per forÃar a Python a carregar l'arxiu StackList i actualitzar-ne les possibles modificacions.
import Pilot
reload(Pilot)     # 'reload' serveix per forÃ§ar a Python a carregar l'arxiu Pilot i actualitzar-ne les possibles modificacions.
import os

class WB(Brain):
    def saveMap(self,fname):
        """
        Method that stores a boolean matrix as a text file.
        :param fname: a string containing the full path to the filename
        """
        bool2str={True:'T',False:'F'}
        rows=[''.join([bool2str[col] for col in line]) for line in self.__map]
        open(fname,'w').write('\n'.join(rows))
    
    def setup(self):
        """
        Initialization
        """
        # Adding functionality for recording the map
        self.cols = 12 #same as world cols
        self.rows = 12 #same as world rows
        self.__map = [[0 for y in range(self.cols)] for x in range(self.rows)]
        yx = self.robot.getItem('location')
        self.__map[self.rows-yx[1]][yx[0]-1]= 1
        #fill in
        self.stack = StackList.StackList()
        self.pilot = Pilot.Pilot()
        self.robot.move('reset')
    def step(self):
        self.pilot.setSonar(self.robot.getItem('sonar'))
        if not self.robot.getItem('win'):
            if self.pilot.isCrossRoad():#si ens trobem en una bifurcacio
                if self.pilot.getCulDeSac(): #bifurcacio ia visitada
                    culdesac,moviment = self.stack.pop()
                    self.pilot.setCulDeSac(culdesac)  
                else: #bifurcacio no visitada
                    accions = self.pilot.possibleActions()
                    while(accions.__len__() != 0):#mentre accions no es buida
                        self.stack.push(accions.pop())
                    culdesac,moviment = self.stack.pop()
                mov = moviment
            else:
                if self.stack.__len__() == 0: #per poder recorrer el laberint una vegada tenim tor l'or
                    self.pilot.setCulDeSac(False)
                mov = self.pilot.nextMove()
            posicio = self.robot.move(self.pilot.moveTo(mov)) #ens movem
            yx = self.robot.getItem('location')#actualitzem la posició
            self.__map[self.rows-yx[1]][yx[0]-1]= 1
            if posicio == 'gold':
                    self.robot.move('grab')
        else:
            self.saveMap(os.path.dirname(os.path.realpath(__file__))+'/maze_map.txt') #save the map
                
            

def INIT(engine):
    return WB('WB', engine)
