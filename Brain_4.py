# -*- coding: latin-1 -*- # Comentari per permetre que s'utilitzin accents i carÃ cters especials als comentaris i les cadenes de text.


from pyrobot.brain import Brain

from LinkedList import * # Es suposa que LinkedList estÃ  implementada correctament.
import StackList
reload(StackList) # 'reload' serveix per forÃar a Python a carregar l'arxiu StackList i actualitzar-ne les possibles modificacions.
import Pilot
reload(Pilot)     # 'reload' serveix per forÃ§ar a Python a carregar l'arxiu Pilot i actualitzar-ne les possibles modificacions.

class WB(Brain):
    def setup(self):
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
            if posicio == 'gold':
                    self.robot.move('grab')

                
            

def INIT(engine):
    return WB('WB', engine)
