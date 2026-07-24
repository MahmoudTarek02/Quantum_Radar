from observation import Observation
from violation import Violation
from rules import Rule

class RuleEngine:
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def evaluate(self, observation: Observation) -> list[Violation]:
        violations = []
        for rule in self.rules:
            violation = rule.evaluate(observation)
            if violation is not None:
                violations.append(violation)
        return violations
