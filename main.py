import os
from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort
from algorithms.quick import partition, quick_sort
from algorithms.merge import merge_sort

dir = os.getcwd()

menu_options = {
    1: '1000 elements',
    2: '10000 elements',
    3: '100000 elements',
    4: 'Exit',
}

menu_options_lv0 = {
    1: 'Insertion Sort',
    2: 'Selection Sort',
    3: 'Quick Sort',
    4: 'Merge Sort',
    5: 'Exit'
}

def print_menu_l0():
    print('\n-----------------------------------------------------------------------')
    print('Please select which algorithm to test')
    for key in menu_options_lv0.keys():
        print (key, '--', menu_options_lv0[key] )

def print_menu_l1():
    print('\n-----------------------------------------------------------------------')
    print('Now please choose 1 of the 3 sizes below to test the algorithm in 4 example arrays:')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def test_example(alg: int):
    with open(dir+'\instancias-numericas\couting.txt','r') as file:
        n = int(file.readline().rstrip())
        A = file.read().splitlines()
        A = list(map(int, A))
        print('Unsorted array of {} elements:\n\n'.format(n), A)
        if alg == 1:
            print('\n\nInsertion Sort:\n')
            B = insertion_sort(A, n)
        elif alg == 2:
            print('\n\nSelection Sort:\n')
            B = selection_sort(A, n)
        elif alg == 3:
            print('\n\Quick Sort:\n')
            B = quick_sort(A, 0, n-1)
        elif alg == 4:
            print('\n\Merge Sort:\n')
            B = merge_sort(A, n)
        print('\nSorted array:\n\n', B)

def one_thousand_test(n: int, alg: int):
    if alg == 1:
        print('\nInsertion Sort:\n')
        for i in range(1,5):
            print('\n----------------------------------------------------------------------')
            print('Example 0{}:'.format(i))
            print('----------------------------------------------------------------------\n\n')
            with open(dir+'\instancias-numericas\instancias-num\\num.{}.{}.in'.format(str(n),str(i)),'r') as file:
                n = int(file.readline().rstrip())
                A = file.read().splitlines()
                A = list(map(int, A))
                print('Unsorted array of {} elements:\n\n'.format(n), A)
                B = insertion_sort(A, n)
                print('\nSorted array:\n\n', B)
    elif alg == 2:
        print('\nSelection Sort:\n')
        for i in range(1,5):
            print('\n----------------------------------------------------------------------')
            print('Example 0{}:'.format(i))
            print('----------------------------------------------------------------------\n\n')
            with open(dir+'\instancias-numericas\instancias-num\\num.{}.{}.in'.format(str(n),str(i)),'r') as file:
                n = int(file.readline().rstrip())
                A = file.read().splitlines()
                A = list(map(int, A))
                print('Unsorted array of {} elements:\n\n'.format(n), A)
                B = selection_sort(A, n)
                print('\nSorted array:\n\n', B)
    elif alg == 3:
        print('\Quick Sort:\n')
        for i in range(1,5):
            print('\n----------------------------------------------------------------------')
            print('Example 0{}:'.format(i))
            print('----------------------------------------------------------------------\n\n')
            with open(dir+'\instancias-numericas\instancias-num\\num.{}.{}.in'.format(str(n),str(i)),'r') as file:
                n = int(file.readline().rstrip())
                A = file.read().splitlines()
                A = list(map(int, A))
                print('Unsorted array of {} elements:\n\n'.format(n), A)
                B = quick_sort(A, 0, n-1)
                print('\nSorted array:\n\n', B)
    elif alg == 4:
        print('\Merge Sort:\n')
        for i in range(1,5):
            print('\n----------------------------------------------------------------------')
            print('Example 0{}:'.format(i))
            print('----------------------------------------------------------------------\n\n')
            with open(dir+'\instancias-numericas\instancias-num\\num.{}.{}.in'.format(str(n),str(i)),'r') as file:
                n = int(file.readline().rstrip())
                A = file.read().splitlines()
                A = list(map(int, A))
                print('Unsorted array of {} elements:\n\n'.format(n), A)
                B = merge_sort(A, n)
                print('\nSorted array:\n\n', B)
    else:
        'Algorithm not defined'
        exit()

if __name__ == '__main__':
    while(True):
        alg = ''
        print_menu_l0()
        try:
            alg = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number from 1 to 3')
        if alg in range(1,5):
            print('\n-----------------------------------------------------------------------\n')
            print('This script sorts an array A of N integers like in the example below:\n\n')
            test_example(alg=alg)
            print_menu_l1()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('Wrong input. Please enter a number ...')
            if option == 1:
                one_thousand_test(n=1000, alg=alg)
            elif option == 2:
                one_thousand_test(n=10000, alg=alg)
            elif option == 3:
                one_thousand_test(n=100000, alg=alg)
            elif option == 4:
                print('Thanks. See you.')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        elif alg == 5:
            print('Thanks. See you.')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')