"""In this project, you’ll build a program that will take the weight of a package and
determine the cheapest way to ship that package using Sal’s Shippers."""


def shipping():
    weight = 1.5
    cost_premium = 125.00
    # Ground Shipping
    if weight <= 2:
        cost_ground = weight * 1.50 + 20
        print("The cost of ground shipping is: ${:.2f}".format(cost_ground))
    elif weight <= 6:
        cost_ground = weight * 3.00 + 20
        print("The cost of ground shipping is: ${:.2f}".format(cost_ground))
    elif weight <= 10:
        cost_ground = weight * 4.00 + 20
        print("The cost of ground shipping is: ${:.2f}".format(cost_ground))
    else:
        cost_ground = weight * 4.75 + 20
        print("The cost of ground shipping is: ${:.2f}".format(cost_ground))

    # Ground Shipping Premium
    print("The cost of premium shipping is: ${:.2f}".format(cost_premium))

    # Drone Shipping
    if weight <= 2:
        cost_drone = weight * 4.50 + 0
        print("The cost of drone shipping is: ${:.2f}".format(cost_drone))
    elif weight <= 6:
        cost_drone = weight * 9.00 + 0
        print("The cost of drone shipping is: ${:.2f}".format(cost_drone))
    elif weight <= 10:
        cost_drone = weight * 12.00 + 0
        print("The cost of drone shipping is: ${:.2f}".format(cost_drone))
    else:
        cost_drone = weight * 14.25 + 0
        print("The cost of drone shipping is: ${:.2f}".format(cost_drone))


shipping()
