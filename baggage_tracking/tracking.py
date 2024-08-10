from .database import Database

def register_baggage(db: Database):
    passenger_name = input("Enter passenger name: ")
    flight_number = input("Enter flight number: ")
    baggage_id = input("Enter baggage ID: ")
    db.register_baggage(passenger_name, flight_number, baggage_id)
    print(f"Baggage {baggage_id} registered for {passenger_name} on flight {flight_number}.")

def scan_baggage(db: Database):
    baggage_id = input("Enter scanned baggage ID: ")
    status = input("Enter baggage status (e.g., Checked-In, Loaded, Unloaded, Delivered): ")
    valid_statuses = {'Checked-In', 'Loaded', 'Unloaded', 'Delivered'}
    if status in valid_statuses:
        db.update_baggage_status(baggage_id, status)
        print(f"Baggage {baggage_id} status updated to {status}.")
    else:
        print("Invalid status. Please enter a valid status.")

def route_baggage(db: Database):
    baggage_id = input("Enter baggage ID for routing: ")
    info = db.get_baggage_info(baggage_id)
    if info:
        print(f"Baggage {baggage_id} is routed for flight {info[2]}. Current status: {info[4]}.")
    else:
        print("Baggage not found.")

def notify_passenger(db: Database):
    baggage_id = input("Enter baggage ID for notification: ")
    info = db.get_baggage_info(baggage_id)
    if info:
        print(f"Notification sent to {info[1]}: Your baggage {baggage_id} is currently {info[4]}.")
    else:
        print("Baggage not found.")

def integrate_with_airport_systems(db: Database):
    print("Integration with Departure Control Systems is simulated.")
