from cart import add_to_cart

def test_add_to_cart():
    cart = []
    product = "Laptop"

    result = add_to_cart(cart, product)

    assert result == ["Laptop"]