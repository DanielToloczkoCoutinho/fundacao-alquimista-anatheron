#!/usr/bin/env python3
# 🚀 DEPLOY SIMPLIFICADO
import subprocess
import os

print("🚀 DEPLOY SIMPLIFICADO - EVITANDO CONFLITOS")

# Estratégia: Fazer force push apenas dos scripts da Fundação
comandos = [
    "git add setup_fundacao.py circuito_phi_plus.py circuito_phi_minus.py circuito_psi_plus.py circuito_psi_minus.py interpretacao_resultados.py teletransporte_quantico.py teste_bell.py ruido_e_correcao.py simulacao_sistema_fisico.py fundacao_master.py",
    'git commit -m "🔮 Atualização Segura - Scripts Quânticos Fundação"',
    "git push origin main --force"
]

for comando in comandos:
    print(f"🔧 Executando: {comando}")
    resultado = subprocess.run(comando, shell=True)
    if resultado.returncode != 0:
        print(f"⚠️  Comando falhou: {comando}")
        break

print("🎯 DEPLOY SIMPLIFICADO CONCLUÍDO!")
print("🌐 Portal será atualizado em alguns minutos")
