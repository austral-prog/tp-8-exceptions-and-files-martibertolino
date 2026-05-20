def read_sales(filename):
    sales = {}

    with open(filename, "r") as file:
        content = file.read()

    items = content.split(";")

    for item in items:
        if item.strip() != "":
            product, value = item.split(":")
            value = float(value)

            if product in sales:
                sales[product].append(value)
            else:
                sales[product] = [value]

    return sales

def process_sales(data):
    for product in data:
        total = sum(data[product])
        average = total / len(data[product])

        print(f"{product}: ventas totales ${total:.2f}, promedio ${average:.2f}")
