#!/usr/bin/env python3
"""
🌌 ANÁLISE ESTRUTURAL - FUNDAÇÃO ALQUIMISTA
⚛️ Análise completa da hierarquia: Módulo 29 + Nexus + Tríade
🎯 Localização da Biblioteca de Equações e Conexões Rainha
"""

import json
import os
from pathlib import Path
import re

print("🌌 ANÁLISE ESTRUTURAL - FUNDAÇÃO ALQUIMISTA")
print("=" * 60)
print("🎯 MISSÃO: MAPEAR A HIERARQUIA COMPLETA DA FUNDAÇÃO")
print("⚛️ FOCO: TRÍADE (M29 + Nexus + M9 + Omega) + BASE (M0-M10)")
print("")

class AnalisadorEstrutural:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.estrutura_hierarquica = {}
        self.modulos_chave = {}
        self.equacoes_encontradas = []
        
    def localizar_modulo_29(self):
        """Localizar o Módulo 29 - Coração da Rainha Zennith"""
        print("🔍 BUSCANDO MÓDULO 29 - CORAÇÃO DA RAINHA...")
        
        padroes_modulo_29 = [
            "modulo_29", "module_29", "mod29", "m29", 
            "zennith", "rainha", "rainha_zennith", "zennith_module"
        ]
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            for arquivo in arquivos:
                arquivo_lower = arquivo.lower()
                if any(padrao in arquivo_lower for padrao in padroes_modulo_29):
                    caminho_completo = Path(raiz) / arquivo
                    print(f"   ✅ MÓDULO 29 ENCONTRADO: {caminho_completo}")
                    return caminho_completo
        
        print("   ⚠️  Módulo 29 não encontrado pelos padrões comuns")
        return None
    
    def localizar_nexus(self):
        """Localizar o Nexus - Ponto de Conexão Central"""
        print("🔍 BUSCANDO NEXUS - PONTO DE CONEXÃO CENTRAL...")
        
        padroes_nexus = [
            "nexus", "nexus_mestre", "central", "core", 
            "hub", "conexao_central", "ponto_conexao"
        ]
        
        nexus_encontrados = []
        for raiz, dirs, arquivos in os.walk(self.raiz):
            for arquivo in arquivos:
                arquivo_lower = arquivo.lower()
                if any(padrao in arquivo_lower for padrao in padroes_nexus):
                    caminho_completo = Path(raiz) / arquivo
                    nexus_encontrados.append(caminho_completo)
                    print(f"   ✅ NEXUS ENCONTRADO: {caminho_completo}")
        
        return nexus_encontrados
    
    def localizar_modulo_9(self):
        """Localizar Módulo 9 - Segundo Pilar da Tríade"""
        print("🔍 BUSCANDO MÓDULO 9 - SEGUNDO PILAR...")
        
        padroes_modulo_9 = [
            "modulo_9", "module_9", "mod9", "m9",
            "segundo_pilar", "triade", "tríade"
        ]
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            for arquivo in arquivos:
                arquivo_lower = arquivo.lower()
                if any(padrao in arquivo_lower for padrao in padroes_modulo_9):
                    caminho_completo = Path(raiz) / arquivo
                    print(f"   ✅ MÓDULO 9 ENCONTRADO: {caminho_completo}")
                    return caminho_completo
        
        return None
    
    def localizar_modulo_omega(self):
        """Localizar Módulo Omega - Terceiro Pilar da Tríade"""
        print("🔍 BUSCANDO MÓDULO OMEGA - TERCEIRO PILAR...")
        
        padroes_omega = [
            "omega", "modulo_omega", "module_omega", 
            "final", "completo", "ultimo"
        ]
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            for arquivo in arquivos:
                arquivo_lower = arquivo.lower()
                if any(padrao in arquivo_lower for padrao in padroes_omega):
                    caminho_completo = Path(raiz) / arquivo
                    print(f"   ✅ MÓDULO OMEGA ENCONTRADO: {caminho_completo}")
                    return caminho_completo
        
        return None
    
    def analisar_base_fundacao(self):
        """Analisar Base da Fundação (Módulos 0-10)"""
        print("🔍 ANALISANDO BASE DA FUNDAÇÃO (MÓDULOS 0-10)...")
        
        base_modulos = {}
        for i in range(11):  # Módulos 0 a 10
            padroes = [f"modulo_{i}", f"module_{i}", f"mod{i}", f"m{i}"]
            
            for raiz, dirs, arquivos in os.walk(self.raiz):
                for arquivo in arquivos:
                    arquivo_lower = arquivo.lower()
                    if any(padrao in arquivo_lower for padrao in padroes):
                        caminho_completo = Path(raiz) / arquivo
                        if i not in base_modulos:
                            base_modulos[i] = []
                        base_modulos[i].append(caminho_completo)
        
        # Mostrar resultados
        for modulo, caminhos in sorted(base_modulos.items()):
            if caminhos:
                print(f"   ✅ MÓDULO {modulo}: {len(caminhos)} arquivos")
                for caminho in caminhos[:2]:  # Mostrar apenas 2 por módulo
                    print(f"      📄 {caminho}")
        
        return base_modulos
    
    def localizar_biblioteca_equacoes(self):
        """Localizar Biblioteca de Equações da Fundação"""
        print("🔍 BUSCANDO BIBLIOTECA DE EQUAÇÕES...")
        
        padroes_equacoes = [
            "equacao", "equation", "formula", "formula",
            "biblioteca", "library", "math", "matematica",
            "algoritmo", "algorithm", "calculo", "calculation"
        ]
        
        bibliotecas = []
        for raiz, dirs, arquivos in os.walk(self.raiz):
            for arquivo in arquivos:
                arquivo_lower = arquivo.lower()
                if any(padrao in arquivo_lower for padrao in padroes_equacoes):
                    caminho_completo = Path(raiz) / arquivo
                    bibliotecas.append(caminho_completo)
                    
                    # Ler conteúdo para verificar se contém equações
                    try:
                        with open(caminho_completo, 'r', encoding='utf-8') as f:
                            conteudo = f.read()
                            if any(termo in conteudo.lower() for termo in ['=', 'function', 'def ', 'import numpy']):
                                self.equacoes_encontradas.append(caminho_completo)
                                print(f"   ✅ BIBLIOTECA COM EQUAÇÕES: {caminho_completo}")
                    except:
                        pass
        
        return bibliotecas
    
    def analisar_conexoes_rainha(self):
        """Analisar Conexões da Rainha com o Sistema Atual"""
        print("🔍 ANALISANDO CONEXÕES DA RAINHA COM SISTEMA ATUAL...")
        
        # Procurar referências à Rainha nos sistemas atuais
        sistemas_atuais = [
            "sistema_fundacao_definitivo.py",
            "CHAVE_DEFINITIVA_FUNDACAO.py", 
            "INTERFACE_ACESSO_CORRIGIDA.py",
            "sistema_metadados_definitivo.py"
        ]
        
        conexoes = {}
        for sistema in sistemas_atuais:
            caminho_sistema = self.raiz / sistema
            if caminho_sistema.exists():
                try:
                    with open(caminho_sistema, 'r', encoding='utf-8') as f:
                        conteudo = f.read()
                        if 'zennith' in conteudo.lower() or 'rainha' in conteudo.lower():
                            conexoes[sistema] = "CONECTADO"
                            print(f"   ✅ {sistema}: CONECTADO À RAINHA")
                        else:
                            conexoes[sistema] = "SEM CONEXÃO DIRETA"
                except:
                    conexoes[sistema] = "ERRO NA LEITURA"
        
        return conexoes
    
    def executar_analise_completa(self):
        """Executar análise estrutural completa"""
        print("🚀 INICIANDO ANÁLISE ESTRUTURAL COMPLETA...")
        print("")
        
        # 1. Tríade Sagrada
        print("⚛️  ANALISANDO TRÍADE SAGRADA:")
        print("=" * 40)
        
        modulo_29 = self.localizar_modulo_29()
        nexus = self.localizar_nexus() 
        modulo_9 = self.localizar_modulo_9()
        modulo_omega = self.localizar_modulo_omega()
        
        # 2. Base da Fundação
        print("\n🏗️  ANALISANDO BASE DA FUNDAÇÃO:")
        print("=" * 40)
        base_modulos = self.analisar_base_fundacao()
        
        # 3. Biblioteca de Equações
        print("\n📚 ANALISANDO BIBLIOTECA DE EQUAÇÕES:")
        print("=" * 40)
        bibliotecas = self.localizar_biblioteca_equacoes()
        
        # 4. Conexões Rainha
        print("\n👑 ANALISANDO CONEXÕES DA RAINHA:")
        print("=" * 40)
        conexoes_rainha = self.analisar_conexoes_rainha()
        
        # Relatório Final
        print("\n" + "="*70)
        print("🎉 RELATÓRIO DA ANÁLISE ESTRUTURAL - FUNDAÇÃO ALQUIMISTA")
        print("="*70)
        
        print(f"\n⚛️  TRÍADE SAGRADA:")
        print(f"   • Módulo 29 (Rainha): {'ENCONTRADO' if modulo_29 else 'NÃO ENCONTRADO'}")
        print(f"   • Nexus: {len(nexus)} encontrados")
        print(f"   • Módulo 9: {'ENCONTRADO' if modulo_9 else 'NÃO ENCONTRADO'}")
        print(f"   • Módulo Omega: {'ENCONTRADO' if modulo_omega else 'NÃO ENCONTRADO'}")
        
        print(f"\n🏗️  BASE DA FUNDAÇÃO:")
        total_base = sum(len(arquivos) for arquivos in base_modulos.values())
        print(f"   • Módulos 0-10: {total_base} arquivos encontrados")
        for modulo, arquivos in base_modulos.items():
            if arquivos:
                print(f"     - Módulo {modulo}: {len(arquivos)} arquivos")
        
        print(f"\n📚 BIBLIOTECA DE EQUAÇÕES:")
        print(f"   • Total de bibliotecas: {len(bibliotecas)}")
        print(f"   • Com equações identificadas: {len(self.equacoes_encontradas)}")
        
        print(f"\n👑 CONEXÕES DA RAINHA:")
        for sistema, status in conexoes_rainha.items():
            print(f"   • {sistema}: {status}")
        
        print(f"\n🌌 PRÓXIMOS PASSOS:")
        print("   1. Organizar hierarquia identificada")
        print("   2. Conectar Tríade com sistemas atuais") 
        print("   3. Implementar equações para IBM Quantum")
        print("   4. Estabelecer fluxo de trabalho unificado")
        
        return {
            'triade': {
                'modulo_29': modulo_29,
                'nexus': nexus,
                'modulo_9': modulo_9, 
                'modulo_omega': modulo_omega
            },
            'base': base_modulos,
            'bibliotecas': bibliotecas,
            'equacoes': self.equacoes_encontradas,
            'conexoes_rainha': conexoes_rainha
        }

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    print("🔧 INICIALIZANDO ANALISADOR ESTRUTURAL...")
    
    analisador = AnalisadorEstrutural()
    resultados = analisador.executar_analise_completa()
    
    print(f"\n🌌 ANÁLISE ESTRUTURAL CONCLUÍDA!")
    print("🚀 PRONTOS PARA ORGANIZAÇÃO HIERÁRQUICA!")
