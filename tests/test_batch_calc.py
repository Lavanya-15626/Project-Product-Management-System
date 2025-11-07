import app.batch_calc as batch_calc

def test_total_stock_value_success():
    # Fetch products from API
    products = batch_calc.fetch_all_products()
    assert products is not None and len(products) > 0

    # Manual calculation
    expected_total = sum(float(p['price']) * int(p['quantity']) for p in products)

    # Function call
    batch_calc.total_stock_value()

    # Check computed result
    calculated_total = sum(float(p['price']) * int(p['quantity']) for p in products)
    assert calculated_total == expected_total


def test_average_price_success():
    products = batch_calc.fetch_all_products()
    assert len(products) > 0

    expected_avg = sum(float(p['price']) for p in products) / len(products)

    batch_calc.average_price()
    calculated_avg = sum(float(p['price']) for p in products) / len(products)

    assert round(calculated_avg, 2) == round(expected_avg, 2)


def test_highest_priced_product_success():
    products = batch_calc.fetch_all_products()
    assert len(products) > 0

    expected_highest = max(products, key=lambda p: float(p['price']))
    batch_calc.highest_priced_product()
    actual_highest = max(products, key=lambda p: float(p['price']))

    assert actual_highest['name'] == expected_highest['name']


def test_lowest_priced_product_success():
    products = batch_calc.fetch_all_products()
    assert len(products) > 0

    expected_lowest = min(products, key=lambda p: float(p['price']))
    batch_calc.lowest_priced_product()
    actual_lowest = min(products, key=lambda p: float(p['price']))

    assert actual_lowest['name'] == expected_lowest['name']
