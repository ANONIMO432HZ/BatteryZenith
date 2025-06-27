@echo off
REM Script para subir el proyecto a GitHub automáticamente

REM Cambia esta URL por la de tu repositorio en GitHub
set REPO_URL=https://github.com/ANONIMO432HZ/BatteryZenith.git

REM Inicializa git si no existe
if not exist ".git" (
    git init
)

REM Añade todos los archivos
git add .

REM Haz el primer commit
git commit -m "Primer commit: proyecto BatteryZenith"

REM Cambia el nombre de la rama a main
git branch -M main

REM Agrega el repositorio remoto (solo si no existe)
git remote | findstr origin >nul
if %errorlevel% neq 0 (
    git remote add origin %REPO_URL%
)

REM Sube el proyecto a GitHub
git push -u origin main

pause