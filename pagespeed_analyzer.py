"""
📊 PageSpeed Insights Analyzer
Autor: Kevin Sepúlveda
Descripción: Script para analizar métricas de rendimiento web usando la API de Google PageSpeed Insights
"""

import requests
import pandas as pd
import os
import re
import logging
from datetime import datetime
from dotenv import load_dotenv

# Configuración inicial
load_dotenv()  # Carga variables de entorno desde .env
logging.basicConfig(filename='pagespeed.log', level=logging.INFO)

API_KEY = os.getenv('PAGESPEED_API_KEY')  # Clave desde variables de entorno
MAX_REQUESTS = 50
OUTPUT_DIR = os.path.join(os.path.expanduser('~'), 'Downloads', 'POWER BI')
METRICS = ['performance', 'first-contentful-paint', 
          'largest-contentful-paint', 'interactive', 
          'cumulative-layout-shift']

def validate_url(url: str) -> bool:
    """Valida el formato de una URL"""
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # Protocolo
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Dominio
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
        r'(?::\d+)?'  # Puerto
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def get_pagespeed_data(url: str) -> dict:
    """Obtiene datos de la API de PageSpeed Insights"""
    try:
        response = requests.get(
            f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed',
            params={'url': url, 'key': API_KEY, 'strategy': 'desktop'},
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Error en la API para {url}: {str(e)}")
        return None

def process_results(data: dict, url: str) -> dict:
    """Procesa la respuesta de la API y extrae métricas clave"""
    if not data or 'lighthouseResult' not in data:
        return None

    lhr = data['lighthouseResult']
    results = {'url': url, 'timestamp': datetime.now().isoformat()}
    
    try:
        results['performance_score'] = lhr['categories']['performance']['score']
        for metric in METRICS:
            results[metric] = lhr['audits'][metric]['numericValue']
        return results
    except KeyError as e:
        logging.error(f"Error procesando métricas para {url}: {str(e)}")
        return None

def save_to_csv(df: pd.DataFrame, filename: str) -> None:
    """Guarda los resultados en un archivo CSV"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    full_path = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(full_path, index=False)
    logging.info(f"Datos guardados en {full_path}")
    print(f"✅ Archivo guardado en: {full_path}")

def main():
    """Función principal del programa"""
    print("🚀 PageSpeed Insights Analyzer v2.0")
    print(f"🔑 API Key: {'✅' if API_KEY else '❌ No encontrada'}")
    
    df = pd.DataFrame()
    try:
        num_requests = min(int(input("\n📝 Número de URLs a analizar (max 50): ")), MAX_REQUESTS)
        
        for _ in range(num_requests):
            while True:
                url = input("\n🔗 Ingrese URL: ").strip()
                if validate_url(url):
                    break
                print("❌ Formato de URL inválido. Intente nuevamente.")
            
            if data := get_pagespeed_data(url):
                if processed := process_results(data, url):
                    df = pd.concat([df, pd.DataFrame([processed])], ignore_index=True)
                    print(f"📊 Datos obtenidos para {url}")
                    
        if not df.empty:
            print("\n📋 Resultados obtenidos:")
            print(df[['url', 'performance_score']])
            save_to_csv(df, 'pagespeed_results.csv')
        else:
            print("⚠️ No se obtuvieron datos válidos")

    except ValueError:
        print("❌ Error: Ingrese un número válido")
    except Exception as e:
        logging.error(f"Error inesperado: {str(e)}")
        print("❌ Ocurrió un error inesperado. Ver logs para detalles.")

if __name__ == "__main__":
    main()