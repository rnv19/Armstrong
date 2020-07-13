# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
    # Your code goes here
    total = 0
    temp = num
    while(num == 0):
        a = num % 10
        num = num / 10
        total = a**2
        
    if(total == temp):
        return True
    else:
        return fase
