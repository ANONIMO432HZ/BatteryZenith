@echo off
echo ========================================
echo    BatteryZenith - Verificador
echo ========================================
echo.

echo Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no encontrado
    pause
    exit /b 1
)

echo.
echo Verificando dependencias instaladas...
echo.

echo 1. Verificando psutil:
python -c "import psutil; print('psutil OK - Version:', psutil.__version__)"
if errorlevel 1 (
    echo ERROR: psutil no esta instalado correctamente
    echo Ejecuta: pip install psutil
) else (
    echo ✓ psutil instalado correctamente
)

echo.
echo 2. Verificando Pillow:
python -c "from PIL import Image; print('Pillow OK - Version:', Image.__version__)"
if errorlevel 1 (
    echo ERROR: Pillow no esta instalado correctamente
    echo Ejecuta: pip install Pillow
) else (
    echo ✓ Pillow instalado correctamente
)

echo.
echo 3. Verificando pywin32:
python -c "import win32api; print('pywin32 OK')"
if errorlevel 1 (
    echo ERROR: pywin32 no esta instalado correctamente
    echo Ejecuta: pip install pywin32
) else (
    echo ✓ pywin32 instalado correctamente
)

echo.
echo 4. Verificando tkinter:
python -c "import tkinter; print('tkinter OK')"
if errorlevel 1 (
    echo ERROR: tkinter no esta disponible
    echo tkinter viene incluido con Python
) else (
    echo ✓ tkinter disponible
)

echo.
echo ========================================
echo    Verificacion completada
echo ========================================
echo.
echo Si todos los componentes muestran ✓, la aplicacion deberia funcionar.
echo.
echo Para ejecutar BatteryZenith:
echo python battery_zenith.py
echo.
pause 