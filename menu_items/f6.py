import qs
import bill as bl


def f():
    f6 = int(input(qs.order_quantity))
    bl.bill += 150*f6
