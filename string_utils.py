def split_before_each_uppercases(formula):
    split_formula = []
    start = 0
    for end in range(1, len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    digit_location = 1
    for ch in formula[1:]:
        if ch.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return formula, 1
    prefix = formula[:digit_location]
    number = int(formula[digit_location:])
    return prefix, number

