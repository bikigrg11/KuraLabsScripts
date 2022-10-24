def f(x):
    def f1(*args, **kwargs):
        print("kuralabs")
        return x(*args, **kwargs)
    return f1

x = [1,2,3]
print(f(x))

# Can only pass 1 Variable

