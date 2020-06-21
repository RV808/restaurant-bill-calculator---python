import qs
import menu as mn
import order


def start():
    print(qs.greet1)
    q1 = str(input(qs.greet2))
    if q1 in qs.greet2_p:
        print(qs.qs2_good)
    elif q1 in qs.greet2_n:
        print(qs.qs2_bad)
    global q2
    q2 = int(input(qs.greet3))
    if (q2 == 0):
        print(qs.greet5)
    elif (0 < q2 <= 12):
        print(qs.qs3)
        print(qs.greet4)
        print(mn.menu)
        order.order()
    else:
        print(qs.greet6[0:23], q2, qs.greet6[23:])
        print(qs.greet5)
