from cryptography.fernet import Fernet

mensaje = "Esta es una prueba para ver como funciona la encriptación / desencriptación con Fernet en Python"

# Atención: La función generar_clave devuelve un objeto fernet , no la clave en sí (que es la variable key)
def generar_clave():
    key = Fernet.generate_key()
    fernet=Fernet(key)
    return fernet

# Encriptar 
def encripta_mensaje(mensaje,clave):
    return clave.encrypt(mensaje.encode())

# Desencriptar 
def desencripta_mensaje(mensaje,clave):
    return clave.decrypt(mensaje).decode()

clave = generar_clave()
mensaje_encriptado = encripta_mensaje(mensaje,clave)
mensaje_desencriptado = desencripta_mensaje(mensaje_encriptado,clave)

print("Mensaje               ; ",mensaje)
print("Mensaje encriptado    : ",mensaje_encriptado) 
print("Mensaje desencriptado : ",mensaje_desencriptado)