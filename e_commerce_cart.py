def calculatevalue(cart_items):
    total_price=sum(cart_items.values())
    if len(cart_items)>5:
        discount=total_price*0.10
        total_price-=discount
    return total_price
cart_items= {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
ans=calculatevalue(cart_items)
if ans!=0:
    print('Total Price:',int(ans))
else:
    print('cart is empty')