#!/usr/bin/env python3
"""
🛠️ CORRETOR COMPLETO - EMOJIS EM F-STRINGS
⚡ Corrige todos os emojis problemáticos de uma vez
🔧 Processa múltiplos arquivos automaticamente
"""

import re
from pathlib import Path

print("🛠️ CORRETOR COMPLETO - EMOJIS EM F-STRINGS")
print("=" * 60)

def corrigir_emojis_fstring(conteudo):
    """Corrigir todos os emojis em f-strings"""
    # Padrão para encontrar f-strings com emojis sem aspas
    padrao = r'print\(f([🎯🌌💫🚀🔍📊📁📚🔗🗺️🌎🎓🏛️📚🔬⚡🛡️💾🛠️🔧]+)'
    
    def substituir_emoji(match):
        emoji = match.group(1)
        return f'print(f"{emoji}'
    
    # Primeira correção: emojis no início da f-string
    conteudo_corrigido = re.sub(padrao, substituir_emoji, conteudo)
    
    # Correção adicional para outros padrões problemáticos
    problemas_comuns = [
        (r'print\(f💫', 'print(f"💫'),
        (r'print\(f🚀', 'print(f"🚀'),
        (r'print\(f🌌', 'print(f"🌌'),
        (r'print\(f🎯', 'print(f"🎯'),
        (r'print\(f🔍', 'print(f"🔍'),
        (r'print\(f📊', 'print(f"📊'),
    ]
    
    for problema, correcao in problemas_comuns:
        conteudo_corrigido = conteudo_corrigido.replace(problema, correcao)
    
    return conteudo_corrigido

def corrigir_chaves_duplas(conteudo):
    """Corrigir problemas de chaves duplas"""
    # Corrigir print(f"{'='*80}") que deveria ser print("="*80)
    conteudo_corrigido = conteudo.replace('print(f"{\'=\'*80}")', 'print("="*80)')
    return conteudo_corrigido

def verificar_e_corrigir_arquivo(nome_arquivo):
    """Verificar e corrigir um arquivo específico"""
    print(f"\n📁 PROCESSANDO: {nome_arquivo}")
    
    if not Path(nome_arquivo).exists():
        print("   📭 Arquivo não encontrado")
        return False
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo_original = f.read()
        
        # Aplicar correções
        conteudo_corrigido = corrigir_emojis_fstring(conteudo_original)
        conteudo_corrigido = corrigir_chaves_duplas(conteudo_corrigido)
        
        # Verificar se houve mudanças
        if conteudo_corrigido != conteudo_original:
            # Fazer backup
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_nome = f"{nome_arquivo}.backup_{timestamp}"
            
            with open(backup_nome, 'w', encoding='utf-8') as f:
                f.write(conteudo_original)
            print(f"   💾 Backup criado: {backup_nome}")
            
            # Salvar correções
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_corrigido)
            print("   ✅ Correções aplicadas")
            
            # Mostrar mudanças
            linhas_originais = conteudo_original.split('\n')
            linhas_corrigidas = conteudo_corrigido.split('\n')
            
            for i, (orig, corr) in enumerate(zip(linhas_originais, linhas_corrigidas)):
                if orig != corr:
                    print(f"      Linha {i+1}:")
                    print(f"        ANTES: {orig}")
                    print(f"        DEPOIS: {corr}")
        else:
            print("   ✅ Nenhuma correção necessária")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Erro ao processar: {e}")
        return False

# Lista de arquivos para corrigir
arquivos_para_corrigir = [
    "PROCESSADOR_EQUACOES_COSMICAS_2.py",
    "VERIFICADOR_TEMPO_REAL.py"
]

print("🔧 INICIANDO CORREÇÕES EM TODOS OS ARQUIVOS...")
arquivos_corrigidos = []

for arquivo in arquivos_para_corrigir:
    if corrigir_e_corrigir_arquivo(arquivo):
        arquivos_corrigidos.append(arquivo)

print(f"\n📊 RELATÓRIO DE CORREÇÕES:")
print(f"   • Arquivos processados: {len(arquivos_para_corrigir)}")
print(f"   • Arquivos corrigidos: {len(arquivos_corrigidos)}")
print(f"   • Arquivos com problemas: {len(arquivos_para_corrigir) - len(arquivos_corrigidos)}")

if arquivos_corrigidos:
    print(f"\n✅ ARQUIVOS CORRIGIDOS COM SUCESSO:")
    for arquivo in arquivos_corrigidos:
        print(f"   • {arquivo}")

print("\n🎯 CORREÇÃO COMPLETA CONCLUÍDA!")
