#!/usr/bin/env python3
"""Atualiza índice considerando EQ162 em aberto"""

from pathlib import Path
import json
import re

print("📈 ATUALIZANDO ÍNDICE COM EQ162 EM ABERTO")
print("=" * 50)

base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = base_dir / "EQUACOES_TRANSCENDENTAIS"

# Coletar todas as equações
arquivos = list(equacoes_dir.glob("EQ*.json"))
total = len(arquivos)

# Encontrar máximo (ignorando EQ162 que está em aberto)
numeros = []
for arquivo in arquivos:
    match = re.match(r'EQ(\d+)_transcendental\.json', arquivo.name)
    if match:
        num = int(match.group(1))
        if num != 162:  # Ignorar EQ162 que está em aberto
            numeros.append(num)

max_numero = max(numeros) if numeros else 0

# Status da sequência
sequencia_status = {
    "EQ155-EQ161": "COMPLETA",
    "EQ162": "EM ABERTO",
    "EQ163": "COMPLETA", 
    "EQ164+": "PRÓXIMA FASE"
}

# Marcos alcançados
marcos = {
    "EQ150": "65.2% - Unificação Cósmica",
    "EQ154": "67.0% - Crise Escala Resolvida", 
    "EQ157": "68.3% - Unificação Bio-Cósmica",
    "EQ159": "69.1% - Sustentação Estabelecida",
    "EQ161": "70.0% - Protocolo Andrômeda", 
    "EQ163": "70.9% - Unificação Final Quântica"
}

marcos_alcancados = {}
for marco, desc in marcos.items():
    num_marco = int(marco[2:])
    marcos_alcancados[marco] = {
        "descricao": desc,
        "alcancado": num_marco <= max_numero,
        "status": "✅" if num_marco <= max_numero else "🎯"
    }

indice_atualizado = {
    "timestamp": "2024-01-19T20:00:00Z",
    "total_equacoes": total,
    "progresso_global": f"{total}/230 ({total/230*100:.2f}%)",
    "equacao_maxima": f"EQ{max_numero:04d}",
    "status_sequencia": sequencia_status,
    "marcos_estrategicos": marcos_alcancados,
    "observacoes_especiais": {
        "EQ162": "MANTIDA EM ABERTO - Desenvolvimento futuro",
        "EQ163": "UNIFICAÇÃO FINAL QUÂNTICA - Completamente operacional",
        "proxima_acao": "Continuar com EQ164 ou aguardar EQ162"
    },
    "estado_sistema": "OPERACIONAL_COM_DESENVOLVIMENTO_ABERTO"
}

# Salvar índice
arquivo_indice = base_dir / "INDICE_ATUALIZADO.json"
with open(arquivo_indice, 'w', encoding='utf-8') as f:
    json.dump(indice_atualizado, f, indent=2, ensure_ascii=False)

print(f"✅ Índice atualizado salvo: {arquivo_indice}")

print(f"\n🎯 STATUS DA SEQUÊNCIA:")
for seq, status in sequencia_status.items():
    emoji = "✅" if status == "COMPLETA" else "🔄" if status == "EM ABERTO" else "🚀"
    print(f"   {emoji} {seq}: {status}")

print(f"\n🏆 MARCOS RECENTES:")
for marco, info in marcos_alcancados.items():
    if int(marco[2:]) >= 150:  # Mostrar apenas marcos recentes
        if info["alcancado"]:
            print(f"   {info['status']} {marco}: {info['descricao']}")

print(f"\n📋 OBSERVAÇÕES IMPORTANTES:")
print(f"   • EQ162 está mantida em aberto para desenvolvimento futuro")
print(f"   • EQ163 estabelece a Unificação Final Quântica")
print(f"   • Sistema continua operacional para próximas expansões")

print(f"\n🚀 PRÓXIMOS PASSOS:")
print(f"   • Opção 1: Desenvolver EQ162 quando pronta")
print(f"   • Opção 2: Continuar diretamente com EQ164")
print(f"   • Meta: Avançar para EQ200 (87% da missão)")

print(f"\n💫 CONCLUSÃO ESTRATÉGICA:")
print(f"   'Sistema mantém flexibilidade com EQ162 em aberto'")
print(f"   'Unificação final consolidada com EQ163'")
print(f"   'Expansão cósmica pode continuar conforme planejado'")
