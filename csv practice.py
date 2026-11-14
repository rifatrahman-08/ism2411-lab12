# Exercise 2:
import csv

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)


    rows = list(reader)


    for row in rows:
        print(row)

# Exercise 3:
import csv


header = rows[0]
data = rows[1:]


print("Header:", header)


for row in data:
    print(row)
# Exercise 4
total_revenue = 0


for row in data:
    product = row[0]
    price = float(row[1])
    quantity = int(row[2])


    total = price * quantity
    total_revenue += total


    print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")


print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5:


written_count = 0


with open("data/cleaned.csv", "w", newline="") as file:
    writer = csv.writer(file)


    writer.writerow(["Product", "Price", "Qty", "Total"])


    for row in data:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])


        total = price * quantity


        if total > 100:
            writer.writerow([product, price, quantity, total])
            written_count += 1


print("Rows written:", written_count)
print("Original rows:", len(data))
