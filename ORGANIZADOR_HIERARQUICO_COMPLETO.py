#!/usr/bin/env python3
"""
🏗️ ORGANIZADOR HIERÁRQUICO COMPLETO - FUNDAÇÃO ALQUIMISTA
⚛️ Mapeamento, categorização e sequenciamento lógico de TODOS os scripts
🌌 Criação de fluxo de execução sistemático
"""

import os
import json
import subprocess
from pathlib import Path
import re
from datetime import datetime

print("🏗️ ORGANIZADOR HIERÁRQUICO COMPLETO - FUNDAÇÃO ALQUIMISTA")
print("=" * 70)
print("⚛️  MAPEAMENTO E SEQUENCIAMENTO LÓGICO DE 14.799 SCRIPTS")
print("")

class OrganizadorHierarquico:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.scripts_mapeados = {}
        self.sequencia_logica = []
        self.grupos_hierarquicos = {}
    
    def executar_mapeamento_completo(self):
        """Executar mapeamento completo de todos os scripts"""
        print("🔍 EXECUTANDO MAPEAMENTO COMPLETO...")
        
        categorias_detalhadas = {
            'configuracao_sistema': [],
            'circuitos_basicos': [],
            'testes_emaranhamento': [],
            'protocolos_avancados': [],
            'algoritmos_complexos': [],
            'interface_usuario': [],
            'analise_dados': [],
            'modulos_rainha': [],
            'scripts_manutencao': [],
            'backup_restore': [],
            'documentacao': [],
            'outros': []
        }
        
        total_encontrados = 0
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            # Ignorar diretórios de sistema
            dirs[:] = [d for d in dirs if d not in ['node_modules', '__pycache__', '.git', '.vscode']]
            
            for arquivo in arquivos:
                if self._e_script_executavel(arquivo):
                    total_encontrados += 1
                    caminho_completo = Path(raiz) / arquivo
                    
                    info_script = self._analisar_script_completo(caminho_completo)
                    categoria = self._determinar_categoria_detalhada(info_script)
                    
                    categorias_detalhadas[categoria].append(info_script)
        
        print(f"   📊 TOTAL DE SCRIPTS MAPEADOS: {total_encontrados}")
        
        # Mostrar distribuição
        for categoria, scripts in categorias_detalhadas.items():
            if scripts:
                print(f"   📁 {categoria.upper():25}: {len(scripts)} scripts")
        
        self.scripts_mapeados = categorias_detalhadas
        return categorias_detalhadas
    
    def _e_script_executavel(self, nome_arquivo):
        """Verificar se é script executável"""
        extensoes = ['.py', '.sh', '.js', '.rb', '.pl', '.r', '.php']
        return any(nome_arquivo.endswith(ext) for ext in extensoes)
    
    def _analisar_script_completo(self, caminho):
        """Analisar script de forma completa"""
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                conteudo = f.read()
        except:
            conteudo = ""
        
        info = {
            'caminho': str(caminho),
            'nome': caminho.name,
            'diretorio': str(caminho.parent),
            'extensao': caminho.suffix,
            'tamanho_bytes': len(conteudo),
            'linhas': conteudo.count('\n') + 1,
            'dependencias': self._extrair_dependencias(conteudo),
            'funcoes': self._extrair_funcoes(conteudo, caminho.suffix),
            'complexidade': self._calcular_complexidade(conteudo),
            'descricao': self._extrair_descricao(conteudo),
            'timestamp_criacao': self._obter_timestamp(caminho)
        }
        
        return info
    
    def _extrair_dependencias(self, conteudo):
        """Extrair dependências do script"""
        dependencias = []
        
        # Dependências quânticas
        quanticas = ['qiskit', 'qiskit-ibm-runtime', 'qiskit-aer', 'cirq', 'pennylane']
        # Dependências científicas
        cientificas = ['numpy', 'scipy', 'matplotlib', 'pandas', 'tensorflow', 'pytorch']
        # Dependências gerais
        gerais = ['requests', 'flask', 'django', 'fastapi', 'sqlalchemy']
        
        todas_deps = quanticas + cientificas + gerais
        
        for dep in todas_deps:
            if dep in conteudo.lower():
                dependencias.append(dep)
        
        return list(set(dependencias))[:10]
    
    def _extrair_funcoes(self, conteudo, extensao):
        """Extrair funções do script"""
        funcoes = []
        
        if extensao == '.py':
            padrao = r'^(?:async\s+)?def\s+(\w+)\s*\('
            matches = re.findall(padrao, conteudo, re.MULTILINE)
            funcoes.extend(matches)
        
        return funcoes[:15]
    
    def _calcular_complexidade(self, conteudo):
        """Calcular complexidade do script"""
        linhas = len(conteudo.split('\n'))
        funcoes = len(re.findall(r'^def\s+\w+', conteudo, re.MULTILINE))
        classes = len(re.findall(r'^class\s+\w+', conteudo, re.MULTILINE))
        
        if linhas < 30:
            return 'MUITO_BAIXA'
        elif linhas < 100:
            return 'BAIXA'
        elif linhas < 300:
            return 'MEDIA'
        elif linhas < 500:
            return 'ALTA'
        else:
            return 'MUITO_ALTA'
    
    def _extrair_descricao(self, conteudo):
        """Extrair descrição do script"""
        # Buscar docstring ou comentário inicial
        padrao_docstring = r'\"\"\"(.*?)\"\"\"'
        match = re.search(padrao_docstring, conteudo, re.DOTALL)
        if match:
            return match.group(1).strip()[:200]
        
        # Buscar comentários iniciais
        linhas = conteudo.split('\n')
        comentarios = []
        for linha in linhas[:10]:
            if linha.strip().startswith('#'):
                comentarios.append(linha.strip()[1:].strip())
        
        return ' | '.join(comentarios[:3]) if comentarios else "Sem descrição"
    
    def _obter_timestamp(self, caminho):
        """Obter timestamp de criação"""
        try:
            stat = caminho.stat()
            return datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        except:
            return "Desconhecido"
    
    def _determinar_categoria_detalhada(self, info_script):
        """Determinar categoria detalhada do script"""
        nome = info_script['nome'].lower()
        caminho = info_script['caminho'].lower()
        descricao = info_script['descricao'].lower()
        
        # Verificar categorias em ordem de prioridade
        if any(termo in nome or termo in caminho for termo in ['config', 'setup', 'install', 'ambiente']):
            return 'configuracao_sistema'
        elif any(termo in nome or termo in descricao for termo in ['circuit', 'qubit', 'quantum', 'bell', 'psi', 'phi']):
            if any(termo in nome for termo in ['test', 'verify', 'valid']):
                return 'testes_emaranhamento'
            elif any(termo in nome for termo in ['teleport', 'algoritmo', 'protocol']):
                return 'protocolos_avancados'
            else:
                return 'circuitos_basicos'
        elif any(termo in nome for termo in ['algoritmo', 'algorithm', 'complex']):
            return 'algoritmos_complexos'
        elif any(termo in nome for termo in ['interface', 'web', 'frontend', 'ui', 'html']):
            return 'interface_usuario'
        elif any(termo in nome for termo in ['analise', 'analysis', 'data', 'dados', 'metric']):
            return 'analise_dados'
        elif any(termo in nome or termo in caminho for termo in ['zennith', 'rainha', 'modulo', 'm29']):
            return 'modulos_rainha'
        elif any(termo in nome for termo in ['backup', 'restore', 'recovery']):
            return 'backup_restore'
        elif any(termo in nome for termo in ['doc', 'readme', 'manual', 'guide']):
            return 'documentacao'
        elif any(termo in nome for termo in ['clean', 'maintenance', 'optimize', 'organize']):
            return 'scripts_manutencao'
        else:
            return 'outros'
    
    def criar_sequencia_logica_execucao(self):
        """Criar sequência lógica de execução"""
        print("\n🔧 CRIANDO SEQUÊNCIA LÓGICA DE EXECUÇÃO...")
        
        sequencia = []
        
        # FASE 1: CONFIGURAÇÃO E PREPARAÇÃO
        sequencia.extend(self._selecionar_scripts_fase(
            self.scripts_mapeados['configuracao_sistema'],
            'CONFIGURAÇÃO DO SISTEMA',
            limite=5
        ))
        
        # FASE 2: CIRCUITOS BÁSICOS
        sequencia.extend(self._selecionar_scripts_fase(
            self.scripts_mapeados['circuitos_basicos'],
            'CIRCUITOS BÁSICOS - ESTADOS BELL',
            limite=10
        ))
        
        # FASE 3: TESTES DE EMARANHAMENTO
        sequencia.extend(self._selecionar_scripts_fase(
            self.scripts_mapeados['testes_emaranhamento'],
            'VERIFICAÇÃO DE EMARANHAMENTO',
            limite=5
        ))
        
        # FASE 4: PROTOCOLOS AVANÇADOS
        sequencia.extend(self._selecionar_scripts_fase(
            self.scripts_mapeados['protocolos_avancados'],
            'PROTOCOLOS QUÂNTICOS AVANÇADOS',
            limite=8
        ))
        
        # FASE 5: ALGORITMOS COMPLEXOS
        sequencia.extend(self._selecionar_scripts_fase(
            self.scripts_mapeados['algoritmos_complexos'],
            'ALGORITMOS QUÂNTICOS COMPLEXOS',
            limite=7
        ))
        
        # FASE 6: MÓDULOS RAINHA
        sequencia.extend(self._selecionar_scripts_fase(
            self.scripts_mapeados['modulos_rainha'],
            'MÓDULOS RAINHA ZENNITH',
            limite=6
        ))
        
        # FASE 7: ANÁLISE E OTIMIZAÇÃO
        sequencia.extend(self._selecionar_scripts_fase(
            self.scripts_mapeados['analise_dados'],
            'ANÁLISE E OTIMIZAÇÃO',
            limite=4
        ))
        
        self.sequencia_logica = sequencia
        return sequencia
    
    def _selecionar_scripts_fase(self, scripts, nome_fase, limite=5):
        """Selecionar scripts para uma fase específica"""
        if not scripts:
            return []
        
        # Ordenar por complexidade e tamanho
        scripts_ordenados = sorted(scripts, 
                                 key=lambda x: (x['complexidade'] != 'MUITO_BAIXA', 
                                               x['linhas']), 
                                 reverse=True)
        
        selecionados = scripts_ordenados[:limite]
        
        fase = {
            'nome_fase': nome_fase,
            'scripts': selecionados,
            'total_scripts': len(selecionados)
        }
        
        print(f"   📋 {nome_fase}: {len(selecionados)} scripts selecionados")
        for script in selecionados[:3]:
            print(f"      • {script['nome']} ({script['complexidade']})")
        
        return [fase]
    
    def gerar_relatorio_hierarquico(self):
        """Gerar relatório hierárquico completo"""
        print(f"\n{'='*80}")
        print("🏗️ RELATÓRIO HIERÁRQUICO COMPLETO - FUNDAÇÃO ALQUIMISTA")
        print(f"{'='*80}")
        
        total_scripts = sum(len(scripts) for scripts in self.scripts_mapeados.values())
        
        print(f"\n📊 VISÃO GERAL DO SISTEMA:")
        print(f"   • Total de scripts mapeados: {total_scripts}")
        print(f"   • Sequências lógicas criadas: {len(self.sequencia_logica)} fases")
        
        print(f"\n📁 DISTRIBUIÇÃO DETALHADA:")
        for categoria, scripts in self.scripts_mapeados.items():
            if scripts:
                total_linhas = sum(s['linhas'] for s in scripts)
                print(f"   • {categoria.replace('_', ' ').title():25}: {len(scripts):4} scripts | {total_linhas:6} linhas")
        
        print(f"\n�� SEQUÊNCIA LÓGICA DE EXECUÇÃO:")
        for i, fase in enumerate(self.sequencia_logica, 1):
            print(f"\n   🔷 FASE {i}: {fase['nome_fase']}")
            for script in fase['scripts']:
                status = "✅" if script['complexidade'] in ['BAIXA', 'MUITO_BAIXA'] else "⚠️"
                print(f"      {status} {script['nome']:40} | {script['linhas']:4} linhas | {script['complexidade']:12}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS:")
        print("   1. 🎯 EXECUTAR SEQUÊNCIA LÓGICA FASE POR FASE")
        print("   2. 📊 VALIDAR RESULTADOS DE CADA FASE")
        print("   3. 🔄 OTIMIZAR SCRIPTS COM PROBLEMAS")
        print("   4. 🌌 INTEGRAR COM IBM QUANTUM")
        print("   5. 📈 IMPLEMENTAR MONITORAMENTO CONTÍNUO")
        
        return {
            'total_scripts': total_scripts,
            'fases_sequencia': len(self.sequencia_logica),
            'scripts_por_fase': [fase['total_scripts'] for fase in self.sequencia_logica]
        }
    
    def criar_scripts_execucao_automatica(self):
        """Criar scripts de execução automática para cada fase"""
        print("\n🔄 CRIANDO SCRIPTS DE EXECUÇÃO AUTOMÁTICA...")
        
        for i, fase in enumerate(self.sequencia_logica, 1):
            nome_script = f"executar_fase_{i:02d}.sh"
            caminho_script = self.raiz / nome_script
            
            with open(caminho_script, 'w') as f:
                f.write("#!/bin/bash\n")
                f.write(f"# 🚀 EXECUTOR DA FASE {i}: {fase['nome_fase']}\n")
                f.write(f"# 📅 Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"# 📊 Scripts: {len(fase['scripts'])}\n")
                f.write("echo \"🚀 INICIANDO FASE $1...\"\n\n")
                
                for script in fase['scripts']:
                    if script['extensao'] == '.py':
                        f.write(f"echo \"🎯 Executando: {script['nome']}\"\n")
                        f.write(f"python3 \"{script['caminho']}\"\n")
                        f.write("if [ $? -eq 0 ]; then\n")
                        f.write("    echo \"✅ SUCESSO: {script['nome']}\"\n")
                        f.write("else\n")
                        f.write("    echo \"❌ FALHA: {script['nome']}\"\n")
                        f.write("    exit 1\n")
                        f.write("fi\n")
                        f.write("echo \"\"\n")
                
                f.write(f"echo \"🎉 FASE {i} CONCLUÍDA COM SUCESSO!\"\n")
            
            # Tornar executável
            caminho_script.chmod(0o755)
            print(f"   ✅ {nome_script} criado com {len(fase['scripts'])} scripts")
        
        # Criar script mestre
        self._criar_script_mestre_execucao()
    
    def _criar_script_mestre_execucao(self):
        """Criar script mestre para execução de todas as fases"""
        caminho_mestre = self.raiz / "EXECUTAR_SEQUENCIA_COMPLETA.sh"
        
        with open(caminho_mestre, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write("# 🚀 EXECUTOR DA SEQUÊNCIA COMPLETA - FUNDAÇÃO ALQUIMISTA\n")
            f.write("# 🌌 Execução hierárquica de todas as fases\n")
            f.write(f"# 📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("echo \"🌌 INICIANDO SEQUÊNCIA COMPLETA DA FUNDAÇÃO ALQUIMISTA\"\n")
            f.write("echo \"====================================================\"\n\n")
            
            for i in range(1, len(self.sequencia_logica) + 1):
                f.write(f"# FASE {i}: {self.sequencia_logica[i-1]['nome_fase']}\n")
                f.write(f"./executar_fase_{i:02d}.sh\n")
                f.write("if [ $? -ne 0 ]; then\n")
                f.write(f'    echo \"❌ FALHA NA FASE {i}. ABORTANDO EXECUÇÃO.\"\n')
                f.write("    exit 1\n")
                f.write("fi\n")
                f.write("echo \"\"\n")
            
            f.write('echo \"🎉 SEQUÊNCIA COMPLETA EXECUTADA COM SUCESSO!\"\n')
            f.write('echo \"🌌 FUNDAÇÃO ALQUIMISTA OPERACIONAL!\"\n')
        
        caminho_mestre.chmod(0o755)
        print(f"   ✅ EXECUTAR_SEQUENCIA_COMPLETA.sh criado")

# EXECUÇÃO PRINCIPAL
def main():
    organizador = OrganizadorHierarquico()
    
    # 1. Mapeamento completo
    scripts_mapeados = organizador.executar_mapeamento_completo()
    
    # 2. Criar sequência lógica
    sequencia_logica = organizador.criar_sequencia_logica_execucao()
    
    # 3. Gerar relatório
    relatorio = organizador.gerar_relatorio_hierarquico()
    
    # 4. Criar scripts de execução automática
    organizador.criar_scripts_execucao_automatica()
    
    print(f"\n🏗️ ORGANIZAÇÃO HIERÁRQUICA CONCLUÍDA!")
    print(f"📊 {relatorio['total_scripts']} scripts organizados em {relatorio['fases_sequencia']} fases lógicas!")
    print("🚀 SISTEMA PRONTO PARA EXECUÇÃO SEQUENCIAL!")

if __name__ == "__main__":
    main()
