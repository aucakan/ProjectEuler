"""
Project Euler Problem 17
"""

"""
When I wrote approximately 40 percent of the code, I realized that there had to be a lot 
of detail, however, because I am stubborn and had a lot of free time, I wrote this code.
It only took about 1 hour and 20 minutes. I do not recommend you to review my code. 
Copilot Pro's solution is at the bottom.
"""
def helper(x):
    match x:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"
        case 10:
            return "ten"
        case 11:
            return "eleven"
        case 12:
            return "twelve"
        case 13:
            return "thirteen"
        case 14:
            return "fourteen"
        case 15:
            return "fifteen"
        case 16:
            return "sixteen"
        case 17:
            return "seventeen"
        case 18:
            return "eighteen"
        case 19:
            return "nineteen"

def converter(x):
    x = str(x)
    if len(x) == 4:
        if int(x[-3]) == 0:
            if int(x[-1]) != 0:
                if int(x[-2:])//10 == 0:
                    return f"{helper(int(x)//1000)} thousand and {helper(int(x[-1:]))}"
                elif int(x[-2:])//10 == 1:
                    return f"{helper(int(x)//1000)} thousand and {helper(int(x[-2:]))}"
                elif int(x[-2:])//10 == 2:
                    return f"{helper(int(x)//1000)} thousand and twenty-{helper(int(x[-1]))}"
                elif int(x[-2:])//10 == 3:
                    return f"{helper(int(x)//1000)} thousand and thirty-{helper(int(x[-1]))}"
                elif int(x[-2:])//10 == 4:
                    return f"{helper(int(x)//1000)} thousand and forty-{helper(int(x[-1]))}"
                elif int(x[-2:])//10 == 5:
                    return f"{helper(int(x)//1000)} thousand and fifty-{helper(int(x[-1]))}"
                elif int(x[-2:])//10 == 6:
                    return f"{helper(int(x)//1000)} thousand and sixty-{helper(int(x[-1]))}"
                elif int(x[-2:])//10 == 7:
                    return f"{helper(int(x)//1000)} thousand and seventy-{helper(int(x[-1]))}"
                elif int(x[-2:])//10 == 8:
                    return f"{helper(int(x)//1000)} thousand and eigthy-{helper(int(x[-1]))}"
                elif int(x[-2:])//10 == 9:
                    return f"{helper(int(x)//1000)} thousand and ninety-{helper(int(x[-1]))}"
            if int(x[-1]) == 0:
                if int(x[-2:])//10 == 0:
                    return f"{helper(int(x)//1000)} thousand"
                elif int(x[-2:])//10 == 1:
                    return f"{helper(int(x)//1000)} thousand and {helper(int(x[-2:]))}"
                elif int(x[-2:])//10 == 2:
                    return f"{helper(int(x)//1000)} thousand and twenty"
                elif int(x[-2:])//10 == 3:
                    return f"{helper(int(x)//1000)} thousand and thirty"
                elif int(x[-2:])//10 == 4:
                    return f"{helper(int(x)//1000)} thousand and forty"
                elif int(x[-2:])//10 == 5:
                    return f"{helper(int(x)//1000)} thousand and fifty"
                elif int(x[-2:])//10 == 6:
                    return f"{helper(int(x)//1000)} thousand and sixty"
                elif int(x[-2:])//10 == 7:
                    return f"{helper(int(x)//1000)} thousand and seventy"
                elif int(x[-2:])//10 == 8:
                    return f"{helper(int(x)//1000)} thousand and eigthy"
                elif int(x[-2:])//10 == 9:
                    return f"{helper(int(x)//1000)} thousand and ninety"
                
        if int(x[-3]) != 0:
            if int(x[-1]) == 0:
                if int(x[-2:])//10 == 0:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred"
                elif int(x[-2:])//10 == 1:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and {helper(int(x[-2:]))}"
                elif int(x[-2:])//10 == 2:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and twenty"
                elif int(x[-2:])//10 == 3:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and thirty"
                elif int(x[-2:])//10 == 4:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and forty"
                elif int(x[-2:])//10 == 5:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and fifty"
                elif int(x[-2:])//10 == 6:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and sixty"
                elif int(x[-2:])//10 == 7:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and seventy"
                elif int(x[-2:])//10 == 8:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and eigthy"
                elif int(x[-2:])//10 == 9:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and ninety"
            if int(x[-1]) != 0:
                if int(x[-2:])//10 == 0:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred"
                elif int(x[-2:])//10 == 1:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and {helper(int(x[-2:]))}"
                elif int(x[-2:])//10 == 2:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and twenty"
                elif int(x[-2:])//10 == 3:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and thirty"
                elif int(x[-2:])//10 == 4:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and forty"
                elif int(x[-2:])//10 == 5:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and fifty"
                elif int(x[-2:])//10 == 6:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and sixty"
                elif int(x[-2:])//10 == 7:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and seventy"
                elif int(x[-2:])//10 == 8:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and eigthy"
                elif int(x[-2:])//10 == 9:
                    return f"{helper(int(x)//1000)} thousand {helper(int(x[-3:])//100)} hundred and ninety"
    if len(x) == 3:
        if int(x[-1]) == 0:
            if int(x[-2:])//10 == 0:
                return f"{helper(int(x[-3:])//100)} hundred"
            elif int(x[-2:])//10 == 1:
                return f"{helper(int(x[-3:])//100)} hundred and {helper(int(x[-2:]))}"
            elif int(x[-2:])//10 == 2:
                return f"{helper(int(x[-3:])//100)} hundred and twenty"
            elif int(x[-2:])//10 == 3:
                return f"{helper(int(x[-3:])//100)} hundred and thirty"
            elif int(x[-2:])//10 == 4:
                return f"{helper(int(x[-3:])//100)} hundred and forty"
            elif int(x[-2:])//10 == 5:
                return f"{helper(int(x[-3:])//100)} hundred and fifty"
            elif int(x[-2:])//10 == 6:
                return f"{helper(int(x[-3:])//100)} hundred and sixty"
            elif int(x[-2:])//10 == 7:
                return f"{helper(int(x[-3:])//100)} hundred and seventy"
            elif int(x[-2:])//10 == 8:
                return f"{helper(int(x[-3:])//100)} hundred and eigthy"
            elif int(x[-2:])//10 == 9:
                return f"{helper(int(x[-3:])//100)} hundred and ninety"
        if int(x[-1]) != 0:
            if int(x[-2:])//10 == 0:
                return f"{helper(int(x[-3:])//100)} hundred and {helper(int(x[-1:]))}"
            elif int(x[-2:])//10 == 1:
                return f"{helper(int(x[-3:])//100)} hundred and {helper(int(x[-2:]))}"
            elif int(x[-2:])//10 == 2:
                return f"{helper(int(x[-3:])//100)} hundred and twenty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 3:
                return f"{helper(int(x[-3:])//100)} hundred and thirty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 4:
                return f"{helper(int(x[-3:])//100)} hundred and forty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 5:
                return f"{helper(int(x[-3:])//100)} hundred and fifty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 6:
                return f"{helper(int(x[-3:])//100)} hundred and sixty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 7:
                return f"{helper(int(x[-3:])//100)} hundred and seventy-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 8:
                return f"{helper(int(x[-3:])//100)} hundred and eigthy-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 9:
                return f"{helper(int(x[-3:])//100)} hundred and ninety-{helper(int(x[-1]))}"     
    if len(x) == 2:
        if int(x[-1]) == 0:
            if int(x[-2:])//10 == 1:
                return f"{helper(int(x[-2:]))}"
            elif int(x[-2:])//10 == 2:
                return "twenty"
            elif int(x[-2:])//10 == 3:
                return "thirty"
            elif int(x[-2:])//10 == 4:
                return "forty"
            elif int(x[-2:])//10 == 5:
                return "fifty"
            elif int(x[-2:])//10 == 6:
                return "sixty"
            elif int(x[-2:])//10 == 7:
                return "seventy"
            elif int(x[-2:])//10 == 8:
                return "eigthy"
            elif int(x[-2:])//10 == 9:
                return "ninety"
        if int(x[-1]) != 0:
            if int(x[-2:])//10 == 1:
                return f"{helper(int(x[-2:]))}"
            elif int(x[-2:])//10 == 2:
                return f"twenty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 3:
                return f"thirty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 4:
                return f"forty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 5:
                return f"fifty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 6:
                return f"sixty-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 7:
                return f"seventy-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 8:
                return f"eigthy-{helper(int(x[-1]))}"
            elif int(x[-2:])//10 == 9:
                return f"ninety-{helper(int(x[-1]))}"  
    if len(x) == 1:
        return helper(int(x))

total_sum = 0
for i in range(1, 1001):
    a = str(converter(i))
    a = a.replace(" ", "")
    a = a.replace("-", "")
    total_sum += len(a)
print(total_sum)

########################################
### Second Solution from Copilot Pro ###
########################################

def number_to_words(n: int):
    # Define words for numbers
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]

    if n < 10:
        return ones[n]
    elif n < 20:
        return teens[n-10]
    elif n < 100:
        return tens[n//10] + ones[n%10]
    elif n < 1000:
        if n % 100 == 0:
            return ones[n//100] + "hundred"
        else:
            return ones[n//100] + "hundredand" + number_to_words(n%100)
    elif n == 1000:
        return "onethousand"

def count_letters(n):
    return sum(len(number_to_words(i).replace(" ", "")) for i in range(1, n+1))

# Calculate the number of letters for numbers from 1 to 1000
total_letters = count_letters(1000)
print(f"The total number of letters used from 1 to 1000 is: {total_letters}")

    


    
