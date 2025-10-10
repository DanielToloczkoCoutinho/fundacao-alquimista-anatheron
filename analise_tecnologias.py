import json
import os
from pathlib import Path

# Tecnologias para buscar
tecnologias = [
    "Apollo", "GraphQL", "Docker", "Firebase", "Next.js", "React", 
    "Three.js", "TypeScript", "Python", "Qiskit", "Blockchain",
    "TensorFlow", "WebGL", "Unity", "WebXR", "WebGPU", "MongoDB",
    "PostgreSQL", "Tailwind", "WebAuthn", "WebBluetooth", "EEG",
    "Quantum", "IBM", "Node.js", "Express", "Vercel", "GitHub"
]

resultados = {}
for tech in tecnologias:
    comando = f"find /home/user -type f \\( -name '*.py' -o -name '*.js' -o -name '*.ts' -o -name '*.json' -o -name '*.md' \\) -exec grep -l -i '{tech}' {{}} \\; 2>/dev/null | wc -l"
    count = int(os.popen(comando).read().strip())
    resultados[tech] = count

print("🔧 TECNOLOGIAS IDENTIFICADAS:")
for tech, count in sorted(resultados.items(), key=lambda x: x[1], reverse=True):
    if count > 0:
        print(f"  {tech}: {count} arquivos")

# Buscar módulos específicos
modulos_misterio = [
    "CONN", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M11", "M12",
    "M13", "M14", "M15", "M16", "M17", "M18", "M19", "M20", "M21",
    "M22", "M23", "M24", "M25", "M26", "M27", "M28", "M30", "M31",
    "M32", "M33", "M34", "M35", "M36", "M37", "M38", "M39", "M40",
    "M41", "M42", "M43", "M44"
]

print("\n🔍 BUSCANDO MÓDULOS MISTERIOSOS:")
for modulo in modulos_misterio:
    comando = f"find /home/user -type f -exec grep -l '{modulo}' {{}} \\; 2>/dev/null | head -5"
    arquivos = os.popen(comando).read().strip()
    if arquivos:
        print(f"  {modulo}: ENCONTRADO em {len(arquivos.splitlines())} arquivos")

