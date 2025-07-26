import csv

# Settings
OVERTIME_RATE = 200  # Set your desired hourly rate here

# Data structure: { 'Employee Name': [ { 'date': str, 'status': str, 'overtime': float } ] }
attendance_data = {}

def add_attendance():
    name = input("Enter employee name: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    status = input("Enter attendance (Present/Absent): ").strip().title()
    overtime = 0.0
    
    if status == "Present":
        try:
            overtime = float(input("Enter overtime hours (0 if none): ").strip())
        except ValueError:
            print("Invalid overtime. Defaulting to 0.")
            overtime = 0.0
    
    record = {'date': date, 'status': status, 'overtime': overtime}
    
    if name not in attendance_data:
        attendance_data[name] = []
    attendance_data[name].append(record)
    print("Attendance added.")

def view_summary():
    for name, records in attendance_data.items():
        presents = sum(1 for r in records if r['status'] == "Present")
        absents = sum(1 for r in records if r['status'] == "Absent")
        total_overtime = sum(r['overtime'] for r in records if r['status'] == "Present")
        overtime_pay = total_overtime * OVERTIME_RATE
        print(f"\n{name}:")
        print(f"  Presents: {presents}")
        print(f"  Absents: {absents}")
        print(f"  Overtime hours: {total_overtime}")
        print(f"  Overtime pay: {overtime_pay:.2f}")

def save_to_file(filename="attendance.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Status", "Overtime"])
        for name, records in attendance_data.items():
            for rec in records:
                writer.writerow([name, rec['date'], rec['status'], rec['overtime']])
    print(f"Data saved to {filename}.")

def load_from_file(filename="attendance.csv"):
    global attendance_data
    attendance_data = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name, date, status, overtime = row['Name'], row['Date'], row['Status'], float(row['Overtime'])
                if name not in attendance_data:
                    attendance_data[name] = []
                attendance_data[name].append({'date': date, 'status': status, 'overtime': overtime})
        print(f"Data loaded from {filename}.")
    except FileNotFoundError:
        print("No saved data found.")

def menu():
    while True:
        print("\nEmployee Attendance Tracker")
        print("1. Add new attendance")
        print("2. View summary report")
        print("3. Save data to file")
        print("4. Load data from file")
        print("5. Exit")
        choice = input("Select an option: ").strip()
        if choice == '1':
            add_attendance()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            save_to_file()
        elif choice == '4':
            load_from_file()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
