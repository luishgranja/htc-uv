

# MiniProyecto Plataformas a Gran Escala

Proyecto para hacer el uso de HTCondor UV

## Integrantes

 1. Luis Granja - 1533329 - luis.granja@correounivalle.edu.co
 2. Iván Toro - 1523548 - ivan.toro@correounivalle.edu.co
 3. Sebástian Villegas - 1533597 - jhoan.villegas@correounivalle.edu.co

## Uso
```bash
condor_submit exec.condor
```

## Archivos

### proc0.py
Script en Python que permite transformar una imagen a blanco y negro a traves de operaciones con la matriz de pixeles.

### proc1.py
Script en Python que usando el operador de Sobel permite hallar los bordes de una imagen, que al final se convierte en un filtro.

### run_py.sh
Script que contiene las ordenes necesarias para llevar a cabo la tarea principal en el nodo del cluster.

### exec.condor
Archivo que especifica los parametros de la ejecución de nuestra tarea en el cluster.

## Licencia
[MIT](https://choosealicense.com/licenses/mit/)
