# buildozer.spec

[app]

# (str) Título de la aplicación
title = Mi Bloc de Notas

# (str) Nombre del paquete (identificador único en la Play Store)
package.name = miblocdenotas

# AÑADE ESTA LÍNEA
version = 0.1

# (str) Dominio del paquete (recomendado usar el tuyo invertido)
package.domain = org.test

# (str) Código fuente de la aplicación
source.dir = .

# (list) Fuentes a incluir en el paquete
source.include_exts = py,png,jpg,kv,ttf

# (list) Lista de requisitos (librerías)
# ¡MUY IMPORTANTE! Aquí va todo lo que tu app necesita para funcionar.
requirements = python3,kivy,kivymd

# (str) Preset para orientación de pantalla
orientation = portrait

# (list) Permisos de Android
# ¡MUY IMPORTANTE! Para poder leer y escribir archivos.
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (bool) Si es True, la app se puede instalar en la tarjeta SD
android.storage_support = True

[buildozer]

# (int) Nivel de log (0 para errores, 1 para información, 2 para depuración)
log_level = 2