def decrypt(letter: str):
    result = []

    for i in letter:
        result.append(i)
        if len(result) > 2 and (result[-1], result[-2]) == (".", "."):
            result.pop()
            result.pop()
            if result:
                result.pop()
    return "".join(i for i in result if i != ".")