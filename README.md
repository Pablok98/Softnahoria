# Softnahoria :carrot:


## Instalación
**NOTA IMPORTANTE**: mientras estaba haciendo el script estuve aprendiendo como hacer argumentos
para correr los comandos en consola. Por lo tanto, por ahora (solución ya viene en camino!), para correr los comandos que 
se indican, **hay que estar ubicado en la carpeta que contiene la aplicación Softnahoria**, no dentro de ella.

**Pasos:**

0. Preparar Python
1. Crear archivos básicos
2. Conseguir api keys y crear archivo .env
3. Generar token oauth

### Preparar Python
Primero tenemos que asegurarnos que el Python que vamos a utilizar tiene todas las librerias necesarias. Podemos instalarlas usando pip.

Este comando es el único que se tiene que hacer **dentro** del directorio Softnahoria

```pip install -r requirements.txt```


### Archivos básicos

Antes de poder utilizar cualquier comando, es necesario crear los archivos básicos necesarios
para que la aplicación funcione. Por suerte, Softnahoria puede hacer esto por nosotros. Solo hay que correr el comando

```python softnahoria install```

### Conseguir API Keys y preparar .env
A continuación, es el paso que se podría considerar más complicado. Necesitaremos conseguir algunas llaves de autentificación
para que la aplicación pueda acceder a tu cuenta, sin tener que loguear cada vez. El proceso es un poco más largo porque no quería
usar librerías externas con información personal.

**Paso 1:** estar logueado en tu cuenta de Trello en tu navegador y visitar la página https://trello.com/app-key

**Paso 2:** crear un archivo de nombre `.env` con los siguientes contenidos:

```
TR_KEY=<llave>
TR_SECRET=<llave_secreta>
```

donde `llave` es el código que aparece al inicio de la página en una cápsula con título "Key" y `llave_secreta` es
el código que aparece al final de la página con título "Secret" (bajo el título OAuth)

### Generando el token de login 

Ahora será necesario volver a editar el archivo `.env`, pero con unos códigos generados con Softnahoria mismo.

**Paso 1**: correr el comando

```python softnahoria oath```

**Paso 2**: dicho comando mostrará un link en consola, el cual tendrás que visitar. Al visitarlo, Trello pedirá que autorices
con tu cuenta el request que estará haciendo esta aplicación. Simplemente tienes que aceptarlo.

**Paso 3**: una vez aceptado, se mostrará en pantalla un código, el cual tienes que ingresar en consola. Si haces los pasos correctamente,
entonces se mostrará en pantalla el siguiente mensaje:

```
oauth_token = <token>
oauth_token_secret = <token_secreto>
```

**Paso 4:** utilizando los datos que se muestran en pantalla, deberás **agregar** las siguientes líneas al archivo
`.env` que habías creado antes:

```
TR_OATH_TOKEN=<token>
TR_OATH_TOKEN_SECRET=<token_secreto>
```
*pd: se creará una archivo con los datos en un archivo secret.json, en caso de necesitarlo*

y con eso, ¡Estás listo para utilizar la aplicación! 


## Como utilizar Softnahoria

### Agregando grupos

El siguiente comando permite agregar nuevos grupos para trackear:

```python softnahoria newgroup```

dicho comando pedirá dos inputs adicionales:

- `nombre`: nombre del grupo. Este es el que tu quieras. Las carpetas y futuras referencias del grupo utilizarán este nombre
- `link`: link al tablero a trackear. Es importante que sea el que utilizas para llegar al "home" del tablero (ej: `https://trello.com/b/QdAMih9N/prueba`)

con esto, el grupo ya estará siendo trackeado con los comandos de la app.

### Guardando el estado actual de los tableros

```python softnahoria update```

Con este comando, se guardará localmente la información de todos los tableros en su estado actual. Se guardará localmente por fecha,
pero puedes hacerlo más de una vez al día (con formato: `fecha|N°update`)

### Generando excels

```python softnahoria excel```

Este comando genera/actualiza los excel de cada grupo, creando un archivo para cada grupo con el nombre del tablero y el número de entrega. Los archivos tendrán una hoja para cada actualización hecha.

**Para encontrar los excels, la ruta es ```data/<nombre_grupo>/excel```**