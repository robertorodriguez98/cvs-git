#!/bin/bash

echo "Dime el nombre del repositorio: "
read repositorio
mkdir $repositorio && cd $repositorio
cvs import -m "Commit inicial" $repositorio ROBERTO V1_0
cd $repositorio
cvs checkout $repositorio
echo "Hola buenos dias a todos" > hola.txt
cvs add hola.txt
cvs commit -m "Añadido hola.txt"
echo "Hola buenas tardes a todos" >> hola.txt
cvs commit -m "Modificado hola.txt"