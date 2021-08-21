camelot_lines = []
with open("scripting/camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)


def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    with open("scripting/flying_circus_cast.txt") as file:
        # use the for loop syntax to process each line
        for line in file:
            # and add the actor name to cast_list
            cast_list.append(line.split(",")[0])
    return cast_list


cast_list = create_cast_list("flying_circus_cast.txt")
for actor in cast_list:
    print(actor)
