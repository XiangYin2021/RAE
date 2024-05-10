class SQDFQUADInfluence:
    def __init__(self, conservativeness) -> None:
        self.conservativeness = conservativeness

    def compute_strength(self, weight, aggregate):
        strength = weight

        scaled_aggregate = aggregate / self.conservativeness
        if scaled_aggregate >= 0:
            h = scaled_aggregate / (1 + scaled_aggregate)
        else:
            h = scaled_aggregate / (1 - scaled_aggregate)
        if (aggregate > 0):
            strength += h * (1 - weight)
        else:
            strength += h * weight

        return strength

    def __str__(self) -> str:
        return __class__.__name__ + f"({self.conservativeness})"
