def grades_stats(filename):
        stats = {}

        with open(filename, "r") as file:
            for line in file:
                if line.strip() != "":
                    student, grades_text = line.strip().split(":")
                    grades = grades_text.split(",")

                    numbers = []

                    for grade in grades:
                        numbers.append(float(grade))

                    average = sum(numbers) / len(numbers)
                    maximum = max(numbers)
                    minimum = min(numbers)

                    stats[student] = (average, maximum, minimum)

        return stats
