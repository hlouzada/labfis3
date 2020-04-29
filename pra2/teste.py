
def teste(*args):
    if args:
        if len(args) == 1:
            if isinstance(args[0],list):
                print("islist!")
                return args[0]
            else:
                print("istuple with one arg!")
                return args[0]
        elif len(args) == 2:
            print("istuple with two arg!")
            return args
        else:
            print("istuple with too many args!")
            return args