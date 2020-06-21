import qs
import order_others


def order():
    x = str(input(qs.order_first))
    if x in qs.order_f1:
        import menu_items.f1 as f1
        f1.f()
        order_others.order_others()

    elif x in qs.order_f2:
        import menu_items.f2 as f2
        f2.f()
        order_others.order_others()

    elif x in qs.order_f3:
        import menu_items.f3 as f3
        f3.f()
        order_others.order_others()

    elif x in qs.order_f4:
        import menu_items.f4 as f4
        f4.f()
        order_others.order_others()

    elif x in qs.order_f5:
        import menu_items.f5 as f5
        f5.f()
        order_others.order_others()

    elif x in qs.order_f6:
        import menu_items.f6 as f6
        f6.f()
        order_others.order_others()

    elif x in qs.order_f7:
        import menu_items.f7 as f7
        f7.f()
        order_others.order_others()

    elif x in qs.order_f8:
        import menu_items.f8 as f8
        f8.f()
        order_others.order_others()

    elif x in qs.order_b1:
        import menu_items.b1 as b1
        b1.b()
        order_others.order_others()

    elif x in qs.order_b2:
        import menu_items.b2 as b2
        b2.b()
        order_others.order_others()

    elif x in qs.order_b3:
        import menu_items.b3 as b3
        b3.b()
        order_others.order_others()

    elif x in qs.order_b4:
        import menu_items.b4 as b4
        b4.b()
        order_others.order_others()

    elif x in qs.order_b5:
        import menu_items.b5 as b5
        b5.b()
        order_others.order_others()

    elif x in qs.order_d1:
        import menu_items.d1 as d1
        d1.d()
        order_others.order_others()

    elif x in qs.order_d2:
        import menu_items.d2 as d2
        d2.d()
        order_others.order_others()

    elif x in qs.order_d3:
        import menu_items.d3 as d3
        d3.d()
        order_others.order_others()

    elif x in qs.order_d4:
        import menu_items.d4 as d4
        d4.d()
        order_others.order_others()

    elif x in qs.order_d5:
        import menu_items.d5 as d5
        d5.d()
        order_others.order_others()

    else:
        print(qs.greet5)
