def mutate_string(string, position, character):
    x = list(string)            #made string to list
    x[position] = character     #changed the specified character in specified position 
    string = ''.join(x)         #made the list back to string and updated the initial string
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
