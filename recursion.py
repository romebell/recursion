# This function gives you back the following error:
# RecursionError: maximum recursion depth exceeded while calling a Python object
def say_hello(name):
    print('Hello, {}'.format(name))
    say_hello(name)

# say_hello('Rome Bell')


def countdown(num):
    # base case
    if num == 0:
        print('Blast off!')
        return

    # recursive step 
    print(num)
    countdown(num - 1)

countdown(10)

# handles edge case for negative number
def countdown_two(num):
    # base case
    if num == 0:
        print('Blast off!')
        return
    elif num < 0:
        print('Sorry, negative numbers are not allowed')
        return

    # recursive step 
    print(num)
    countdown(num - 1)

countdown_two(100)
countdown_two(-10)

numbers = [1,2,3,4,5]

def add_number(numbers_array, result=0):
    num = numbers_array.pop() # 5
    result += num # 5

    # base case
    if len(numbers_array) == 0:
        return result

    # recursive step
    return add_number(numbers_array, result)

print(add_number(numbers))