"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    user_dict = {}
    for item in notes:
        if item in user_dict:
            user_dict[item] += 1
        else:
            user_dict[item] = 1
    return user_dict
    


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for item in recipe_updates:
       if item[0] in ideas.keys():
           ideas[item[0]] = item[1]
       else:
           ideas[item[0]] = item[1]   
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    dict_to_send = {}
    for k in aisle_mapping.keys():
        value = aisle_mapping[k]
        aisle = value[0]
        refri_needed = value[1]
        if k in cart:
            count = cart[k]
            dict_to_send[k]=[
                count,
                aisle,
                refri_needed
            ]
    return dict(sorted(dict_to_send.items(),reverse=True))    



def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key in fulfillment_cart.keys():
        fulfillment_cart_item_list = fulfillment_cart[key]
        if key in store_inventory.keys():
            store_inventory[key][0] -= fulfillment_cart_item_list[0]
            if store_inventory[key][0] <= 0:
                store_inventory[key][0] = 'Out of Stock'
    return store_inventory
    
                



