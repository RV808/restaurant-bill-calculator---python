import qs
import bill as bl


def d():
    d2 = int(input(qs.order_quantity))
    bl.bill += 30*d2
