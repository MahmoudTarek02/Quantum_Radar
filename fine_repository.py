from collections import defaultdict
from fine import Fine

class FineRepository:
    def __init__(self):
        self.fines = []

    def add_fine(self, fine: Fine):
        
        self.fines.append(fine)

    def get_all_fines(self) -> list[Fine]:

        return self.fines

    def get_all_fines_summary(self) -> list[tuple[str, int]]:


        return [(fine.plate_number, fine.total_amount) for fine in self.fines]

    def get_violation_counts(self) -> dict[str, int]:

        counts = defaultdict(int)

        for fine in self.fines:

            for violation in fine.violations:
                counts[violation.rule_name] += 1

        return dict(counts)
