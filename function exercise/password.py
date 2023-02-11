def lenght_pass (password):
    return 6 <= len(password) <= 10

def pass_al_num (password):
    return password.isalnum()

def contains_at_least_two_digits(password):
    digit_count = 0
    for ch in password:
       if ch.isdigit():
           digit_count += 1
    return  digit_count >=2


password_as_str = input()
is_valid = True

if not lenght_pass(password_as_str):
    print('Password must be between 6 and 10 characters')
    is_valid = False
if not pass_al_num(password_as_str):
    is_valid = False
    print('Password must consist only of letters and digits')
if not contains_at_least_two_digits(password_as_str):
    is_valid = False
    print('Password must have at least 2 digits')
else:
    print('Password is valid')
