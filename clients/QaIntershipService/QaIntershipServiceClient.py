import requests

class QAIntershipServiceClient:
    def __init__(self, base_url: str = "https://qa-internship.avito.com"):
        self.base_url = base_url

    def createItem(self,
        seller_id: int,
        name: str,
        price: int,
        likes: int = 0,
        view_count: int = 0,
        contacts: int = 0,
    ):
        payload = {
            "sellerId": seller_id,
            "name": name,
            "price": price,
            "statistics": {
                "likes": likes,
                "viewCount": view_count,
                "contacts": contacts,
            },
        }
        response = requests.post(f'{self.base_url}/api/1/item', json=payload).json()
        return response
    def deleteItem(self, item_id):
        response = requests.delete(f'{self.base_url}/api/2/item/{item_id}')
        return response
    def checkFullItem(self, item_id):
        response = requests.get(f'{self.base_url}/api/1/item/{item_id}').json()
        return response
    def checkStatsItem(self, item_id, api_version):
        response = requests.get(f'{self.base_url}/api/{api_version}/statistic/{item_id}').json()
        return response
    def getSellerItems(self, seller_id):
        response = requests.get(f'{self.base_url}/api/1/{seller_id}/item').json()
        return response

