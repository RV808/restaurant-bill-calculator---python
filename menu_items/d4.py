import qs
import bill as bl


def d():
    d4 = int(input(qs.order_quantity))
    bl.bill += 90*d4
