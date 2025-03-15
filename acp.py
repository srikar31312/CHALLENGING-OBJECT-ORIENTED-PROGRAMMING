class IntegerToRoman:
    def __init__(self,number):
        """Initialize with an integer value."""
        if not (1 <= number <= 3999):
            raise ValueError("Number must be between 1 and 3999")
        self.number = number
    def convert_to_roman(self):
        """convert the integers to a roman numeral"""
        roman_numerals = [
            (1000, "M"), (900,"CM"), (500, "D"),(400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL")
            (10, "X"),(9,"IX"), (5, 'V'), (4, "IV"), (1,"I")]
        
        num = self.number
        roman_string = " "
        for value, numeral in roman_numerals:
          for value, symbol in roman_numerals:
              while num >= value:
                  roman_string += symbol
                  num -= value
        return roman_string
# Example usage:
num  = int(input("Enter an integer (1 to 3999): "))
converter = IntegerToRoman(num)
print(f"Roman numeral: {converter.converter_to_roman()}")