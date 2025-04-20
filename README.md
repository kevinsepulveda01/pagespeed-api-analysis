# 📊 PageSpeed Insights Analyzer

**Autor:** Kevin Sepúlveda  
**Descripción:** Script en Python para analizar métricas de rendimiento web utilizando la API de Google PageSpeed Insights.  
**Versión:** 2.0

---

## 📌 Índice

- [📚 Descripción](#-descripción)
- [🚀 Características](#-características)
- [⚙️ Requisitos](#️-requisitos)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🔧 Instalación](#-instalación)
- [✅ Uso](#-uso)
- [📝 Variables de Entorno](#-variables-de-entorno)
- [📤 Resultados](#-resultados)
- [🧪 Ejemplo de Ejecución](#-ejemplo-de-ejecución)
- [🛠️ Posibles Errores y Soluciones](#️-posibles-errores-y-soluciones)
- [📄 Licencia](#-licencia)

---

## 📚 Descripción

Este script automatiza la consulta de métricas de rendimiento web utilizando la API pública de [Google PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/about). Analiza varias URLs (hasta 50), extrae métricas clave de rendimiento, y guarda los resultados en un archivo `.csv` listo para ser utilizado en herramientas como Power BI.

---

## 🚀 Características

- Validación de URLs antes del análisis.
- Uso de la API oficial de PageSpeed Insights (modo escritorio).
- Extracción de métricas clave como:
  - `performance`
  - `first-contentful-paint`
  - `largest-contentful-paint`
  - `interactive`
  - `cumulative-layout-shift`
- Guardado automático de resultados en un archivo CSV.
- Logging de errores y eventos.
- Compatible con `.env` para mayor seguridad.

---

## ⚙️ Requisitos

- Python 3.7 o superior
- Una cuenta de Google Cloud con una clave de API habilitada para PageSpeed Insights

---

## 📁 Estructura del Proyecto
pagespeed_analyzer/
│
├── .env # Archivo de variables de entorno (contiene API_KEY)
├── pagespeed_analyzer.py # Script principal de análisis PageSpeed
├── pagespeed.log # Archivo de registro de actividades
└── README.md # Documentación del proyecto (este archivo)


---

## 🔧 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/pagespeed_analyzer.git
cd pagespeed_analyzer
```

2. Instala los paquetes necesarios:
```bash
pip install -r requirements.txt
```
Si no tienes requirements.txt, puedes instalar manualmente:

3. Crea un archivo .env con tu clave de API de Google:
```bash
PAGESPEED_API_KEY=tu_clave_aqui
```

## ✅ Uso
Ejecuta el script desde consola:
```bash
python pagespeed_analyzer.py
```
1. Se te pedirá el número de URLs a analizar (máx 50).
2. Ingresa las URLs una por una.
3. El programa validará el formato y procesará cada URL.
4. Al finalizar, los resultados se guardarán en la carpeta de Descargas/POWER BI en un archivo llamado pagespeed_results.csv.


## 📝 Variables de Entorno
El script utiliza la librería python-dotenv para cargar tu API Key de forma segura desde un archivo .env.

Ejemplo:
```bash
PAGESPEED_API_KEY=AIzaSyXXXXXXXXXXXXXXX
```
Nunca compartas tu API Key públicamente.

## 🧪 Ejemplo de Ejecución
```text
🚀 PageSpeed Insights Analyzer v2.0
🔑 API Key: ✅

📝 Número de URLs a analizar (max 50): 2

🔗 Ingrese URL: https://example.com
📊 Datos obtenidos para https://example.com

🔗 Ingrese URL: https://openai.com
📊 Datos obtenidos para https://openai.com

📋 Resultados obtenidos:
                         url  performance_score
0        https://example.com               0.92
1         https://openai.com               0.88

✅ Archivo guardado en: /Users/tu_usuario/Downloads/POWER BI/pagespeed_results.csv

```
