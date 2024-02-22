"""

Name: Logan Roman
Lab Time: 2:00 Thurs

"""

def feet_to_steps(user_feet):
   #write your code here
   return round(float(user_feet)/2.5,0)

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
   user_steps = input()
    #print your steps here
   print(int(feet_to_steps(user_steps)))