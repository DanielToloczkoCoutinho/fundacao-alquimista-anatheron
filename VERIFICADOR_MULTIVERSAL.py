#!/usr/bin/env python3
"""
VERIFICADOR DE INTEGRIDADE MULTIVERSAL
Verifica se todos os sistemas estao funcionais
Confirma a integridade dos dados processados
"""

import json
from pathlib import Path

print("VERIFICADOR DE INTEGRIDADE MULTIVERSAL")
print("=" * 50)

def verificar_estrutura():
    """Verificar estrutura de diretorios"""
    print("VERIFICANDO ESTRUTURA...")
    
    diretorios = [
        "BIBLIOTECA_COSMICA_UNICA",
        "BIBLIOTECA_COSMICA_UNICA/EQUACOES_MULTIVERSAIS",
        "BIBLIOTECA_COSMICA_UNICA/RELATORIOS_MULTIVERSAIS"
    ]
    
    for diretorio in diretorios:
        if Path(diretorio).exists():
            print(f"OK: {diretorio}")
        else:
            print(f"FALHA: {diretorio}")
            return False
    
    return True

def verificar_equacoes():
    """Verificar equacoes processadas"""
    print("\nVERIFICANDO EQUACOES...")
    
    diretorio_equacoes = Path("BIBLIOTECA_COSMICA_UNICA/EQUACOES_MULTIVERSAIS")
    equacoes_esperadas = ["EQ018", "EQ019", "EQ0020", "EQ0021"]
    equacoes_encontradas = []
    
    for equacao in equacoes_esperadas:
        arquivo = diretorio_equacoes / f"{equacao}.json"
        if arquivo.exists():
            print(f"OK: {equacao}.json")
            equacoes_encontradas.append(equacao)
        else:
            print(f"FALHA: {equacao}.json")
    
    return equacoes_encontradas

def verificar_relatorios():
    """Verificar relatorios gerados"""
    print("\nVERIFICANDO RELATORIOS...")
    
    diretorio_relatorios = Path("BIBLIOTECA_COSMICA_UNICA/RELATORIOS_MULTIVERSAIS")
    relatorios = list(diretorio_relatorios.glob("relatorio_*.json"))
    
    if relatorios:
        print(f"OK: {len(relatorios)} relatorio(s) encontrado(s)")
        return True
    else:
        print("FALHA: Nenhum relatorio encontrado")
        return False

def verificar_integridade_dados():
    """Verificar integridade dos dados"""
    print("\nVERIFICANDO INTEGRIDADE DOS DADOS...")
    
    diretorio_equacoes = Path("BIBLIOTECA_COSMICA_UNICA/EQUACOES_MULTIVERSAIS")
    problemas = 0
    
    for arquivo_json in diretorio_equacoes.glob("*.json"):
        try:
            with open(arquivo_json, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            # Verificar campos essenciais
            campos_obrigatorios = ["codigo", "titulo_simbolico", "estrutura_matematica", "validacao_ressonancia"]
            for campo in campos_obrigatorios:
                if campo not in dados:
                    print(f"FALHA: {arquivo_json} - campo {campo} faltando")
                    problemas += 1
                    break
            else:
                print(f"OK: {arquivo_json} - estrutura valida")
                
        except Exception as e:
            print(f"ERRO: {arquivo_json} - {e}")
            problemas += 1
    
    return problemas == 0

# EXECUTAR VERIFICACAO COMPLETA
print("INICIANDO VERIFICACAO DE INTEGRIDADE...\n")

estrutura_ok = verificar_estrutura()
equacoes_ok = verificar_equacoes()
relatorios_ok = verificar_relatorios()
dados_ok = verificar_integridade_dados()

print(f"\nRESULTADO FINAL:")
print(f"ESTRUTURA: {'OK' if estrutura_ok else 'FALHA'}")
print(f"EQUACOES: {len(equacoes_ok)}/4 encontradas")
print(f"RELATORIOS: {'OK' if relatorios_ok else 'FALHA'}")
print(f"DADOS: {'OK' if dados_ok else 'FALHA'}")

if estrutura_ok and len(equacoes_ok) == 4 and relatorios_ok and dados_ok:
    print("\nSTATUS: SISTEMA MULTIVERSAL 100% OPERACIONAL!")
    print("TODAS AS EQUACOES PROCESSADAS COM SUCESSO!")
else:
    print("\nSTATUS: ALGUNS AJUSTES NECESSARIOS")
    print("EXECUTE NOVAMENTE O PROCESSADOR COMPLETO")
