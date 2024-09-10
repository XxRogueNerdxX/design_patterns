
class HeroStats(object): 
    def __init__(self, name) -> None:
        self.name = name
        self.attack = 100
        self.defence = 50 
        self.health = 100
    
    def __str__(self) -> str:
        return f"Attack : {self.attack} \n Defence: {self.defence} \n Health: {self.health}"


class BasicGameObject(object): 
    def __init__(self, nextHandler=None) -> None:
        self.nextHandler = nextHandler
    
    def handle(self, game_object:HeroStats):
        if self.nextHandler: 
            self.nextHandler.handle(game_object) 

class ChainSword(BasicGameObject): 
    def handle(self, hero_game_obj:HeroStats):
        hero_game_obj.attack += 10 
        hero_game_obj.defence -= 5
        print(hero_game_obj)
        return super().handle(hero_game_obj)

class ArmourOfGod(BasicGameObject): 
    def handle(self, game_object: HeroStats):
        game_object.attack -= 10
        game_object.defence += 100
        print(game_object)
        return super().handle(game_object)

class Asiprine(BasicGameObject): 
    def handle(self, game_object: HeroStats):
        game_object.health += 100
        print(game_object)
        return super().handle(game_object)
    


titus_game_obj = HeroStats("Titus") 
chain_sword = ChainSword() 
armour_of_god = ArmourOfGod(chain_sword)
aspirin = Asiprine(armour_of_god)
aspirin.handle(titus_game_obj)





