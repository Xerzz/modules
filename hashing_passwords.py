import hashlib
import random
import string

salt_len = 64
iterations = 100_000


def hash_password(password, salt=None):
    # Do type checking
    if not isinstance(password, str):
        raise TypeError("Password should be a string")

    # if no salt is given
    # generate salt_len alphanumeric long salt using system random
    if not salt:
        salt = ''.join(random.SystemRandom().choice(string.digits + string.ascii_letters) for _ in range(salt_len))

    # encode to make it compatible with hashlib algorithm
    encoded_password = bytes(password, encoding='utf-8')
    encoded_salt = bytes(salt, encoding='utf-8')

    pass_hash = hashlib.sha3_512(encoded_password + encoded_salt).hexdigest()

    # use iterative hashing
    for _ in range(iterations):
        pass_hash = hashlib.sha3_512(bytes(pass_hash, encoding="utf-8") + encoded_password).hexdigest()

    return pass_hash + salt


def validate_password(password, hashed_password):
    # Do input validation
    if not isinstance(password, str):
        raise TypeError("Password should be a string")

    for item in hashed_password:
        if not isinstance(item, str):
            raise TypeError("Items in hashed_password should be strings")

    stored_pw_hash = hashed_password[0:128]
    stored_pw_salt = hashed_password[-salt_len:]

    # compute the hash of guess password using the same salt
    user_pw_hash_tuple = hash_password(password, salt=stored_pw_salt)

    # compare the two hashes
    if user_pw_hash_tuple == stored_pw_hash + stored_pw_salt:
        return True
    else:
        return False
