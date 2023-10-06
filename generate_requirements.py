import subprocess
import os

python_executable = os.path.join("venv", "bin", "python")

if os.name == "nt":
    python_executable = os.path.join("venv", "Scripts", "python")

# Construa o comando
command = [python_executable, "-m", "pip", "freeze"]

# Execute o comando e capture a saída
result = subprocess.run(command, capture_output=True, text=True)

# Escreva a saída para requirements.txt
with open("requirements.txt", "w") as f:
    f.write(result.stdout)
