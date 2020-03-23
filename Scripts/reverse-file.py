# This script is used to create files for which we can diff daily changes

filename = "2020-03-23.txt"
fileloc = "../MOH-daily-dump/raw/" + filename
output = "../MOH-daily-dump/parsed/" + filename
for line in reversed(list(open(fileloc, 'r'))):
    read = (line.rstrip())
    with open(output, "a") as parsed_file:
        parsed_file.write(read + '\n')