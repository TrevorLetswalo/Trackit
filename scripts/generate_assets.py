import sqlite3
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Connect to the database
conn = sqlite3.connect("backend/assets.db")
cursor = conn.cursor()

# Sample data lists
models = [
    "Dell Latitude 5500", "HP EliteBook 840", "MacBook Pro 13",
    "Lenovo ThinkPad X1", "Dell XPS 13", "Surface Laptop 4"
]
statuses = ["Active", "Inactive", "Retired"]
departments = ["Finance", "IT", "HR", "Legal", "Marketing", "Operations"]
locations = ["Johannesburg", "Cape Town", "Durban", "Pretoria", "Sandton"]

# Generate and insert 300 fake assets
for i in range(1, 301):
    asset_tag = f"LT{i:04d}"
    model = random.choice(models)
    assigned_to = fake.first_name()
    status = random.choice(statuses)
    last_seen = fake.date_between(start_date='-6m', end_date='today')
    warranty_end = fake.date_between(start_date='today', end_date='+1y')
    department = random.choice(departments)
    location = random.choice(locations)

    cursor.execute("""
        INSERT INTO assets (AssetTag, Model, AssignedTo, Status, LastSeenDate, WarrantyEndDate, Department, Location)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        asset_tag, model, assigned_to, status,
        last_seen, warranty_end, department, location
    ))

conn.commit()
conn.close()
print("✅ Inserted 300 fake asset records into the database.")
