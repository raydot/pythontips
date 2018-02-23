#01-args_kwargs.py

# *args and **kwargs allow you to send variable numbers of arguments to a function

#args is used to send *non-keyworded* arguments:
def test_var_args(f_arg, *argv):
	print("first normal arg:", f_arg)
	for arg in argv:
		print("another arg through *argv:", arg)

test_var_args('eeny', 'meeny', 'miney', 'fred')

#kwargs lets you pass *keyworded* variable length of arguments
#this allows you to pass named arguments in a function.  
def greet_me(**kwargs):
	for key, value in kwargs.items():
		print("{0} is set to {1}".format(key, value))

greet_me(name="dave")

#all you really need is the *'s!
def test_args_kwargs(arg1, arg2, arg3):
        print("arg1:", arg1)
        print("arg2:", arg2)
        print("arg3:", arg3)

'''
TEST CODE:
# notice the arguments have to match the variable names
>>> someargs = {'one&', 'two&', 'three&'}
>>> test_args_kwargs(*someargs)

>>> otherargs = {"arg1":"something", "arg2":{1, 3, 5, 7, 9}, "arg3":3}
>>> test_args_kwargs(**otherargs)
'''

'''
NOTES:
"argv" and "kwargs" are arbitrary.  All you really need is the * and **

if you want to use all three the order is:
(formal_args, *args, **kwargs)
'''
