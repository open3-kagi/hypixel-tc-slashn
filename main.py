def tc_slashn(text: str, length: int):
    marks = ("，", "。", "、", "！", "？","；", "：", "」", "》", "～", "—", "「", "《")

    length_counter = [0, 0]
    result = ""

    for character in text:
        length_counter[1] = 0
        is_english = (not (ord(character) > 127)) and (character != " ")

        length_counter[0] += 2
        if ord(character) <= 127:
            length_counter[0] -= 1

        if character in marks:
            if (length_counter[0] == 2) and (character not in marks[-2:]):
                result = result[:-1]
                result += character + "⠀"
            elif (length_counter[0] >= length) and (character not in marks[-2:]):
                result += character + "⠀"
            elif (length_counter[0] == length) and (character in marks[-2:]):
                result += "⠀" + character
            else:
                result += character
                length_counter[1] = length_counter[0]

            length_counter[0] = length_counter[1]
        elif (length_counter[0] >= length) and (not is_english):
            result += character.replace(" ", "") + "⠀"
            length_counter[0] = length_counter[1]
        else:
            result += character

    return result.replace("⠀", "\n")
