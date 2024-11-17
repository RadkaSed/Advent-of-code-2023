def translate_numbers(line, translator):
    result = ""
    i = 0
    while i < len(line):
        for word, number in translator.items():
            if line[i:i+len(word)] == word:
                result += str(number)
                i += len(word) - 1
                break
        else:
            result += line[i]
            i += 1
    return result

input_puzzle = []

with open('input1.txt', mode='r', encoding='utf-8') as input_file:
    for line in input_file:
        line = line.strip()
        input_puzzle.append(line)

print(input_puzzle)
translator = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5, 
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

numbers_by_line = []

for line in input_puzzle:
    line_numbers = []
    line = translate_numbers(line, translator)
    for char in line:
        if char.isdigit():
            line_numbers.append(char)
    numbers_by_line.append(line_numbers)
 
# print(numbers_by_line)   
values = []

for numbers in numbers_by_line:
    if len(numbers) >= 1:
        value = int(numbers[0] + numbers[-1])
        values.append(value)
        print(value)
    else:
        values.append(0)
        
len_of_values = len(values)
sum_of_values = sum(values)

print(len_of_values)
print(sum_of_values)