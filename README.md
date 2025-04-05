# Curso de Testing de la UCSM

Para levantar y probar los escenarios de test deben de instalar las librerias, para ello, primeramente deben de crear un entorno virtual

```
py -m venv entorno
```

Luego deben activar ese entorno virtual

## En Windows

- Usando Gitbash

```
source entorno/Scripts/activate
```

- Usando Powershell | CMD

```
source entorno/Scripts/activate
```

## En MAC

```
source entorno/bin/activate
```

Una vez con el entorno activado instalar las librerias

```
pip install -r requirements.txt
```

Ahora ya tienes todo instalado, para correr los escenarios de test, usa el siguiente comando

- Esto correra todos los escenarios de test de la carpeta `test`

```
pytest test/
```

- Para correr un solo archivo

```
pytest test/suma_test.py
```

- Para correr una sola funcion del archivo

```
pytest test/suma_test::test_suma
```

Eso es todo, ya puedes empezar a testear en Python, para mas información puedes mandarme un correo a ederivero@ucsm.edu.pe
