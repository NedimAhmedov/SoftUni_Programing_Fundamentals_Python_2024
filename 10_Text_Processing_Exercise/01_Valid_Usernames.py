def username_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def valid_characters(username):
    for character in username:
        if not (character.isalnum()
                or character == "-"
                or character == "_"):
            return False
    return True


def no_redundant_symbol(username):
    if " " in username:
        return False
    return True


def username_is_valid(username):
    if username_length(username) and valid_characters(username) and no_redundant_symbol(username):
        return True
    return False


username_string = input().split(", ")
for each_username in username_string:
    if username_is_valid(each_username):
        print(each_username)
