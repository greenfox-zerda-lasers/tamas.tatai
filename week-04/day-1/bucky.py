fw = open('bab.txt', 'w')
fw.write('432142342134\n')
fw.write('szartalicska\n')
fw.close()

fr = open('bab.txt', 'r')
text = fr.read()
print(text)
fr.close()