# Devon Taylor
# U4L1
# DS
# 12/4/24

class ArrayStack:
  def __init__(self):
    self.__stack = []
    self.__size = 0

  def push(self, item):
    """Adds an element to the top of the collection"""
    self.__stack.append(item)
    self.__size += 1

  def pop(self):
    """Removes an element from the top of the collection"""
    try:
      item = self.__stack[-1]
      del self.__stack[-1]
      self.__size -= 1
      return item
    except:
      raise IndexError("index out of range")

  def top(self):
    """Returns the element at the top of the collection"""
    try:
      item = self.__stack[-1]
      return item
    except:
      raise IndexError("index out of range")

  def __is_empty(self):
    if self.__size == 0:
      return True
    else:
      return False

  def __len__(self):
    """Returns the length of the collection"""
    return self.__size

  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out