import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    print (user) 

    assert user[0][0] == 'Sergii'
    assert user[0][1] == 'Maydan Nezalezhnosti 1'
    assert user[0][2] == 'Kyiv'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.get_prodcut_qnt_by_id(1)
    print('Water Quantity:', water_qnt)
    assert water_qnt[0][1] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'cookie', 'sweet', 40)
    product_qnt = db.get_prodcut_qnt_by_id(4)
    print('Product:', product_qnt)
    assert product_qnt[0][1] == 40

@pytest.mark.database
def test_delete_product():
    db = Database()
    db.insert_product(111, 'test', 'test', 1)
    db.delete_product(111)
    product = db.get_prodcut_qnt_by_id(111)

    assert len(product) == 0 

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Orders", orders)
    
    # Check quantity of orders equal to 1
    # assert len(orders) == 3

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'

# Add new Order
@pytest.mark.database
def test_insert_order():
    db = Database()
    order = db.add_order(123, 1, 1, '11:00:00')
    orders = db.get_detailed_orders()
    print("GS Orders:", orders)

    # check new order ID is added
    assert orders[1][0] == 123

# Add oorder WITHOUT Date !!test failed, record is added with none as a date !
@pytest.mark.database
def test_add_order_no_date():
    db = Database()
    orders = db.get_detailed_orders()
    len_before = len(orders)
    order = db.add_order(230, 1, 1, None)
    
    orders = db.get_detailed_orders()
    len_after = len(orders)
    print('GS Orders', orders)
    print("before = ", len_before, "after = ", len_after)
    # Check that order without date isn't created and no additional element is added to list
    assert len_before == len_after

