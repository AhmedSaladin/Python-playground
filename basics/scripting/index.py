camelot_lines = []
with open("scripting/camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)