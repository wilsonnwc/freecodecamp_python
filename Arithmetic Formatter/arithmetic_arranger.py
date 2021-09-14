#def arithmetic_arranger(problems):

#ask for the arithmetic problems
problems = input("Please enter your problems:")

#extract the problems one by one
data = problems.split()
operand_1_1 = data[0]
operator_1 = data[1]
operand_1_2 = data[2]

print(data)
print(operand_1_1)
print(operator_1)
print(operand_1_2)

#calculate the answer for addition
if operator_1 == "+":
    answer_1 = int(operand_1_1) + int(operand_1_2)
    print(answer_1)

    #if length of 1st operand is bigger or equals to 2nd
    if len(operand_1_1) >= len(operand_1_2):
        line_1 = "  " + operand_1_1
        line_2 = "+ " + " "*(len(operand_1_1)-len(operand_1_2)) + operand_1_2
        line_3 = "--" + "-"*len(operand_1_1)
        print(line_1)
        print(line_2)
        print(line_3)
        if len(str(answer_1)) > len(operand_1_1):
            line_4 = " " + str(answer_1)
            print(line_4)
        else:
            line_4 = "  " + str(answer_1)
            print(line_4)

    #if length of 2nd operand is bigger
    else:
        line_1 = "  " + " "*(len(operand_1_2)-len(operand_1_1)) + operand_1_1
        line_2 = "+ " + operand_1_2
        line_3 = "--" + "-"*len(operand_1_2)
        print(line_1)
        print(line_2)
        print(line_3)
        if len(str(answer_1)) > len(operand_1_2):
            line_4 = " " + str(answer_1)
            print(line_4)
        else:
            line_4 = "  " + str(answer_1)
            print(line_4)

#calculate the answer for subtraction
if operator_1 == "-":
    answer_1 = int(operand_1_1) - int(operand_1_2)
    print(answer_1)

    #if length of 1st operand is bigger or equals to 2nd
    if len(operand_1_1) >= len(operand_1_2):
        line_1 = "  " + operand_1_1
        line_2 = "- " + " "*(len(operand_1_1)-len(operand_1_2)) + operand_1_2
        line_3 = "--" + "-"*len(operand_1_1)
        print(line_1)
        print(line_2)
        print(line_3)
        if len(str(answer_1)) > len(operand_1_1):
            line_4 = " " + str(answer_1)
            print(line_4)
        else:
            line_4 = "  " + str(answer_1)
            print(line_4)

    #if length of 2nd operand is bigger
    else:
        line_1 = "  " + " "*(len(operand_1_2)-len(operand_1_1)) + operand_1_1
        line_2 = "- " + operand_1_2
        line_3 = "--" + "-"*len(operand_1_2)
        print(line_1)
        print(line_2)
        print(line_3)
        if len(str(answer_1)) > len(operand_1_2):
            line_4 = " " + str(answer_1)
            print(line_4)
        else:
            line_4 = "  " + str(answer_1)
            print(line_4)


#special case to deal with: -ve minus -ve


#check if problems are within limit
#if problems.count(",") >= 5:
#    print("Error: Too many problems")



#ask if the answers are wanted
#display_answer = input("Yes/No")



#    return arranged_problems
