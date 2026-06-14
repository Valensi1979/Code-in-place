"""
Transaction Data Generator
Generates a realistic CSV file of payment transactions for testing
the Payment Transaction Analyser.
"""

import csv
import random

def generate_transactions(num_transactions):
    """Generate a list of realistic payment transactions."""
    
    merchants = [
        "Amazon", "Apple", "Mercadona", "Booking.com", "Glovo",
        "El Corte Ingles", "Zara", "Netflix", "Spotify", "Uber",
        "Repsol", "Ikea", "MediaMarkt", "Decathlon", "Carrefour",
        "Airbnb", "Renfe", "Iberia", "PayPal", "Google"
    ]
    
    currencies = ["EUR", "EUR", "EUR", "EUR", "USD", "GBP"]
    
    dates = [
        "2026-01-01", "2026-01-15", "2026-02-01", "2026-02-15",
        "2026-03-01", "2026-03-15", "2026-04-01", "2026-04-15",
        "2026-05-01", "2026-05-15"
    ]
    
    transactions = []
    for i in range(1, num_transactions + 1):
        transaction = {
            "id": f"tx_{i:04d}",
            "amount": random.choice([
                random.randint(10, 500),    # Most transactions small
                random.randint(10, 500),
                random.randint(10, 500),
                random.randint(500, 5000),  # Occasional large ones
            ]),
            "currency": random.choice(currencies),
            "merchant": random.choice(merchants),
            "date": random.choice(dates)
        }
        transactions.append(transaction)
    
    # Inject deliberate duplicates so detector has something to find
    for _ in range(20):
        original = random.choice(transactions)
        duplicate = {
            "id": f"tx_{len(transactions) + 1:04d}",
            "amount": original["amount"],
            "currency": original["currency"],
            "merchant": original["merchant"],
            "date": original["date"]
        }
        transactions.append(duplicate)
    
    return transactions

def save_to_csv(transactions, filename):
    """Save transactions list to a CSV file."""
    fieldnames = ["id", "amount", "currency", "merchant", "date"]
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
    print(f"Generated {len(transactions)} transactions → {filename}")

def main():
    num = int(input("How many transactions to generate? "))
    filename = input("Output filename (e.g. large_transactions.csv): ")
    transactions = generate_transactions(num)
    save_to_csv(transactions, filename)

if __name__ == '__main__':
    main()