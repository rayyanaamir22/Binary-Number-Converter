# FUNCTIONS

def decimalToBinary(decimal): # Recusive
  if decimal >= 1: 
    decimalToBinary(decimal//2)
    print(decimal%2, end='')


def binaryToDecimal(binary):
  decimal = 0
  for digit in str(binary):
    decimal = decimal*2 + int(digit)

  print(decimal)

def reuse(thisCode):
  while True:
    print(f"\nDo you want to reuse {thisCode}?")
    re = input()
    if re.lower().startswith('y'):
      return True
    elif re.lower().startswith('n'):
      return False
    else:
      print("(Yes or no)")
