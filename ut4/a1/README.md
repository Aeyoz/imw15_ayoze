
<center>

# TÍTULO DE LA PRÁCTICA


</center>

***Nombre:*** Ayoze Hernández Díaz
***Curso:*** 2º de Ciclo Superior de Administración de Sistemas Informáticos en Red.

### ÍNDICE

+ [Introducción](#id1)
+ [Objetivos](#id2)
+ [Creación y administración de la base de datos](#id3)
+ [Creación de la página de Wordpress](#id4)
+ [Generado de certificado SSL con certbot.](#id5)


#### ***Introducción***. <a name="id1"></a>

Wordpress es una plataforma que permite la creación de sitios web de manera sencilla y guiada al 80% de manera gráfica.

#### ***Objetivos***. <a name="id2"></a>

El objetivo es la creación de un sitio wordpress con certificado SSL.

#### ***Creación y administración de la base de datos***. <a name="id3"></a>

Empezamos creando una base de datos en la máquina de Azure (hecho en clase y no mostrado en el informe por temas de seguridad).

![](./img/001.png)

Descargamos y descomprimimos la ultima versión de Wordpress.

![](./img/002.png)

![](./img/003.png)

![](./img/004.png)

![](./img/005.png)

#### ***Creación de la página de Wordpress***. <a name="id4"></a>

Empezamos editando el fichero wp-config.php y cambiamos los campos que definen tanto la base de datos, como la contraseña y usuario que se van a usar.

![](./img/013.png)

Creamos un fichero de configuración de nginx.

![](./img/007.png)

Hacemos un enlace simbólico.

![](./img/008.png)

Instalamos un par de paquetes faltantes.

![](./img/009.png)

![](./img/010.png)

Añadimos la en nuestro dominio la extensión de **wordpress**.

![](./img/011.png)

Y vemos que podemos acceder a la instalación de wordpress. Ahora continuamos con valores por defecto y datos de usuario.

![](./img/014.png)

![](./img/015.png)

![](./img/016.png)

Entramos a nuestro wordpress y añadimos una entrada e instalamos un tema.

![](./img/017.png)

![](./img/018.png)

Vamos al apartado apariencia>temas e instalamos uno gratuito.

![](./img/019.png)

Lo personalizamos un poco.

![](./img/020.png)

![](./img/021.png)

![](./img/022.png)

![](./img/023.png)

Cambiamos el formato de la url para que aparezca la fecha actual, para ello vamos a **ajustes>enlaces permanentes>ajusts de los enlaces permanentes**.

![](./img/024.png)


![](./img/025.png)

Ahora añadimos una entrada tan fácil como ir a **Entradas>Añadir una nueva entrada** y escribir el contenido deseado.
![](./img/026.png)

#### ***Generado de certificado SSL con certbot***. <a name="id5"></a>

Instalamos certbot con sudo **apt install certbot** y ejecutamos los siguientes comandos:

![](./img/027.png)

![](./img/028.png)

![](./img/029.png)

Con esto el sitio ya es accesible por **https**
