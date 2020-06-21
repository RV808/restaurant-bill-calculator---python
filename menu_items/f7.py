import qs
import bill as bl


def f():
    f7 = int(input(qs.order_quantity))
    bl.bill += 250*f7
