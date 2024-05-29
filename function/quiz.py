
while True:
    try:
        user_input = input()
        if ' ' not in user_input:
            raise ValueError()
        
        T1, S = user_input.split()
        T = int(T1)

        for n in S:
            for i in range(T):
                print(n, end='')
        print()

    except ValueError as e:
        print(end='')
