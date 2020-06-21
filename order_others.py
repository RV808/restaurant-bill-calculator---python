import qs
import bill as bl


def order_others():
    y = str(input(qs.order_others))
    if y in qs.order_f1:
        import menu_items.f1 as f1
        f1.f()

    elif y in qs.order_f2:
        import menu_items.f2 as f2
        f2.f()

    elif y in qs.order_f3:
        import menu_items.f3 as f3
        f3.f()

    elif y in qs.order_f4:
        import menu_items.f4 as f4
        f4.f()

    elif y in qs.order_f5:
        import menu_items.f5 as f5
        f5.f()

    elif y in qs.order_f6:
        import menu_items.f6 as f6
        f6.f()

    elif y in qs.order_f7:
        import menu_items.f7 as f7
        f7.f()

    elif y in qs.order_f8:
        import menu_items.f8 as f8
        f8.f()

    elif y in qs.order_b1:
        import menu_items.b1 as b1
        b1.b()

    elif y in qs.order_b2:
        import menu_items.b2 as b2
        b2.b()

    elif y in qs.order_b3:
        import menu_items.b3 as b3
        b3.b()

    elif y in qs.order_b4:
        import menu_items.b4 as b4
        b4.b()

    elif y in qs.order_b5:
        import menu_items.b5 as b5
        b5.b()

    elif y in qs.order_d1:
        import menu_items.d1 as d1
        d1.d()

    elif y in qs.order_d2:
        import menu_items.d2 as d2
        d2.d()

    elif y in qs.order_d3:
        import menu_items.d3 as d3
        d3.d()

    elif y in qs.order_d4:
        import menu_items.d4 as d4
        d4.d()

    elif y in qs.order_d5:
        import menu_items.d5 as d5
        d5.d()

    if y in qs.no:
        cancel = str(input(qs.order_cancel))
        if cancel in qs.yes:
            print()
            print(qs.qs3)
            print(qs.greet5)

        elif cancel in qs.no:
            print()
            print(qs.qs3)
            x = str(input(qs.name))
            z = input(qs.pn)
            billf1 = int(bl.bill+bl.bill*0.14)
            billf = ("""
            * * * * * * * * * * * * * * * * * * * * * *
            *             THE RESTAURANT              *
            *                                         *
            *   NAME: {}                           *
            *   PHONE NUMBER: {}              *
            *                                         *
            *   Bill Amount                    {}   *
            *                                         *
            *   TAX                             14%   *
            *   Total Bill Amount              {}   *
            *                                         *
            * * * * * * * * * * * * * * * * * * * * * *
            """).format(x, z, bl.bill, billf1)

            print(qs.bqs, billf)

    if y not in qs.no:
        order_others()
