


def answer(question):
    try:
        print(question)
        question = question.split("What is ")[1].split("?")[0]
    except IndexError:
        raise ValueError('syntax error')
    tokens = question.split(" ")
    print(tokens)
    is_number_present = False
    is_operator_present = False
    final_list = []
    valid_operators = ["plus", "minus", "multiplied", "divided"]
    try:
        number = int(tokens[0])
        number = int(tokens[-1])
    except ValueError:
        if tokens[-1] in valid_operators:
            raise ValueError('syntax error')

    for token in tokens:
        if token == 'by':
            continue
        try:
            number = int(token)
            if is_number_present:
                raise ValueError('syntax error')
            is_number_present = True
            is_operator_present = False
            final_list.append(number)
        except ValueError:
            if is_operator_present:
                raise ValueError('syntax error')
            if is_number_present:
                if token in valid_operators:
                    final_list.append(token)
                    is_operator_present = True
                    is_number_present = False
                else:
                    if token.isnumeric():
                        raise ValueError('syntax error')
                    else:
                        raise ValueError('unknown operation')
    print(final_list)
    total = final_list[0]
    i=1
    while i < len(final_list)-1:
        sec_num = final_list[i+1]
        match final_list[i]:
            case 'plus':
                total += sec_num
            case 'minus':
                total -= sec_num
            case 'multiplied':
                total *= sec_num
            case 'divided':
                total //= sec_num
            case _:
                raise ValueError("unknown operation")
        i+=2
    print(total)
    return total



if __name__ == '__main__':
    # answer("What is 52 cubed?")
    answer("What is -12 divided by 2 divided by -3?")

