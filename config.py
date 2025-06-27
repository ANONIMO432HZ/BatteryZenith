# Configuración de BatteryZenith

# Colores de la aplicación
COLORS = {
    'primary': '#2c3e50',      # Azul oscuro principal
    'secondary': '#34495e',    # Azul grisáceo secundario
    'accent': '#3498db',       # Azul claro para botones
    'success': '#2ecc71',      # Verde para batería alta
    'warning': '#f39c12',      # Naranja para batería media
    'danger': '#e74c3c',       # Rojo para batería baja
    'text_primary': '#ecf0f1', # Blanco para texto principal
    'text_secondary': '#bdc3c7' # Gris claro para texto secundario
}

# Configuración de la ventana
WINDOW_CONFIG = {
    'width': 400,
    'height': 500,
    'title': 'BatteryZenith - Monitor de Batería',
    'resizable': False
}

# Configuración de monitoreo
MONITORING_CONFIG = {
    'update_interval': 2,  # Segundos entre actualizaciones
    'conservation_threshold': 80  # Porcentaje para modo conservación
}

# Configuración de fuentes
FONTS = {
    'title': ('Arial', 24, 'bold'),
    'subtitle': ('Arial', 14, 'bold'),
    'body': ('Arial', 12),
    'small': ('Arial', 10)
}

# Mensajes de la aplicación
MESSAGES = {
    'conservation_enabled': 'El modo de conservación está activado.\nLa carga se limitará al 80% para prolongar la vida de la batería.',
    'conservation_disabled': 'El modo de conservación está desactivado.\nLa batería puede cargarse al 100%.',
    'no_battery': 'Batería no disponible',
    'calculating': 'Calculando...',
    'time_remaining': 'Tiempo restante: {}',
    'time_charging': 'Tiempo para carga completa: {}',
    'connected_charging': '🔌 Conectado y cargando',
    'connected_conservation': '🔌 Conectado - Modo conservación activo',
    'battery_power': '🔋 Funcionando con batería'
} 