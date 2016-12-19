def string_change(string):
   if len(string) == 0:
       return ""
   else:
       if string[0] == "x":
           return "y" + string_change(string[1:])
       else:
           return string[0] + string_change(string[1:])

print string_change("xnkjanskjxajsnasjkx")
