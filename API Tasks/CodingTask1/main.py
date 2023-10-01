word = input("Enter your word: ")

count = int(len(word)/2)
if len(word)%2 != 0:
    count+=1

for n in range(count):
    if word[n].lower() != word[-n-1].lower():
        print(f"{word} - NOT a palindrome")
        break
    if n == count-1:
        print(f"{word} - is a palindrome")
    