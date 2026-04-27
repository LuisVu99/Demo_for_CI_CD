import json
from jsonschema import validate, ValidationError

class APIHelpers:
    def parse_json(response):  #Chuyen tu dang chuoi sang dang python Object (dict, list...)
        try:
            return response.json()  #Cu phap chuyen
        except json.JSONDecodeError:  #fallback: xu ly du phong va neu loi thi tra ve None
            return None
        
    def assert_status_code(response, expected_code):  #Check status code
        actual_code = response.status_code
        assert actual_code == expected_code , f"Expected {expected_code}, but got {actual_code}"

    def assert_json_value(response_json, key: str, expected_value, strict: bool = True):
        assert key in response_json, f"Key '{key}' not found in response"  #Danh gia xem key no ton tai o response ko?
        if strict: #Su dung if else de: 1. Danh gia xem neu key co value thi value co dung khong. 2. Danh gia xem key co value hay khong
            assert response_json[key] == expected_value, \
                f"Expected '{expected_value}', but got '{response_json[key]}'"
        else:
            assert response_json is not None, \
                f"Value for Key '{key}' is None"

    def assert_json_key(response_json, expected_keys):
        # for key in expected_keys:  #Duyet trong so cac key, xem co cai key match with expected ko, neu ko in loi
        #     assert key in response_json == expected_keys, f"Missing key: {key}"
        if isinstance(response_json, dict):
            for key in expected_keys:
                assert key in response_json, f"Missing key: {key}"
        elif isinstance(response_json, list):
            for item in response_json:
                for key in expected_keys:
                    assert key in item, f"Missing key: {key} in {item}"
        else:
            raise TypeError(f"Unsupported type: {type(response_json)}")

    def validate_json_schema(response_json, schema: dict):  #Validate xem response co dung dang dict hay k
        try:
            validate(instance=response_json, schema=schema)  #So sanh rsponse vaf schema xem co giong dang schema(kieu) nhau k
        except ValidationError as e:  #fallback: xu ly du phong, neu loi thi in ra error message
            raise AssertionError(f"Schema validation failed: {e.message}")
        
    def get_json_value(response, key, default = None): #Lay gia tri trong Json theo 1 key
        # return response_json.get(key, default)  #Lay ra gia tri key, neu khong co thi lay default
        # Nếu response là requests.Response → chuyển sang dict/list
        if hasattr(response, "json") and callable(response.json):
            data = response.json()
        else:
            data = response

        # Nếu data là dict → lấy value theo key
        if isinstance(data, dict):
            return data.get(key, default)

        # Nếu data là list of dict → trả về list giá trị key
        if isinstance(data, list):
            return [item.get(key, default) for item in data]

        # Nếu type khác → trả về default
        return default

    def log_request_response(response): #Log nhanh request & response cho debug.
        req  = response.request
        print("------REQUEST--------")
        print(f"URL: {req.url}")
        print(f"Method: {req.method}")
        print(f"Headers: {req.headers}")
        if req.body:  #Khong phai request nao cung co body, nen su dung ham if
            print(f"Body: {req.body}")

        print("------RESPONSE-------")
        print(f"Status: {req.response.status_code}")
        print(f"Header: {req.response.headers}")
        print(f"Body: {req.response.body}")


