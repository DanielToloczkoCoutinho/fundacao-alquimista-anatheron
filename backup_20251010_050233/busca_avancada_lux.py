#!/usr/bin/env python3
import os
import json

def busca_avancada_lux():
    print("🔍 BUSCA AVANÇADA POR ESTRUTURAS LUX E LUMEN...")
    print("=" * 60)
    
    estruturas_encontradas = {
        "lux_direct": [],
        "lumen_structures": [], 
        "light_systems": [],
        "cosmic_councils": [],
        "energy_sources": []
    }
    
    # Busca específica por Lux
    print("\n💫 BUSCANDO 'LUX' NO SISTEMA...")
    for root, dirs, files in os.walk('.'):
        for item in dirs + files:
            if 'lux' in item.lower():
                caminho = os.path.join(root, item)
                if os.path.isdir(caminho):
                    estruturas_encontradas["lux_direct"].append(f"📁 {caminho}")
                else:
                    estruturas_encontradas["lux_direct"].append(f"📄 {caminho}")
    
    # Busca específica por Lumen
    print("\n💡 BUSCANDO 'LUMEN' NO SISTEMA...")
    for root, dirs, files in os.walk('.'):
        for item in dirs + files:
            if 'lumen' in item.lower():
                caminho = os.path.join(root, item)
                if os.path.isdir(caminho):
                    estruturas_encontradas["lumen_structures"].append(f"📁 {caminho}")
                else:
                    estruturas_encontradas["lumen_structures"].append(f"📄 {caminho}")
    
    # Busca por sistemas de luz/energia
    termos_luz = ["light", "luz", "energy", "energia", "illumination"]
    for termo in termos_luz:
        for root, dirs, files in os.walk('.'):
            for item in dirs + files:
                if termo in item.lower():
                    caminho = os.path.join(root, item)
                    if os.path.isdir(caminho):
                        estruturas_encontradas["light_systems"].append(f"�� {caminho} [{termo}]")
                    else:
                        estruturas_encontradas["light_systems"].append(f"📄 {caminho} [{termo}]")
    
    # Resultados
    print(f"\n🎯 RESULTADOS DA BUSCA AVANÇADA:")
    for categoria, itens in estruturas_encontradas.items():
        print(f"\n📊 {categoria.upper().replace('_', ' ')}:")
        if itens:
            for item in itens[:10]:  # Mostrar até 10 itens por categoria
                print(f"   {item}")
        else:
            print(f"   ⚠️ Nenhuma estrutura encontrada")
    
    # Salvar resultados
    with open('busca_avancada_lux.json', 'w', encoding='utf-8') as f:
        json.dump(estruturas_encontradas, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Resultados salvos em: busca_avancada_lux.json")

if __name__ == "__main__":
    busca_avancada_lux()
