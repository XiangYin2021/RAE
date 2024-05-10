class ProductAggregation:
    def __init__(self) -> None:
        pass

    def aggregate_strength(self, attackers, supporters, state):
        support_value = 1
        for a in attackers:
            support_value *= 1-state[a]

        attack_value = 1
        for s in supporters:
            attack_value *= 1-state[s]

        # print(f"v_att={1-support_value}")
        # print(f"v_sup={1-attack_value}")
        # print(f"1-|sup-att|={1-abs(support_value - attack_value)}")

        return support_value - attack_value
        # return 1-support_value, 1-attack_value, support_value - attack_value

    def __str__(self) -> str:
        return __class__.__name__
