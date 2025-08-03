message = "sahilbawa" # this is the message you want to encrypt
shift = 2 # this is the shift in letters you want
def ciphere(message, shift): # Here you are defining the function

    sample="abcdefghijklmnopqrstuvwxyz" #This is the sample space for letters to shift
    result = '' #This is empty here your end output will be placed 
    for char in message: #loop telling char variable to enter message one by one 
        if char.isalpha():# conditon to check if message has letter deal here
            index = sample.find(char) # tells to go to sample and find letter one by one letters from message to find their positon in sample 
            new_index   =   (index  +   shift)  %   len(sample) # this eg of a this takes a from message finds 'a' in sample checks its index and add to shift , len sample ensures limit is not crossed so a is 0 so 0+2= 2%26 which is 2 
            result  +=   sample[new_index] # now it finds 2 as new index goes therough sample and adds that to result 
         
        else:
            result  += char # this is for if there are any spaces or anything meanning anuthing except letter it just copy pastes that 

    return result # This returns the result 
print(ciphere(message, shift)) # this prints for function to perform
            
        
