import string


def transform(input_str):
    # string.punctuation example
    cleaned = "".join(ch for ch in input_str if ch not in string.punctuation)
    return cleaned


input = "Boots the bear! ' '"

# result = transform(input)
# print("result: ", result)
#
# input_token = result.split()
# print("input_token: ", input_token)


query_token = ["Boots", "the", "bear"]

title_token = ["Big", "bear"]

# if query_token in title_token:
#     print("yes")
# else:
#     print("no")


# at least one token from the query matches any
# part of a token from the title
for i in range(len(query_token)):
    if query_token[i] in title_token:
        query_token[i]
        print("yes")
    # else:
    #     query_token[i]
    #     print("no")
