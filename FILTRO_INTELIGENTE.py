#!/usr/bin/env python3
"""
🎯 FILTRO INTELIGENTE - FUNDAÇÃO ALQUIMISTA
⚛️ Sistema avançado de filtragem para 590 laboratórios
🌌 Foco em: Módulos Rainha, Equações Reais, Hierarquia Estrutural
"""

import os
import re
from pathlib import Path

print("🎯 FILTRO INTELIGENTE - FUNDAÇÃO ALQUIMISTA")
print("=" * 60)
print("⚛️  FILTRANDO 590 LABORATÓRIOS PARA ENCONTRAR OS ESSENCIAIS")
print("🌌 FOCO: MÓDULOS RAINHA, EQUAÇÕES REAIS, HIERARQUIA")
print("")

class FiltroInteligente:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.resultados_filtrados = {
            'modulos_rainha': [],
            'equacoes_reais': [],
            'laboratorios_quanticos_essenciais': [],
            'nexus_conexoes': [],
            'hierarquia_estrutural': []
        }
    
    def filtrar_modulos_rainha(self):
        """Filtrar módulos da Rainha com padrões inteligentes"""
        print("🔍 FILTRANDO MÓDULOS RAINHA (padrões múltiplos)...")
        
        # Padrões INTELIGENTES para módulos Rainha
        padroes_modulos = [
            # Padrão 1: modulo-9, modulo_9, mod9, m9
            r'.*(modulo[-_]?9|mod9|m9).*',
            # Padrão 2: modulo-29, modulo_29, mod29, m29  
            r'.*(modulo[-_]?29|mod29|m29).*',
            # Padrão 3: zennith, rainha
            r'.*(zennith|rainha).*',
            # Padrão 4: omega
            r'.*omega.*',
            # Padrão 5: nexus
            r'.*nexus.*'
        ]
        
        modulos_encontrados = []
        for raiz, dirs, arquivos in os.walk(self.raiz):
            for item in dirs + arquivos:
                item_path = Path(raiz) / item
                
                # Verificar TODOS os padrões
                for padrao in padroes_modulos:
                    if re.match(padrao, item, re.IGNORECASE):
                        modulos_encontrados.append(item_path)
                        print(f"   ✅ MÓDULO ENCONTRADO: {item_path}")
                        break  # Evitar duplicatas
        
        return modulos_encontrados
    
    def filtrar_equacoes_reais(self):
        """Filtrar equações REAIS (não bibliotecas node_modules)"""
        print("🔍 FILTRANDO EQUAÇÕES REAIS (excluindo node_modules)...")
        
        # Extensões de arquivos com equações reais
        extensoes_equacoes = ['.py', '.js', '.ts', '.md', '.txt', '.json']
        
        equacoes_reais = []
        for raiz, dirs, arquivos in os.walk(self.raiz):
            # PULAR node_modules - isso elimina 90% do ruído!
            if 'node_modules' in raiz:
                continue
                
            for arquivo in arquivos:
                if any(arquivo.endswith(ext) for ext in extensoes_equacoes):
                    caminho_completo = Path(raiz) / arquivo
                    
                    # Ler conteúdo para verificar se tem equações REAIS
                    try:
                        with open(caminho_completo, 'r', encoding='utf-8') as f:
                            conteudo = f.read()
                            
                        # Verificar se tem equações matemáticas ou código quântico
                        if self.contem_equacoes_reais(conteudo):
                            equacoes_reais.append(caminho_completo)
                            print(f"   ✅ EQUAÇÃO REAL: {caminho_completo}")
                    except:
                        pass
        
        return equacoes_reais
    
    def contem_equacoes_reais(self, conteudo):
        """Verificar se o conteúdo contém equações REAIS"""
        indicadores_equacoes = [
            'import numpy', 'import math', 'def ', 'class ',
            'QuantumCircuit', 'qiskit', 'AerSimulator',
            'np.', 'math.', '= lambda', 'return '
        ]
        
        # Verificar múltiplos indicadores
        indicadores_encontrados = sum(1 for indicador in indicadores_equacoes 
                                    if indicador in conteudo)
        
        return indicadores_encontrados >= 2  # Pelo menos 2 indicadores
    
    def filtrar_laboratorios_quanticos_essenciais(self):
        """Filtrar laboratórios quânticos ESSENCIAIS"""
        print("🔍 FILTRANDO LABORATÓRIOS QUÂNTICOS ESSENCIAIS...")
        
        laboratorios_essenciais = []
        
        # Procurar nos diretórios PRINCIPAIS (não em node_modules)
        diretorios_principais = ['laboratorios', 'scripts', 'src', 'app', '.']
        
        for dir_principal in diretorios_principais:
            dir_path = self.raiz / dir_principal
            if dir_path.exists():
                for item in dir_path.rglob('*'):
                    if item.is_file():
                        nome_lower = item.name.lower()
                        
                        # Verificar se é laboratório quântico ESSENCIAL
                        if self.e_laboratorio_quantico_essencial(item):
                            laboratorios_essenciais.append(item)
                            print(f"   ✅ LAB QUÂNTICO ESSENCIAL: {item}")
        
        return laboratorios_essenciais
    
    def e_laboratorio_quantico_essencial(self, caminho):
        """Verificar se é um laboratório quântico ESSENCIAL"""
        nome = caminho.name.lower()
        
        # Padrões de laboratórios quânticos ESSENCIAIS
        padroes_essenciais = [
            'quant', 'qiskit', 'quantum', 'circuit', 'qubit',
            'bell', 'teleport', 'algoritmo', 'algorithm',
            'simulacao', 'simulation', 'experiment', 'teste'
        ]
        
        # Verificar se contém padrões essenciais E não está em node_modules
        return (any(padrao in nome for padrao in padroes_essenciais) 
                and 'node_modules' not in str(caminho))
    
    def filtrar_nexus_conexoes(self):
        """Filtrar conexões de Nexus e pontos centrais"""
        print("🔍 FILTRANDO NEXUS E CONEXÕES CENTRAIS...")
        
        nexus_conexoes = []
        
        # Procurar arquivos de conexão e configuração
        padroes_nexus = [
            'nexus', 'conexao', 'connection', 'hub', 'central',
            'config', 'configuration', 'setup', 'organizacao'
        ]
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            if 'node_modules' in raiz:
                continue
                
            for arquivo in arquivos:
                arquivo_lower = arquivo.lower()
                if any(padrao in arquivo_lower for padrao in padroes_nexus):
                    caminho = Path(raiz) / arquivo
                    nexus_conexoes.append(caminho)
                    print(f"   ✅ NEXUS/CONEXÃO: {caminho}")
        
        return nexus_conexoes
    
    def executar_filtragem_inteligente(self):
        """Executar filtragem inteligente completa"""
        print("🚀 INICIANDO FILTRAGEM INTELIGENTE COMPLETA...")
        print("💡 Eliminando ruído (node_modules, arquivos irrelevantes)")
        print("")
        
        # Executar todos os filtros
        self.resultados_filtrados['modulos_rainha'] = self.filtrar_modulos_rainha()
        self.resultados_filtrados['equacoes_reais'] = self.filtrar_equacoes_reais()
        self.resultados_filtrados['laboratorios_quanticos_essenciais'] = self.filtrar_laboratorios_quanticos_essenciais()
        self.resultados_filtrados['nexus_conexoes'] = self.filtrar_nexus_conexoes()
        
        # Relatório Final FILTRADO
        print("\n" + "="*70)
        print("🎉 RELATÓRIO FILTRADO - FUNDAÇÃO ALQUIMISTA")
        print("="*70)
        
        total_filtrado = sum(len(items) for items in self.resultados_filtrados.values())
        print(f"\n�� RESUMO FILTRADO (eliminando ruído):")
        print(f"   • De 590 laboratórios para {total_filtrado} ESSENCIAIS")
        print(f"   • Redução de {((590 - total_filtrado) / 590 * 100):.1f}% de ruído")
        
        print(f"\n🎯 CATEGORIAS ESSENCIAIS IDENTIFICADAS:")
        for categoria, itens in self.resultados_filtrados.items():
            print(f"   • {categoria.upper():30} : {len(itens):3d} itens")
        
        print(f"\n🌌 PRINCIPAIS DESCOBERTAS FILTRADAS:")
        
        # Mostrar exemplos de cada categoria
        for categoria, itens in self.resultados_filtrados.items():
            if itens:
                print(f"\n   📁 {categoria.upper()}:")
                for item in itens[:3]:  # Mostrar apenas 3 por categoria
                    print(f"      • {item.name}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS COM DADOS FILTRADOS:")
        print("   1. Organizar hierarquia com dados limpos")
        print("   2. Conectar módulos Rainha identificados")
        print("   3. Implementar equações reais para IBM Quantum")
        print("   4. Estabelecer fluxo com laboratórios essenciais")
        
        return self.resultados_filtrados

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    filtro = FiltroInteligente()
    resultados = filtro.executar_filtragem_inteligente()
    
    print(f"\n🎯 FILTRAGEM INTELIGENTE CONCLUÍDA!")
    print(f"🌌 {sum(len(items) for items in resultados.values())} itens ESSENCIAIS identificados!")
