import qs
import bill as bl


def f():
    f5 = int(input(qs.order_quantity))
    bl.bill += 320*f5
