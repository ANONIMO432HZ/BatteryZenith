# 🔧 Documentación Técnica - BatteryZenith

<div align="center">

![Documentación Técnica](https://img.shields.io/badge/Documentación-Técnica-blue?style=for-the-badge)
![Arquitectura](https://img.shields.io/badge/Arquitectura-Python-green?style=for-the-badge)
![Interfaz](https://img.shields.io/badge/Interfaz-Tkinter-orange?style=for-the-badge)

**Guía técnica completa para desarrolladores y usuarios avanzados**

</div>

---

## 📋 Índice

- [🏗️ Arquitectura del Sistema](#️-arquitectura-del-sistema)
- [🔧 Componentes Principales](#-componentes-principales)
- [⚙️ Configuración](#️-configuración)
- [🔄 Flujo de Datos](#-flujo-de-datos)
- [🎨 Interfaz de Usuario](#-interfaz-de-usuario)
- [🛠️ API y Funciones](#️-api-y-funciones)
- [🔍 Monitoreo y Debugging](#-monitoreo-y-debugging)
- [🚀 Optimización](#-optimización)

---

## 🏗️ Arquitectura del Sistema

### 📊 Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                    BatteryZenith App                        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   GUI       │  │  Monitor    │  │  Config     │         │
│  │ (Tkinter)   │  │ (psutil)    │  │ (config.py) │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │  Threading  │  │  Windows    │  │   Images    │         │
│  │ (Updates)   │  │ (pywin32)   │  │  (Pillow)   │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

### 🔧 Tecnologías Utilizadas

| Componente | Tecnología | Versión | Propósito |
|------------|------------|---------|-----------|
| 🐍 **Lenguaje** | Python | 3.7+ | Lógica principal |
| 🖥️ **GUI** | Tkinter | Nativo | Interfaz gráfica |
| 📊 **Monitoreo** | psutil | 5.9.6+ | Datos del sistema |
| 🖼️ **Imágenes** | Pillow | 10.1.0+ | Manejo de iconos |
| 🪟 **Windows** | pywin32 | 306+ | Funcionalidades específicas |

---

## 🔧 Componentes Principales

### 🔋 **battery_zenith.py** - Aplicación Principal

#### 📋 Clase Principal: `BatteryZenith`

```python
class BatteryZenith:
    def __init__(self, root):
        # Inicialización de la aplicación
        # Configuración de ventana y variables
        
    def create_widgets(self):
        # Creación de la interfaz gráfica
        
    def start_monitoring(self):
        # Inicio del monitoreo en tiempo real
```

#### 🎯 Funciones Principales

| Función | Descripción | Frecuencia |
|---------|-------------|------------|
| `get_battery_info()` | Obtiene datos de batería | Cada 2s |
| `update_battery_display()` | Actualiza interfaz | Cada 2s |
| `update_system_info()` | Actualiza info del sistema | Cada 2s |
| `toggle_conservation_mode()` | Controla modo conservación | Manual |

### ⚙️ **config.py** - Configuración Centralizada

#### 🎨 Paleta de Colores

```python
COLORS = {
    'primary': '#2c3e50',      # Azul oscuro principal
    'secondary': '#34495e',    # Azul grisáceo secundario
    'accent': '#3498db',       # Azul claro para botones
    'success': '#2ecc71',      # Verde para batería alta
    'warning': '#f39c12',      # Naranja para batería media
    'danger': '#e74c3c',       # Rojo para batería baja
}
```

#### 📱 Configuración de Ventana

```python
WINDOW_CONFIG = {
    'width': 400,
    'height': 500,
    'title': 'BatteryZenith - Monitor de Batería',
    'resizable': False
}
```

#### ⏱️ Configuración de Monitoreo

```python
MONITORING_CONFIG = {
    'update_interval': 2,  # Segundos entre actualizaciones
    'conservation_threshold': 80  # Porcentaje para modo conservación
}
```

---

## ⚙️ Configuración

### 🔧 Variables de Entorno

```bash
# Configuración opcional (no requerida)
BATTERY_ZENITH_DEBUG=1        # Habilita modo debug
BATTERY_ZENITH_LOG_LEVEL=INFO # Nivel de logging
```

### 📁 Archivos de Configuración

| Archivo | Propósito | Ubicación |
|---------|-----------|-----------|
| `config.py` | Configuración principal | Raíz del proyecto |
| `requirements.txt` | Dependencias | Raíz del proyecto |
| `icon.ico` | Icono de la aplicación | Raíz del proyecto |

---

## 🔄 Flujo de Datos

### 📊 Diagrama de Flujo

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Sistema   │───▶│   psutil    │───▶│  Battery    │
│  Windows    │    │  Monitor    │    │   Data      │
└─────────────┘    └─────────────┘    └─────────────┘
                           │
                           ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   GUI       │◀───│  Process    │◀───│  Thread     │
│  Update     │    │   Data      │    │  Monitor    │
└─────────────┘    └─────────────┘    └─────────────┘
```

### ⏱️ Ciclo de Actualización

1. **Inicio**: Thread de monitoreo se inicia
2. **Lectura**: psutil obtiene datos del sistema
3. **Procesamiento**: Datos se formatean y validan
4. **Actualización**: GUI se actualiza con nuevos datos
5. **Espera**: Thread espera 2 segundos
6. **Repetición**: Ciclo se repite

---

## 🎨 Interfaz de Usuario

### 📱 Layout de la Interfaz

```
┌─────────────────────────────────────────────────────────┐
│                    BatteryZenith                        │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐ │
│  │              Estado de la Batería                   │ │
│  │  [████████████████████████████████████████] 80%    │ │
│  │  🔌 Conectado y cargando                           │ │
│  │  Tiempo restante: 2h 30m                           │ │
│  └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐ │
│  │            Modo de Conservación                     │ │
│  │  ☐ Limitar carga al 80%                            │ │
│  │  Reduce el desgaste de la batería                  │ │
│  └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐ │
│  │           Información del Sistema                   │ │
│  │  CPU: 45% | Memoria: 60% | Disco: 75%              │ │
│  └─────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│                    [Actualizar]                         │
└─────────────────────────────────────────────────────────┘
```

### 🎨 Sistema de Colores

#### 🔋 Colores de Batería

| Nivel | Color | Código | Descripción |
|-------|-------|--------|-------------|
| 🟢 **Alto** | Verde | `#2ecc71` | 50-100% |
| 🟡 **Medio** | Naranja | `#f39c12` | 20-49% |
| 🔴 **Bajo** | Rojo | `#e74c3c` | 0-19% |

#### 🎯 Colores de Interfaz

| Elemento | Color | Código | Uso |
|----------|-------|--------|-----|
| **Fondo Principal** | Azul Oscuro | `#2c3e50` | Ventana principal |
| **Fondo Secundario** | Azul Gris | `#34495e` | Paneles |
| **Texto Principal** | Blanco | `#ecf0f1` | Títulos |
| **Texto Secundario** | Gris Claro | `#bdc3c7` | Descripciones |

---

## 🛠️ API y Funciones

### 🔋 Funciones de Batería

#### `get_battery_info()`
```python
def get_battery_info(self):
    """
    Obtiene información completa de la batería.
    
    Returns:
        dict: {
            'percent': int,      # Porcentaje de batería
            'power_plugged': bool, # Conectado a corriente
            'time_left': int     # Tiempo restante en segundos
        }
    """
```

#### `format_time(seconds)`
```python
def format_time(self, seconds):
    """
    Formatea tiempo en formato legible.
    
    Args:
        seconds (int): Segundos a formatear
        
    Returns:
        str: Tiempo formateado (ej: "2h 30m")
    """
```

### 💻 Funciones del Sistema

#### `update_system_info()`
```python
def update_system_info(self):
    """
    Actualiza información del sistema:
    - Uso de CPU
    - Uso de memoria
    - Uso de disco
    """
```

### 🛡️ Funciones de Conservación

#### `toggle_conservation_mode()`
```python
def toggle_conservation_mode(self):
    """
    Activa/desactiva el modo de conservación.
    Muestra notificaciones informativas.
    """
```

---

## 🔍 Monitoreo y Debugging

### 📊 Logs de la Aplicación

```python
# Habilitar logging detallado
import logging
logging.basicConfig(level=logging.DEBUG)

# Ejemplo de log
2024-01-15 10:30:15 INFO - BatteryZenith iniciado
2024-01-15 10:30:15 DEBUG - Batería detectada: 75%
2024-01-15 10:30:17 DEBUG - CPU: 45%, Memoria: 60%
```

### 🔧 Verificación de Dependencias

```bash
# Verificar instalación
.\verify_install.bat

# Verificar manualmente
python -c "import psutil; print('psutil OK')"
python -c "from PIL import Image; print('Pillow OK')"
python -c "import win32api; print('pywin32 OK')"
```

### 🐛 Debugging Común

#### Problema: No se muestra información de batería
```python
# Verificar si hay batería
import psutil
battery = psutil.sensors_battery()
if battery:
    print(f"Batería: {battery.percent}%")
else:
    print("No se detectó batería")
```

#### Problema: Error de importación
```bash
# Reinstalar dependencias
pip uninstall psutil Pillow pywin32
pip install psutil Pillow pywin32
```

---

## 🚀 Optimización

### ⚡ Optimizaciones de Rendimiento

#### 1. **Threading Eficiente**
```python
# Usar threading para no bloquear la GUI
monitor_thread = threading.Thread(target=monitor, daemon=True)
monitor_thread.start()
```

#### 2. **Actualización Inteligente**
```python
# Solo actualizar si hay cambios
if self.last_battery_percent != current_percent:
    self.update_display()
    self.last_battery_percent = current_percent
```

#### 3. **Gestión de Memoria**
```python
# Limpiar recursos no utilizados
def cleanup(self):
    self.monitoring = False
    # Limpiar referencias
```

### 📊 Métricas de Rendimiento

| Métrica | Valor Objetivo | Valor Actual |
|---------|----------------|--------------|
| **Uso de CPU** | <1% | ~0.5% |
| **Uso de Memoria** | <50MB | ~25MB |
| **Tiempo de Inicio** | <3s | ~2s |
| **Frecuencia de Actualización** | 2s | 2s |

### 🔧 Configuración de Optimización

```python
# Configuración para mejor rendimiento
OPTIMIZATION_CONFIG = {
    'update_interval': 2,      # Segundos entre actualizaciones
    'memory_limit': 50,        # MB límite de memoria
    'cpu_threshold': 1,        # % límite de CPU
    'cleanup_interval': 60     # Segundos entre limpiezas
}
```

---

## 📚 Recursos Adicionales

### 🔗 Enlaces Útiles

- [📖 Documentación de psutil](https://psutil.readthedocs.io/)
- [🎨 Guía de Tkinter](https://docs.python.org/3/library/tkinter.html)
- [🖼️ Documentación de Pillow](https://pillow.readthedocs.io/)
- [🪟 Documentación de pywin32](https://github.com/mhammond/pywin32)

### 📝 Notas de Desarrollo

- **Compatibilidad**: Windows 10+ con Python 3.7+
- **Dependencias**: Todas las dependencias están en `requirements.txt`
- **Testing**: Usar `demo.py` para pruebas básicas
- **Debugging**: Habilitar logging para diagnóstico

---

<div align="center">

### 🔧 **¿Necesitas Ayuda Técnica?**

[📧 Contacto Técnico](mailto:usuario432hz@gmail.com) • [🐛 Reportar Bug](https://github.com/ANONIMO432HZ/BatteryZenith/issues) • [📖 Wiki](https://github.com/ANONIMO432HZ/BatteryZenith/wiki)

**Documentación técnica actualizada para BatteryZenith v1.0**

</div> 