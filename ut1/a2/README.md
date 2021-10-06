# Configuración de listado de archivos

### Configuración previa.

Creamos la carpeta shared en ```/home/alu<cial>/webapps/shared```.

## Archivos.

Empezamos enlazando los ficheros del sistema mediante enlaces simbólicos en la carpeta **shared**.

![](./img/001.png)

Procedemos a editar el fichero alu<cial>.me y añadimos las siguientes líneas.

* location= especifica la carpeta en la que está metido el index o archivos.

* root= especifica la ruta de nuestra carpeta.

* autoindex on genera un index automático y simple.

![](./img/002.png)

![](./img/003.png)

Recargamos el servicio y comprobamos que no hay nada que impida su funcionamiento.

![](./img/004.png)

Comprobamos que funciona nuestro sitio.

![](./img/005.png)

Ahora comprobamos que los archivos se pueden descargar.

![](./img/006.png)
