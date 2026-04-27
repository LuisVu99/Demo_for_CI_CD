from tests.api.helpers.api_utils import APIHelpers

def test_get_token(client, token_body):
    response = client.get_token(token_body)
    APIHelpers.assert_status_code(response, 200)