from Swordsman import Swordsman
from Archer import Archer
from Mage import Mage

class Boss(Swordsman,Archer,Mage):
    def __init__(self, username):
        super().__init__(username)
        self.setStr(15)
        self.setVit(50)
        self.setInt(15)
        self.setHp(self.getHp() + self.getVit())
