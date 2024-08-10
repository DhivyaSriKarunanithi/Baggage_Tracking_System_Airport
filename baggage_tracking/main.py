from baggage_tracking.database import Database
from baggage_tracking.tracking import register_baggage, scan_baggage, route_baggage, notify_passenger, integrate_with_airport_systems

def main():
    db = Database()
    try:
        while True:
            print("\n--- Baggage Tracing System ---")
            print("1. Register Baggage")
            print("2. Scan Baggage")
            print("3. Route Baggage")
            print("4. Notify Passenger")
            print("5. Integrate with Airport Systems")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                register_baggage(db)
            elif choice == '2':
                scan_baggage(db)
            elif choice == '3':
                route_baggage(db)
            elif choice == '4':
                notify_passenger(db)
            elif choice == '5':
                integrate_with_airport_systems(db)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
