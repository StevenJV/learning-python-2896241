def is_palindrome(teststr):
    teststr ="".join(ch for ch in teststr if ch.isalnum()).lower()
    reversedStr = teststr [::-1]
    return (teststr == reversedStr)

total = 0
test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.", "Taco Cat",
    "Race car!"]
for word in test_words:
    total += is_palindrome(word)
print("there are",total,"palindromes in the list", test_words)
