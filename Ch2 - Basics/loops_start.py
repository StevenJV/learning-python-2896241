#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while (x <= 5):
        print(x)
        x = x+1 #no increment operator?



    # TODO: define a for loop
    for x in range(5,10):
        print(x)


    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    print("weekdays")
    for day in days[0:5]:
        print(day)


    # TODO: use the break and continue statements
    for x in range(5,20):
        if (x % 2 == 0): continue
        if (x > 17): break
        print (x)

    # TODO: using the enumerate() function to get index
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i, d in enumerate(days):
        print (i, d)

if __name__ == "__main__":
    main()
