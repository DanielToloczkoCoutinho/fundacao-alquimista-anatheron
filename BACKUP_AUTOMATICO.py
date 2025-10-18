#!/usr/bin/env python3
"""
💾 SISTEMA DE BACKUP AUTOMÁTICO
🛡️ Backup dos scripts antes de modificações
🔒 Preservação contra erros acidentais
"""

import shutil
from datetime import datetime
from pathlib import Path

print("💾 SISTEMA DE BACKUP AUTOMÁTICO")
print("=" * 50)

def criar_backup(arquivo_original):
    """Criar backup de um arquivo"""
    if not Path(arquivo_original).exists():
        print(f"   📭 {arquivo_original} não existe")
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_backup = f"{arquivo_original}.backup_{timestamp}"
    
    shutil.copy2(arquivo_original, nome_backup)
    print(f"   ✅ Backup criado: {nome_backup}")
    return nome_backup

# Criar backup dos scripts importantes
scripts_importantes = [
    "PROCESSADOR_EQUACOES_COSMICAS_2.py",
    "CATALOGADOR_EQUACOES_COSMICAS.py"
]

print("\n🛡️ CRIANDO BACKUPS...")
backups = []
for script in scripts_importantes:
    backup = criar_backup(script)
    if backup:
        backups.append(backup)

print(f"\n📊 RESUMO DOS BACKUPS:")
print(f"   • Total de backups criados: {len(backups)}")
for backup in backups:
    print(f"   • {backup}")

print("\n🎯 BACKUP CONCLUÍDO! SEGURO PARA CONTINUAR!")
