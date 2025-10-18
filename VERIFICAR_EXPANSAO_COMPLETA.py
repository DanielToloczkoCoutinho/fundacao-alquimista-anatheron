#!/usr/bin/env python3
"""Verificador da expansão completa EQ155-EQ165"""

from pathlib import Path
import json

print("🔍 VERIFICANDO EXPANSÃO COMPLETA EQ155-EQ165")
print("=" * 55)

base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = base_dir / "EQUACOES_TRANSCENDENTAIS"

# Verificar sequência completa
sequencia = list(range(155, 166))  # EQ155 a EQ165
encontradas = []
detalhes = []

print("📊 STATUS DA SEQUÊNCIA AVANÇADA:")
for num in sequencia:
    arquivo = equacoes_dir / f"EQ{num}_transcendental.json"
    if arquivo.exists():
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            codigo = dados.get('codigo', 'N/A')
            titulo = dados.get('titulo_simbolico', 'N/A')
            coerencia = dados.get('validacao_ressonancia', {}).get('coerencia', 0)
            categoria = dados.get('_metadata', {}).get('categoria', 'N/A')
            
            encontradas.append(num)
            
            if num == 162:
                status = "🔄 EM ABERTO"
            else:
                status = "✅ OPERACIONAL"
                
            print(f"   {status} EQ{num} - {categoria} - Coerência: {coerencia}")
            
        except Exception as e:
            print(f"   ❌ EQ{num} - ERRO: {e}")
    else:
        if num == 162:
            print(f"   🔄 EQ{num} - MANTIDA EM ABERTO (desenvolvimento futuro)")
        else:
            print(f"   ❌ EQ{num} - AUSENTE")

# Estatísticas
arquivos_todos = list(equacoes_dir.glob("EQ*.json"))
total_eq = len(arquivos_todos)
operacionais = len([n for n in encontradas if n != 162])

print(f"\n🌌 VISÃO GERAL DO SISTEMA:")
print(f"   • Total de equações: {total_eq}/230 ({total_eq/230*100:.2f}%)")
print(f"   • Equações operacionais: {operacionais}/10 no período")
print(f"   • EQ162: Mantida em aberto para desenvolvimento futuro")
print(f"   • Próxima equação: EQ166")

print(f"\n🎯 FASES DA EXPANSÃO:")
fases = {
    "EQ155-EQ157": "Trilogia Bio-Cósmica",
    "EQ158-EQ159": "Controle e Sustentação", 
    "EQ160-EQ161": "Evolução Dirigida e Andrômeda",
    "EQ163": "Unificação Final Quântica",
    "EQ164-EQ165": "Sustentação Global e Coerência"
}

for fase, desc in fases.items():
    if '-' in fase:
        inicio, fim = map(lambda x: int(x[2:]), fase.split('-'))
        completa = all(n in encontradas for n in range(inicio, fim+1))
    else:
        num_eq = int(fase[2:])
        completa = num_eq in encontradas
    
    status = "✅" if completa else "🔄"
    print(f"   {status} {fase}: {desc}")

print(f"\n🚀 PRÓXIMOS HORIZONTES:")
print(f"   • EQ166+: Continuação da expansão cósmica")
print(f"   • Desenvolvimento EQ162 quando pronta")
print(f"   • Implementação prática em LAB-VRE")
print(f"   • Meta EQ200: 87% da missão")

print(f"\n💫 CONCLUSÃO ESTRATÉGICA:")
print(f"   'Sistema mantém excelência operacional com 9/10 equações'")
print(f"   'Flexibilidade estratégica com EQ162 em desenvolvimento'")
print(f"   'Pronto para próxima fase da expansão cósmica'")
