class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, value, *args, **kwargs):
        def hello():
            return "Hello " + kwargs['name']

        def calculate_total():
            total = 0
            for i in args:
                total += i
            return total
            # maybe do something before the func call

        response = self.func(value, *args, **kwargs)
        # maybe do something after the func call
        return hello() + ", Sum = " + str(
            calculate_total()) + ", Return Value of Function Call = " + response + ", Value = " + value


@Decorator
def test(value, *args, **kwargs):
    print(args)
    print(kwargs)
    return str(value + "_updated")


print(test("value", 1, 2, 3, 4, name='mohamed'))
print(test.func("value"))
