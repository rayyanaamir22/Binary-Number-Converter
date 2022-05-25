'''
Name: Rayyan Aamir
Date: May 25, 2022
Program: Binary Conversion
'''

# Modules
import os

# Other files
import functions as f

def main():
  while True:
    print("BINARY CONVERSION CALCULATOR")

    # User selects conversion type
    while True:
      print("\n1. Decimal to Binary\n2. Binary to Decimal")
      try:
        method = int(input("Enter the number denoting which method to use: "))
        if method in [1,2]:
          break
        else:
          raise ValueError
      except (ValueError, TypeError):
        os.system('clear')
        print("Enter an available option")
      

    # User enters value to convert
    while True:
      try:
        value = int(input("Enter the value to convert: "))
        break
      except (ValueError, TypeError):
        os.system('clear')
        print("Invalid input.")

    print('\n')
    if method == 1:
      f.decimalToBinary(value)
    else:
      f.binaryToDecimal(value)
    
    print('\n')
    if f.reuse('the binary conversion calculator'):
      os.system('clear')
      continue
    else: 
      os.system('clear')
      break
    

if __name__ == '__main__':
  main()
