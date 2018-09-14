arabian = int(input("a number, please: \n"))


roman_singles = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

def get_digits(number):
    digits = list()
    while number > 0:
        digits.append(number% 10)
        number = int(number/10)


    return digits
def is_single_digit(number):
    for i, x in enumerate(roman_singles):
        if number == 0:
            return ""
        elif number == i + 1:
            return roman_singles[i]


def is_below_fifty(number):
    result = ""
    if number < 40:
        result = "{}{}".format(int((number/10))* "X", converter(number%10))
    else:
        result = "XL" + converter(number%10)

    return result

def is_below_hundred(number):
    result = ""
    if number < 90:
        #result = "L{}{}".format(int((after_c/10))* "X", is_single_digit(after_c%10))
        result = "L{}".format(converter(number - 50))

    else:
        result = "XC" + converter(number%10)

    return result

def is_below_five_hundred(number):
    print("func running")
    result = ""
    if number < 400:
        result = "C" * int(number/100) + converter(number%100)
    else:
        result = "CD{}".format(converter(number - 400))

    return result

def is_below_thousand(number):
    if number < 900:
        result = "D{}".format(converter(number - 500))
    else:
        result = "CM{}".format(converter(number - 900))

    return result
def converter(arabian):
    if arabian < 10:
        result = is_single_digit(arabian)
    elif arabian < 50:
        result = is_below_fifty(arabian)
    elif arabian < 100:
        result = is_below_hundred(arabian)
    elif arabian < 500:
        result = is_below_five_hundred(arabian)
    elif arabian <1000:
        result = is_below_thousand(arabian)

    return result

print(converter(arabian))
