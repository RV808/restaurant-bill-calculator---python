import qs
import bill as bl


def b():
    b4 = int(input(qs.order_quantity))
    bl.bill += 85*b4
