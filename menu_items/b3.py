import qs
import bill as bl


def b():
    b3 = int(input(qs.order_quantity))
    bl.bill += 30*b3
