import string


def transform(input_str):
    # string.punctuation example
    cleaned = "".join(ch for ch in input_str if ch not in string.punctuation)
    return cleaned


input = "Boots the bear!"

result = transform(input)
print("result: ", result)
