
def verify_Card_number(card_number):
  card_number_reversed = card_number[::-1]
  sum_of_odd_digits = 0
  odd_digits = card_number_reversed[::2]
  for digit in odd_digits:
    sum_of_odd_digits += int(digit)

  sum_of_even_digits = 0
  even_digits = card_number_reversed[1::2]
  for digit in even_digits:
    number = int(digit) *2
    if number  >= 10:
      number = (number // 10  + (number %10))
      sum_of_even_digits += int(number) 
  
  total = sum_of_even_digits + sum_of_odd_digits
  print(total)
  return total % 10 == 0 


def main():
  card_number = '4111-1111-4555-1141'
  new_card_number = card_number.maketrans({'-': '', ' ': ''})
  translated_card_number = card_number.translate(new_card_number)

  if verify_Card_number(translated_card_number):
    print("VALID")
  else:
    print("INVALID")

main()