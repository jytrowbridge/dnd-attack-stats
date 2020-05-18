import characters
from Enemy import Enemy
from PlayerChar import PlayerChar

def getUserInput(prompt):
    userInput = input(prompt)
    commandValueTuple = userInput.split(' ')
    command =  commandValueTuple[0]
    inputVal = None if len(commandValueTuple) == 1 else commandValueTuple[1]
    return [command, inputVal]

def main():
    ac = input('Enter enemy ac: ')
    while True:
        try:
            ac = int(ac)
            break
        except ValueError:
            ac = input('Please enter an integer: ')
    enemy = Enemy(ac)
    char = characters.chars[0]

    helpStr = ("Commands:\n" 
            +  "\tq                 :   quit\n"
            +  "\tadv               :   return stats with advantage\n"
            +  "\tadv-on            :   toggle advantage always on\n"
            +  "\tadv-off           :   toggle advantage off\n"
            +  "\tbonus-dmg <int>   :   set bonus dmg value\n"
            +  "\tac <int>          :   set enemy ac\n"
            +  "\tchar-print        :   print stats of current char\n"
            +  "\tchar-list         :   list characters in characters.py file\n"
            +  "\tchar <char>       :   change character\n"
            +  "\t[enter]           :   return stats\n"
            +  "\th                 :   print this again\n"
            + "~"
                )
    adv = False
    bonusDmg = 0
    command, inputVal = getUserInput(helpStr)
    while command != 'q':
        if command == 'adv':
            char.printAtkHitStats(enemy,adv=True,bonusDmg=bonusDmg)
        if command == 'adv-on':
            adv = True
        if command == 'adv-off':
            adv = False
        if command == 'bonus-dmg':
            try:
                bonusDmg = int(inputVal)
            except ValueError:
                print("Bonus damage value must be an integer")
        if command == 'ac':
            try:
                enemy.set_ac((int(inputVal)))
            except ValueError:
                print("AC value must be an integer")
        if command == 'char-print':
            char.printStats()
        if command == 'char-list':
            for char in characters.chars:
                print(char.get_name())
        if command == 'char':
            found = False
            for charVal in characters.chars:
                if charVal.get_name() == inputVal:
                    char = charVal
                    found = True
                    break
            if not found: print("Character not in list")
        if command == '':
            char.printAtkHitStats(enemy,adv=adv,bonusDmg=bonusDmg)
        if command == 'h':
            print(helpStr)

        command, inputVal = getUserInput("\n~")


if __name__ == "__main__":
    main()