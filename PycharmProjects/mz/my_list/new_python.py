def print_func(par):
    print("hello：",par)
    return

def my_max(*args):
    return max(args)

def my_min(*args):
    return min(args)

if __name__=="__main__":
    print_func(my_min(2, 4, 967, 6, 75))
    print_func(my_max(2, 4, 967, 6, 75))
