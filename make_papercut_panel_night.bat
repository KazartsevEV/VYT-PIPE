@echo off
setlocal enableextensions enabledelayedexpansion

rem Batch runner for overnight papercut generation across a directory tree.
rem Asks for a root folder, processes all supported images recursively,
rem and stores results in numbered subfolders containing PPTX, PDF, PNG,
rem and a copy of the source image.

pushd "%~dp0" >nul 2>&1

set "PYEXE=python"
set "SCRIPT=make_papercut_panel.py"

rem Default parameter pack for automated batches
set "FORMAT=both"
set "THRESHOLD=200"
set "DETAIL_DELTA=60"
set "BLUR=0.6"
set "DILATE_PX=1"
set "DETAIL_JOIN_PX=2"
set "ANTIALIAS_RADIUS=0.8"
set "NORMALIZE_DPI=300"
set "NORMALIZE_SCALE=2.0"
set "NORMALIZE_BLUR=0.8"
set "NORMALIZE_PRESET=default"
set "INVERT_MODE=auto"

if not exist "%SCRIPT%" (
    echo [ERR] %SCRIPT% not found next to this batch file.
    popd >nul 2>&1
    exit /b 1
)

set "LOGFILE=%~n0.log"
>"%LOGFILE%" echo [LOG] Working dir: %cd%

set "ROOT_PATH="
set /p ROOT_PATH=Enter absolute path to scan for images (leave blank for current dir):
if "%ROOT_PATH%"=="" set "ROOT_PATH=%cd%"

for %%R in ("%ROOT_PATH%") do set "ROOT_PATH=%%~fR"
if not exist "%ROOT_PATH%" (
    echo [ERR] Directory not found: %ROOT_PATH%
    >>"%LOGFILE%" echo [ERR] Directory not found: %ROOT_PATH%
    popd >nul 2>&1
    exit /b 2
)

echo [INFO] Scanning root: %ROOT_PATH%
>>"%LOGFILE%" echo [INFO] Scanning root: %ROOT_PATH%
>>"%LOGFILE%" echo [INFO] DETAIL: THRESH=%THRESHOLD% DELTA=%DETAIL_DELTA% BLUR=%BLUR% DILATE=%DILATE_PX% JOIN=%DETAIL_JOIN_PX% ANTIALIAS=%ANTIALIAS_RADIUS%
>>"%LOGFILE%" echo [INFO] NORMALIZE: DPI=%NORMALIZE_DPI% SCALE=%NORMALIZE_SCALE% BLUR=%NORMALIZE_BLUR% PRESET=%NORMALIZE_PRESET% INVERT=%INVERT_MODE% FORMAT=%FORMAT%

for /f "usebackq delims=" %%T in (`powershell -NoProfile -Command "Get-Date -Format yyyyMMdd_HHmmss"`) do set "STAMP=%%T"
set "OUT_ROOT=%ROOT_PATH%\papercut_batch_%STAMP%"
if exist "%OUT_ROOT%" (
    echo [WARN] Output root already exists: %OUT_ROOT%
) else (
    mkdir "%OUT_ROOT%" >nul 2>&1
)
>>"%LOGFILE%" echo [INFO] Output root: %OUT_ROOT%

echo [INFO] Output root: %OUT_ROOT%

for /f "delims=" %%V in ('"%PYEXE%" -V 2^>^&1') do set "PY_VERSION=%%V"
if defined PY_VERSION (
    echo [INFO] %PY_VERSION%
    >>"%LOGFILE%" echo [INFO] %PY_VERSION%
)

set "COUNT=0"
set "FAILURES=0"

for /r "%ROOT_PATH%" %%F in (*.png *.jpg *.jpeg *.bmp *.tif *.tiff) do (
    set "CURRENT=%%~fF"
    set "FNAME=%%~nxF"
    set "PROCESS=1"
    if /i not "!CURRENT:%OUT_ROOT%=!"=="!CURRENT!" set "PROCESS=0"
    if /i "!FNAME:~-12!"=="_original.png" set "PROCESS=0"
    if /i "!FNAME:~-10!"=="_panel.png" set "PROCESS=0"
    if /i "!FNAME:~-11!"=="_3x4_A4.pdf" set "PROCESS=0"
    if /i "!FNAME:~-12!"=="_3x4_A4.pptx" set "PROCESS=0"
    if !PROCESS! EQU 0 (
        rem Skip generated outputs
    ) else (
        set /a COUNT+=1
        set "PAD=0000!COUNT!"
        set "ID=!PAD:~-4!"
        call :PROCESS "%%~fF" "!ID!"
    )
)

