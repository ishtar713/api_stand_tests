import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

# Obtener la tabla de usuarios (asumiendo que existe esta función)
    users_table_response = sender_stand_request.get_users_table()

# Crear la cadena que representa al usuario en la tabla
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
# Comprobar si el usuario existe y es único
    assert users_table_response.text.count(str_user) == 1

    print("Prueba completada con éxito: Se creó un usuario con nombre de 2 letras, se verificó su token y su unicidad en la tabla de usuarios.")

# Prueba 2. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene 15 caracteres
def test_create_user_15_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
#print("Prueba completada con éxito: Se creó un usuario con nombre de 15 letras.")


def test_create_user_1_letter_in_first_name_get_error_response():
    user_body = get_user_body("A")
    response = sender_stand_request.post_new_user(user_body)

# Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400
    assert response.json()["message"] == expected_message
# Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400
# Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  " \
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos, " \
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaa")

def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A a")

def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

def negative_assert_no_first_name(user_body):
    response = sender_stand_request.post_new_user(user_body)
# Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

# Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

# Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

# Prueba 8. Error
# La solicitud no contiene el parámetro "firstName"
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

# Prueba 9. Error
# El parámetro "firstName" contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body("")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

# Prueba 10. Error
# El tipo del parámetro "firstName" es un número
def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400

 # Comprobar el código de estado de la respuesta
    assert response.status_code == 400

