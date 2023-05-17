from number_words import read_numeral

def test_read_numeral():
    # Test cases for numbers from 0 to 999
    assert read_numeral(0) == 'zero'
    assert read_numeral(5) == 'five'
    assert read_numeral(12) == 'twelve'
    assert read_numeral(100) == 'one hundred'
    assert read_numeral(345) == 'three hundred forty-five'
    assert read_numeral(999) == 'nine hundred ninety-nine'

    # Test cases for numbers in the thousands
    assert read_numeral(1000) == 'one thousand'
    assert read_numeral(3456) == 'three thousand four hundred fifty-six'
    assert read_numeral(7890) == 'seven thousand eight hundred ninety'
    assert read_numeral(9999) == 'nine thousand nine hundred ninety-nine'

    # Test cases for numbers in the millions
    assert read_numeral(1_000_000) == 'one million'
    assert read_numeral(2_345_678) == 'two million three hundred forty-five thousand six hundred seventy-eight'
    assert read_numeral(5_600_000) == 'five million six hundred thousand'
    assert read_numeral(9_999_999) == 'nine million nine hundred ninety-nine thousand nine hundred ninety-nine'

    # Test cases for numbers in the billions
    assert read_numeral(1_000_000_000) == 'one billion'
    assert read_numeral(3_456_789_012) == 'three billion four hundred fifty-six million seven hundred eighty-nine thousand twelve'
    assert read_numeral(7_890_000_000) == 'seven billion eight hundred ninety million'
    assert read_numeral(9_999_999_999) == 'nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine'

    # Test cases for numbers in the trillions
    assert read_numeral(1_000_000_000_000) == 'one trillion'
    assert read_numeral(9_876_543_210_987) == 'nine trillion eight hundred seventy-six billion five hundred forty-three million two hundred ten thousand nine hundred eighty-seven'
    assert read_numeral(7_890_000_000_000) == 'seven trillion eight hundred ninety billion'
    assert read_numeral(999_999_999_999_999) == 'nine hundred ninety-nine trillion nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine'

    print("All tests passed!")

test_read_numeral()
