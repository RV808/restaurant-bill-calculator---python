import qs
import bill as bl


def f():
    f2 = int(input(qs.order_quantity))
    bl.bill += 250*f2
