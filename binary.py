def base_convert(number, from_base, to_base):
    def to_decimal(num, base):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = num.upper()
        decimal_value = 0
        for char in num:
            decimal_value = decimal_value * base + digits.index(char)
        return decimal_value
    
    def from_decimal(num, base):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if num == 0:
            return "0"
        result = ""
        while num > 0:
            result = digits[num % base] + result
            num //= base
        return result

    decimal = to_decimal(number, from_base)
    return from_decimal(decimal, to_base)

number_in_base = "10"
from_base = 8
to_base = 2
result = base_convert(number_in_base, from_base, to_base)
print(result)
