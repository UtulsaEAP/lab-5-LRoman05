def swap_values(user_val1, user_val2, user_val3, user_val4):   
   hold_between = 0
   #write your code here
   hold_between = user_val1
   user_val1 = user_val2
   user_val2 = hold_between

   hold_between = user_val3
   user_val3 = user_val4
   user_val4 = hold_between

   
   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   #print those output
   swap_output = swap_values(user_input1,user_input2,user_input3,user_input4)
   print(f"{swap_output[0]} {swap_output[1]} {swap_output[2]} {swap_output[3]}")