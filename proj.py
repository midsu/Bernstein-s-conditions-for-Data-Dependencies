# Authors:  Chandra Lindy & Hamid Suha
# Contact Info:  chandra.lindy@csu.fullerton.edu
# Date:  Oct 14, 2022
# Purpose:  Data dependency checking within sets of instructions

import re

def calculate(si, b):
  '''Takes a string si of simple instruction and checks it against
  a string list b of instruction(s) for dependency, returns a list of
  at least one simple instruction string that can be run in parallel
  with simple instruction si, or "NONE" when dependency is found in
  all of instructions in b.
  '''

  result = []
  for i in b:
    out1 = set(re.sub(r'[^a-z]', '', si[:si.index("=")]))
    in1 = set(re.sub(r'[^a-z]', '', si[si.index("="):]))
    out2 = set(re.sub(r'[^a-z]', '', i[:i.index("=")]))
    in2 = set(re.sub(r'[^a-z]', '', i[i.index("="):]))

    if not out1.intersection(in2) and not out2.intersection(in1) and not out1.intersection(out2):
      result.append(i)

  return result if len(result) > 0 else "NONE"


def validate(block):
  '''Takes a list b of instructions, returns all pairs of instructions
  that can be run in parallel.
  '''

  result = []
  for i in range(0, len(block) - 1):
    instructions = calculate(block[i], block[i+1:len(block)])
    if instructions != "NONE":
      for inst in instructions:
        result.append((block[i], inst))

  return result if len(result) > 0 else "NONE"


running = True

menu = """\
       ***  DEPENDENCY CHECKING MAIN MENU

  1.  Execute example #1 inputs:
        instruction:  d = b + ( c - d / e)
        block:
          b = b * c
          c = c - a
          a = a + b * c

  2.  Execute example #2 inputs:
        block:
          a = a * b * c
          c = c - a
          a = a + b * c

  3.  Validate a custom block of instructions

  4.  Exit Program
"""


while running:
  print(menu)
  choice = int(input("Enter menu choice: "))

  #example 1
  if choice == 1:
    instruction = "d = b + ( c - d / e)"
    block = "b = b * c,c = c - a,a = a + b * c".split(",")
    result = calculate(instruction, block)
    print("\n\n\n\n\nOutput from calculate algorithm:  ", result, "\n\n\n\n\n")

  #example 2
  elif choice == 2:
    block = "a = a * b * c, c = c - a, a = a + b * c".split(",")
    result = validate(block)
    print("\n\n\n\n\nOutput from validdate algorithm:  ", result, "\n\n\n\n\n")

  #example 3
  elif choice == 3:
    block = input("Please input two or more simple instructions separated by a comma (,): ")
    try:
      result = [(inst[0].strip(), inst[1].strip()) for inst in validate(block.split(","))]
      print("\n\n\n\n\nThe following, if any, are pairs of instructions that can be executed in parallel:\n", result, "\n\n\n\n\n")
    except BaseException as err:
      print(f"\nOne or more of inputted instruction(s) does not follow the format specified in assignment specification!\nError: {err=}, {type(err)=}\n")
      print("\nTry again.\n\n\n\n")

  #to end program
  elif choice == 4:
    print("\n\n\nThank you for running our program, and have a great day!!")
    running = False
  else:
    print("Please select one of the valid menu options!")
