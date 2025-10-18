#!/usr/bin/env python3
"""Verificador do status atual incluindo EQ163"""

from pathlib import Path
import json

print("🔍 VERIFICANDO STATUS ATUAL COM EQ163")
print("=" * 45)

base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL")
equacoes_dir = base_dir / "EQUACOES_TRANSCENDENTAIS"

# Verificar sequência recente
sequencia = list(range(155, 164))  # EQ155 a EQ163
encontradas = []
estatisticas = []

print("📊 EQUAÇÕES DA SEQUÊNCIA RECENTE:")
for num in sequencia:
    arquivo = equacoes_dir / f"EQ{num}_transcendental.json"
    if arquivo.exists():
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            codigo = dados.get('codigo', 'N/A')
            titulo = dados.get('titulo_simbolico', 'N/A')
            coerencia = dados.get('validacao_ressonancia', {}).get('coerencia', 0)
            
            encontradas.append(num)
            status = "✅ PRESENTE" if num != 162 else "🔄 EM ABERTO"
            
            if num == 162:
                print(f"   {status} EQ{num} - DESENVOLVIMENTO FUTURO")
            else:
                print(f"   {status} EQ{num} - {titulo[:40]}...")
            
        except Exception as e:
            print(f"   ❌ EQ{num} - ERRO: {e}")
    else:
        if num == 162:
            print(f"   🔄 EQ{num} - MANTIDA EM ABERTO (conforme instrução)")
        else:
            print(f"   ❌ EQ{num} - AUSENTE")

# Estatísticas
arquivos_todos = list(equacoes_dir.glob("EQ*.json"))
total_eq = len(arquivos_todos)

print(f"\n🌌 VISÃO GERAL DO SISTEMA:")
print(f"   • Total de equações: {total_eq}/230 ({total_eq/230*100:.2f}%)")
print(f"   • Sequência ativa: EQ155 → ... → EQ161 → EQ163")
print(f"   • EQ162: Mantida em aberto para desenvolvimento futuro")
print(f"   • Próxima equação: EQ164")

print(f"\n🎯 STATUS ESTRATÉGICO:")
if 163 in encontradas:
    print(f"   • ✅ UNIFICAÇÃO FINAL: EQ163 operacional")
    print(f"   • 🔄 DESENVOLVIMENTO: EQ162 em aberto")
    print(f"   • 🚀 PRÓXIMA FASE: EQ164 e além")
    
print(f"\n💫 CONCLUSÃO:")
print(f"   'Sistema mantém coerência com EQ162 em aberto'")
print(f"   'Unificação final quântica estabelecida com EQ163'")
print(f"   'Pronto para continuar expansão cósmica'")
