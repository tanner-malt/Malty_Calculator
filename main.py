def string_parser(string_to):
    full_numbers = []
    symbols = []
    number = [] 

    for ele in string_to:
        if ele.isnumeric(): 
            number.append(ele)
        else:
            if number:  
                full_numbers.append("".join(number))  
                number = []  
            if ele.strip(): 
                symbols.append(ele)  

    if number: 
        full_numbers.append("".join(number))

    return full_numbers, symbols



def math(numbers, symbols):
    numbers = list(map(int, numbers))

    result = numbers[0]
    
    for i, symbol in enumerate(symbols):
        if symbol == '+':
            result += numbers[i + 1]
        elif symbol == '-':
            result -= numbers[i + 1]

    return result

if __name__ == '__main__':
    string_test = "12 + 1"
    numbers, symbols = string_parser(string_test)

    print(math(numbers,symbols))