if %COUNT%==0 (
    echo [ERR] No image files found under %ROOT_PATH%.
    >>"%LOGFILE%" echo [ERR] No image files found under %ROOT_PATH%.
    popd >nul 2>&1
    exit /b 3
)

if %FAILURES% gtr 0 (
    echo [WARN] Completed with %FAILURES% failure(s). See %LOGFILE% for details.
    >>"%LOGFILE%" echo [WARN] Completed with %FAILURES% failure(s).
    popd >nul 2>&1
    exit /b 4
)

echo [INFO] Completed successfully. Processed %COUNT% file(s).
>>"%LOGFILE%" echo [INFO] Completed successfully. Processed %COUNT% file(s).

popd >nul 2>&1
exit /b 0

:PROCESS
setlocal enableextensions enabledelayedexpansion
set "SRC=%~1"
set "ID=%~2"
set "DEST=%OUT_ROOT%\%ID%"
if not exist "%DEST%" mkdir "%DEST%" >nul 2>&1

set "NAME=%~n1"
set "OUTBASE=%DEST%\%NAME%"

>>"%LOGFILE%" echo [TASK %ID%] Source: %SRC%
echo [TASK %ID%] Source: %SRC%

if defined PY_VERSION >>"%LOGFILE%" echo [TASK %ID%] %PY_VERSION%

set CMDLINE=%PYEXE% -X utf8 "%SCRIPT%" "%SRC%" --output "%OUTBASE%" --format %FORMAT% --threshold %THRESHOLD% --detail-delta %DETAIL_DELTA% --blur %BLUR% --dilate-px %DILATE_PX% --detail-join-px %DETAIL_JOIN_PX% --antialias-radius %ANTIALIAS_RADIUS% --normalize-dpi %NORMALIZE_DPI% --normalize-scale %NORMALIZE_SCALE% --normalize-blur %NORMALIZE_BLUR% --normalize-preset %NORMALIZE_PRESET% --invert-mode %INVERT_MODE% --shift-x-mm 0 --shift-y-mm 0 --debug-panel
>>"%LOGFILE%" echo [TASK %ID%] [RUN] %CMDLINE%
echo [TASK %ID%] [RUN] %CMDLINE%

powershell -NoProfile -Command "& { & '%PYEXE%' -X utf8 '%SCRIPT%' '%SRC%' --output '%OUTBASE%' --format '%FORMAT%' --threshold '%THRESHOLD%' --detail-delta '%DETAIL_DELTA%' --blur '%BLUR%' --dilate-px '%DILATE_PX%' --detail-join-px '%DETAIL_JOIN_PX%' --antialias-radius '%ANTIALIAS_RADIUS%' --normalize-dpi '%NORMALIZE_DPI%' --normalize-scale '%NORMALIZE_SCALE%' --normalize-blur '%NORMALIZE_BLUR%' --normalize-preset '%NORMALIZE_PRESET%' --invert-mode '%INVERT_MODE%' --shift-x-mm '0' --shift-y-mm '0' --debug-panel 2>&1 | Tee-Object -FilePath '%LOGFILE%' -Append; exit $LASTEXITCODE }"
set "RC=%ERRORLEVEL%"
>>"%LOGFILE%" echo [TASK %ID%] [LOG] Exit code: %RC%

if not "%RC%"=="0" (
    echo [TASK %ID%] [ERR] Failed with code %RC%.
    endlocal & set /a FAILURES+=1 & goto :EOF
)

set "SRC_DIR=%~dp1"
set "ORIGPNG=%SRC_DIR%%NAME%_original.png"
if exist "%ORIGPNG%" (
    copy /Y "%ORIGPNG%" "%DEST%" >nul 2>&1
    >>"%LOGFILE%" echo [TASK %ID%] Copied original PNG: %ORIGPNG%
) else (
    >>"%LOGFILE%" echo [TASK %ID%] [WARN] Original PNG not found: %ORIGPNG%
)

copy /Y "%SRC%" "%DEST%" >nul 2>&1
>>"%LOGFILE%" echo [TASK %ID%] Copied source image to %DEST%

echo [TASK %ID%] Completed.
endlocal & goto :EOF
