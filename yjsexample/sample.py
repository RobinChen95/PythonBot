import json


class A:
    def __init__(self, age):
        self.name = "default name"
        self.age = age

    def sayHello(self, name):
        self.name = name
        print("hello ", self.name)
        return self.name

    def classGeneralMethod(self):
        print("Hello, this is a general class method.", "My name is ", self.name)
        return "This is a general class method."

    def func_necessary_argument_f(self, arg_a):
        print("This function need a necessary argument. arg_a= ", arg_a)
        res = {}
        res["arg_a"] = arg_a
        res["ohter"] = "flags"
        print(res)
        return json.dumps(res)

    def func_default_argument_f(self, arg_a, arg_default=10):
        print("This function need a necessary argument, and default argument is optional. arg_a= ", arg_a,
              "default args: arg_default=", arg_default)
        return json.dumps({"status": "request success.", "data": {"arg_default": arg_default, "arg_a": arg_a}})

    def func_positional_argument_f(self, arg_a, *args):
        print("This function need a necessary argument and a positional argument. arg_a= ", arg_a,
              " positional argument: args=", args)
        return json.dumps({"status": "request success.", "data": {"arg_a": arg_a, "args": args}})

    def func_keyword_argument(self, arg_a, arg_b='hello', *args, **kwargs):
        print("arg_a=", arg_a, " arg_b=", arg_b, " args=", args, " keyword argument : kwargs=", kwargs)
        return json.dumps(
            {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "args": args, "kwargs": kwargs}})

    def func_keyword_argument_1(self, arg_a, arg_b='hello', *, kwargs):
        return json.dumps(
            {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "kwargs": kwargs}})

    def func_keyword_only_argument(self, arg_a, arg_b='hello', *, kwonly=1):
        return json.dumps(
            {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "kwonly": kwonly}})

    def func_keyword_only_argument_with_args(self, arg_a, arg_b='hello', *args, kwonly=1):
        return json.dumps(
            {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "args": args, "kwonly": kwonly}})

    @classmethod
    def classMethod(cls):
        print("This is a class method.")

    @staticmethod
    def classStaticMethod():
        print("This is a class static method.")


class B:
    # def __init__(self, age):
    #     self.name = "default name"
    #     self.age = age

    def __new__(cls, *args, **kwargs):
        cls.age = 18

    def sayHello(self, name):
        self.name = name
        print("hello ", self.name)
        return self.name

    def classGeneralMethod(self):
        print("Hello, this is a general class method.", "My name is ", self.name)
        return "This is a general class method."

    def func_necessary_argument_f(self, arg_a):
        print("This function need a necessary argument. arg_a= ", arg_a)
        res = {}
        res["arg_a"] = arg_a
        res["ohter"] = "flags"
        print(res)
        return json.dumps(res)

    def func_default_argument_f(self, arg_a, arg_default=10):
        print("This function need a necessary argument, and default argument is optional. arg_a= ", arg_a,
              "default args: arg_default=", arg_default)
        return json.dumps({"status": "request success.", "data": {"arg_default": arg_default, "arg_a": arg_a}})

    def func_positional_argument_f(self, arg_a, *args):
        print("This function need a necessary argument and a positional argument. arg_a= ", arg_a,
              " positional argument: args=", args)
        return json.dumps({"status": "request success.", "data": {"arg_a": arg_a, "args": args}})

    def func_keyword_argument(self, arg_a, arg_b='hello', *args, **kwargs):
        print("arg_a=", arg_a, " arg_b=", arg_b, " args=", args, " keyword argument : kwargs=", kwargs)
        return json.dumps(
            {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "args": args, "kwargs": kwargs}})

    def func_keyword_argument_1(self, arg_a, arg_b='hello', *, kwargs):
        return json.dumps(
            {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "kwargs": kwargs}})

    def func_keyword_only_argument(self, arg_a, arg_b='hello', *, kwonly=1):
        return json.dumps(
            {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "kwonly": kwonly}})

    def func_keyword_only_argument_with_args(self, arg_a, arg_b='hello', *args, kwonly=1):
        return json.dumps(
            {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "args": args, "kwonly": kwonly}})

    @classmethod
    def classMethod(cls):
        print("This is a class method.")

    @staticmethod
    def classStaticMethod():
        print("This is a class static method.")


def moduleFunc():
    print("Hello, this is module functions.")
    return 1


