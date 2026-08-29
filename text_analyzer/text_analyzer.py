print("=========== Text Analyezer ===========")

text  = input("Enter your text: ")
print(f"Original Text: {text}")

len_text = len(text)
print(f"Characters: {len_text}")

text = text.strip()
print(f"Characters (without spaces): {text}")

print(len(text.split()))

print(f"First Character {text[0]}")
print(f"Last Character {text[-1]}")


print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")



print(f"Python Find: {text.count("Python")}")










