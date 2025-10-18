#!/usr/bin/env python3
"""
CORRETOR DEFINITIVO SIMPLES
Corrige problemas de sintaxe nos verificadores
Versão ultra-simples e funcional
"""

import re

print("CORRETOR DEFINITIVO SIMPLES")
print("=" * 40)

def corrigir_verificador_cronologia():
    """Corrigir o verificador de cronologia"""
    print("�� CORRIGINDO VERIFICADOR_CRONOLOGIA_COMPLETA.py...")
    
    try:
        with open('VERIFICADOR_CRONOLOGIA_COMPLETA.py', 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Corrigir f-string problemática (linha ~137)
        # Encontrar e corrigir a linha com backslash em f-string
        linhas = conteudo.split('\n')
        for i, linha in enumerate(linhas):
            if "print(f\"   • Equações de EQ001 a EQ021:" in linha and "re.search" in linha:
                # Substituir por versão mais simples
                linhas[i] = '        print(f"   • Equações de EQ001 a EQ021: {len([eq for eq in equacoes if int(re.search(r\\'EQ0*(\\d+)\\', eq).group(1)) <= 21])}")'
                print("   ✅ Linha 137 corrigida")
        
        # Salvar correção
        with open('VERIFICADOR_CRONOLOGIA_COMPLETA.py', 'w', encoding='utf-8') as f:
            f.write('\n'.join(linhas))
        
        print("   ✅ VERIFICADOR_CRONOLOGIA_COMPLETA.py corrigido")
        return True
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def corrigir_resumo_visual():
    """Corrigir o resumo visual"""
    print("🔧 CORRIGINDO RESUMO_VISUAL_EQUACOES.py...")
    
    try:
        with open('RESUMO_VISUAL_EQUACOES.py', 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Corrigir problema de regex
        linhas = conteudo.split('\n')
        for i, linha in enumerate(linhas):
            if "key=lambda x: int(re.search(r'EQ0*(\\d+)', x).group(1)))" in linha:
                # Adicionar verificação de segurança
                linhas[i] = '    equacoes_ordenadas = sorted([eq for eq in equacoes_encontradas if re.search(r\\'EQ0*(\\d+)\\', eq)],'
                linhas.insert(i+1, '                               key=lambda x: int(re.search(r\\'EQ0*(\\d+)\\', x).group(1)) if re.search(r\\'EQ0*(\\d+)\\', x) else 0)')
                print("   ✅ Problema de regex corrigido")
                break
        
        # Salvar correção
        with open('RESUMO_VISUAL_EQUACOES.py', 'w', encoding='utf-8') as f:
            f.write('\n'.join(linhas))
        
        print("   ✅ RESUMO_VISUAL_EQUACOES.py corrigido")
        return True
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def verificar_correcoes():
    """Verificar se as correções funcionaram"""
    print("\n✅ VERIFICANDO CORREÇÕES...")
    
    arquivos = ["VERIFICADOR_CRONOLOGIA_COMPLETA.py", "RESUMO_VISUAL_EQUACOES.py"]
    
    for arquivo in arquivos:
        try:
            # Teste de sintaxe simples
            with open(arquivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
            compile(codigo, arquivo, 'exec')
            print(f"   ✅ {arquivo} - Sintaxe OK")
        except Exception as e:
            print(f"   ❌ {arquivo} - Erro: {e}")

# EXECUTAR CORREÇÕES
print("🎯 APLICANDO CORREÇÕES...\n")

corrigir_verificador_cronologia()
corrigir_resumo_visual()
verificar_correcoes()

print(f"\n💫 CORREÇÕES APLICADAS!")
print("🎯 AGORA EXECUTE O VERIFICADOR UNIVERSAL NOVAMENTE")
