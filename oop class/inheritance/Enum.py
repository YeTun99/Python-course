from enum import Enum
class Suite(Enum):

    """Suits (enumeration)"""
    SPADE,HEART,CLUB,DIAMOND= range(4) #SPADE=0,HEART=1,CLUB=2,DIAMOND=3

class Card:
    """card"""
    def __init__(self,suite,face):
        self.suite=suite
        self.face=face
    
    def __repr__(self):
        suites='SHCD'
        faces=['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
        # Get the corresponding characters according 
        return f'{suites[self.suite.value]}{faces[self.face]}'
    
#https://symbl.cc/e
card1=Card(Suite.SPADE,5)
card2=Card(Suite.HEART,13)
print(Suite.SPADE)
print(card1,card2)