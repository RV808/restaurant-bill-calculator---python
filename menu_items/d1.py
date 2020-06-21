import qs
import bill as bl


def d():
    d1 = int(input(qs.order_quantity))
    bl.bill += 70*d1
