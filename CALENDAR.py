import datetime

# A dictionary to store events. Key: (year, month, day), Value: event_name
events = {}

def main():
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add an Event")
        print("2. View Events on a Date")
        print("3. View All Events")
        print("4. Delete an Event")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            print("\n--- ADD AN EVENT ---")
            print("Enter the date:")
            
            try:
                year = int(input("Year(2026-2028): "))
                month = int(input("Month (1-12): "))
                day = int(input("Day: "))
                event_name = input("Enter event name: ")

                # Store the event
                events[(year, month, day)] = event_name

                # Format date for the success message
                date_obj = datetime.date(year, month, day)
                formatted_date = date_obj.strftime("%B %d, %Y")

                print(f"\n[SUCCESS] Event '{event_name}' Added on {formatted_date}!")
            
            except ValueError:
                print("[ERROR] Please enter valid numbers for the date.")

        elif choice == '2':
            # Placeholder for viewing specific dates
            print("\nFunctionality coming soon!")
            
        elif choice == '3':
            # View all events
            if not events:
                print("\nNo events found.")
            else:
                print("\n--- ALL EVENTS ---")
                for (y, m, d), name in events.items():
                    print(f"{y}-{m:02d}-{d:02d}: {name}")

        elif choice == '4':
            # Placeholder for deleting
            print("\nFunctionality coming soon!")

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
