@echo off
setlocal enableextensions enabledelayedexpansion

rem Directory of this batch file
pushd "%~dp0" >nul 2>&1

set "PYEXE=python"
set "SCRIPT=make_papercut_panel.py"

rem Default parameter set aligned with DoD tuning
set "FORMAT=pptx"
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

set "counter=0"
for %%F in (*.png *.jpg *.jpeg *.bmp *.tif *.tiff) do (
    set /a counter+=1
    set "FILE_NAME[!counter!]=%%~nxF"
    set "FILE_INPUT[!counter!]=%%~fF"
    set "FILE_OUTBASE[!counter!]=%%~dpnF"
)

if !counter!==0 (
    echo [ERR] No image files found in %cd%.
    echo Supported extensions: PNG, JPG, JPEG, BMP, TIF, TIFF.
    popd >nul 2>&1
    exit /b 2
)

echo Files:
for /L %%I in (1,1,!counter!) do (
    echo   [%%I] !FILE_NAME[%%I]!
)

echo.
:ASK_FILE
set "CHOICE="
set /p CHOICE=Select file number:
if not defined CHOICE goto ASK_FILE
for /f "delims=0123456789" %%Z in ("!CHOICE!") do goto ASK_FILE
set /a CHOICE=!CHOICE! + 0 >nul 2>&1
if !CHOICE! lss 1 goto ASK_FILE
if !CHOICE! gtr !counter! goto ASK_FILE
for %%I in (!CHOICE!) do (
    call set "INPUT_NAME=%%FILE_NAME[%%I]%%"
    call set "INPUT_FULL=%%FILE_INPUT[%%I]%%"
    call set "OUTBASE_FULL=%%FILE_OUTBASE[%%I]%%"
)

if not defined INPUT_NAME goto ASK_FILE
if not defined INPUT_FULL goto ASK_FILE
if not defined OUTBASE_FULL goto ASK_FILE

echo.
set "SHIFT_X_MM=0"
set /p SHIFT_X_MM=Shift X (mm) [0]: 
if "%SHIFT_X_MM%"=="" set "SHIFT_X_MM=0"
for /f "tokens=*" %%A in ("!SHIFT_X_MM!") do set "SHIFT_X_MM=%%A"

set "SHIFT_Y_MM=0"
set /p SHIFT_Y_MM=Shift Y (mm) [0]: 
if "%SHIFT_Y_MM%"=="" set "SHIFT_Y_MM=0"
for /f "tokens=*" %%A in ("!SHIFT_Y_MM!") do set "SHIFT_Y_MM=%%A"

>>"%LOGFILE%" echo [CFG] INPUT="!INPUT_FULL!" OUTBASE="!OUTBASE_FULL!" SHIFT=!SHIFT_X_MM!x!SHIFT_Y_MM!mm
>>"%LOGFILE%" echo [CFG] THRESH=%THRESHOLD% DETAIL_DELTA=%DETAIL_DELTA% BLUR=%BLUR% DILATE=%DILATE_PX% DETAIL_JOIN=%DETAIL_JOIN_PX% ANTIALIAS=%ANTIALIAS_RADIUS%
>>"%LOGFILE%" echo [CFG] NORMALIZE_DPI=%NORMALIZE_DPI% SCALE=%NORMALIZE_SCALE% BLUR=%NORMALIZE_BLUR% PRESET=%NORMALIZE_PRESET% INVERT=%INVERT_MODE% FORMAT=%FORMAT%
echo [CFG] INPUT="!INPUT_FULL!" OUTBASE="!OUTBASE_FULL!" SHIFT=!SHIFT_X_MM!x!SHIFT_Y_MM!mm
echo [CFG] DETAIL: threshold=%THRESHOLD% delta=%DETAIL_DELTA% blur=%BLUR% dilate=%DILATE_PX% join=%DETAIL_JOIN_PX% antialias=%ANTIALIAS_RADIUS%
echo [CFG] NORMALIZE: dpi=%NORMALIZE_DPI% scale=%NORMALIZE_SCALE% blur=%NORMALIZE_BLUR% preset=%NORMALIZE_PRESET% invert=%INVERT_MODE% format=%FORMAT%

for /f "delims=" %%V in ('"%PYEXE%" -V 2^>^&1') do (
    echo %%V
    >>"%LOGFILE%" echo %%V
)

set CMDLINE=%PYEXE% -X utf8 "%SCRIPT%" "!INPUT_FULL!" --output "!OUTBASE_FULL!" --format %FORMAT% --threshold %THRESHOLD% --detail-delta %DETAIL_DELTA% --blur %BLUR% --dilate-px %DILATE_PX% --detail-join-px %DETAIL_JOIN_PX% --antialias-radius %ANTIALIAS_RADIUS% --normalize-dpi %NORMALIZE_DPI% --normalize-scale %NORMALIZE_SCALE% --normalize-blur %NORMALIZE_BLUR% --normalize-preset %NORMALIZE_PRESET% --invert-mode %INVERT_MODE% --shift-x-mm !SHIFT_X_MM! --shift-y-mm !SHIFT_Y_MM!
echo [RUN] %CMDLINE%
>>"%LOGFILE%" echo [RUN] %CMDLINE%

powershell -NoProfile -Command "& { & '%PYEXE%' -X utf8 '%SCRIPT%' '%INPUT_FULL%' --output '%OUTBASE_FULL%' --format '%FORMAT%' --threshold '%THRESHOLD%' --detail-delta '%DETAIL_DELTA%' --blur '%BLUR%' --dilate-px '%DILATE_PX%' --detail-join-px '%DETAIL_JOIN_PX%' --antialias-radius '%ANTIALIAS_RADIUS%' --normalize-dpi '%NORMALIZE_DPI%' --normalize-scale '%NORMALIZE_SCALE%' --normalize-blur '%NORMALIZE_BLUR%' --normalize-preset '%NORMALIZE_PRESET%' --invert-mode '%INVERT_MODE%' --shift-x-mm '%SHIFT_X_MM%' --shift-y-mm '%SHIFT_Y_MM%' 2>&1 | Tee-Object -FilePath '%LOGFILE%' -Append; exit $LASTEXITCODE }"
set "RC=%ERRORLEVEL%"

>>"%LOGFILE%" echo [LOG] Exit code: %RC%

echo.
echo ===== LOG: "%LOGFILE%" =====
type "%LOGFILE%"

echo.
if not "%RC%"=="0" (
    echo [ERR] FAILED. See log above.
    popd >nul 2>&1
    pause
    exit /b %RC%
)

echo OK. Outputs saved using base "!OUTBASE_FULL!".
popd >nul 2>&1
pause
exit /b 0
