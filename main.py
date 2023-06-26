"""In this project, you’ll build a program that will take the weight of a package and
determine the cheapest way to ship that package using Sal’s Shippers."""


def shipping():
    weight = 8.4
    # Ground Shipping
    if weight <= 2:
        cost_ground = weight * 1.50 + 20
        print(cost_ground)
    elif weight <= 6:
        cost_ground = weight * 3.00 + 20
        print(cost_ground)
    elif weight <= 10:
        cost_ground = weight * 4.00 + 20
        print(cost_ground)
    else:
        cost_ground = weight * 4.75 + 20
        print(cost_ground)


shipping()
