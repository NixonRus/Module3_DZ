calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(arg):
    count_calls()
    return (len(arg), arg.upper(), arg.lower())

def is_contains(arg1, arg2):
    count_calls()
    if arg1.lower() in str(arg2).lower():
        return True
    else:
        return False




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(is_contains('clear', ['snow', 'CleAr', 'Mobil']))
print(calls)

