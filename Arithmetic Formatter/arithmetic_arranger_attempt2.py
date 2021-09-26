def arithmetic_arranger(problems, solve = False):

  #check Error: Too many problems
  if len(problems) > 5:
    return "Error: Too many problems."

  answer = ""
  maxlength = ""
  boxline1 = ""
  boxline2 = ""
  boxline3 = ""
  boxline4 = ""
  arrangedline1 = ""
  arrangedline2 = ""
  arrangedline3 = ""
  arrangedline4 = ""
  arranged_problems = ""

  for problem in problems:

    firstnumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondnumber = problem.split(" ")[2]
    print(firstnumber)
    print(operator)
    print(secondnumber)

    if operator != "+" and operator != "-":
      return "Error: Operator must be '+' or '-'."

    if len(firstnumber) > 4 or len(secondnumber) > 4:
      return "Error: Numbers cannot be more than four digits."

    if firstnumber.isdigit() and secondnumber.isdigit():
      pass
    else:
      return "Error: Numbers must only contain digits."

    if operator == "+":
      answer = int(firstnumber) + int(secondnumber)
    elif operator == "-":
      answer = int(firstnumber) - int(secondnumber)
    print(answer)

    maxlength = max(len(firstnumber), len(secondnumber), len(str(answer))) + 2
    print(maxlength)

    boxline1 = str(firstnumber).rjust(maxlength)
    boxline2 = operator + str(secondnumber).rjust(maxlength - 1)
    boxline3 = "-" * maxlength
    boxline4 = str(answer).rjust(maxlength)
    print(boxline1)
    print(boxline2)
    print(boxline3)
    print(boxline4)

    if problem != problems[-1]:
      arrangedline1 += boxline1 + "    "
      arrangedline2 += boxline2 + "    "
      arrangedline3 += boxline3 + "    "
      arrangedline4 += boxline4 + "    "

    else:
      arrangedline1 += boxline1
      arrangedline2 += boxline2
      arrangedline3 += boxline3
      arrangedline4 += boxline4

    print(arrangedline1)
    print(arrangedline2)
    print(arrangedline3)
    print(arrangedline4)

  if solve:
    arranged_problems = arrangedline1 + "\n" + arrangedline2 + "\n" + arrangedline3 + "\n" + arrangedline4
  else:
    arranged_problems = arrangedline1 + "\n" + arrangedline2 + "\n" + arrangedline3

  return arranged_problems
