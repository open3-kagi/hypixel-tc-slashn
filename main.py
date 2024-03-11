def tc_slashn(text: str, length: int):
    marks_1 = ("，", "。", "、", "！", "？","；", "：", "」", "》", "～", "—")
    marks_2 = ("「", "《")

    length_counter = 0
    is_english = True
    result = ""    

    for character in text:
        if ord(character) > 127:
            length_counter += 2
            is_english = False
        else:
            length_counter += 1

            if character != " ":
                is_english = True
            else:
                is_english = False
        
        if character in marks_1 or character in marks_2:
            tmp_result = result.split("\n")

            if length_counter == 2 and character not in marks_2:
                tmp_result[-2] += character
                tmp_result.pop(-1)

                result = ""

                for l in tmp_result:
                    result += l + "\n"
                
                length_counter = 0
            elif length_counter >= length and character not in marks_2:
                result += character + "\n"
                length_counter = 0
            elif length_counter == length and character in marks_2:
                result += "\n" + character
                length_counter = 0
            else:
                result += character
        elif length_counter >= length and not is_english:
            if character == " ":
                result += "\n"
            else:
                result += character + "\n"
            length_counter = 0
        else:
            result += character
    return result
