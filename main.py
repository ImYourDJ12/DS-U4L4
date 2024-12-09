# Devon Taylor
# U4L2
# DS
# 12/9/24

from StackClass import ArrayStack

def main():
    original = "Sphinx of black quartz, judge my vow"
    new = ""

    stack = ArrayStack()

    newOriginal = list(original)

    for i in range(len(newOriginal)):
      stack.push(newOriginal[0])
      del newOriginal[0]

    for i in range(len(stack)):
      new += stack.pop()

    print(f"Original: {original}")
    print(f"Reversed: {new}")

if __name__ == "__main__":
    main()