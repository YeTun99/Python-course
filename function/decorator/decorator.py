def new_decorator(original_func):
    def wrap_func():
        print("some extra cod, befor original function")
        original_func()
        print("some extra code,after original function")
    return wrap_func

def func_need_decorator():
    print("I want to be decorated")

#decorated_func=new_decorator(func_need_decorator)
#decorated_func()

@new_decorator
def func_need_decorator():
    print("I want to be decorated")

func_need_decorator