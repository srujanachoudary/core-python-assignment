def check_item(x,li):
    if x in li:
        return True
    return False
def add_item(x,li):
    li.append(x)
def remove_item(x,li):
    if x in li:
        li.remove(x)
    else:
        print(x, ' is not in the menu')
initial_menu=['Pizza','Burger','Pasta','Salad']
add_item('Tacos',initial_menu)
remove_item('Salad',initial_menu)
print('Updated Menu:',initial_menu)
ans=check_item('Pizza',initial_menu)
if ans:
    print('Availability: Pizza is available')
else:
    print('Availability: Pizza is not available')
