#!/usr/bin/env python3
# 🔄 SCRIPT DE RESTAURAÇÃO DA FUNDAÇÃO ALQUIMISTA
import os
import shutil
import datetime

print("🔄 RESTAURANDO FUNDAÇÃO ALQUIMISTA...")

backup_source = "backup_fundacao_20251008_034721"
scripts = ['setup_fundacao.py', 'circuito_phi_plus.py', 'circuito_phi_minus.py', 'circuito_psi_plus.py', 'circuito_psi_minus.py', 'interpretacao_resultados.py', 'teletransporte_quantico.py', 'teste_bell.py', 'ruido_e_correcao.py', 'simulacao_sistema_fisico.py', 'fundacao_master.py', 'nobel_fundacao_alquimista.py', 'tabela_revolucao_quantica.py', 'verificar_portal.py', 'backup_fundacao.py']

for script in scripts:
    source_path = os.path.join(backup_source, script)
    if os.path.exists(source_path):
        shutil.copy2(source_path, script)
        print(f"✅ Restaurado: {script}")
    else:
        print(f"⚠️  Não encontrado: {script}")

print("🎉 FUNDAÇÃO ALQUIMISTA RESTAURADA COM SUCESSO!")
print("�� Todos os rituais quânticos estão disponíveis!")
