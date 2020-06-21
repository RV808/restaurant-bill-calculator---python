import qs
import bill as bl


def f():
    f8 = int(input(qs.order_quantity))
    bl.bill += 140*f8
