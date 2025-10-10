#!/usr/bin/env python3
import json
import re

print("🚀 EXPANDINDO PARA AS 231 EQUAÇÕES COMPLETAS...")

# Carregar biblioteca atual
with open('biblioteca_equacoes.json', 'r') as f:
    biblioteca = json.load(f)

# Gerar equações faltantes baseadas no padrão
categorias = {
    "EQ01-EQ50": "FUNDAMENTOS QUÂNTICOS",
    "EQ51-EQ100": "ALQUIMIA MODERNA", 
    "EQ101-EQ231": "EXPANSÃO CÓSMICA"
}

# Adicionar equações padrão para completar
for i in range(1, 232):
    eq_id = f"EQ{i:03d}"
    
    if eq_id not in biblioteca:
        # Determinar categoria
        if i <= 50:
            categoria = "FUNDAMENTOS QUÂNTICOS"
            descricao = f"Equação quântica fundamental {i} - base do sistema"
        elif i <= 100:
            categoria = "ALQUIMIA MODERNA" 
            descricao = f"Equação alquímica moderna {i} - transmutação consciente"
        else:
            categoria = "EXPANSÃO CÓSMICA"
            descricao = f"Equação de expansão cósmica {i} - unificação universal"
        
        biblioteca[eq_id] = {
            "nome": f"Equação {i:03d} - Em Desenvolvimento",
            "descricao": descricao,
            "categoria": categoria,
            "documento": "equacoes_fundamentais.md",
            "status": "EM EXPANSÃO"
        }

# Salvar biblioteca expandida
with open('biblioteca_completa_231.json', 'w') as f:
    json.dump(biblioteca, f, indent=2, ensure_ascii=False)

print(f"✅ EXPANSÃO CONCLUÍDA!")
print(f"📊 Equações na biblioteca: {len(biblioteca)}")
print(f"🎯 Faixa completa: EQ001-EQ231")

# Estatísticas
cats = {}
for info in biblioteca.values():
    cat = info['categoria']
    cats[cat] = cats.get(cat, 0) + 1

print(f"\n📁 DISTRIBUIÇÃO FINAL:")
for cat, count in cats.items():
    print(f"   • {cat}: {count} equações")
