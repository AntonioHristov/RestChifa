# RestChifa
Proyecto Final Daw2V ies Juan de la Cierva

Próximo paso: 

paginar las páginas restantes (lo que hice con los platos populares en el menú principal, no mostrarlos todos a la vez, sino en grupos de x platos)
crear logo,
intentar hacer la pagina bonita, probablemente con bootstrap,
Crear datos guiandome de la pagina chifadomari

// Opcional si voy sobrado

pk de Menu_Dish sea un mixto de name_menu y name_dish, con barra de busqueda en admin
crear telefonos e emails extra y pintarlos en la pagina contact,
poder buscar por pk en admin
boton reset despues de submit (tal vez https://stackoverflow.com/questions/14589193/clearing-my-form-inputs-after-submission)
crear una barra de búsqueda que filtre los resultados,
datos reservas solo visible para los administradores,
en página platos los menus que toquen (detectando el dia, etc)
intentar de nuevo conseguir la hora local del usuario o guardar una lista y dar a elegir la zona horaria en el formulario,
validaciones del formulario en cliente, probablemente con javascript,
crear algún restaurante más y considerar datos distintos entre ellos,
actualizar los dibujos
optimizar, limpiar el código y pensar más cosas



Requerimientos:

	* Sistema Operativo Windows
		Instalar Python (https://www.python.org/downloads/) 
		Abrir CMD (como administrador recomiendo), 
		(con el comando cd) ir a la carpeta django
		ejecutar el comando virtualProyect\Scripts\activate.bat
		(con el comando cd) ir a la carpeta finalProyect (el primero solo)
		ejecutar el comando py manage.py runserver
		Abrir un navegador con http://localhost:8000/restChifa/

	* Sistema Operativo Linux
		Abrir terminal (como administrador recomiendo), 
		Instalar Python (sudo apt-get install python3) 
		(con el comando cd) ir a la carpeta django\finalProyect
		ejecutar el comando python manage.py runserver
		Abrir un navegador con http://localhost:8000/restChifa/

	* Para entrar en http://localhost:8000/restChifa/admin como administrador:
		usuario: ah
		contraseña: ah
		email: ah@ah.ah

Referencias destacadas:

	https://docs.djangoproject.com/en/4.1/howto/windows/
	https://ourcodeworld.com/articles/read/236/how-to-setup-your-first-django-project-and-say-hello-world-in-windows
	https://docs.djangoproject.com/en/4.1/intro/tutorial01/
	https://projectsplaza.com/how-to-save-form-data-in-database-in-django/
	https://stackoverflow.com/questions/24710233/python-convert-time-to-utc-format
	https://docs.djangoproject.com/en/4.2/topics/pagination/
	http://www.chifadoromari.com



