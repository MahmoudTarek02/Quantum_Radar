from car_type import CarType
from observation import Observation
from rules import TruckSpeedRule, PrivateSpeedRule, SeatbeltRule
from rule_engine import RuleEngine
from fine_repository import FineRepository
from radar import Radar

def main():
    rules = [
        TruckSpeedRule(),
        SeatbeltRule(),
        PrivateSpeedRule()
    ]
    
    rule_engine = RuleEngine(rules)
    repository = FineRepository()
    radar = Radar(rule_engine, repository)
    
    observations = [
        Observation(
            plate_number="ABC1234",
            date_time="2026-07-24 12:00",
            car_type=CarType.PRIVATE,
            speed=94.0,
            seatbelt_fastened=False
        ),
        Observation(
            plate_number="TRK5678",
            date_time="2026-07-24 2:05",
            car_type=CarType.TRUCK,
            speed=75.0,
            seatbelt_fastened=True
        ),
        Observation(
            plate_number="BUS9999",
            date_time="2026-07-24 3:10",
            car_type=CarType.BUS,
            speed=90.0,
            seatbelt_fastened=False
        ),
        Observation(
            plate_number="OKC4321",
            date_time="2026-07-24 4:00",
            car_type=CarType.PRIVATE,
            speed=75.0,
            seatbelt_fastened=True
        ),
        Observation(
            plate_number="BELT111",
            date_time="2026-07-24 5:00",
            car_type=CarType.PRIVATE,
            speed=50.0,
            seatbelt_fastened=False
        ),
        Observation(
            plate_number="TRK1111",
            date_time="2026-07-24 6:00",
            car_type=CarType.TRUCK,
            speed=55.0,
            seatbelt_fastened=True
        )
    ]
    
    for observation in observations:
        radar.observe(observation)
        
    print("All fines:")
    all_fines = repository.get_all_fines_summary()
    for plate, total in all_fines:
        print(f"{plate}: {total} EGP")
    print()

    print("Violated rules count:")
    stats = repository.get_violation_counts()
    for rule_name, count in stats.items():
        print(f"{rule_name}: {count}")

if __name__ == "__main__":
    main()
