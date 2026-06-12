# PEC4 Programción para la Ciencia de Datos
#Brandon Naranjo

DESCRIPCIÓN

El proyecto analiza los resultados históricos de la LaLiga apartir del año 1995 hasta 2025 utlizando Python, Pandas, Matplotlib y NetworkX.


ESTRUCTURA DEL PROYECTO
 - src/data: LaLiga_Matches.csv
 - src/exercises: 1,2,3,4,5,6,7
 - src/img: gráficos
 - screemshots: resultados del análisis
 - tests: test_exe6.py (fun_total_goals)
 - doc: documentación HTML 

EJECUCIÓN PARA GRAFICOS

- pip install -r requeriments.txt
- python  src/main.py

 
 EJECUCIÓN DEL TEST
- pip install -r requeriments.txt
- python -m unittest tests/test_ex6.py

COMPROBACIÓN DE LINTER

Instalación de pylint:
- pip install pylint

Ejecutar pylint
- pylint src/exercises/*.py

DOCUMENTACIÓN (PYDOC)
- python -m pydoc -w src.exercises.ex1
- python -m pydoc -w src.exercises.ex2
- python -m pydoc -w src.exercises.ex3
- python -m pydoc -w src.exercises.ex4
- python -m pydoc -w src.exercises.ex5
- python -m pydoc -w src.exercises.ex6
- python -m pydoc -w src.exercises.ex7

Mover archivos HTML generados
- mv *.html doc/
  

