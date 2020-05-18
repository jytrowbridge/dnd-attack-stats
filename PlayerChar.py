import math

from Enemy import Enemy
import helperFuncs
import probFuncs

class PlayerChar:
    def __init__(self, atkMod, dmgDie, proficient=True, dualWield=False, name=None):
        self.atkMod = atkMod
        self.dmgDie = dmgDie
        self.proficient = proficient
        self.dualWield = dualWield
        self.name = name

    def getAtkHitStats(self, enemy, adv=False, bonusDmg=0):
        """
        given instance of Enemy or an int representing armor class, 
        return odds of hitting and how much damage
        """
        if type(enemy) is not Enemy and type(enemy) is not int:
            print("Please provide instance of Enemy class or an int representing armor class")

        ac = enemy if type(enemy) is int else enemy.get_ac()
        profBonus = 2 if self.get_proficient() else 0
        
        avgDmg = probFuncs.avgDieRoll(self.get_dmgDie()) + self.get_atkMod() + bonusDmg
        
        #probToHit = (20 - ac + self.get_atkMod() + profBonus) / 20
        probToHit = probFuncs.probDieRoll(ac - self.get_atkMod() - profBonus, 20)
        if adv: probToHit = probFuncs.probOr(probToHit, probToHit)

        avgDmgPerRound = probToHit * avgDmg
        
        statsDic = {
            'enemyAc'           : ac
        ,   'avgDmg'            : avgDmg
        ,   'avgDmgPerRound'    : avgDmgPerRound
        ,   'probToHit'         : probToHit
        }

        if self.get_dualWield():
            probToHitEither = probFuncs.probOr(probToHit, probToHit)
            probToHitBoth = probFuncs.probAnd(probToHit, probToHit)
            avgDmgOffHand = probFuncs.avgDieRoll(self.get_dmgDie()) + bonusDmg
            avgDmgPerRound = (probToHit * avgDmg) + (probToHit * avgDmgOffHand)
            statsDic['probToHitEither']   = probToHitEither
            statsDic['probToHitBoth']     = probToHitBoth
            statsDic['avgDmgOffHand']     = avgDmgOffHand
            statsDic['avgDmgPerRound']     = avgDmgPerRound

        return statsDic

    def simulateRound(self, enemy, adv=False, bonusDmg=0):
        # statsDic = self.getAtkHitStats(self, enemy, adv)

        # probToHit       = statsDic['probToHit']
        # avgDmg          = statsDic['avgDmg']
        # avgDmgOffHand   = statsDic['avgDmgOffHand']      

        return

    def printAtkHitStats(self, enemy, adv=False, bonusDmg=0):
        if adv: print('With advantage')
        statsDic = self.getAtkHitStats(enemy, adv, bonusDmg)
        lenToColon = helperFuncs.getMaxDicKeyLen(statsDic) + 4
        for k,v in statsDic.items():
            if type(v) is float: v = round(v,2)
            spaces = (lenToColon - len(k)) * ' '
            print('{k}{spaces}: {v}'.format(k=str(k), spaces=spaces, v=str(v)))
        return

    def printStats(self):
        print('Name: '              + str(self.get_name()))
        print('Attack modifier: '   + str(self.get_atkMod()))
        print('Proficiency: '       + str(self.get_proficient()))
        print('Damage Die: '        + str(self.get_dmgDie()))
        print('Dual Wield: '        + str(self.get_dualWield()))

    def get_name(self):
        return self.name
    
    def get_atkMod(self):
        return self.atkMod

    def get_proficient(self):
        return self.proficient

    def get_dmgDie(self):
        return self.dmgDie

    def get_dualWield(self):
        return self.dualWield