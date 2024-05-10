class Support:
    def __init__(self, supporter, supported) -> None:
        self.supporter = supporter
        self.supported = supported

    def get_supporter(self):
        return self.supporter

    def get_supported(self):
        return self.supported

    def __repr__(self) -> str:
        return f"Support({self.supporter}, {self.supported})"

    def __str__(self) -> str:
        return f"Support by {self.supporter} to {self.supported}"