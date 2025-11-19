def split_before_each_uppercases(formula):
    split_formula = []
    start = 0
    for end in range(len(formula)):
        if end != start and formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
    split_formula.append(formula[start:])
    return split_formula
    

def split_at_first_digit(formula):
    digit_location = 0
    while digit_location < len(formula) and not formula[digit_location].isdigit():
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1

    start_digit = digit_location
    while digit_location < len(formula) and formula[digit_location].isdigit():
        digit_location += 1

    prefix = formula[:start_digit]
    number = int(formula[start_digit:digit_location])
    return prefix, number

