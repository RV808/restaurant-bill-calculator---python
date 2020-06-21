import qs
import bill as bl


def b():
    b1 = int(input(qs.order_quantity))
    bl.bill += 40*b1
