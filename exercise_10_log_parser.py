def parse_log(filename):
    logs = {}

    with open(filename, "r") as file:
        for line in file:
            clean_line = line.strip()

            if clean_line != "":
                if ":" not in clean_line:
                    raise ValueError("invalid log line")

                level, message = clean_line.split(":", 1)

                level = level.strip()
                message = message.strip()

                if level in logs:
                    logs[level].append(message)
                else:
                    logs[level] = [message]

    return logs
