from ArrayStack import *
def eval_prefix(exp_str):
    s = ArrayStack()
    lst = exp_str.split()
    for i in range(len(lst)):
        cur = lst.pop()
        if cur in "+-*/":
            first = s.pop()
            second = s.pop()
            res = eval(str(first) + cur + str(second))
            s.push(int(res))
        else:
            s.push(int(cur))
    return s.pop()
print(eval_prefix("- + * 16 5 * 8 4 20"))
print(eval_prefix("- *  3 4 10"))