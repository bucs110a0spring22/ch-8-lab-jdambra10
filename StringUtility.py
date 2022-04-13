class StringUtility:
  def __init__(self, string):
    self.string = string
    self.text = "string"

  def __str__(self):
    obj_string = str(self.string)
    return obj_string

  def vowels(self):
    string = self.string
    num_vowels = 0
    for char in string:
      if char in "aeiouAEIOU":
        num_vowels += 1
    if num_vowels >= 5:
      num_vowels = "many"
    return str(num_vowels)

  def bothEnds(self):
    string = self.string
    if len(string) <= 2:
      empty = ""
      return empty
    else:
      myString = "" + string[0] + string[1] + string[-2] + string[-1] 
      return myString

  def fixStart(self):
    string = self.string
    if len(string) <= 1:
      return string
    else:
      first_char = string[0]
      string = string.replace(first_char, '*')
      string = first_char + string[1:]
      return string

  def asciiSum(self):
    string = self.string
    sum = 0
    for char in string:
      sum += ord(char)
    return sum

  def cipher(self):
    string = self.string
    cipher = ""
    for char in string:
      if char.isalpha():
        if char.isupper():
          alphabet = (ord(char) - 65 + len(self.string)) % (26)
          alphabet += 65
        if char.islower():
          alphabet = (ord(char) - 97 + len(self.string)) % (26)
          alphabet += 97
        new_char = chr(alphabet)
      else:
        new_char = char
      cipher += new_char
    return cipher
