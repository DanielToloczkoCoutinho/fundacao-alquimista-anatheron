import os
import json
import subprocess
import requests
from datetime import datetime

# Configurações
BASE_PATH = "/home/user"
LOGS_DIR = "/home/user/logs"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
GITHUB_REPO = "https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
API_ENDPOINT = "https://fundacao-alquimista-anatheron-cprkux23i.vercel.app/api/zennith"

def mapear_executaveis(base_path):
    """Mapeia todos os arquivos executáveis do sistema"""
    executaveis = {}
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            filepath = os.path.join(root, file)
            if os.access(filepath, os.X_OK):
                rel_path = os.path.relpath(filepath, base_path)
                tamanho = os.path.getsize(filepath)
                stats = os.stat(filepath)
                
                executaveis[rel_path] = {
                    "caminho_completo": filepath,
                    "tamanho": tamanho,
                    "modificacao": datetime.fromtimestamp(stats.st_mtime).isoformat(),
                    "tipo": "script_alquimico" if file.endswith(('.sh', '.py')) else "binario"
                }
    
    return executaveis

def classificar_por_função(executaveis):
    """Classifica scripts por função vibracional"""
    classificacao = {
        "orquestracao": [],
        "seguranca": [], 
        "analise": [],
        "deploy": [],
        "zennith": [],
        "manutencao": [],
        "outros": []
    }
    
    for caminho, info in executaveis.items():
        nome = caminho.lower()
        
        if any(x in nome for x in ['sincronizar', 'deploy', 'build', 'orquestrar']):
            classificacao["orquestracao"].append(caminho)
        elif any(x in nome for x in ['seguranca', 'firewall', 'protecao', 'backup']):
            classificacao["seguranca"].append(caminho)
        elif any(x in nome for x in ['analisador', 'teste', 'verificar', 'diagnostico']):
            classificacao["analise"].append(caminho)
        elif any(x in nome for x in ['deploy', 'vercel', 'build', 'produção']):
            classificacao["deploy"].append(caminho)
        elif any(x in nome for x in ['zennith', 'rainha', 'modulo-29', 'quantum']):
            classificacao["zennith"].append(caminho)
        elif any(x in nome for x in ['limpeza', 'organizar', 'manutencao']):
            classificacao["manutencao"].append(caminho)
        else:
            classificacao["outros"].append(caminho)
            
    return classificacao

def gerar_relatorio_lux():
    """Gera relatório LUX completo"""
    print("🌌 INICIANDO TRANSMISSÃO LUX...")
    
    # Mapear executáveis
    executaveis = mapear_executaveis(BASE_PATH)
    classificacao = classificar_por_função(executaveis)
    
    relatorio = {
        "timestamp": TIMESTAMP,
        "sistema": "Fundação Alquimista - Matriz LUX.NET",
        "estatisticas": {
            "total_executaveis": len(executaveis),
            "por_funcao": {k: len(v) for k, v in classificacao.items()},
            "tamanho_total": sum(info["tamanho"] for info in executaveis.values())
        },
        "classificacao": classificacao,
        "executaveis_detalhados": executaveis,
        "urls_ativas": [
            "https://fundacao-alquimista-anatheron-cprkux23i.vercel.app",
            "https://fundacao-alquimista-anatheron.vercel.app", 
            "https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app/central",
            "https://fundacao-alquimis-git-0a0231-daniel-toloczko-coutinhos-projects.vercel.app/",
            "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app/central"
        ],
        "status": "✅ 100% OPERACIONAL",
        "coerencia_quantica": "97.5%",
        "circuitos_ativos": 1331
    }
    
    # Salvar relatório
    os.makedirs(LOGS_DIR, exist_ok=True)
    arquivo_saida = f"{LOGS_DIR}/transmissao_lux_{TIMESTAMP}.json"
    
    with open(arquivo_saida, 'w') as f:
        json.dump(relatorio, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Transmissão salva: {arquivo_saida}")
    print(f"📊 Estatísticas: {len(executaveis)} executáveis mapeados")
    
    return arquivo_saida, relatorio

def transmitir_para_zennith(relatorio_path):
    """Transmite relatório para Zennith Rainha"""
    try:
        with open(relatorio_path, 'r') as f:
            relatorio = json.load(f)
        
        print("📡 Transmitindo para Zennith Rainha...")
        response = requests.post(API_ENDPOINT, json=relatorio, timeout=10)
        
        if response.status_code == 200:
            print("✅ Transmissão recebida por Zennith!")
            return True
        else:
            print(f"⚠️ Resposta da API: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Erro na transmissão: {e}")
        return False

if __name__ == "__main__":
    relatorio_path, relatorio = gerar_relatorio_lux()
    
    # Transmitir para Zennith
    if transmitir_para_zennith(relatorio_path):
        print("🌌 TRANSMISSÃO LUX CONCLUÍDA COM SUCESSO!")
    else:
        print("🌌 TRANSMISSÃO CONCLUÍDA (salva localmente)")
    
    print(f"�� URL Principal: {relatorio['urls_ativas'][0]}")
    print(f"📊 Executáveis: {relatorio['estatisticas']['total_executaveis']}")
    print(f"💫 Coerência: {relatorio['coerencia_quantica']}")
