import os
import subprocess
import sys
from tqdm import tqdm
import time

print("\n==============================")
print(" INICIANDO PROCESSO COMPLETO ")
print("==============================\n")

def run_script(script_name, titulo):
    print(f"📌 {titulo}...\n")

    python_exec = sys.executable  # Python interno do EXE

    try:
        process = subprocess.Popen(
            [python_exec, script_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        with tqdm(desc=f"Executando {script_name}", bar_format="{l_bar}{bar}") as pbar:
            while True:
                line = process.stdout.readline()
                if line:
                    print(line.strip())
                if process.poll() is not None:
                    break

                pbar.update(1)
                time.sleep(0.05)

        stderr = process.stderr.read()
        if stderr.strip():
            print("❌ ERRO ENCONTRADO:")
            print(stderr)
            return False

        print(f"\n✅ Finalizado: {titulo}\n")
        return True

    except Exception as e:
        print(f"❌ Falha ao executar {script_name}: {e}")
        return False

# ===============================
# EXECUÇÃO SEQUENCIAL
# ===============================

if not run_script("relatorio.py", "Gerando planilha (relatorio.py)"):
    sys.exit(1)

if not run_script("nota.py", "Gerando nota (nota.py)"):
    sys.exit(1)

print("\n🎉 PROCESSO COMPLETO FINALIZADO COM SUCESSO!\n")
