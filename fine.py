from violation import Violation

class Fine:
    def __init__(self, plate_number: str, violations: list[Violation]):

        self.plate_number = plate_number

        self.violations = violations

    @property
    def total_amount(self) -> int:

        return sum(violation.fine_amount for violation in self.violations)

    def __str__(self) -> str:
        lines = [
            f"Traffic fine for car {self.plate_number}",
            f"Total amount: {self.total_amount} EGP",
            "Violations:"
        ]
        for violation in self.violations:

            if "exceeded max" in violation.description:
                lines.append(f"- {violation.description}: {violation.fine_amount} EGP")
                
            else:
                
                lines.append(f"- {violation.description} : {violation.fine_amount} EGP")
        return "\n".join(lines)
