#def arithmetic_arranger(problems):

#ask for the arithmetic problems
problems = input("Please enter your problems:")

#extract the problems one by one
delimiter = ","
data = problems.split(delimiter)

problem_1 = data[0]
problem_1n = problem_1.strip('"')
print("First problem: ", problem_1n)

problem_2 = data[1]
problem_2n = problem_2.strip('"')
print("Second problem: ", problem_2)


# splitproblem_0 = problem_1.split()
# operand_1_1 = splitproblem_1[0]
# operator_1 = splitproblem_1[1]
# operand_1_2 = splitproblem_1[2]
# # operand_2_1 = data[3]
# # operator_2 = data[4]
# # operand_2_2 = data[5]
#
# #print("Data split: ", data)
#
# print("Operand #1.1: ", operand_1_1)
# print("Operator #1: ", operator_1)
# print("Operand #1.2: ", operand_1_2)
#
# print("Operand #2.1: ", operand_2_1)
# print("Operator #2: ", operator_2)
# print("Operand #2.2: ", operand_2_2)

#try calculating the answer regardless of addition or subtraction

# if operator_1 == "+":
#     answer_1 = int(operand_1_1) + int(operand_1_2)
#     print("Answer #1: ", answer_1)
#
# if operator_1 == "-":
#     answer_1 = int(operand_1_1) - int(operand_1_2)
#     print("Answer #1: ", answer_1)
#
# if len(operand_1_1) >= len(operand_1_2):
#     blockwidth_1 = 2 + len(operand_1_1)
# else:
#     blockwidth_1 = 2 + len(operand_1_2)
#
# print("Width of block #1: ", blockwidth_1)
#
# line_1_1 = " " * (blockwidth_1 - len(operand_1_1)) + operand_1_1
# line_1_2 = operator_1 + " " * (blockwidth_1 - len(operand_1_2) - 1) + operand_1_2
# line_1_3 = "-" * blockwidth_1
# line_1_4 = " " * (blockwidth_1 - len(str(answer_1))) + str(answer_1)
#
# print(line_1_1)
# print(line_1_2)
# print(line_1_3)
# print(line_1_4)













#    return arranged_problems
