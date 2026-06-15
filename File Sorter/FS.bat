@echo off
setlocal enabledelayedexpansion
color a
set "potbf=%~dp0"
set "napotbf=%~dp0File Sorter.bat"
cd "C:\Program Files\File Sorter\Backend\"
REM nap stands for name and path
REM potbf stands for path of the batch file
REM napotbf stands for name and path of the batch file
mkdir %USERPROFILE%\OneDrive\Desktop\sort >nul
echo Lege die zu sortierenden Dateien in den sort-Ordner auf deinem Desktop und druecke eine Taste
pause > nul
mkdir %USERPROFILE%\OneDrive\Desktop\sorted >nul

for %%f in (%USERPROFILE%\OneDrive\Desktop\sort\*) do (
    set "nap=%%f"
   

    echo !nap! >file.name
    python "C:\Program Files\File Sorter\Backend\Backend File Sorter.py"
    if exist file.extension (


        set /P FILEFORMAT=<file.extension


        if exist !potbf!!FILEFORMAT! (

            C:\Windows\System32\xcopy.exe "!nap!" "%USERPROFILE%\OneDrive\Desktop\sorted\!FILEFORMAT!" /Y /I
            del file.name
            del file.extension


        ) else (
            mkdir "%USERPROFILE%\OneDrive\Desktop\sorted\!FILEFORMAT!"
            C:\Windows\System32\xcopy.exe "!nap!" "%USERPROFILE%\OneDrive\Desktop\sorted\!FILEFORMAT!" /Y /I
            del file.name
            del file.extension
        )

    ) else (

        echo Error
        goto end        

    )


)
:end
del "%USERPROFILE%\OneDrive\Desktop\sort" /q /f
pause