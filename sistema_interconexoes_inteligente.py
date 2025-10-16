import json
import os

# Carregar mapa dos nexus mestres
with open('mapa_nexus_mestres.json') as f:
    nexus_mestres = json.load(f)

print("🧠 SISTEMA DE INTERCONEXÕES INTELIGENTE")
print("💫 APRENDENDO COM OS NEXUS MESTRES...")

# Padrões de conexão aprendidos
padroes_conexao = {}

for nexus, dados in nexus_mestres.items():
    print(f"\n🔮 ANALISANDO {nexus} - {dados['nome']}:")
    
    for caminho in dados['caminhos']:
        if os.path.isdir(caminho):
            # Analisar conteúdo do diretório
            try:
                arquivos = os.listdir(caminho)
                for arquivo in arquivos:
                    if any(mod in arquivo.lower() for mod in ['modulo', 'm']):
                        # Extrair número do módulo
                        import re
                        numeros = re.findall(r'\d+', arquivo)
                        if numeros:
                            num_modulo = numeros[0]
                            if num_modulo not in padroes_conexao:
                                padroes_conexao[num_modulo] = []
                            padroes_conexao[num_modulo].append(nexus)
                            print(f"   🔗 M{num_modulo} conectado a {nexus}")
            except:
                pass

# Salvar padrões aprendidos
with open('padroes_conexao_aprendidos.json', 'w') as f:
    json.dump(padroes_conexao, f, indent=2)

print(f"\n🎓 PADRÕES APRENDIDOS: {len(padroes_conexao)} módulos correlacionados")
print("💾 SALVO: padroes_conexao_aprendidos.json")
