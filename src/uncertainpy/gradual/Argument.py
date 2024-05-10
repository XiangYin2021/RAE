class Argument:
    def __init__(self, name, initial_weight, strength=None, attackers=None, supporters=None, strength_att=None, strength_sup=None):
        self.name = name
        self.initial_weight = initial_weight
        self.strength = strength
        self.attackers = attackers
        self.supporters = supporters
        self.origin_attackers = self.attackers.copy()
        self.origin_supporters = self.supporters.copy()
        self.strength_att = strength_att
        self.strength_sup = strength_sup
        if type(initial_weight) != int and type(initial_weight) != float:
            raise TypeError("initial_weight must be of type integer or float")

        if strength is None:
            self.strength = initial_weight

        if attackers is None:
            self.attackers = []
        
        if supporters is None:
            self.supporters = []

    def get_name(self):
        return self.name

    def get_all_attacker(self):
        return self.attackers

    def get_all_supporter(self):
        return self.supporters

    def add_attacker(self, attacker):
        self.attackers.append(attacker)

    def add_supporter(self, supporter):
        self.supporters.append(supporter)

    def remove_attacker(self, attacker):
        self.attackers.remove(attacker)

    def remove_supporter(self, supporter):
        self.supporters.remove(supporter)

    # def recover_attacker(self):
    #     self.attackers = self.origin_attackers
    #
    # def recover_supporter(self):
    #     self.supporters = self.origin_supporters

    def get_initial_weight(self):
        return self.initial_weight

    def get_strength(self):
        return self.strength
    
    def reset_initial_weight(self, weight):
        self.initial_weight = weight
        
    def __repr__(self) -> str:
        return f"Argument {self.name}: initial weight {self.initial_weight}, strength {self.strength}, attackers {self.attackers}, supporters {self.supporters}"

    def __str__(self) -> str:
        return f"Argument(name={self.name}, weight={self.initial_weight}, strength={self.strength})"
