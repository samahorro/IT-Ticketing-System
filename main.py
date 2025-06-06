import json
import os

TICKET_FILE = "tickets.json"

# Load tickets from JSON file, safely handle empty or invalid JSON
def load_tickets():
    if os.path.exists(TICKET_FILE):
        try:
            with open(TICKET_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # File is empty or corrupted, return empty list
            return []
    return []

# Save tickets to JSON file
def save_tickets(tickets):
    with open(TICKET_FILE, "w") as file:
        json.dump(tickets, file, indent=4)

# Create a new ticket
def create_ticket(tickets):
    name = input("Enter your name: ")
    issue = input("Describe the issue: ")
    priority = input("Enter priority (Low, Medium, High): ")

    ticket_id = len(tickets) + 1
    ticket = {
        "ticket_id": ticket_id,
        "name": name,
        "issue": issue,
        "priority": priority.capitalize(),
        "status": "Open"
    }

    tickets.append(ticket)
    save_tickets(tickets)
    print(f"\n✅ Ticket #{ticket_id} created successfully!\n")

# View all tickets
def view_tickets(tickets):
    if not tickets:
        print("No tickets found.\n")
        return
    print("\n--- All Tickets ---")
    for t in tickets:
        print(f"ID: {t['ticket_id']}, Name: {t['name']}, Issue: {t['issue']}, Priority: {t['priority']}, Status: {t['status']}")
    print()

# Mark a ticket as resolved
def resolve_ticket(tickets):
    ticket_id = input("Enter ticket ID to resolve: ")
    found = False
    for ticket in tickets:
        if str(ticket["ticket_id"]) == ticket_id:
            ticket["status"] = "Resolved"
            save_tickets(tickets)
            print(f"\n✅ Ticket #{ticket_id} marked as resolved.\n")
            found = True
            break
    if not found:
        print("❌ Ticket not found.\n")

# Main menu loop
def main():
    tickets = load_tickets()

    while True:
        print("=== IT Help Desk Ticketing System ===")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Resolve Ticket")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            create_ticket(tickets)
        elif choice == "2":
            view_tickets(tickets)  # fixed typo here
        elif choice == "3":
            resolve_ticket(tickets)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
