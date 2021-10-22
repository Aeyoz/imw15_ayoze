# Aplicaciones en php y python.

Lista de paquetes necesarios para que la practica pueda realizarse:
* Php
* Python3.8
* pip
* uwsgi
* supervisor

#### Preparativos

Debemos de tener una ip fija en la máquina, en mi caso la ip es: **172.19.28.15** y tener configurado en el fichero **/etc/hosts** añadidos los nombres de los servidores que vamos a usar para que las aplicaciones web tengan un sitio en el que mostrarse.

Debemos de tener añadidos los nombres de now."cial".me y php."cial.me"

![](./img/php/008.png)

Debemos de tener descargado y descompreso el archivo **demo_php.zip** que se adjunta con los requisitos de la práctica. Este contienne la carpeta demo_php que he llamado demo para más comodidad. Los permisos de esta carpeta deben ser **755** para todos los archivos y el usuario propietario debe ser el usuario **alu"cial"**

En caso de haber descomprimido la carpeta como usuario root se debe cambiar los permisos con:

Debemos crear y enlazar los ficheros **/etc/nginx/sites-available/php."cial".me** y **/etc/nginx/sites-available/now."cial".me** en la carpeta de **sites-enabled** dentro de **/etc/nginx**.

Para ello podemos ejecutar el comando **ln -s ../sites-available nombre-fichero** desde **/etc/nginx/sites-enable**.

![](./img/php/007.png)

~~~

chmod 755 demo/*

chown alu"cial" demo/*

chgrp alu"cial" demo/*

~~~

![](./img/php/002.png)

## Aplicación Php

Dentro del fichero **/etc/nginx/sites-available/php."cial".me** se encuentra escrita la configuracion del servidor que hace posible la visualización de la aplicacion web de php, el contenido es el siguiente:

![](./img/php/003.png)

Aquí tenemos un vistazo de la aplicación funcionando en el navegador.

![](./img/php/004.png)

## Aplicación Python

Empezamos escribiendo la configuración del servidor que mostrará la aplicación.

![](./img/python/004.png)

Ahora debemos de crear un entorno de desarrollo de aplicaciones dentro de la carpeta **webapps/now**, para ello ejecutamos los comandos sudo pipenv install y sudo pipenv --venv.

![](./img/python/001.png)

Creamos dentro de la carpeta now el fichero main.py que será la aplicación que correrá la página web de now."cial".me.

![](./img/python/002.png)

Dentro del fichero escribimos lo siguiente.

![](./img/python/010.png)

Creamos un fichero **run.sh** para la aplicación y lo rellenamos con la siguientes líneas:

~~~
#!/bin/bash
cd "$(dirname "$0")"
PYTHON_VENV=$(pipenv --venv)
uwsgi --socket :8081 --home $PYTHON_VENV -w main:app
~~~

Cuando ejecutamos la aplicación y escribimos la direccion del servidor en el buscador nos sale la siguiente página.


![](./img/python/006.png)

## Preparativos para supervisor

Para obtener supervisor debemos de ejecutar el comando sudo apt install supervisor.

Debemos de acceder a los ficheros de configuracion en /etc/supervisor/ y añadir/cambiar las siguientes lineas


## Supervisor para aplicaciones Python

Al consultar el estado de la página **now** con supervisorctl status now como usuario con permisos para usar supervisor vemos que no está activa.

![](./img/python/011.png)

Por lo que si fueramos a usar la página no nos llevaría hasta ella.

![](./img/python/012.png)

Ahora encendemos **now**.

![](./img/python/013.png)

Ahora vemos que si es accesible la página.

![](./img/python/017.png)

Paramos el servicio y como antes cuando estaba parado no se puede acceder.

![](./img/python/015.png)

Si reiniciamos el servicio e intentamos acceder de nuevo a la página vemos que sí está operativa

![](./img/python/016.png)

![](./img/python/017.png)
