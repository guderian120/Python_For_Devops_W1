# script to read from file
with open("files/reader.txt", "r") as files:
    for file in files:
        print(file.strip())


# script to write to a file
with open("files/output.txt", "w") as file:
    file.write("This is a DevOps Module. \n")

# script to append to a file
with open("files/output.txt", "a") as file:
    file.write("This is an appended text. \n")


# writing multiple lines to a file
lines = ["This is line one. \n", "This is line two. \n"]

with open("files/multiple_output.txt", "w") as file:
    file.writelines("\n".join(lines))
