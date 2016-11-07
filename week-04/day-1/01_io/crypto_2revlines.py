# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    file_name = open('texts/reversed_zen_lines.txt', 'r')
    rows = file_name.readlines()

    result = ''

    for line in rows:
        for index in range(len(line)-2, -1, -1):
            result += line[index]
        result += '\n'
    return result

print decrypt('texts/reversed_zen_lines.txt')
