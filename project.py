import csv
import uuid
import os
from datetime import datetime

FILENAME = "transactions.csv"

def main():
    while True:
        print("\n=== Budget Tracker ===")
        print("1. Add transaction")
        print("2. View all transactions")
        print("3. View transactions by date range")
        print("4. Monthly summary")
        print("5. Delete transaction by ID")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format.")
                continue

            description = input("Description: ")
            category = input("Category: ")
            try:
                amount = float(input("Amount (use negative for expenses): "))
            except ValueError:
                print("Invalid amount.")
                continue
            add_transaction(date, description, category, amount)

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            view_transactions_by_date(start, end)

        elif choice == "4":
            summarize_by_month()

        elif choice == "5":
            tid = input("Enter transaction ID to delete: ")
            delete_transaction(tid)

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


def add_transaction(date, description, category, amount):
    tid = str(uuid.uuid4())
    write_header = not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0
    try:
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(["ID", "Date", "Description", "Category", "Amount"])
            writer.writerow([tid, date, description, category, amount])
        print("Transaction added successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")


def view_transactions():
    balance = 0.0
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            headers = next(reader, None)  
            print("\nID\t\tDate\t\tDescription\tCategory\tAmount")
            print("-" * 80)
            for row in reader:
                tid, date, desc, cat, amt = row
                balance += float(amt)
                print(f"{tid[:8]}...\t{date}\t{desc:<12}\t{cat:<10}\t${float(amt):.2f}")
            print(f"\nRunning Balance: ${balance:.2f}")
    except FileNotFoundError:
        print("No transactions yet.")


def view_transactions_by_date(start, end):
    try:
        start_date = datetime.strptime(start, "%Y-%m-%d").date()
        end_date = datetime.strptime(end, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return

    print(f"\nTransactions from {start} to {end}:")
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            headers = next(reader, None)  
            found = False
            for row in reader:
                tid, date_str, desc, cat, amt = row
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                if start_date <= date <= end_date:
                    print(f"{date} | {desc} | {cat} | ${float(amt):.2f}")
                    found = True
            if not found:
                print("No transactions in that range.")
    except FileNotFoundError:
        print("No transactions to filter.")


def summarize_by_month():
    summary = {}
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            headers = next(reader, None)  
            for row in reader:
                _, date_str, _, _, amt = row
                date = datetime.strptime(date_str, "%Y-%m-%d")
                key = date.strftime("%Y-%m")
                summary[key] = summary.get(key, 0) + float(amt)

        if summary:
            print("\nMonthly Summary:")
            for month, total in sorted(summary.items()):
                print(f"{month}: ${total:.2f}")
        else:
            print("No transactions to summarize.")
    except FileNotFoundError:
        print("No transactions to summarize.")


def delete_transaction(tid):
    try:
        transactions = []
        found = False
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            transactions.append(headers)
            for row in reader:
                if row[0] != tid:
                    transactions.append(row)
                else:
                    found = True

        if found:
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(transactions)
            print("Transaction deleted.")
        else:
            print("Transaction ID not found.")
    except FileNotFoundError:
        print("No transactions to delete.")

if __name__ == "__main__":
    main()
