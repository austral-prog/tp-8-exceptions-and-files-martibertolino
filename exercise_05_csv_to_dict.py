def csv_to_dict(filename):
    people = []

    with open(filename, "r") as file:
        lines = file.readlines()

    if len(lines) <= 1:
        return []

    headers = lines[0].strip().split(",")
    for line in lines[1:]:
        if line.strip() != "":
                values = line.strip().split(",")
                person = {}
                person[headers[0]] = values[0].strip()
                person[headers[1]] = int(values[1].strip())
                person[headers[2]] = values[2].strip()

                people.append(person)

    return people
