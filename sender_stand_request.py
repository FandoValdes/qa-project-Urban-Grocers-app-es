import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response1 = post_new_user(data.user_body)
print(response1.status_code)
print(response1.json())
auth_token = response1.json()['authToken']

def post_new_client_kitgi(kit_body):
    headers_con_token = data.headers.copy()
    headers_con_token['Authorization'] = f'Bearer {auth_token}'

    return requests.post(configuration.URL_SERVICE + configuration.endpoint_crear_kit,
                         json=kit_body,
                         headers=headers_con_token)


kit_response = post_new_client_kit(data.kit_body)

print(kit_response.status_code)
print(kit_response.json())

