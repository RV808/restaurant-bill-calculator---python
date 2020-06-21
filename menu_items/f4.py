import qs
import bill as bl


def f():
    f4 = int(input(qs.order_quantity))
    bl.bill += 200*f4
