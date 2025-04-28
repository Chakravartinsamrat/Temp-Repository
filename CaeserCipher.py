def CaeserCipher(text, shift):
    res =""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            ascii_offset = 65 if char.isupper() else 97
            new_position = (ord(char) - ascii_offset + shift_amount) % 26
            new_char = chr(new_position+ ascii_offset)
            res += new_char
        else:
            res +=char
    return res

text = "Mordern Day Slavery"
shift = 3
answer = CaeserCipher(text, shift)
print(answer)