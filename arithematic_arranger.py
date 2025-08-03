
def arithematic_arranger(problems, show_answers = False):
	# Check if there are too many problems
	if len(problems) > 5:
		return "Error: Too many problems."
	# Initialize lists to store formatted parts
	top_operands = []
	bottom_operands = []
	dashes = []
	answers = []
	# Loop through each problem
	for problem in problems:
		# Split the problem into parts
		parts = problem.split()
		if len(parts) != 3:
			return "Error: Each problem must contain two operands and one operator."
		operand1 = parts[0]
		operator = parts[1]
		operand2 = parts[2]
		# Validate the operator
		if operator not in ['-', '+']:
			return "Error: Operator must be '+' or '-'."
		# Validate the operands by digits and not more than 4 length
		if not operand1.isdigit() or not operand2.isdigit():
			return "Error: Numbers must only contain digits."
		if len(operand1) > 4 or len(operand2) > 4:
			return "Error: Numbers cannot be more than four digits."
		# Calculate the width of the problem
		width = max(len(operand1), len(operand2)) + 2
		# Format the operands and operator
		top_operands.append(operand1.rjust(width))
		bottom_operands.append(operator + operand2.rjust(width - 1))
		dashes.append('-' * width)
		# Calculate the answer if show_answers is True
		if show_answers:
			if operator == '+':
				result = str(int(operand1) + int(operand2))
			else:
				result = str(int(operand1) - int(operand2))
			answers.append(result.rjust(width))
	# Combine the formatted parts into strings
	arranged_top = '    '.join(top_operands)
	arranged_bottom = '    '.join(bottom_operands)
	arranged_lines = '    '.join(dashes)
	# Add answers if required
	if show_answers:
		arranged_answers = '    '.join(answers)
		return f"{arranged_top}\n{arranged_bottom}\n{arranged_lines}\n{arranged_answers}"
	else:
		return f"{arranged_top}\n{arranged_bottom}\n{arranged_lines}"