with open("input.txt", "r") as infile:
    # TODO: read all lines from input.txt into the list called lines_list
    lines_list = []
    for lines in infile:
        lines_list.append(lines)

if __name__ == "__main__":
    print(lines_list)
