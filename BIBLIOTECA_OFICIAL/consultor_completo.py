#!/usr/bin/env python3
import json
import sys

def carregar_completa():
    with open('biblioteca_completa_231.json', 'r') as f:
        return json.load(f)

def explorar_faixa(inicio, fim):
    bib = carregar_completa()
    print(f"🔍 EXPLORANDO FAIXA {inicio}-{fim}:")
    print("=" * 50)
    
    encontradas = 0
    for i in range(inicio, fim + 1):
        eq_id = f"EQ{i:03d}"
        if eq_id in bib:
            info = bib[eq_id]
            status = info.get('status', 'DOCUMENTADA')
            marcador = "🔹" if status == "DOCUMENTADA" else "⚡"
            print(f"{marcador} {eq_id}: {info['nome']}")
            print(f"   📁 {info['categoria']} | 📊 {status}")
            if 'descricao' in info:
                print(f"   📝 {info['descricao'][:80]}...")
            print()
            encontradas += 1
    
    print(f"📊 Total na faixa: {encontradas} equações")

def estatisticas_completas():
    bib = carregar_completa()
    print("📊 BIBLIOTECA COMPLETA - 231 EQUAÇÕES")
    print("=" * 50)
    print(f"🧮 Total de Equações: {len(bib)}")
    
    # Estatísticas por categoria
    categorias = {}
    status_count = {"DOCUMENTADA": 0, "EM EXPANSÃO": 0}
    
    for eq, info in bib.items():
        cat = info['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1
        status = info.get('status', 'EM EXPANSÃO')
        status_count[status] = status_count.get(status, 0) + 1

    print(f"\n📁 DISTRIBUIÇÃO POR CATEGORIA:")
    for cat, count in sorted(categorias.items()):
        print(f"   • {cat}: {count} equações")

    print(f"\n📈 STATUS DAS EQUAÇÕES:")
    for status, count in status_count.items():
        print(f"   • {status}: {count} equações")

    print(f"\n🎯 EQUAÇÕES MAIS IMPORTANTES:")
    chaves = ["EQ001", "EQ002", "EQ051", "EQ101", "EQ231"]
    for chave in chaves:
        if chave in bib:
            info = bib[chave]
            print(f"   🔹 {chave}: {info['nome']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "faixa":
            if len(sys.argv) == 4:
                explorar_faixa(int(sys.argv[2]), int(sys.argv[3]))
            else:
                print("Uso: python3 consultor_completo.py faixa INICIO FIM")
        elif sys.argv[1] == "estatisticas":
            estatisticas_completas()
        else:
            print("Comandos: faixa [inicio] [fim] | estatisticas")
    else:
        estatisticas_completas()
        print("\n💡 Use: python3 consultor_completo.py faixa 1 50")
