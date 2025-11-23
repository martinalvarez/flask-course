# FLASK_APP=app.py

FLASK_APP=app.py
flask run

Flask busca el archivo app.py, importa el módulo, encuentra la variable global app y la ejecuta.

✔ Simple
✔ Rápido
❌ NO escalable
❌ NO apto para apps grandes
❌ NO permite configurar cosas antes de crear la app
❌ No podés crear varias instancias de la app (tests, multi-tenant, etc.)
