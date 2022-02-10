#Section C: Code Challenge
#using function
numberText = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred', 1000: 'thousand', 1000000: 'million'
}


def numberToWords(n):
    if n == 0:
        return 'zero'
    if n < 0:
        return 'negative ' + numberToWords(-n)

    result = ''

    for num in sorted(numberText.keys(), reverse=True):
        count = int(n/num)

        if (count < 1):
            continue

        if (num >= 100):
            result += numberToWords(count) + ' '

        result += numberText[num]
        n -= count * num
        if (n > 0):
            result += ' '

    return(result)

print(numberToWords(0))
print(numberToWords(99999999))
print(numberToWords(122334456789900))




#using dictionary
"""" string = input("Enter a string: ")
my_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
for item in string:
  if item in my_dict.keys():
    string = string.replace(item, my_dict[item])
print(string)
"""

