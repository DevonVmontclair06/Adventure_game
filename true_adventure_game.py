def scenario_1():
    options = ['1a','1b']
    print('You wake up to find yourself in a cold, dark cave.')
    print('The air is damp, and the faint echo of dripping water fills your ears.')
    print('You have no memory of how you got here.')
    print('As you get up and dust yourself off, you notice two paths ahead:')
    print('1a:')
    print('To your left, a narrow tunnel leads deeper into darkness')
    print('The air is colder there, and you can faintly hear the sound of rushing water.')
    print('1b:')
    print('To your right, a wider passage seems to have some light coming from it.')
    print('The source of the light is unclear, but you hear distant whispers echoing from within.')
    user_input = ''
    while user_input not in options:
        print('Choose between 1a or 1b')
        user_input = input().strip()
        if user_input == '1a':
            scenario_2()
        elif user_input == '1b':
            scenario_5()
        else:
            print('Invalid answer')

def scenario_2():
    options = ['2a','2b']
    print('Testing')
    user_input = ''
    while user_input not in options:
        print('Choose between 2a or 2b')
        user_input = input().strip()
        if user_input == '2a':
            scenario_3()
        elif user_input == '2b':
            print(end_a)
        else:
            print('Invalid answer')
end_a = 'he'

def scenario_3():
    options = ['3a','3b']
    print('True test')
    user_input = ''
    while user_input not in options:
        print('Choose between 3a or 3b')
        user_input = input().strip()
        if user_input == '3b':
            scenario_4()
        elif user_input == '3a':
            print(end_b)
        else:
            print('Invalid answer')
end_b = 'p'

def scenario_4():
    options = ['4a','4b']
    print('True test')
    user_input = ''
    while user_input not in options:
        print('Choose between 4a or 4b')
        user_input = input().strip()
        if user_input == '4a':
            print(end_c)
        elif user_input == '4b':
            print(end_d)
        else:
            print('Invalid answer')
end_c = 'why'
end_d = 'where'

def scenario_5():
    options = ['5a','5b']
    print('True test')
    user_input = ''
    while user_input not in options:
        print('Choose between 5a or 5b')
        user_input = input().strip()
        if user_input == '5a':
            scenario_7()
        elif user_input == '5b':
            scenario_6()
        else:
            print('Invalid answer')

def scenario_6():
    options = ['6a','6b']
    print('True test')
    user_input = ''
    while user_input not in options:
        print('Choose between 6a or 6b')
        user_input = input().strip()
        if user_input == '6a':
            print(end_e)
        elif user_input == '6b':
            print(end_f)
        else:
            print('Invalid answer')
end_e = 'd'
end_f = 's'

def scenario_7():
    options = ['7a','7b']
    print('True test')
    user_input = ''
    while user_input not in options:
        print('Choose between 7a or 7b')
        user_input = input().strip()
        if user_input == '7a':
            print(end_g)
        elif user_input == '7b':
            scenario_8()
        else:
            print('Invalid answer')
end_g = 'e'

def scenario_8():
    options = ['8a','8b']
    print('True test')
    user_input = ''
    while user_input not in options:
        print('Choose between 8a or 8b')
        user_input = input().strip()
        if user_input == '8a':
            print(end_h)
        elif user_input == '8b':
            print(end_i)
        else:
            print('Invalid answer')
end_h = 'p'
end_i = 'd'

def main():
    while True:
        print('Welcome to the Adventure game run in python.')
        print('Read the story and choose the right path in order to escape your predicament!')
        scenario_1()
        break

if __name__=="__main__":
    main()
