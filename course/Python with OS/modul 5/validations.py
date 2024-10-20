def validate_user(username, minlen):
    assert type(username) == str, "username must be string"
    if minlen < 1:
        raise ValueError("Minlen must be at leat 1")
    if(len(username) < minlen):
        return False
    if not username.isalnum():
        return False
    return True