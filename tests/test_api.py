import pytest
from clients.QaIntershipService.QaIntershipServiceClient import QAIntershipServiceClient


@pytest.fixture()
def getitemid1():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=111321, name="Механическая клавиатура", price=1000, likes=1, view_count=1, contacts=1)
    item_id = response['status'].split(" - ")[-1]
    yield item_id
    client.deleteItem(item_id)

def test_valid_item(getitemid1):
    client = QAIntershipServiceClient()
    response_item = client.checkFullItem(getitemid1)
    found_item = response_item[0]
    selleritems = client.getSellerItems(111321)
    needed_item = [item['id'] for item in selleritems]
    assert found_item['id'] == getitemid1
    assert getitemid1 in needed_item

def test_negative_seller():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=-228, name="Монитор Asus", price=1000, likes=1, view_count=1, contacts=1)
    item_id = response['status'].split(" - ")[-1]
    client.deleteItem(item_id)  # Если объявление будет создано, то оно удалится, чтобы не засорять
    assert response['status'] == '400'

def test_noname_item():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=111321, name="", price=1000, likes=1, view_count=33, contacts=33)
    item_id = response['status'].split(" - ")[-1]
    client.deleteItem(item_id)  # Если объявление будет создано, то оно удалится, чтобы не засорять
    assert response['status'] == '400'

def test_negative_price():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=111321, name="Монитор Asus", price=-1000, likes=1, view_count=1, contacts=1)
    item_id = response['status'].split(" - ")[-1]
    client.deleteItem(item_id)  # Если объявление будет создано, то оно удалится, чтобы не засорять
    assert response['status'] == '400'

def test_zero_likes():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=111321, name="Монитор Zowie", price=1000, likes=0, view_count=1, contacts=1)
    item_id = response['status'].split(" - ")[-1]
    client.deleteItem(item_id)  # Если объявление будет создано, то оно удалится, чтобы не засорять
    assert response['status'] == '400'

def test_zero_views():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=111321, name="Монитор DEXP", price=1000, likes=1, view_count=0, contacts=1)
    item_id = response['status'].split(" - ")[-1]
    client.deleteItem(item_id)  # Если объявление будет создано, то оно удалится, чтобы не засорять
    assert response['status'] == '400'

def test_zero_contacts():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=111321, name="Монитор LG", price=1000, likes=1, view_count=1, contacts=0)
    item_id = response['status'].split(" - ")[-1]
    client.deleteItem(item_id)  # Если объявление будет создано, то оно удалится, чтобы не засорять
    assert response['status'] == '400'

def test_negative_likes():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=111321, name="Монитор ACER", price=1000, likes=-1, view_count=1, contacts=1)
    item_id = response['status'].split(" - ")[-1]
    client.deleteItem(item_id)  # Если объявление будет создано, то оно удалится, чтобы не засорять
    assert response['status'] == '400'

def test_negative_views():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=111321, name="Монитор Samsung", price=1000, likes=1, view_count=-1, contacts=1)
    item_id = response['status'].split(" - ")[-1]
    client.deleteItem(item_id)  # Если объявление будет создано, то оно удалится, чтобы не засорять
    assert response['status'] == '400'

def test_negative_contacts():
    client = QAIntershipServiceClient()
    response = client.createItem(seller_id=111321, name="Монитор Sony", price=1000, likes=1, view_count=1, contacts=-1)
    item_id = response['status'].split(" - ")[-1]
    client.deleteItem(item_id)  # Если объявление будет создано, то оно удалится, чтобы не засорять
    assert response['status'] == '400'

def test_get_item(getitemid1):
    client = QAIntershipServiceClient()
    response_item = client.checkFullItem(getitemid1)
    found_item = response_item[0]
    payload = {
        "sellerId": 111321,
        "name": "Механическая клавиатура",
        "price": 1000,
        "statistics": {
            "likes": 1,
            "viewCount": 1,
            "contacts": 1,
            },
        }
    assert found_item['name'] == payload['name']
    assert found_item['price'] == payload['price']
    assert found_item['sellerId'] == payload['sellerId']
    assert found_item['statistics']['contacts'] == payload['statistics']['contacts']
    assert found_item['statistics']['likes'] == payload['statistics']['likes']
    assert found_item['statistics']['viewCount'] == payload['statistics']['viewCount']

def test_get_notexist_item():
    client = QAIntershipServiceClient()
    response_item = client.checkFullItem('abc')
    assert response_item['status'] == '400'

def test_delete_notexist_item():
    client = QAIntershipServiceClient()
    response_item = client.deleteItem("abc")
    assert response_item.status_code == 400

def test_delete_item(getitemid1):
    client = QAIntershipServiceClient()
    response_delete = client.deleteItem(getitemid1)
    assert response_delete.status_code == 200
    response_item = client.checkFullItem(getitemid1)
    assert response_item['status'] == '404'
    selleritems = client.getSellerItems(111321)
    needed_item = [item['id'] for item in selleritems]
    assert getitemid1 not in needed_item

def test_statistics(getitemid1):
    client = QAIntershipServiceClient()
    payload = {
        "likes": 1,
        "viewCount": 1,
        "contacts": 1,

    }
    response_statistics = client.checkStatsItem(getitemid1, 1)
    found_statistics = response_statistics[0]
    assert found_statistics['likes'] == payload['likes']
    assert found_statistics['viewCount'] == payload['viewCount']
    assert found_statistics['contacts'] == payload['contacts']
    response_statistics = client.checkStatsItem(getitemid1, 2)
    assert found_statistics['likes'] == payload['likes']
    assert found_statistics['viewCount'] == payload['viewCount']
    assert found_statistics['contacts'] == payload['contacts']

def test_notexist_statistics():
    client = QAIntershipServiceClient()
    response_statistics = client.checkStatsItem('abc', 1)
    assert response_statistics['status'] == '400'
    response_statistics = client.checkStatsItem('abc', 2)
    assert response_statistics['status'] == '400'

def test_deleted_item_statistics(getitemid1):
    client = QAIntershipServiceClient()
    payload = {
        "likes": 1,
        "viewCount": 1,
        "contacts": 1,

    }
    client.deleteItem(getitemid1)
    client.deleteItem(getitemid1)
    response_statistics = client.checkStatsItem(getitemid1, 1)
    found_statistics = response_statistics[0]
    assert found_statistics['likes'] == payload['likes']
    assert found_statistics['viewCount'] == payload['viewCount']
    assert found_statistics['contacts'] == payload['contacts']
    response_statistics = client.checkStatsItem(getitemid1, 2)
    found_statistics = response_statistics[0]
    assert found_statistics['likes'] == payload['likes']
    assert found_statistics['viewCount'] == payload['viewCount']
    assert found_statistics['contacts'] == payload['contacts']
