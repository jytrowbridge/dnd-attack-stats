def probOr(prob1, prob2):
    """
    Return probability of prob1 or prob2

    Equivalent to the probability of them both not happening
    """
    prob = probInv(
            probAnd(
                probInv(prob1), 
                probInv(prob2)))
    return prob if prob <= 1 else 1

def probInv(prob):
    return 1 - prob

def probAnd(prob1, prob2):
    prob = prob1 * prob2
    return prob if prob <= 1 else 1

def avgDieRoll(die):
    return (((die*(die + 1)) / 2) / die)

def probDieRoll(modifier, die):
    prob = (die - modifier) / die
    return prob if prob <= 1 else 1