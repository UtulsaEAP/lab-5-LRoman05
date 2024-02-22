"""

Name: Logan Roman
Lab Time: 2:00 Thurs

"""

def int_to_reverse_binary(num1):
    operative_num = int(num1) #just copied this code from a previous lab.
    binary_string = ""
    while(operative_num>0):
        binary_string = f"{binary_string}{operative_num%2}"
        operative_num //= 2
    return(binary_string)
    

def string_reverse(input_string): 
    reverse_input = ''
    
   #write your for loop here
    for i in range(len(input_string),0,-1):
        reverse_input+=input_string[i-1]
    
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)