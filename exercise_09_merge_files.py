def merge_files(file1, file2, output):
    with open(file1, "r") as first_file:
        content1 = first_file.read()

    with open(file2, "r") as second_file:
        content2 = second_file.read()

    with open(output, "w") as output_file:
        output_file.write(content1 + content2)
