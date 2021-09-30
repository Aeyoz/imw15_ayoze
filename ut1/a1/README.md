# Creación de mi propia página web "Mis Series"

Debemos de tener el servicio de Nginx instalado y funcionando, es decir, activo.

Para ello debemos de ejecutar `` sudo apt install nginx `` y una vez se acabe el proceso de instalación ejecutamos `` systemctl start nginx `` y ``systemctl enable nginx``.

## Configuraciones previas de archivos y carpetas.

Debemos de crear un directorio en el que alojar nuestro proyecto con nuestro propio index.html, este será ``/home/alu<cial>/webapps/series``.

Ahora tenemos que crear nuestros archivos de configuración de nginx para hacer que la página funcione, para ello nos dirigimos al directorio ``/etc/nginx/sites-enable`` y debemos de borrar el archivo ``default`` que está ahí dentro para que no nos muestre la página de Nginx.

Nos dirigimos a ``/etc/nginx/sites-available`` y creamos el archivo ``alu<cial>.me`` y dentro escribiremos la siguiente configuración:

```

server {
    server_name alu<cial>.me
    location /series {
        root /home/alu<cial>/webapps  
    }

}


```

Con esto ya tenemos una parte de nuestra página configurada; nos movemos a la carpeta ``/etc/nginx/sites-enable`` y hacemos un enlace simbólico al fichero que acabamos de crear, para ello ejecutamos ``ln -s ../sites-available``. Hecho esto debemos de recargar el servicio Nginx y comprobar que todo está correcto.

Ahora debemos de editar el fichero ``/etc/hosts`` y debemos de añadir la linea siguiente

```

ip-de-la-máquina       alu<cial>.me

```

## Creación de la página web.

Para nuestra página web crearemos dentro de la carpeta un **index.html** y 2 carpetas más (**img** y **styles**) donde meteremos imágenes y archivos de estilos para "decorar" nuestra página.

Dentro del index montaremos nuestra página, una vez terminemos ahí configuramos el archivo css para ordenar los elementos de esta.

## Vista de la página

La página debería quedar de la siguiente manera.

![pagina](./img/001.png)

Al hacer click en una imagen debería de abrirse su respectiva página en imdb.
