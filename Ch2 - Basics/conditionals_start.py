#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 100, 10

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is the same as y"
    else:
        result = "x is greater than y"


    # conditional statements let you use "a if C else b"
    result = "x is less than y" if x < y else "x is greater than or equal to y"

    # match-case makes it easy to compare multiple values
    value = "one"
    match value:  #match-case only in Python 3.10 and newer
        case "one":
            result = 1
        case "two":
            result = 2

    print(result)


if __name__ == "__main__":
    main()
