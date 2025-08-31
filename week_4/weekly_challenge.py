# with automatically closes a file


with open('input.txt', 'r') as f:
    content = f.read()

word_count = len(content.split())
content_upper = content.upper()

with open('output.txt', 'w') as f:
    f.write(content_upper + "\n")
    f.write(f"Word count: {word_count}\n")

print("File 'output.txt' created successfully!")