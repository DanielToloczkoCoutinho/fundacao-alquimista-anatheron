# 👑 FUNDAÇÃO ALQUIMISTA - SETUP
print("🌌 CONFIGURANDO FUNDAÇÃO ALQUIMISTA...")

try:
    import subprocess
    import sys
    import os
    
    packages = ["qiskit", "qiskit-aer", "matplotlib", "numpy"]
    for pkg in packages:
        subprocess.run([sys.executable, "-m", "pip", "install", pkg])
    
    os.makedirs("resultados_alquimistas", exist_ok=True)
    print("✅ AMBIENTE CONFIGURADO! Fundação Alquimista pronta!")
    
except Exception as e:
    print(f"❌ ERRO: {e}")
