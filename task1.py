open_list = ["[","{","("]
close_list = ["]","}",")"]


def check(myStr):
   stack = []
   for i in myStr:
      if i in open_list:
         stack.append(i)
      elif i in close_list:
         pos = close_list.index(i)
         if ((len(stack) > 0) and
            (open_list[pos] == stack[len(stack)-1])):
            stack.pop()
         else:
            return "No"
   if len(stack) == 0:
      return "Correct"
   else:
      return "No"


string1=input(str("brackets:"))
#string = "{[]{()}}"
print(string1,"-", check(string1))
