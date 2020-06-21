import qs
import bill as bl


def f():
    f1 = int(input(qs.order_quantity))
    bl.bill += 350*f1
