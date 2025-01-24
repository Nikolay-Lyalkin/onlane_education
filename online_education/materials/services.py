import stripe

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


def get_product(course_payment):
    return stripe.Product.create(name=course_payment).get("id")


def get_price(amount, product):
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product,
    ).get("id")


def get_session(price):
    return stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    ).get("url")
