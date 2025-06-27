#!/usr/bin/env python3
"""
Demo de BatteryZenith
Este archivo demuestra las funcionalidades básicas de la aplicación
"""

import psutil
import time
from config import MESSAGES, MONITORING_CONFIG

def demo_battery_info():
    """Demostrar cómo obtener información de la batería"""
    print("=== Demo de Información de Batería ===")
    
    try:
        battery = psutil.sensors_battery()
        if battery:
            print(f"Nivel de batería: {battery.percent}%")
            print(f"Conectado: {'Sí' if battery.power_plugged else 'No'}")
            
            if battery.secsleft != -1:
                hours = battery.secsleft // 3600
                minutes = (battery.secsleft % 3600) // 60
                print(f"Tiempo restante: {hours}h {minutes}m")
            else:
                print("Tiempo restante: Calculando...")
        else:
            print("No se detectó batería")
    except Exception as e:
        print(f"Error al obtener información de batería: {e}")

def demo_system_info():
    """Demostrar cómo obtener información del sistema"""
    print("\n=== Demo de Información del Sistema ===")
    
    try:
        # CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"Uso de CPU: {cpu_percent}%")
        
        # Memoria
        memory = psutil.virtual_memory()
        print(f"Uso de memoria: {memory.percent}%")
        print(f"Memoria total: {memory.total // (1024**3):.1f} GB")
        print(f"Memoria disponible: {memory.available // (1024**3):.1f} GB")
        
        # Disco
        disk = psutil.disk_usage('/')
        print(f"Uso de disco: {disk.percent}%")
        print(f"Espacio total: {disk.total // (1024**3):.1f} GB")
        print(f"Espacio libre: {disk.free // (1024**3):.1f} GB")
        
    except Exception as e:
        print(f"Error al obtener información del sistema: {e}")

def demo_conservation_mode():
    """Demostrar el modo de conservación"""
    print("\n=== Demo de Modo de Conservación ===")
    
    threshold = MONITORING_CONFIG['conservation_threshold']
    print(f"Umbral de conservación: {threshold}%")
    print(f"Mensaje activado: {MESSAGES['conservation_enabled']}")
    print(f"Mensaje desactivado: {MESSAGES['conservation_disabled']}")

def demo_monitoring():
    """Demostrar el monitoreo en tiempo real"""
    print("\n=== Demo de Monitoreo en Tiempo Real ===")
    print("Monitoreando durante 10 segundos...")
    
    start_time = time.time()
    while time.time() - start_time < 10:
        try:
            battery = psutil.sensors_battery()
            if battery:
                print(f"\rBatería: {battery.percent}% | CPU: {psutil.cpu_percent()}% | Memoria: {psutil.virtual_memory().percent}%", end='')
            time.sleep(MONITORING_CONFIG['update_interval'])
        except KeyboardInterrupt:
            break
        except:
            pass
    
    print("\nMonitoreo completado.")

def main():
    """Función principal del demo"""
    print("BatteryZenith - Demo de Funcionalidades")
    print("=" * 50)
    
    # Ejecutar demos
    demo_battery_info()
    demo_system_info()
    demo_conservation_mode()
    demo_monitoring()
    
    print("\n" + "=" * 50)
    print("Demo completado. Para usar la aplicación completa, ejecuta:")
    print("python battery_zenith.py")

if __name__ == "__main__":
    main() 