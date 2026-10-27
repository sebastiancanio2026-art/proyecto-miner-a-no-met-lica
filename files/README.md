# Proyecto Final Integrador: Análisis de Minería No Metálica en Chile (Proyecto 12)

## Descripción del Proyecto
Este repositorio corresponde al **Avance 1 del Proyecto Final Integrador** de la asignatura de **Programación Avanzada**. El objetivo del proyecto es analizar las estadísticas históricas de producción y exportación de la minería no metálica en Chile (utilizando registros oficiales de Cochilco y el Servicio Nacional de Aduanas) para comprender la evolución del sector, identificar tendencias y apoyar la toma de decisiones informadas mediante un pipeline automatizado en Python.

## Estructura del Repositorio
El proyecto cuenta con la siguiente organización modular:


proyecto12/
│
├── datos/
│   ├── Produccion-Mineria-No-Metalica-1996-2025.xlsx
│   ├── Exportaciones-Fisicas-Por-Destino-Mineria-No-Metalica-2002-2025.xlsx
│   ├── Exportaciones-Valorizadas-Por-Destino-Mineria-No-Metalica-2002-2025 (1).xlsx
│   └── README.md
│
├── reportes/
│   └── avance_1.pdf
│
├── src/
│   ├── __init__.py
│   ├── carga.py
│   ├── limpieza.py
│   ├── transformacion.py
│   ├── analisis.py
│   └── reporte.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py

```

## Requisitos y Dependencias

El proyecto utiliza **Python 3** y requiere las siguientes bibliotecas especificadas en el archivo `requirements.txt`:

* `pandas`
* `openpyxl`
* `matplotlib`

## Instrucciones de Instalación

Para instalar de forma automática las dependencias requeridas, abre tu terminal en la raíz del proyecto y ejecuta:

python -m pip install -r requirements.txt

```

## Instrucciones de Ejecución

Para poner en marcha el pipeline completo (carga, inspección inicial, análisis y generación del gráfico de evolución), ejecuta el archivo principal desde la raíz del proyecto con el siguiente comando:

python main.py

```

## Fuentes de Datos

* **Organización responsable:** Comisión Chilena del Cobre (Cochilco) y Servicio Nacional de Aduanas de Chile.
* **Período cubierto:** 1996 - 2025 (Producción) y 2002 - 2025 (Exportaciones).

