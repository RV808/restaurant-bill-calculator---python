import qs
import bill as bl


def b():
    b2 = int(input(qs.order_quantity))
    bl.bill += 70*b2
