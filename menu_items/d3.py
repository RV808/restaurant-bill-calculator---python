import qs
import bill as bl


def d():
    d3 = int(input(qs.order_quantity))
    bl.bill += 35*d3
