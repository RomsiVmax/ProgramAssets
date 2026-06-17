@echo off
:start
echo Welcome to the Options O' Mat!
:firstquestion
echo Copy your options.txt to this modpack:
set /P modpack=""

if exist "%USERPROFILE%\curseforge\minecraft\Instances\%modpack%\minecraftinstance.json" (
    goto secondquestion
) else (
    echo This modpack does'nt seem to exist. Note: Modpacks that have been RENAMED via CurseForge are not supported!
    goto firstquestion
)

:secondquestion
echo From which modpack shall we get your options.txt?
set /P copyfrom=""

if exist "%USERPROFILE%\curseforge\minecraft\Instances\%copyfrom%\options.txt" (
    goto thirdquestion
) else (
    echo This modpack does'nt seem to exist. Note: Modpacks that have been RENAMED via CurseForge are not supported!
    goto secondquestion
)



:thirdquestion

echo Are you sure that you want to copy your options.txt (y/n)?
set /P allow=""
goto check

:check
if %allow% == y (
    goto copy
)

if %allow% == n (
    echo Bro why have you opened this program
    goto end
) else (
    echo You need to enter y or n!
    goto thirdquestion
)

:copy
xcopy "%USERPROFILE%\curseforge\minecraft\Instances\%copyfrom%\options.txt" "%USERPROFILE%\curseforge\minecraft\Instances\%modpack%\" /s /e /y >nul
echo Done!
goto end

:end
pause
