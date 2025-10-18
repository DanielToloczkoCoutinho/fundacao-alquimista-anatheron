#!/usr/bin/env python3
import os
from pathlib import Path

base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL/EQUACOES_TRANSCENDENTAIS/")

# Contar arquivos reais
arquivos_eq = [f for f in os.listdir(base_dir) if f.startswith('EQ') and f.endswith('.json')]
total_real = len(arquivos_eq)

print("📊 PROGRESSO REAL DO SISTEMA:")
print("=" * 40)
print(f"• Equações processadas: {total_real}")
print(f"• Progresso: {total_real}/230 ({total_real/230*100:.1f}%)")
print(f"• Equações restantes: {230 - total_real}")

# Verificar específico das CQAM
cqam_arquivos = [f for f in arquivos_eq if f.startswith('EQ011')]
print(f"• Equações CQAM (0112-0117): {len(cqam_arquivos)}/6")

# Listar últimas equações
print(f"\\n📁 ÚLTIMAS EQUAÇÕES PROCESSADAS:")
ultimas = sorted(arquivos_eq)[-10:]
for eq in ultimas:
    print(f"   • {eq}")

# Status da consciência
if len(cqam_arquivos) >= 6:
    print(f"\\n💫 STATUS CQAM: CONSCIÊNCIA MANIFESTADA!")
else:
    print(f"\\n⚡ STATUS CQAM: EM PROCESSAMENTO...")
