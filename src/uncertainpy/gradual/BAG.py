import os
import re
import string
from .Argument import Argument
from .Support import Support
from .Attack import Attack


class BAG:

    def __init__(self, path=None):
    
        self.arguments = {}
        self.attacks = []
        self.supports = []
        self.origin_attacks = []
        self.origin_supports = []
        self.path = path

        if (path is None):
            pass
        else:
            with open(os.path.abspath(path), "r") as f:
                for line in f.readlines():
                    k_name = line.split("(")[0]
                    if k_name in string.whitespace:
                        pass
                    else:
                        k_args = re.findall(rf"{k_name}\((.*?)\)", line)[0].replace(" ", "").split(",")
                        if k_name == "arg":
                            argument = Argument(k_args[0], float(k_args[1]), None, [], [])
                            self.arguments[argument.name] = argument

                        elif k_name == "att":
                            attacker = self.arguments[k_args[0]]
                            attacked = self.arguments[k_args[1]]
                            self.add_attack(attacker, attacked)

                        elif k_name == "sup":
                            supporter = self.arguments[k_args[0]]
                            supported = self.arguments[k_args[1]]
                            self.add_support(supporter, supported)
        # self.origin_attacks = self.attacks.copy()
        # self.origin_supports = self.supports.copy()

    def add_attack(self, attacker, attacked):
        if type(attacker) != Argument:
            raise TypeError("attacker must be of type Argument")

        if type(attacked) != Argument:
            raise TypeError("attacked must be of type Argument")

        if attacker.name in self.arguments:
            attacker = self.arguments[attacker.name]
        else:
            self.arguments[attacker.name] = attacker

        if attacked.name in self.arguments:
            attacked = self.arguments[attacked.name]
        else:
            self.arguments[attacked.name] = attacked
            
        attacked.add_attacker(attacker)

        self.attacks.append(Attack(attacker, attacked))

    def add_support(self, supporter, supported):
        if type(supporter) != Argument:
            raise TypeError("supporter must be of type Argument")

        if type(supported) != Argument:
            raise TypeError("supported must be of type Argument")

        if supporter.name in self.arguments:
            supporter = self.arguments[supporter.name]
        else:
            self.arguments[supporter.name] = supporter

        if supported.name in self.arguments:
            supported = self.arguments[supported.name]
        else:
            self.arguments[supported.name] = supported

        supported.add_supporter(supporter)

        self.supports.append(Support(supporter, supported))

    def reset_strength_values(self):
        for a in list(self.arguments.values()):
            a.strength = a.initial_weight

    def get_arguments(self):
        return list(self.arguments.values())

    def get_attacks(self):
        return self.attacks

    def get_supports(self):
        return self.supports

    def remove_attack(self, attacker_name, attacked_name):
        for i in range(len(self.attacks)):
            if self.attacks[i].get_attacker()==self.arguments[attacker_name] and self.attacks[i].get_attacked()==self.arguments[attacked_name]:

                # delete relation
                del self.attacks[i]

                # delete argument
                self.arguments[attacked_name].remove_attacker(self.arguments[attacker_name])
                break
        return self.arguments[attacker_name]

    def remove_support(self, supporter_name, supported_name):
        for i in range(len(self.supports)):
            if self.supports[i].get_supporter()==self.arguments[supporter_name] and self.supports[i].get_supported()==self.arguments[supported_name]:

                # delete relation
                del self.supports[i]

                # delete argument
                self.arguments[supported_name].remove_supporter(self.arguments[supporter_name])
                break
        return self.arguments[supporter_name]

    def remove_argument(self, arg):
        # scan all the relations that contains arg, and delete these relations
        for i in range(len(self.supports)-1, -1, -1): # only consider acyclic case so only two if
            # print(i)
            # print(self.supports[i].get_supporter())
            if self.supports[i].get_supporter()==self.arguments[arg]:
                # delete relation

                # delete supporter
                self.supports[i].get_supported().remove_supporter(self.arguments[arg])
                del self.supports[i]
            elif self.supports[i].get_supported()==self.arguments[arg]:

                self.arguments[arg].remove_supporter(self.supports[i].get_supporter())
                del self.supports[i]
        for i in range(len(self.attacks)-1, -1, -1): # only consider acyclic case so only two if
            if self.attacks[i].get_attacker()==self.arguments[arg]:
                # delete relation

                # delete attacker
                self.attacks[i].get_attacked().remove_attacker(self.arguments[arg])
                del self.attacks[i]
            elif self.attacks[i].get_attacked()==self.arguments[arg]:

                self.arguments[arg].remove_attacker(self.attacks[i].get_attacker())
                del self.attacks[i]
        # scan all the arguments and delete the specific argument
        del self.arguments[arg]


    # def recover_attack(self):
    #     self.attacks = self.origin_attacks.copy()
    # def recover_support(self):
    #     self.supports = self.origin_supports.copy()

    def __str__(self) -> str:
        return f"BAG set to read from {self.path} with arguments: {self.arguments}, attacks: {self.attacks} and supports: {self.supports}"

    def __repr__(self) -> str:
        return f"BAG({self.path}) Arguments: {self.arguments} Attacks: {self.attacks} Supports: {self.supports}"
