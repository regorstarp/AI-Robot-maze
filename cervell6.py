from math import *
from StackList import * #change this to the name of the stack you implemented

import Pilot;Pilot=reload(Pilot) #change this to the name of the pilot you implemented

from pyrobot.brain import Brain
from pyrobot.brain import avg
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
        if not(self.robot.getItem('win')):
            #fill in
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
            if posicio == 'gold':
                    self.robot.move('grab')

        else:
            self.saveMap(os.path.dirname(os.path.realpath(__file__))+'/maze_map.txt')

def INIT(engine):
    return WB('WB', engine)

