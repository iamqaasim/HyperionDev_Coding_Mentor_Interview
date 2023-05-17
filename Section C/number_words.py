def read_numeral(numeral):
    singles = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    def convert_two_digits(num):
        '''
        Convert a two-digit number into words
        '''
        if num < 10:
            return singles[num]
        elif num < 20:
            return teens[num - 10]
        else:
            ten_digit = num // 10
            single_digit = num % 10
            if single_digit == 0:
                return tens[ten_digit]
            else:
                return tens[ten_digit] + '-' + singles[single_digit]
    
    def convert_three_digits(num):
        '''
        Convert a three-digit number into words
        '''
        hundred_digit = num // 100
        two_digit_num = num % 100
        if hundred_digit == 0:
            return convert_two_digits(two_digit_num)
        elif two_digit_num == 0:
            return singles[hundred_digit] + ' hundred'
        else:
            return singles[hundred_digit] + ' hundred ' + convert_two_digits(two_digit_num)
    
    if numeral == 0:
        return singles[0]
    
    result = ''
    trillion_digit = numeral // 1_000_000_000_000
    billion_digit = (numeral % 1_000_000_000_000) // 1_000_000_000
    million_digit = (numeral % 1_000_000_000) // 1_000_000
    thousand_digit = (numeral % 1_000_000) // 1_000
    last_three_digits = numeral % 1_000
    
    # Convert each part of the number and concatenate the words
    if trillion_digit > 0:
        result += convert_three_digits(trillion_digit) + ' trillion '
    if billion_digit > 0:
        result += convert_three_digits(billion_digit) + ' billion '
    if million_digit > 0:
        result += convert_three_digits(million_digit) + ' million '
    if thousand_digit > 0:
        result += convert_three_digits(thousand_digit) + ' thousand '
    if last_three_digits > 0:
        result += convert_three_digits(last_three_digits)
    
    return result.strip()

if __name__ == '__main__':
    numeral = 19093
    result = read_numeral(numeral)
    print(result)  # Output: "nineteen thousand ninety-three"
