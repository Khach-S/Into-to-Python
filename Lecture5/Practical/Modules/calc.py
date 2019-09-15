import pretty_print


def calculate_cube(x):

    return x*x*x

def calculate_square(x):

    return x*x


def main():
    
    pretty_print.simple_print(calculate_cube(2))
    pretty_print.pro_print(calculate_square(4))
main()
#or
if __name__ == "__main__":
    main()