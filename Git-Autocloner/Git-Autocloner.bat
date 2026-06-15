@echo off
color a
cd %USERPROFILE%\OneDrive\Desktop
echo Enter the repository link:
set /P link=""
git clone %link%
cls
echo Cloned Repository, please make your changes, then press Enter.
pause >nul
cd C:\Program Files\Git-Autocloner\Backend
echo %link% >repository.iurl
python "C:\Program Files\Git-Autocloner\Backend\Backend Git-Autocloner.py"
set /P repositoryname=<repository.name
del "repository.name" /q /f
del "repository.iurl" /q /f
cd %USERPROFILE%\OneDrive\Desktop
cd %repositoryname% >nul
git init
cls
git add --all
cls
echo Enter the changes:
set /P commit=""
git commit -m "%commit%"
cls
echo Press Enter to push the changes to the server
pause >nul
git push
cls
echo Changes got pushed, press any key to end the process
pause >nul