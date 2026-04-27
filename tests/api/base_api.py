import requests

class BaseAPI:
    #Ham khoi tao -> Luu tru info dung cho cac ham khac, ko phai token nao cung can truyen nen token = None
    #Cac doi so nhan tt tu ham test, sau do cac ham ben trong nay se su dung lai
    def __init__(self, base_url, token = None): 
        self.base_url = base_url
        self.token = token

    #Khoi tao header de dung cho cac ham trong class
    def _headers(self, extra_headers=None):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}
    
    #Ham get API
    def get(self, endpoint: str, **kwargs):  #**kwargs: cho phép truyền thêm tham số tùy ý (ví dụ params, timeout, …).
        return requests.get(f"{self.base_url}{endpoint}",
                            headers= self._headers(),
                            **kwargs)
    
    #Ham post API
    def post(self, endpoint: str, data = None, json = None, **kwargs):
        return requests.post(f"{self.base_url}{endpoint}",
                             headers= self._headers(),
                             json = data,
                            #  json = json,
                             **kwargs)
    
    #Ham put API
    def put(self, endpoint: str, data = None, headers= None, **kwargs):
        return requests.put(f"{self.base_url}{endpoint}",
                            headers=headers,
                            json=data,
                            **kwargs)
    
    #Ham delet API
    def delete(self, endpoint: str, headers = None, **kwargs):
        return requests.delete(f"{self.base_url}{endpoint}",
                               headers = headers,
                               **kwargs)


