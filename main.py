

from custom_types import * 
"""Main file """

def main():
    print("-----Starting the program-----")
    a = Any(1)
    b = call(a)
    c = dict_(b)
    d = list_(c)
    e = seq(d)
    f = str_(e)
    g = opt(f)
    h = lambda_(g)
    i = check_type(h)
    print(i)
    print("-----Ending the program-----")


if __name__ == "__main__":
    main()