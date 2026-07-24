class Violation:
    def __init__(self, rule_name: str, description: str, fine_amount: int):
        self.rule_name = rule_name
        self.description = description
        self.fine_amount = fine_amount
