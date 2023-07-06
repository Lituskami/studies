def main():

    print("WeLcome to the Tip Calculator.\n")

    bill = float(input("How much was the bill? \n"))
    split = float(input("How many people to split the bill? \n")) 
    percentage= float(input("What percentage tips would you like to give? 10, 12 or 15? \n"))

    result = (bill/split) 


    if(percentage == 10):
        percentage = result*(10/100)
        finalPayment = result + percentage
        print(f"Your final payment each ${finalPayment:.1f}")
    elif(percentage == 12):
        percentage = result*(12/100)
        finalPayment = result + percentage
        print(f"Your final payment each ${finalPayment:.1f}")
    elif(percentage == 15):
        percentage = result*(15/100)
        finalPayment = result + percentage
        print(f"Your final payment each ${finalPayment:.1f}")
    else:
        print("percentage invalid")



main()
