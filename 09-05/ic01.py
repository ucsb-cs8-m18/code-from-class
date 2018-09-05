def maskedPassword(password):
    l = len(password)
    if l > 3:
        # we definitely have to add some x's now
        xs_to_add = l - 3
        first_three_chars = password[:3] # shorthand for password[0:3]
        return first_three_chars + 'x' * xs_to_add
    else:
        # the length of the password is <= 3,
        # so I don't add any x's
        return password

def test_maskedPassword_1():
    assert(maskedPassword("secret1") == "secxxxx")

def test_maskedPassword_2():
    assert(maskedPassword("sec") == "sec")

def test_maskedPassword_3():
    assert(maskedPassword("secr") == "secx")

def isValidPassword(password):
    if type(password) != str:
        return False
    else:
        # now we know we have a string
        if len(password) < 8:
            # password is too smalle
            return False

        # if we're still in this function, the password was long enough
        if "*" not in password and "#" not in password:
            return False

        if password[-1] not in "0123456789":
            return False

        # if we got this far, we know the password is valid
        return True

def test_isValidPassword_1():
    assert(isValidPassword("secret*1") == True)
def test_isValidPassword_2():
    assert(isValidPassword("secret#1") == True)
def test_isValidPassword_3():
    assert(isValidPassword("secret*#1") == True)
def test_isValidPassword_4():
    assert(isValidPassword("secasdfret1") == False)
def test_isValidPassword_5():
    assert(isValidPassword("se*1") == False)
def test_isValidPassword_6():
    assert(isValidPassword(42) == False)