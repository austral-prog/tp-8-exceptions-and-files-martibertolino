def read_lines(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            linea_limpia = line.strip()

            if linea_limpia != "":
                lines.append(linea_limpia)
    return lines
