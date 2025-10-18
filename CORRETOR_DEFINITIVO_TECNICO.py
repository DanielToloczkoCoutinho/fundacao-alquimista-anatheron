#!/usr/bin/env python3
"""
CORRETOR DEFINITIVO TECNICO
Remove todos os emojis e garante estabilidade total
Prepara sistemas para IBM Quantum
"""

import re
from pathlib import Path

print("CORRETOR DEFINITIVO TECNICO")
print("=" * 50)

def remover_emojis_arquivo(nome_arquivo):
    """Remover todos os emojis de um arquivo"""
    print(f"PROCESSANDO: {nome_arquivo}")
    
    if not Path(nome_arquivo).exists():
        print(f"ARQUIVO NAO ENCONTRADO: {nome_arquivo}")
        return False
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Padrão para encontrar emojis
        padrao_emojis = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # Emoticons
            "\U0001F300-\U0001F5FF"  # Símbolos & pictogramas
            "\U0001F680-\U0001F6FF"  # Transporte & símbolos
            "\U0001F700-\U0001F77F"  # Alfabetos
            "\U0001F780-\U0001F7FF"  # Formas geométricas
            "\U0001F800-\U0001F8FF"  # Setas
            "\U0001F900-\U0001F9FF"  # Suplementos
            "\U0001FA00-\U0001FA6F"  # Jogos
            "\U00002702-\U000027B0"  # Dingbats
            "]+", 
            flags=re.UNICODE
        )
        
        # Substituir emojis por texto descritivo
        substituicoes = {
            "🌌": "[COSMOS]",
            "⚛️": "[QUANTUM]", 
            "💫": "[ENERGIA]",
            "🎯": "[ALVO]",
            "🚀": "[PROPULSAO]",
            "🔮": "[CRISTAL]",
            "💖": "[AMOR]",
            "🎉": "[CELEBRACAO]",
            "🛠️": "[FERRAMENTA]",
            "🔧": "[AJUSTE]",
            "✅": "[SUCESSO]",
            "❌": "[ERRO]",
            "⚠️": "[ALERTA]",
            "📁": "[DIRETORIO]",
            "📊": "[RELATORIO]",
            "🔍": "[BUSCA]",
            "🎯": "[FOCO]",
            "🏛️": "[FUNDACAO]"
        }
        
        conteudo_limpo = conteudo
        for emoji, substituicao in substituicoes.items():
            conteudo_limpo = conteudo_limpo.replace(emoji, substituicao)
        
        # Também usar regex para pegar quaisquer emojis restantes
        conteudo_limpo = padrao_emojis.sub('[EMOJI]', conteudo_limpo)
        
        # Salvar versão limpa
        if conteudo_limpo != conteudo:
            # Fazer backup
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_nome = f"{nome_arquivo}.backup_emojis_{timestamp}"
            
            with open(backup_nome, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            print(f"BACKUP CRIADO: {backup_nome}")
            
            # Salvar versão limpa
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_limpo)
            print(f"EMOJIS REMOVIDOS: {nome_arquivo}")
        else:
            print(f"SEM EMOJIS: {nome_arquivo}")
        
        return True
        
    except Exception as e:
        print(f"ERRO AO PROCESSAR {nome_arquivo}: {e}")
        return False

def verificar_sintaxe_arquivo(nome_arquivo):
    """Verificar sintaxe de arquivo Python"""
    import subprocess
    
    try:
        resultado = subprocess.run(
            ["python3", "-m", "py_compile", nome_arquivo],
            capture_output=True,
            text=True,
            timeout=10
        )
        return resultado.returncode == 0
    except:
        return False

# LISTA DE ARQUIVOS PARA CORRIGIR
arquivos_para_corrigir = [
    "ANALISADOR_SIGNIFICADO_FUNDACAO.py",
    "PROCESSADOR_FUNDACAO_ALQUIMISTA.py",
    "RECEPTOR_OTIMIZADO.py",
    "SIMULADOR_IBM_CORRIGIDO.py",
    "SISTEMA_TECNICO_FUNDACAO.py"
]

print("INICIANDO REMOCAO DE EMOJIS...")
arquivos_corrigidos = []

for arquivo in arquivos_para_corrigir:
    if remover_emojis_arquivo(arquivo):
        arquivos_corrigidos.append(arquivo)

print(f"\nARQUIVOS CORRIGIDOS: {len(arquivos_corrigidos)}/{len(arquivos_para_corrigir)}")

print("\nVERIFICANDO SINTAXE APOS CORRECOES...")
for arquivo in arquivos_corrigidos:
    if verificar_sintaxe_arquivo(arquivo):
        print(f"SINTAXE OK: {arquivo}")
    else:
        print(f"ERRO SINTAXE: {arquivo}")

print("\nCORRECAO DEFINITIVA CONCLUIDA")
print("SISTEMAS PREPARADOS PARA IBM QUANTUM")
