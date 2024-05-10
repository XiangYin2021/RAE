class TopAggregation:
    def __init__(self) -> None:
        pass

    def aggregate_strength(self, attackers, supporters, state):
        aggregate_neg = 0
        aggregate_pos = 0

        for a in attackers:
            if state[a] > aggregate_neg:
                aggregate_neg = state[a]

        for s in supporters:
            if state[s] > aggregate_pos:
                aggregate_pos = state[s]

        return aggregate_pos - aggregate_neg
    
    def __str__(self) -> str:
        return __class__.__name__
