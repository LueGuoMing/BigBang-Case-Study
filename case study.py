import json

result = []

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        result.append("BIGBANG")
    elif num % 3 == 0:
        result.append("BIG")
    elif num % 5 == 0:
        result.append("BANG")
    else:
        result.append(str(num))

# Write the result array to 'output.json'
with open('output.json', 'w') as f:
    json.dump(result, f)