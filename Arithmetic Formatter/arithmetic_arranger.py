#def arithmetic_arranger(problems):

#ask for the arithmetic problems
problems = input("Please enter your problems:")

#extract the problems one by one
data = problems.split()
operand_1_1 = data[0]
operator_1 = data[1]
operand_1_2 = data[2]

#print(data)
#print(operand_1_1)
#print(operator_1)
#print(operand_1_2)

#calculate the answer for first problem
if operator_1 == "+":
    answer_1 = int(operand_1_1) + int(operand_1_2)
    print(answer_1)

#check if problems are within limit
if problems.count(",") >= 5:
    print("Error: Too many problems")



#ask if the answers are wanted
#display_answer = input("Yes/No")



#    return arranged_problems
