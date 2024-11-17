         
def translate_numbers(line, translator):
    result = ""
    i = 0
    while i < len(line):
        for word, number in translator.items():
            if line[i:i+len(word)] == word:
                result += str(number)
                i += len(word)
                break
        else:
            result += line[i]
            i += 1
    return result

numbers = [
    '99lbqpxzzlbtvkmfrvrnmcxttseven',
    'q7cnfslbtpkvseven',
    '6threezlljtzcr1sdjkthree4cx',
    '21xfxfourmzmqbqp1',
    'lkdbjd5',
    '8three27',
    '21three',
    '3lqrzdq16',
    '49threenjdgrmgfnfhcgz',
    'fourmsmjqfmbjvtwosevendcljsdcstl3one',
    'four98',
    '4sevenfddxgcvdgx',
    'dffmkvmhhdbzjcgrjc5132',
    'eight4one31nxlnrzvtfvrkfvgbbqmvff',
    'mdmvbhqjt5rkfpcnfvzhkkfbjvh8three9',
    'four32',
    'seven6pljhqnineeightjjsvnqblk8eight',
    '6glzfour77fiveone',
    'ntvhxqzsixxcrfpgstwo915onevxz',
    '81four8xkttczb2vj'
]

numbers_by_line = []

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


for line in numbers:
    line_numbers = []
    line = translate_numbers(line, translator)
    print(line)
    for char in line:
        if char.isdigit():
            line_numbers.append(char)
    numbers_by_line.append(line_numbers)
    
values = []

for numbers in numbers_by_line:
    if len(numbers) > 0:
        value = int(numbers[0] + numbers[-1])
        values.append(value)
    else:
        values.append(0)

sum_o_values = sum(values)
print(sum_o_values)        
print(values)
        
        
        
        