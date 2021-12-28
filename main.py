weight = 4.8
cost = ""
#Ground shipping

if weight <= 2:
    cost_ground = weight * 1.50 + 20
elif weight <= 6:
    cost_ground = weight * 3.00 + 20
elif weight <= 10:
    cost_ground = weight * 4.00 + 20
else:
    cost_ground = weight * 4.75 + 20

print("Ground shipping costs: ", cost_ground)

#Premium_shipping
cost_premium_shipping = 125.00

print("Premium shipping costs: ", cost_premium_shipping)


#Drone_shipping

if weight <= 2:
    cost_drone = weight * 4.5
elif weight <= 6:
    cost_drone = weight * 9.00
elif weight <= 10:
    cost_drone = weight * 12.00
else:
    cost_drone = weight * 14.25

print("Drone shipping costs: ", cost_drone)