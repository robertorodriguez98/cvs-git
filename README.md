# cvs-git

1. Montar un servidor cvs (se puede usar docker)
2. Investigar como crear un repositorio cvs, tras ello crearlo
3. Darle contenido ha dicho repositorio (se recomiendan hacer commits)
4. Investigar como funciona la herramienta cvs-fast-export
5. Instalarse cvs-fast-export (no vale con apt install pues la versión de los repositorios es antigua. Se recomienda descargarse el codigo del repositorio oficial y compilarlo)
6. Instalar gitlab en docker (edicio ce). Se recomienda usar docker-compose.
7. Migrar el repositorio de cvs a git
8. Automatizar el séptimo paso con un script de python. Al lanzar este script se debe crear un repositorio en el gitlab y subir el repositorio migrado. Los parámetros de este script pueden ser los que queráis.
9. Documentación del proceso.

## 1. Montar un servidor cvs 

Para montarlo simplemente instalamos el paquete CVS en el servidor. Para ello, ejecutamos el siguiente comando:

```console
sudo apt install cvs
```


Vamos a instalarlo sobre la máquina directamente. Para ello, seguimos los pasos explicados en el siguiente enlace: [https://www.linuxfromscratch.org/blfs/view/5.1/server/cvsserver.html](https://www.linuxfromscratch.org/blfs/view/5.1/server/cvsserver.html)

1. Creamos un repositorio

```bash
mkdir /home/USUARIO/cvsroot &&
chmod 1777 /home/USUARIO/cvsroot &&
export CVSROOT=/home/USUARIO/cvsroot &&
cvs init
```

2. Importar contenido al repositorio

```bash
export CVSROOT=/home/USUARIO/cvsroot &&
cd [directorio del proyecto] &&
cvs import -m "Commit inicial" [nombre del proyecto] [nombre del vendedor] [nombre de la rama]
```

3. verificar el acceso a los repositorios locales

```bash
$ cvs co [nombre del proyecto]
cvs checkout: Updating cvstest
U cvstest/codigo.py
U cvstest/index.html
cvs checkout: Updating cvstest/CVSROOT
U cvstest/CVSROOT/checkoutlist
U cvstest/CVSROOT/commitinfo
U cvstest/CVSROOT/config
U cvstest/CVSROOT/cvswrappers
U cvstest/CVSROOT/loginfo
U cvstest/CVSROOT/modules
U cvstest/CVSROOT/notify
U cvstest/CVSROOT/postadmin
U cvstest/CVSROOT/postproxy
U cvstest/CVSROOT/posttag
U cvstest/CVSROOT/postwatch
U cvstest/CVSROOT/preproxy
U cvstest/CVSROOT/rcsinfo
U cvstest/CVSROOT/taginfo
U cvstest/CVSROOT/verifymsg
```

4. Verificar el acceso al repositorio remoto

```bash
export CVS_RSH=/usr/bin/ssh &&
cvs -d:ext:localhost:/var/cvsroot co cvstest
```
