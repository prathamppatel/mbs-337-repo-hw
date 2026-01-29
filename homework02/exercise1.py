
def even_or_odd(int_list):
    for num in int_list: 
        if num%2 >= 1:
            print(f'{num} is odd!')
        elif num%2 == 0:
            print(f'{num} is even!')

int_list = [1, 2, 3, 4, 5, 6 , 7, 8 , 9, 10]

even_or_odd(int_list)
