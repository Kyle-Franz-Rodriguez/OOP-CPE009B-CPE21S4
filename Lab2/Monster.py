from Boss import Boss

class Monster(Boss):
    def __init__(self, username):
        super().__init__(username)
        self.setStr(1)
        self.setVit(-150)
        self.setInt(5)
        self.setHp(self.getHp() + self.getVit())
