# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def line_number(filename):
    try:
        file_name = open(filename, 'r')
        rows = file_name.readlines()
        file_name.close()
        return len(rows)

    except FileNotFoundError:
        return 0

print(line_number('text.txt'))
