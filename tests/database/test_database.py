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
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'

