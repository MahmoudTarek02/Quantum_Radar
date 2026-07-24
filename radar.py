from observation import Observation
from rule_engine import RuleEngine
from fine_repository import FineRepository
from fine import Fine

class Radar:
    def __init__(self, rule_engine: RuleEngine, repository: FineRepository):
        self.rule_engine = rule_engine
        self.repository = repository

    def observe(self, observation: Observation):
        violations = self.rule_engine.evaluate(observation)
        if violations:
            fine = Fine(observation.plate_number, violations)
            self.repository.add_fine(fine)
            print(fine)
