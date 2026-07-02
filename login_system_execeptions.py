class AuthError(Exception): pass
class UserNotFoundError(AuthError): pass
class InvalidPasswordError(AuthError): pass

users = {"amit": "1234"}

def login(username, password):
    # TODO: raise UserNotFoundError if username not in users
    # raise InvalidPasswordError if password doesn't match
    # return "Login successful" otherwise
    pass

# Test:
try:
    login("rahul", "xxxx")
except AuthError as e:
    print(f"Caught: {type(e).__name__} - {e}")
# Expected: Caught: UserNotFoundError - ...
