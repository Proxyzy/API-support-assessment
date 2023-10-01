input = input()
if input[0] == "[" and input[-1] == "]":
    input = input.replace('[', '')
    input = input.replace(']', '')
    input = input.replace(',', '')
    input = input.replace(' ', '')


results = {}
for element in input:
    if element in results:
        results[element] += 1
    else:
        results[element] = 1
print(results)