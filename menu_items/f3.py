import qs
import bill as bl


def f():
    f3 = int(input(qs.order_quantity))
    bl.bill += 180*f3
