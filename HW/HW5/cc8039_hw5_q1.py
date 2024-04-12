from ArrayStack import *
var = {}
operators = "+-*/"

def format_float(n):
    if n % 1 == 0:
        return int(n)
    return n

def eval(a, b, op):
    if op == '-':
        return a-b
    if op == '+':
        return a+b
    if op == '*':
        return a*b
    if op == '/':
        return a/b

def eval_postfix(lst):
    s = ArrayStack()
    for x in lst:
        if x in var.keys():
            s.push(var[x])
        elif x in operators:
            b = s.pop()
            a = s.pop()
            s.push(eval(a, b, x))
        else:
            s.push(float(x))
    return s.top()



while True:
    exp = input("-->")
    if exp == "done()":
        break
    if '=' in exp:
        exp_lst = exp.split()
        var[exp_lst[0]] = float(eval_postfix(exp_lst[2:]))
        print(exp_lst[0])
    else:
        exp_lst = exp.split()
        print(format_float(eval_postfix(exp_lst)))
