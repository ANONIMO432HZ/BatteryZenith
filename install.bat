@echo off
echo ========================================
echo    BatteryZenith - Instalador Mejorado
echo ========================================
echo.

echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo Por favor instala Python desde https://python.org
    pause
    exit /b 1
)

echo Python encontrado. Mostrando version...
python --version

echo.
echo Actualizando pip...
python -m pip install --upgrade pip

echo.
echo ========================================
echo    Instalando dependencias...
echo ========================================

echo.
echo Instalando psutil 5.9.6...
pip install psutil==5.9.6
if errorlevel 1 (
    echo ERROR: Error al instalar psutil
    echo Intentando instalar version mas reciente...
    pip install psutil
    if errorlevel 1 (
        echo ERROR: No se pudo instalar psutil
        pause
        exit /b 1
    )
)

echo.
echo Instalando Pillow...
pip install Pillow
if errorlevel 1 (
    echo ERROR: Error al instalar Pillow
    echo Intentando instalar version especifica...
    pip install Pillow==10.1.0
    if errorlevel 1 (
        echo ERROR: No se pudo instalar Pillow
        pause
        exit /b 1
    )
)

echo.
echo Instalando pywin32...
pip install pywin32
if errorlevel 1 (
    echo ERROR: Error al instalar pywin32
    echo Intentando instalar version especifica...
    pip install pywin32==306
    if errorlevel 1 (
        echo ERROR: No se pudo instalar pywin32
        pause
        exit /b 1
    )
)

echo.
echo Verificando instalaciones...
echo.
echo Verificando psutil:
pip show psutil
echo.
echo Verificando Pillow:
pip show Pillow
echo.
echo Verificando pywin32:
pip show pywin32

echo.
echo ========================================
echo    Instalacion completada exitosamente!
echo ========================================
echo.
echo Dependencias instaladas:
echo - psutil: Para monitoreo del sistema y bateria
echo - Pillow: Para manejo de imagenes
echo - pywin32: Para funcionalidades de Windows
echo.
echo Para ejecutar BatteryZenith, usa:
echo python battery_zenith.py
echo.
echo Para ver la demostracion, usa:
echo python demo.py
echo.
echo Para ejecutar rapidamente, usa:
echo run.bat
echo.
pause 