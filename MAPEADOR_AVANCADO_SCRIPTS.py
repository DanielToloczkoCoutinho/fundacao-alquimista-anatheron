#!/usr/bin/env python3
"""
🗺️ MAPEADOR AVANÇADO DE SCRIPTS - FUNDAÇÃO ALQUIMISTA
⚛️ Mapeamento detalhado de TODOS os scripts existentes
🌌 Análise de dependências e relações
"""

import os
import json
from pathlib import Path
import re

print("🗺️ MAPEADOR AVANÇADO DE SCRIPTS - FUNDAÇÃO ALQUIMISTA")
print("=" * 65)
print("⚛️  MAPEAMENTO COMPLETO E ANÁLISE DE DEPENDÊNCIAS")
print("")

class MapeadorAvancadoScripts:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.mapeamento_completo = {}
    
    def executar_mapeamento_exaustivo(self):
        """Executar mapeamento exaustivo de todos os scripts"""
        print("🔍 EXECUTANDO MAPEAMENTO EXAUSTIVO...")
        
        categorias = {
            'scripts_quanticos': [],
            'scripts_configuracao': [],
            'scripts_interface': [],
            'scripts_analise': [],
            'scripts_rainha': [],
            'scripts_desenvolvimento': [],
            'scripts_testes': [],
            'outros_scripts': []
        }
        
        total_arquivos = 0
        total_scripts = 0
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            # Ignorar diretórios de sistema
            dirs_ignorar = ['node_modules', '__pycache__', '.git', '.vscode']
            dirs[:] = [d for d in dirs if d not in dirs_ignorar]
            
            for arquivo in arquivos:
                total_arquivos += 1
                caminho_completo = Path(raiz) / arquivo
                
                # Verificar se é script executável
                if self._e_script_executavel(arquivo):
                    total_scripts += 1
                    info_script = self._analisar_script_detalhado(caminho_completo)
                    
                    # Categorizar
                    categoria = self._determinar_categoria_avancada(info_script)
                    categorias[categoria].append(info_script)
        
        # Mostrar relatório do mapeamento
        print(f"\n📊 ESTATÍSTICAS DO MAPEAMENTO:")
        print(f"   • Total de arquivos analisados: {total_arquivos}")
        print(f"   • Total de scripts identificados: {total_scripts}")
        print(f"   • Taxa de scripts: {(total_scripts/total_arquivos)*100:.1f}%")
        
        print(f"\n📁 DISTRIBUIÇÃO POR CATEGORIA:")
        for categoria, scripts in categorias.items():
            if scripts:
                print(f"   • {categoria.replace('_', ' ').title():25}: {len(scripts)} scripts")
        
        return categorias
    
    def _e_script_executavel(self, nome_arquivo):
        """Verificar se o arquivo é um script executável"""
        extensoes_scripts = ['.py', '.sh', '.js', '.rb', '.pl', '.php', '.r']
        return any(nome_arquivo.endswith(ext) for ext in extensoes_scripts)
    
    def _analisar_script_detalhado(self, caminho):
        """Analisar script de forma detalhada"""
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                conteudo = f.read()
        except:
            conteudo = ""
        
        info = {
            'caminho': str(caminho),
            'nome': caminho.name,
            'extensao': caminho.suffix,
            'tamanho_bytes': len(conteudo),
            'linhas': conteudo.count('\n') + 1,
            'diretorio': str(caminho.parent),
            'imports': self._extrair_imports(conteudo, caminho.suffix),
            'funcoes': self._extrair_funcoes(conteudo, caminho.suffix),
            'dependencias': self._identificar_dependencias(conteudo),
            'complexidade': self._estimar_complexidade(conteudo)
        }
        
        return info
    
    def _extrair_imports(self, conteudo, extensao):
        """Extrair imports do script"""
        imports = []
        
        if extensao == '.py':
            # Padrão para imports Python
            padrao = r'^(import\s+[\w\.]+|from\s+[\w\.]+\s+import\s+[\w\*, ]+)'
            for linha in conteudo.split('\n'):
                match = re.match(padrao, linha.strip())
                if match:
                    imports.append(match.group(1))
        
        return imports[:10]  # Limitar a 10 imports
    
    def _extrair_funcoes(self, conteudo, extensao):
        """Extrair funções do script"""
        funcoes = []
        
        if extensao == '.py':
            # Padrão para def Python
            padrao = r'^def\s+(\w+)\s*\('
            for linha in conteudo.split('\n'):
                match = re.search(padrao, linha)
                if match:
                    funcoes.append(match.group(1))
        
        return funcoes[:10]  # Limitar a 10 funções
    
    def _identificar_dependencias(self, conteudo):
        """Identificar dependências do script"""
        dependencias = []
        
        # Verificar dependências comuns
        bibliotecas_quanticas = ['qiskit', 'qiskit-ibm-runtime', 'qiskit-aer', 'cirq', 'pennylane']
        bibliotecas_cientificas = ['numpy', 'scipy', 'matplotlib', 'pandas', 'tensorflow', 'pytorch']
        
        for lib in bibliotecas_quanticas + bibliotecas_cientificas:
            if lib in conteudo.lower():
                dependencias.append(lib)
        
        return dependencias
    
    def _estimar_complexidade(self, conteudo):
        """Estimar complexidade do script"""
        linhas = len(conteudo.split('\n'))
        funcoes = len(re.findall(r'^def\s+\w+', conteudo, re.MULTILINE))
        classes = len(re.findall(r'^class\s+\w+', conteudo, re.MULTILINE))
        
        if linhas < 50:
            return 'baixa'
        elif linhas < 200:
            return 'media'
        else:
            return 'alta'
    
    def _determinar_categoria_avancada(self, info_script):
        """Determinar categoria avançada do script"""
        nome = info_script['nome'].lower()
        conteudo = open(info_script['caminho'], 'r').read().lower() if os.path.exists(info_script['caminho']) else ""
        
        # Verificar categorias específicas
        if any(termo in nome for termo in ['quant', 'qiskit', 'circuit', 'qubit']):
            return 'scripts_quanticos'
        elif any(termo in nome for termo in ['config', 'setup', 'install', 'ambiente']):
            return 'scripts_configuracao'
        elif any(termo in nome for termo in ['interface', 'web', 'frontend', 'ui']):
            return 'scripts_interface'
        elif any(termo in nome for termo in ['analise', 'analysis', 'data', 'dados']):
            return 'scripts_analise'
        elif any(termo in nome for termo in ['zennith', 'rainha', 'modulo', 'm29']):
            return 'scripts_rainha'
        elif any(termo in nome for termo in ['test', 'teste', 'verify', 'valid']):
            return 'scripts_testes'
        elif any(termo in nome for termo in ['dev', 'develop', 'code', 'script']):
            return 'scripts_desenvolvimento'
        else:
            return 'outros_scripts'
    
    def gerar_relatorio_estrutural(self, categorias):
        """Gerar relatório estrutural completo"""
        print(f"\n{'='*80}")
        print("🏗️ RELATÓRIO ESTRUTURAL - MAPEAMENTO AVANÇADO")
        print(f"{'='*80}")
        
        # Análise por categoria
        for categoria, scripts in categorias.items():
            if scripts:
                print(f"\n📊 {categoria.upper().replace('_', ' ')}:")
                print(f"   • Quantidade: {len(scripts)} scripts")
                
                # Estatísticas da categoria
                total_linhas = sum(s['linhas'] for s in scripts)
                media_linhas = total_linhas / len(scripts)
                scripts_complexos = sum(1 for s in scripts if s['complexidade'] == 'alta')
                
                print(f"   • Total de linhas: {total_linhas}")
                print(f"   • Média de linhas: {media_linhas:.1f}")
                print(f"   • Scripts complexos: {scripts_complexos}")
                
                # Principais scripts da categoria
                print(f"   • Principais scripts:")
                scripts_ordenados = sorted(scripts, key=lambda x: x['linhas'], reverse=True)
                for script in scripts_ordenados[:3]:
                    print(f"      ↳ {script['nome']} ({script['linhas']} linhas, {script['complexidade']})")
        
        # Análise geral
        todos_scripts = [script for scripts in categorias.values() for script in scripts]
        total_geral_linhas = sum(s['linhas'] for s in todos_scripts)
        
        print(f"\n🌌 VISÃO GERAL DO SISTEMA:")
        print(f"   • Total de scripts: {len(todos_scripts)}")
        print(f"   • Total de linhas de código: {total_geral_linhas}")
        print(f"   • Média de linhas por script: {total_geral_linhas/len(todos_scripts):.1f}")
        
        # Scripts mais importantes
        print(f"\n🎯 SCRIPTS MAIS RELEVANTES:")
        scripts_importantes = sorted(todos_scripts, key=lambda x: x['linhas'], reverse=True)[:5]
        for i, script in enumerate(scripts_importantes, 1):
            print(f"   {i}. {script['nome']}")
            print(f"      📍 {script['caminho']}")
            print(f"      📏 {script['linhas']} linhas | 🏷️ {script['complexidade']}")
            if script['dependencias']:
                print(f"      📦 Dependências: {', '.join(script['dependencias'][:3])}")
        
        return {
            'total_scripts': len(todos_scripts),
            'total_linhas': total_geral_linhas,
            'scripts_principais': scripts_importantes
        }

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    mapeador = MapeadorAvancadoScripts()
    
    # Executar mapeamento exaustivo
    categorias = mapeador.executar_mapeamento_exaustivo()
    
    # Gerar relatório estrutural
    relatorio = mapeador.gerar_relatorio_estrutural(categorias)
    
    print(f"\n🗺️ MAPEAMENTO AVANÇADO CONCLUÍDO!")
    print(f"📊 {relatorio['total_scripts']} scripts mapeados com {relatorio['total_linhas']} linhas de código!")
    print("🌌 SISTEMA COMPLETAMENTE DOCUMENTADO!")