def moduleFunc1(arg_a):
    print("Hello, this is module functions. arg_a= ", arg_a)


emptyDict = {}
print(moduleFunc(**emptyDict))

print("++++++++++++")

dict1 = {"arg_a": "sdfa"}
print(moduleFunc1(**dict1))


def func_necessary_argument_f(arg_a):
    print("This function need a necessary argument. arg_a= ", arg_a)
    res = {}
    res["arg_a"] = arg_a
    print(res)
    return json.dumps(res)


func_necessary_argument_f(arg_a=123)


def func_default_argument_f(arg_a, arg_default=10):
    print("This function need a necessary argument, and default argument is optional. arg_a= ", arg_a,
          "default args: arg_default=", arg_default)
    return json.dumps({"status": "request success.", "data": {"arg_default": arg_default, "arg_a": arg_a}})


def func_positional_argument_f(arg_a, *args):
    print("This function need a necessary argument and a positional argument. arg_a= ", arg_a,
          " positional argument: args=", args)
    return json.dumps({"status": "request success.", "data": {"arg_a": arg_a, "args": args}})


# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
def func_keyword_argument(arg_a, arg_b='hello', *args, **kwargs):
    print("arg_a=", arg_a, " arg_b=", arg_b, " args=", args, " keyword argument : kwargs=", kwargs)
    return json.dumps(
        {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "args": args, "kwargs": kwargs}})


def func_keyword_argument_1(arg_a, arg_b='hello', *, kwargs):
    return json.dumps(
        {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "kwargs": kwargs}})


def func_keyword_only_argument(arg_a, arg_b='hello', *, kwonly=1):
    return json.dumps(
        {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "kwonly": kwonly}})


def func_keyword_only_argument_with_args(arg_a, arg_b='hello', *args, kwonly=1):
    return json.dumps(
        {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "args": args, "kwonly": kwonly}})


def func_keyword_only_argument_with_args_with_no_default(arg_a, arg_b, *args, kwonly=1):
    return json.dumps(
        {"status": "request success.", "data": {"arg_a": arg_a, "arg_b": arg_b, "args": args, "kwonly": kwonly}})


# 与形参一一对应,关键字参数 必须加 关键字形参名
print(func_keyword_argument_1(1, 'hh', kwargs={"a": 1}))
# 错误
# print(func_keyword_argument_1(1, 'hh', {"a": 1}))
# 所有变量全部显式使用 形参变量名，与形参位置无关
print(func_keyword_argument_1(arg_a=1, arg_b='hh', kwargs={"a": 1}))
print(func_keyword_argument_1(arg_b='hh', arg_a=1, kwargs={"a": 1}))
# test
print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
# arguments = {"arg_b": 'hh', "arg_a": 1, "kwargs": {"a": 1}}
arguments = {"arg_b": 'hh', "arg_a": [1, 2, 3], "kwargs": {"a": 1}}
print(func_keyword_argument_1(**arguments))
# {"data": {"arg_a": 1, "arg_b": "hh", "kwargs": {"a": 1}}, "status": "request success."}
# 要做的就只有把对应key的valueObj转换成python对象即可。。。。。。。。。。。

# 这种特别容易引起错误
print(func_keyword_only_argument_with_args(23, (1, "aa", "ssss"), kwonly=24))
# 这种本来不对
# print(func_keyword_only_argument_with_args_with_no_default((1, "aa", "ssss"), kwonly=24))
# 特别注意，当传入一个参数列表时，解引用的操作是在用户端添加，在python解释器中执行的，这样操作就给互操作的传参带来困难，所以需要做一些约定
# 或者后续支持这种操作: * ** 运算符
args = (1, "aa", "ssss")
print(func_keyword_only_argument_with_args_with_no_default(*args, kwonly=24))


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#
# 比如定义一个函数，包含上述若干种参数：
#
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


#
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
#
# >>> f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
# >>> f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
# >>> f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
# >>> f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
# >>> f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
#
# >>> args = (1, 2, 3, 4)
# >>> kw = {'d': 99, 'x': '#'}
# >>> f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
# >>> args = (1, 2, 3)
kw = {'e': 88, 'd': 99, 'x': '#'}
# error TypeError: f2() takes from 2 to 3 positional arguments but 4 positional arguments (and 1 keyword-only argument) were given
# args = (1, "aa", "ssss",6)
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
#
#  虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
