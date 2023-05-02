import os

repo = input ('Introduce el nombre del repositorio: ')
usuario = input ('Introduce el usuario de gitlab: ')
repogit = repo + '_git'
os.system('git cvsimport -C ' + repogit + ' -r cvs -k -vA authors-file.txt -d $CVSROOT ' + repo)
os.chdir(repogit)

os.system('git remote add origin ssh://git@localhost:8022/' + usuario + '/' + repo + '.git')
os.system('git push -u origin --all && git push -u origin --tags')
