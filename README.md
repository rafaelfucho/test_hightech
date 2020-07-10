# test_hightech
prueba basica backen

contiene:
base de datos mongodb
proyecto postman
requerimientos
archivo index

proyecto realizado en python para una pequeña api rest con metodos get, post y put

(GET)
http://127.0.0.1:5000/usuario
muestra json con data de usuarios (id, nombre, apellido, tdc)


(GET)
http://127.0.0.1:5000/usuario/2
muestra json con data de usuario especifico por id (id, nombre, apellido, tdc)


(POST)
http://127.0.0.1:5000/usuario
se pasa por parametro json con datos para ingresar nuevo usuario con token (si el token es incorrecto no guarda)
{
    "nombre":"Prueba",
    "apellido":"test",
    "tdc":"111111111111111",
    "token":"aKc8Rk390UqDD24i"
}


(PUT)
http://127.0.0.1:5000/usuario/"
se pasa por parametro json con datos para editar usuario existente segun id con token (si el token es incorrecto no actualiza)
{
    "nombre":"Prueba",
    "apellido":"test22222",
    "tdc":"111111111111111",
    "token":"aKc8Rk390UqDD24i"
}
