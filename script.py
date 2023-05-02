import os

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
lineas = "--------------------------------------------------------------------------"

## Fichero authors-file.txt
print(style.GREEN)
print(lineas)
print("Se va a generar el fichero authors-file.txt\nIntroduzca los datos de todos los autores.\nCuando acabe introduzca un punto (.)")
print(lineas)
print(style.RESET)
usuario = ""
while usuario != ".":
    usuario = input ('Introduce el usuario de linux: ')
    if usuario != ".":
        nombre = input ('Introduce el nombre completo del usuario: ')
        email = input ('Introduce el email del usuario: ')
        fichero = open("authors-file.txt", "a")
        fichero.write(usuario + " = " + nombre + " <" + email + ">\n")
        fichero.close()

## datos de git
print(style.GREEN)
print(lineas)
print("Se va a generar el repositorio de git.")
print(lineas)
print(style.RESET)
repo = input ('Introduce el nombre del repositorio de CVS: ')
usuarioGitlab = input ('Introduce el usuario de gitlab: ')
repogit = repo + '_git'

## Crear repositorio
print(style.GREEN)
print(lineas)
print("Creando repositorio de git")
print(lineas)
print(style.RESET)
os.system('git cvsimport -C ' + repogit + ' -r cvs -k -a -A authors-file.txt -d $CVSROOT ' + repo + ' 2>&1')
os.chdir(repogit)

##subiendo repositorio
print(style.GREEN)
print(lineas)
print("Subiendo repositorio a gitlab")
print(lineas)
print(style.RESET)
os.system('git remote add origin ssh://git@localhost:8022/' + usuarioGitlab + '/' + repo + '.git')
os.system('git push -u origin --all && git push -u origin --tags && echo "Repositorio subido con exito"')

