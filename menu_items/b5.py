import qs
import bill as bl


def b():
    b5 = int(input(qs.order_quantity))
    bl.bill += 85*b5
