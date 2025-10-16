import os
import json
from datetime import datetime

def mapear_fundacao():
    print("🌌 MAPEANDO FUNDAÇÃO ALQUIMISTA...")
    
    base_path = "/home/user"
    estrutura = {
        "timestamp": datetime.now().isoformat(),
        "sistema": "Fundação Alquimista - Matriz LUX.NET",
        "estatisticas": {}
    }
    
    # Contar arquivos por tipo
    tipos = {
        "documentos": [".md"],
        "scripts_python": [".py"], 
        "scripts_shell": [".sh"],
        "interfaces": [".js", ".ts", ".jsx", ".tsx"],
        "configuracoes": [".json"]
    }
    
    for tipo, extensoes in tipos.items():
        count = 0
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if any(file.endswith(ext) for ext in extensoes):
                    count += 1
        estrutura["estatisticas"][tipo] = count
    
    # Salvar relatório
    with open("mapeamento_fundacao.json", "w") as f:
        json.dump(estrutura, f, indent=2)
    
    print("✅ MAPEAMENTO CONCLUÍDO!")
    print(f"📊 Estatísticas: {json.dumps(estrutura['estatisticas'], indent=2)}")
    return estrutura

if __name__ == "__main__":
    mapear_fundacao()
