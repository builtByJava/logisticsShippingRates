#shipping cost calculator

##input package weight and shipping rate
weight = float(input("Enter the package weight in kilos:"))
rate = float(input("Enter the shipping rate per kilo:"))

##calculate shipping costs
shipping_cost = weight * rate


##display the result
print(f"Shipping Cost: {shipping_cost} USD")
