import os

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
dir = os.getcwd()

menu_options = {
    1: '1000 elements',
    2: '10000 elements',
    3: '100000 elements',
    4: 'Exit',
}

def print_menu():
    print('\n-----------------------------------------------------------------------')
    print('Now please choose 1 of the 3 sizes below to test the InsertionSort algorithm in 4 example arrays:')
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def insertion_sort(A: list, n:int):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j]>key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        if i == round(n/4):
            print('----25% concluded----')
        elif i == round(n/2):
            print('----50% concluded----')
        elif i == round(3*n/4):
            print('----75% concluded----')
    return A

def test_example():
    with open(dir+'\instancias-numericas\couting.txt','r') as file:
                n = int(file.readline().rstrip())
                A = file.read().splitlines()
                A = list(map(int, A))
                print('Unsorted array of {} elements:\n\n'.format(n), A)
                B = insertion_sort(A, n)
                print('\nSorted array:\n\n', B)

def one_thousand_test(n: int):
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

if __name__ == '__main__':
    print('\n-----------------------------------------------------------------------\n')
    print('This script sorts an array A of N integers like in the example below:\n\n')
    test_example()
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            one_thousand_test(n=1000)
        elif option == 2:
            one_thousand_test(n=10000)
        elif option == 3:
            one_thousand_test(n=100000)
        elif option == 4:
            print('Thanks. See you.')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')