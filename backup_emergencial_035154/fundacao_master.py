# 👑 FUNDAÇÃO ALQUIMISTA - SCRIPT MESTRE
import subprocess
import sys

print("👑 INICIANDO FUNDAÇÃO ALQUIMISTA...")
print("🌌 CARREGANDO TODOS OS MÓDULOS...")

scripts = [
    "setup_fundacao.py",
    "circuito_phi_plus.py", 
    "circuito_phi_minus.py",
    "circuito_psi_plus.py",
    "circuito_psi_minus.py",
    "interpretacao_resultados.py",
    "teletransporte_quantico.py",
    "teste_bell.py",
    "ruido_e_correcao.py",
    "simulacao_sistema_fisico.py"
]

for script in scripts:
    print(f"\\n🎯 EXECUTANDO: {script}")
    try:
        result = subprocess.run([sys.executable, script], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"⚠️  AVISO: {result.stderr}")
    except Exception as e:
        print(f"❌ ERRO em {script}: {e}")

print("\\n✅ FUNDAÇÃO ALQUIMISTA COMPLETA!")
print("🌠 TODOS OS RITUAIS QUÂNTICOS CONCLUÍDOS!")
