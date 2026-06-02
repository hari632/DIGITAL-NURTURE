def displaycart(cart,value):
    if not cart:
        print("INVALID CART")
        return
    cart.append(value)
    print("cart items:",cart)
c=[100,250,75]
v=int(input("Enter the value"))
displaycart(c,v)    
        