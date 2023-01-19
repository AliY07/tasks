arr = []

for _ in range(5):
    arr.append(input('Enter a word: '))

if not arr:
  print("There is no longest common prefix:", "")

elif len(arr) == 1:
  print("Longest common prefix:", arr[0])
else:

  arr.sort()
  result = ""

  for i in range(len(arr[0])):

      if arr[0][i] == arr[-1][i]:
          result += arr[0][i]

      else:
          break
  print("Longest common prefix:", result)
