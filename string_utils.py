def split_before_each_uppercases(formula):
    split_formula = []
    start = 0
    for end, ch in enumerate(formula[1:], start=1):
        if ch.isupper():
            split_formula.append(formula[start:end])
            start = end
    split_formula.append(formula[start:])
    return split_formula


def split_at_first_digit(formula):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1
