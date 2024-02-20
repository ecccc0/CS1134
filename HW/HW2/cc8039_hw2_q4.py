def e_approx(n):
    cur_fact = 1
    res = 1
    for i in range(1, n+1):
        res += 1 / (cur_fact*i)
        cur_fact *= i
    return res

# for n in range(15): 
#     curr_approx = e_approx(n) 
#     approx_str = "{:.15f}".format(curr_approx) 
#     print("n =", n, "Approximation:", approx_str)