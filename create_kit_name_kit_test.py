import sender_stand_request
import data

def get_new_user_token():
    return sender_stand_request.auth_token

def get_kit_body(name):
    kit = data.kit_body.copy()
    kit["name"] = name
    return kit

def positive_assert(kit_body):
    kit = get_kit_body(kit_body)
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 201
    assert response.json()["name"] != ""

def negative_assert_code_400(name):
    kit = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 400

def test_kit_name_length_1_caracter():
    positive_assert("a")

def test_kit_name_511_caracteres():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    positive_assert(name)

def test_kit_name_vacio():
    negative_assert_code_400("")

def test_kit_name_512_caracteres():
    name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    negative_assert_code_400(name)

def test_kit_name_caracteres_especiales():
    positive_assert("№%@,")

def test_kit_name_espacios_entre_letras():
    positive_assert(" A Aaa ")

def test_kit_name_numeros_string():
    positive_assert("123")

def test_kit_name_vacio2():
        kit = data.kit_body.copy()
        kit.pop("name")
        assert sender_stand_request.post_new_client_kit(kit).status_code == 400

def test_kit_es_un_int():
    positive_assert(123)