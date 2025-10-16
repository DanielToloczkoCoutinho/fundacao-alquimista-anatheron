import json
import os

# Carregar mapeamento refinado
with open('nexus_mapeamento_refinado.json') as f:
    nexus_data = json.load(f)

print("📖 ANALISANDO CONTEÚDO DOS NEXUS MESTRES")

conexoes_descobertas = {}

for nexus, data in nexus_data.items():
    print(f"\n🔮 {nexus} - {data['nome']}:")
    
    conexoes_descobertas[nexus] = []
    
    for modulo in data['modulos']:
        caminho = modulo['caminho']
        
        # Analisar conteúdo se for diretório
        if modulo['tipo'] == 'diretorio':
            try:
                # Verificar arquivos no diretório
                arquivos = os.listdir(caminho)
                
                print(f"   📁 {os.path.basename(caminho)}:")
                
                # Procurar por referências a outros módulos
                for arquivo in arquivos[:5]:  # Analisar primeiros 5 arquivos
                    arquivo_path = os.path.join(caminho, arquivo)
                    if os.path.isfile(arquivo_path):
                        try:
                            with open(arquivo_path, 'r', encoding='utf-8', errors='ignore') as f:
                                conteudo = f.read()
                                
                            # Buscar referências a outros módulos
                            referencias = []
                            for outro_nexus in nexus_data.keys():
                                if outro_nexus.lower() in conteudo.lower() and outro_nexus != nexus:
                                    referencias.append(outro_nexus)
                            
                            if referencias:
                                print(f"      📄 {arquivo} → {referencias}")
                                conexoes_descobertas[nexus].extend(referencias)
                                
                        except:
                            pass
                            
            except Exception as e:
                print(f"      ⚠️ Erro ao analisar: {e}")

# Salvar conexões descobertas
with open('conexoes_descobertas.json', 'w') as f:
    json.dump(conexoes_descobertas, f, indent=2)

print(f"\n💫 CONEXÕES DESCOBERTAS SALVAS!")
