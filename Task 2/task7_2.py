print('\n'*100)

my_rows = int(input("Enter the number of rows: "))
my_columns = int(input("Enter the number of columns: "))


def multi_tab(function, rows, columns):
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            print("{:3}".format(function(i, j)), end='   ')
        print('\n')


multi_tab(lambda x, y: x*y, my_rows, my_columns)
