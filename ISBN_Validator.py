###first validate the input by removing spaces, -, and then check for first 9 digits and then 10th pos to check and then pass input then validator first then each digit by its pos for first 9 digits if 10th is x then 10 by 10 and if number then by 10 then to checksum and sum % 11 valid or nah 

def validate_input(isbn):
  #Removing spaces and '-'
  isbn = isbn.replace('-', '').replace(' ','')
  #checking the length
  if len(isbn) != 10:
    return False, "INVALID: Please provide the correct length"
  
  #checking first 9 digits
  if not isbn[:9].isdigit():
    return False, "Please provide isbn correctly again "
  
  #checking the 10th digit
  if not (isbn[9].isdigit() or isbn[9] == 'X'):
    return False, "Please provide isbn correctly"
  #if everything is ok 
  return True, isbn

def isbn_validator(isbn):
  """Validates an ISBN-10 number using the checksum formula."""

  #input Validation 
  is_valid, isbn = validate_input(isbn)

  if not is_valid:
    return isbn #return error 
  
  #calculate checksum
  total = 0
  #for the first 9 
  for i in range(9):
    total += int(isbn[i]) * (i + 1)

  if isbn[9] == 'X':
    total += 10 * 10 

  else:
    total += int(isbn[9]) * 10

  if total % 11 == 0:
    return "VALID"
  else:
    return "INVALID"
  

  def main():
      isbn = input("Enter the isbn number you want to validate ").strip()
      result = isbn_validator(isbn)
      print(result)


if __name__ == "__main__":
  main
