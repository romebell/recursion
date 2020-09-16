abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def alphabet(letters):
    sing = abc.pop(0)
    print(sing)
    if len(letters):
        alphabet(letters)
    else:
        print('Now I know my abc\'s, next time won\'t you sing with me')
        return
alphabet(abc)