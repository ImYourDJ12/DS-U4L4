# Devon Taylor
# U4L4
# DS
# 12/11/24

from StackClass import ArrayStack

def balanceCheck(test, stack):
  balanced = True
  closing = []

  for i in test:
    if i == "(" or i == "[" or i == "{":
      stack.push(i)
    else:
      closing.append(i)

  for i in range(len(stack)):
    item = stack.pop()
    try:
      if item == "(":
        closing.remove(")")
      elif item == "[":
        closing.remove("]")
      elif item == "{":
        closing.remove("}")
    except:
      balanced = False
      break

  return balanced


def main():
  test1 = "()(()){([()])}"
  test2 = "((()(()){([()])}))"
  test3 = ")(()){([()])]"
  test4 = "({[])}"
  test5 = "("

  stack = ArrayStack()

  for test in [test1, test2, test3, test4, test5]:
    balanced = balanceCheck(test, stack)
    if balanced == True:
      print(f"{test} - Balanced")
    else:
      print(f"{test} - Unbalanced")

if __name__ == "__main__":
    main()