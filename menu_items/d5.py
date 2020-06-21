import qs
import bill as bl


def d():
    d5 = int(input(qs.order_quantity))
    bl.bill += 75*d5
