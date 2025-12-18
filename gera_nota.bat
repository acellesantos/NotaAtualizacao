@echo off
REM ===== Roda o script Python =====
"C:\Users\Camim\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\Camim\OneDrive\NotaAtualizacao\nota.py"

REM ===== Pausa para mostrar mensagens no CMD =====
pause

REM ===== Abre automaticamente o HTML mais recente =====
for /f "delims=" %%f in ('dir /b /o-d "C:\Users\Camim\OneDrive\NotaAtualizacao\nota_atualizacao_*.html"') do (
    start "" "C:\Users\Camim\OneDrive\NotaAtualizacao\%%f"
    goto :break
)
:break