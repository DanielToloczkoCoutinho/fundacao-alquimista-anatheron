#!/usr/bin/env python3
import json
import sys

def carregar_biblioteca():
    with open('biblioteca_equacoes.json', 'r') as f:
        return json.load(f)

def listar_todas():
    bib = carregar_biblioteca()
    print("📋 EQUAÇÕES DA FUNDAÇÃO ALCHEMISTA")
    print("=" * 50)
    print(f"🎯 TOTAL: {len(bib)} equações documentadas")
    
    categorias = {}
    for eq, info in bib.items():
        cat = info['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1

    print("\n📚 CATEGORIAS:")
    for cat, count in categorias.items():
        print(f"   • {cat}: {count} equações")

    print(f"\n🧮 LISTA COMPLETA:")
    for eq, info in sorted(bib.items()):
        print(f"🔹 {eq}: {info['nome']}")
        print(f"   📝 {info['descricao']}")
        print(f"   📁 {info['categoria']}")
        print()

def buscar_equacao(eq):
    bib = carregar_biblioteca()
    if eq in bib:
        info = bib[eq]
        print(f"🎯 {eq}: {info['nome']}")
        print(f"📁 Categoria: {info['categoria']}")
        print(f"📝 Descrição: {info['descricao']}")
        print(f"📄 Documento: {info['documento']}")
    else:
        print(f"❌ {eq} não encontrada")
        print("💡 Equações disponíveis:", ", ".join(sorted(bib.keys())))

def estatisticas():
    bib = carregar_biblioteca()
    print("�� ESTATÍSTICAS OFICIAIS DA FUNDAÇÃO")
    print("=" * 50)
    print(f"🧮 Total de Equações Documentadas: {len(bib)}")
    print(f"📅 Documento Principal: equacoes_fundamentais.md")
    print(f"🎯 Faixa Completa no Sistema: EQ01-EQ231")
    
    categorias = {}
    for info in bib.values():
        cat = info['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1

    print(f"\n📁 DISTRIBUIÇÃO POR CATEGORIA:")
    for cat, count in categorias.items():
        print(f"   • {cat}: {count} equações")

    print(f"\n🌟 EQUAÇÕES FUNDAMENTAIS:")
    destaques = ["EQ01", "EQ02", "EQ51", "EQ101", "EQ231"]
    for eq in destaques:
        if eq in bib:
            info = bib[eq]
            print(f"   🔹 {eq}: {info['nome']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("🎯 USO: python3 consulta_equacoes.py [comando]")
        print("  listar      - Listar todas equações")
        print("  buscar EQXX - Buscar equação específica")
        print("  estatisticas - Estatísticas completas")
        sys.exit(1)
    
    comando = sys.argv[1]
    
    if comando == "listar":
        listar_todas()
    elif comando == "buscar" and len(sys.argv) > 2:
        buscar_equacao(sys.argv[2])
    elif comando == "estatisticas":
        estatisticas()
    else:
        print("❌ Comando inválido")
