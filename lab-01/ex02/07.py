print("Enter text lines (type 'done' to finish):")
lines = []

while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("\nThe entered lines after converting to uppercase:")
for line in lines:
    print(line.upper())