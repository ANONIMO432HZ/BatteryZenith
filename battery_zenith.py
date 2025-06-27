"""Aplicación BatteryZenith: Monitoriza y optimiza la batería de portátiles Windows con interfaz gráfica."""
import threading
import time
import os
import sys
import logging

import tkinter as tk
from tkinter import ttk, messagebox

import psutil
try:
    import win32api
    import win32con
    import win32gui
except ImportError:
    win32api = None
    win32con = None
    win32gui = None
from PIL import Image, ImageTk

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s - %(message)s')

class BatteryZenith:
    def __init__(self, root):
        self.root = root
        self.root.title("BatteryZenith - Monitor de Batería")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        # Variables
        self.conservation_mode = tk.BooleanVar(value=False)
        self.monitoring = True
        self._warned_conservation = False
        
        # Configurar icono de la aplicación
        self.setup_icon()
        
        # Crear interfaz
        self.create_widgets()
        
        # Iniciar monitoreo
        self.start_monitoring()
        
        # Configurar cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_icon(self):
        """Configurar icono de la aplicación"""
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
            # Crear un icono simple si no existe
            if not os.path.exists(icon_path):
                self.create_simple_icon(icon_path)
            if win32api is not None:
                self.root.iconbitmap(icon_path)
        except Exception as e:
            logging.warning(f"No se pudo configurar el icono: {e}")
    
    def create_simple_icon(self, icon_path=None):
        """Crear un icono simple para la aplicación"""
        try:
            if icon_path is None:
                icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
            # Crear una imagen simple de 32x32 píxeles
            img = Image.new('RGBA', (32, 32), (52, 73, 94, 255))
            img.save(icon_path, format='ICO')
        except Exception as e:
            logging.error(f"No se pudo crear el icono: {e}")
    
    def create_widgets(self):
        """Crear todos los widgets de la interfaz"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#2c3e50', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = tk.Label(
            main_frame, 
            text="BatteryZenith", 
            font=("Arial", 24, "bold"), 
            fg='#ecf0f1', 
            bg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))
        
        # Frame para información de batería
        battery_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        battery_frame.pack(fill=tk.X, pady=10)
        
        # Título del frame de batería
        battery_title = tk.Label(
            battery_frame, 
            text="Estado de la Batería", 
            font=("Arial", 14, "bold"), 
            fg='#ecf0f1', 
            bg='#34495e'
        )
        battery_title.pack(pady=10)
        
        # Nivel de batería
        self.battery_level_label = tk.Label(
            battery_frame, 
            text="Cargando...", 
            font=("Arial", 18, "bold"), 
            fg='#2ecc71', 
            bg='#34495e'
        )
        self.battery_level_label.pack()
        
        # Barra de progreso
        self.battery_progress = ttk.Progressbar(
            battery_frame, 
            length=300, 
            mode='determinate',
            style='Custom.Horizontal.TProgressbar'
        )
        self.battery_progress.pack(pady=10)
        
        # Estado de carga
        self.charging_status_label = tk.Label(
            battery_frame, 
            text="", 
            font=("Arial", 12), 
            fg='#ecf0f1', 
            bg='#34495e'
        )
        self.charging_status_label.pack(pady=5)
        
        # Tiempo restante
        self.time_remaining_label = tk.Label(
            battery_frame, 
            text="", 
            font=("Arial", 10), 
            fg='#bdc3c7', 
            bg='#34495e'
        )
        self.time_remaining_label.pack(pady=5)
        
        # Frame para modo de conservación
        conservation_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        conservation_frame.pack(fill=tk.X, pady=10)
        
        # Título del frame de conservación
        conservation_title = tk.Label(
            conservation_frame, 
            text="Modo de Conservación", 
            font=("Arial", 14, "bold"), 
            fg='#ecf0f1', 
            bg='#34495e'
        )
        conservation_title.pack(pady=10)
        
        # Checkbox para modo de conservación
        self.conservation_checkbox = tk.Checkbutton(
            conservation_frame,
            text="Limitar carga al 80%",
            variable=self.conservation_mode,
            font=("Arial", 12),
            fg='#ecf0f1',
            bg='#34495e',
            selectcolor='#2c3e50',
            activebackground='#34495e',
            activeforeground='#ecf0f1',
            command=self.toggle_conservation_mode
        )
        self.conservation_checkbox.pack(pady=5)
        
        # Descripción del modo de conservación
        conservation_desc = tk.Label(
            conservation_frame,
            text="Reduce el desgaste de la batería\nextendiendo su vida útil",
            font=("Arial", 10),
            fg='#bdc3c7',
            bg='#34495e',
            justify=tk.CENTER
        )
        conservation_desc.pack(pady=5)
        
        # Frame para información adicional
        info_frame = tk.Frame(main_frame, bg='#34495e', relief=tk.RAISED, bd=2)
        info_frame.pack(fill=tk.X, pady=10)
        
        # Título del frame de información
        info_title = tk.Label(
            info_frame, 
            text="Información del Sistema", 
            font=("Arial", 14, "bold"), 
            fg='#ecf0f1', 
            bg='#34495e'
        )
        info_title.pack(pady=10)
        
        # Información del sistema
        self.system_info_label = tk.Label(
            info_frame,
            text="",
            font=("Arial", 10),
            fg='#bdc3c7',
            bg='#34495e',
            justify=tk.LEFT
        )
        self.system_info_label.pack(pady=5)
        
        # Botón de actualizar
        refresh_button = tk.Button(
            main_frame,
            text="Actualizar",
            command=self.refresh_battery_info,
            font=("Arial", 12, "bold"),
            bg='#3498db',
            fg='white',
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        refresh_button.pack(pady=20)
        
        # Configurar estilos
        self.setup_styles()
    
    def setup_styles(self):
        """Configurar estilos personalizados"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilo para la barra de progreso
        style.configure(
            'Custom.Horizontal.TProgressbar',
            background='#2ecc71',
            troughcolor='#34495e',
            borderwidth=0,
            lightcolor='#2ecc71',
            darkcolor='#2ecc71'
        )
    
    def get_battery_info(self):
        """Obtener información de la batería"""
        try:
            battery = psutil.sensors_battery()
            if battery:
                return {
                    'percent': battery.percent,
                    'power_plugged': battery.power_plugged,
                    'time_left': battery.secsleft if battery.secsleft != -1 else None
                }
            else:
                return None
        except Exception as e:
            logging.error(f"Error al obtener información de batería: {e}")
            return None
    
    def format_time(self, seconds):
        """Formatear tiempo en horas y minutos"""
        if seconds is None or seconds == -1:
            return "Calculando..."
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        if hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return f"{minutes}m"
    
    def update_battery_display(self):
        """Actualizar la visualización de la batería"""
        battery_info = self.get_battery_info()
        try:
            if battery_info:
                percent = battery_info['percent']
                power_plugged = battery_info['power_plugged']
                time_left = battery_info['time_left']
                # Actualizar nivel de batería
                self.battery_level_label.config(text=f"{percent}%")
                # Actualizar barra de progreso
                self.battery_progress['value'] = percent
                # Cambiar color según el nivel
                if percent > 50:
                    color = '#2ecc71'  # Verde
                elif percent > 20:
                    color = '#f39c12'  # Naranja
                else:
                    color = '#e74c3c'  # Rojo
                self.battery_level_label.config(fg=color)
                # Detectar transición de desconectado a conectado
                if not hasattr(self, '_last_power_plugged'):
                    self._last_power_plugged = False
                # Mostrar advertencia solo si se acaba de conectar el cargador, el modo conservación está activo y el porcentaje >= 80%
                if power_plugged and not self._last_power_plugged:
                    if self.conservation_mode.get() and percent >= 80 and not self._warned_conservation:
                        messagebox.showwarning(
                            "Desconecta el cargador",
                            "La batería ha superado el 80% y el modo de conservación está activo.\nPor favor, desconecta el cargador manualmente para prolongar la vida útil de la batería."
                        )
                        self._warned_conservation = True
                # Actualizar estado de carga
                if power_plugged:
                    if self.conservation_mode.get() and percent >= 80:
                        self.charging_status_label.config(text="🔌 Conectado - Modo conservación activo")
                    else:
                        self.charging_status_label.config(text="🔌 Conectado y cargando")
                else:
                    self.charging_status_label.config(text="🔋 Funcionando con batería")
                    self._warned_conservation = False
                # Guardar el estado anterior de power_plugged
                self._last_power_plugged = power_plugged
                # Actualizar tiempo restante
                if power_plugged:
                    if time_left:
                        self.time_remaining_label.config(text=f"Tiempo para carga completa: {self.format_time(time_left)}")
                    else:
                        self.time_remaining_label.config(text="Calculando tiempo de carga...")
                else:
                    if time_left:
                        self.time_remaining_label.config(text=f"Tiempo restante: {self.format_time(time_left)}")
                    else:
                        self.time_remaining_label.config(text="Calculando tiempo restante...")
            else:
                self.battery_level_label.config(text="Batería no disponible")
                self.charging_status_label.config(text="")
                self.time_remaining_label.config(text="")
        except Exception as e:
            logging.error(f"Error al actualizar la visualización de la batería: {e}")
    
    def update_system_info(self):
        """Actualizar información del sistema"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            system_info = f"CPU: {cpu_percent}%\n"
            system_info += f"Memoria: {memory.percent}%\n"
            system_info += f"Disco: {disk.percent}%"
            self.system_info_label.config(text=system_info)
        except Exception as e:
            logging.error(f"Error al actualizar información del sistema: {e}")
            self.system_info_label.config(text="Información no disponible")
    
    def toggle_conservation_mode(self):
        """Activar/desactivar modo de conservación"""
        if self.conservation_mode.get():
            messagebox.showinfo(
                "Modo de Conservación",
                "El modo de conservación está activado.\nLa carga se limitará al 80% para prolongar la vida de la batería."
            )
        else:
            messagebox.showinfo(
                "Modo de Conservación",
                "El modo de conservación está desactivado.\nLa batería puede cargarse al 100%."
            )
    
    def refresh_battery_info(self):
        """Actualizar información de batería manualmente"""
        self.update_battery_display()
        self.update_system_info()
    
    def start_monitoring(self):
        """Iniciar monitoreo en tiempo real"""
        def monitor():
            while self.monitoring:
                try:
                    self.root.after(0, self.update_battery_display)
                    self.root.after(0, self.update_system_info)
                    time.sleep(2)  # Actualizar cada 2 segundos
                except Exception as e:
                    logging.error(f"Error en el hilo de monitoreo: {e}")
                    break
        monitor_thread = threading.Thread(target=monitor, daemon=True)
        monitor_thread.start()
    
    def on_closing(self):
        """Manejar el cierre de la aplicación"""
        self.monitoring = False
        self.root.destroy()

def main():
    """Función principal"""
    root = tk.Tk()
    app = BatteryZenith(root)
    root.mainloop()

if __name__ == "__main__":
    main() 