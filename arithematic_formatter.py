def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems. "
top_operands = []
bottom_operands = []
dashes = []
answers = []

for problem in problems:
    parts = problem.split()
    operand1 = parts[0]
    operator = parts[1]
    operand2 = parts[2]

    # Checking if operator is only + or -
    if operator not in ['-', '+']:
        return "Error: Operator must be '+' or '-'."
    if not operand1.isdigit() or not operand2.isdigit():
        return "Error: Numbers must only contain digits."
    if len(operand1) > 4 or len(operand2) > 4:
        return "Error: Numbers cannot be more than four digits."

    width = max(len(operand1), len(operand2)) + 2
    top_operands.append(operand1.rjust(width))
    bottom_operands.append(operator + operand2.rjust(width - 1))
    dashes.append("-" * width)

    if show_answers:
        result = str(eval(operand1 + operator + operand2))
        answers.append(result.rjust(width))

arranged_top = '    '.join(top_operands)
    return
arranged_lines = '    '.join(dashes)

if show_answers:
    arranged_answers = '    '.join(answers)
    return f"{arranged_top}\n{arranged_bottom}\n{arranged_lines}\n{arranged_answers}"
else:
    return f"{arranged_top}\n{arranged_bottom}\n{arranged_lines}"
    

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')