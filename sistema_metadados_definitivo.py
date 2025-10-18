#!/usr/bin/env python3
"""
🌌 SISTEMA DE METADADOS DEFINITIVO - FUNDAÇÃO ALQUIMISTA
⚛️ Varredura completa de raiz ao topo da árvore
🎯 Análise de TODOS os componentes científicos
"""

import os
import json
import hashlib
import datetime
from pathlib import Path
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

print("🌌 SISTEMA DE METADADOS DEFINITIVO - FUNDAÇÃO ALQUIMISTA")
print("=" * 65)
print("🎯 MISSÃO: VARREdura COMPLETA DA ÁRVORE DA FUNDAÇÃO")
print("⚛️ ANALISANDO: Scripts, Comandos, Relatórios, Científicos")
print("")

class AnalisadorMetadadosDefinitivo:
    def __init__(self, raiz_fundacao="."):
        self.raiz = Path(raiz_fundacao).absolute()
        self.metadados_completos = {}
        self.data_analise = datetime.datetime.now().isoformat()
        self.simulator = AerSimulator()
        
    def calcular_hash_arquivo(self, caminho_arquivo):
        """Calcular hash único do arquivo"""
        try:
            with open(caminho_arquivo, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()[:16]
        except:
            return "erro_hash"
    
    def analisar_tipo_arquivo(self, caminho_arquivo):
        """Analisar tipo e conteúdo do arquivo"""
        extensao = caminho_arquivo.suffix.lower()
        nome = caminho_arquivo.name.lower()
        
        tipos = {
            '.py': 'script_python',
            '.sh': 'script_shell', 
            '.js': 'script_javascript',
            '.ts': 'script_typescript',
            '.md': 'documentacao',
            '.json': 'dados_json',
            '.txt': 'texto',
            '.nix': 'config_nix',
            '.yml': 'config_yaml',
            '.yaml': 'config_yaml',
            '.jsx': 'react_component',
            '.tsx': 'react_typescript',
            '.css': 'estilo',
            '.html': 'pagina_web'
        }
        
        # Análise por conteúdo no nome
        if 'quant' in nome or 'quantum' in nome:
            return 'arquivo_quantico'
        elif 'alquim' in nome or 'fundacao' in nome:
            return 'arquivo_fundacao' 
        elif 'config' in nome or 'setup' in nome:
            return 'configuracao'
        elif 'test' in nome or 'teste' in nome:
            return 'teste'
        elif 'lab' in nome or 'laboratorio' in nome:
            return 'laboratorio'
        elif 'relat' in nome or 'report' in nome:
            return 'relatorio'
        elif 'script' in nome:
            return 'script'
        else:
            return tipos.get(extensao, 'outros')
    
    def analisar_conteudo_cientifico(self, caminho_arquivo):
        """Analisar conteúdo científico do arquivo"""
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
                conteudo = f.read().lower()
                
            marcadores_cientificos = {
                'quantico': 'fisica_quantica',
                'quantum': 'fisica_quantica', 
                'qiskit': 'computacao_quantica',
                'qubit': 'computacao_quantica',
                'circuito': 'computacao_quantica',
                'entrelacamento': 'fisica_quantica',
                'superposicao': 'fisica_quantica',
                'alquimista': 'fundacao_alquimista',
                'zennith': 'rainha_zennith',
                'grokkar': 'liga_quantica',
                'numpy': 'computacao_cientifica',
                'matplotlib': 'visualizacao_cientifica',
                'simulacao': 'simulacao_cientifica',
                'algoritmo': 'algoritmo_cientifico',
                'estatistica': 'analise_estatistica',
                'entropia': 'teoria_informacao'
            }
            
            categorias = set()
            for marcador, categoria in marcadores_cientificos.items():
                if marcador in conteudo:
                    categorias.add(categoria)
            
            return list(categorias) if categorias else ['geral']
            
        except:
            return ['indeterminado']
    
    def analisar_estrutura_arquivo(self, caminho_arquivo):
        """Analisar estrutura interna do arquivo"""
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
                linhas = f.readlines()
            
            return {
                'total_linhas': len(linhas),
                'linhas_nao_vazias': len([l for l in linhas if l.strip()]),
                'linhas_comentario': len([l for l in linhas if l.strip().startswith('#') or l.strip().startswith('//')]),
                'tamanho_bytes': os.path.getsize(caminho_arquivo)
            }
        except:
            return {'total_linhas': 0, 'linhas_nao_vazias': 0, 'linhas_comentario': 0, 'tamanho_bytes': 0}
    
    def executar_varredura_completa(self):
        """Executar varredura completa de toda a árvore"""
        print("🚀 INICIANDO VARREdura COMPLETA DA FUNDAÇÃO...")
        print(f"📁 Diretório raiz: {self.raiz}")
        print("")
        
        total_arquivos = 0
        total_diretorios = 0
        
        for raiz, diretorios, arquivos in os.walk(self.raiz):
            # Ignorar alguns diretórios
            diretorios[:] = [d for d in diretorios if not d.startswith('.') and d not in ['node_modules', '__pycache__']]
            
            total_diretorios += len(diretorios)
            
            for arquivo in arquivos:
                caminho_completo = Path(raiz) / arquivo
                caminho_relativo = caminho_completo.relative_to(self.raiz)
                
                # Analisar arquivo
                tipo_arquivo = self.analisar_tipo_arquivo(caminho_completo)
                categorias_cientificas = self.analisar_conteudo_cientifico(caminho_completo)
                estrutura = self.analisar_estrutura_arquivo(caminho_completo)
                hash_arquivo = self.calcular_hash_arquivo(caminho_completo)
                
                # Salvar metadados
                self.metadados_completos[str(caminho_relativo)] = {
                    'tipo': tipo_arquivo,
                    'categorias_cientificas': categorias_cientificas,
                    'estrutura': estrutura,
                    'hash': hash_arquivo,
                    'caminho_absoluto': str(caminho_completo),
                    'tamanho_bytes': estrutura['tamanho_bytes'],
                    'data_modificacao': datetime.datetime.fromtimestamp(
                        caminho_completo.stat().st_mtime).isoformat()
                }
                
                total_arquivos += 1
                
                if total_arquivos % 100 == 0:
                    print(f"🔍 Analisados {total_arquivos} arquivos...")
        
        print(f"✅ VARREdura COMPLETA: {total_arquivos} arquivos, {total_diretorios} diretórios")
        return total_arquivos, total_diretorios
    
    def gerar_relatorio_estatistico(self):
        """Gerar relatório estatístico completo"""
        print("\n📊 GERANDO RELATÓRIO ESTATÍSTICO COMPLETO...")
        
        # Estatísticas por tipo
        tipos_contagem = {}
        categorias_contagem = {}
        tamanho_total = 0
        
        for metadados in self.metadados_completos.values():
            tipo = metadados['tipo']
            tipos_contagem[tipo] = tipos_contagem.get(tipo, 0) + 1
            
            for categoria in metadados['categorias_cientificas']:
                categorias_contagem[categoria] = categorias_contagem.get(categoria, 0) + 1
            
            tamanho_total += metadados['tamanho_bytes']
        
        print(f"📈 ESTATÍSTICAS GERAIS:")
        print(f"   📁 Total de arquivos: {len(self.metadados_completos)}")
        print(f"   💾 Tamanho total: {tamanho_total / (1024*1024):.2f} MB")
        print(f"   📅 Data da análise: {self.data_analise}")
        
        print(f"\n🎯 DISTRIBUIÇÃO POR TIPO:")
        for tipo, count in sorted(tipos_contagem.items(), key=lambda x: x[1], reverse=True)[:10]:
            porcentagem = (count / len(self.metadados_completos)) * 100
            print(f"   {tipo:25} : {count:4d} arquivos ({porcentagem:5.1f}%)")
        
        print(f"\n🔬 CATEGORIAS CIENTÍFICAS:")
        for categoria, count in sorted(categorias_contagem.items(), key=lambda x: x[1], reverse=True)[:15]:
            porcentagem = (count / len(self.metadados_completos)) * 100
            print(f"   {categoria:25} : {count:4d} arquivos ({porcentagem:5.1f}%)")
    
    def criar_mapa_interconexoes(self):
        """Criar mapa de interconexões entre arquivos"""
        print("\n🔗 CRIANDO MAPA DE INTERCONEXÕES...")
        
        interconexoes = {}
        
        for caminho, metadados in self.metadados_completos.items():
            if metadados['tipo'] in ['script_python', 'script_shell']:
                # Analisar dependências (simplificado)
                try:
                    with open(metadados['caminho_absoluto'], 'r') as f:
                        conteudo = f.read()
                    
                    dependencias = []
                    
                    # Buscar imports e includes
                    if metadados['tipo'] == 'script_python':
                        import re
                        imports = re.findall(r'^(?:from|import)\s+(\w+)', conteudo, re.MULTILINE)
                        dependencias.extend(imports)
                    
                    elif metadados['tipo'] == 'script_shell':
                        includes = re.findall(r'source\s+([^\s]+)', conteudo)
                        dependencias.extend(includes)
                    
                    if dependencias:
                        interconexoes[caminho] = dependencias
                        
                except:
                    pass
        
        print(f"   🔗 {len(interconexoes)} arquivos com dependências identificadas")
        return interconexoes
    
    def executar_teste_sistema_operacional(self):
        """Executar teste do sistema quântico operacional"""
        print("\n⚛️ EXECUTANDO TESTE DO SISTEMA QUÂNTICO OPERACIONAL...")
        
        try:
            # Teste básico do sistema
            qc = QuantumCircuit(3, name="Teste_Metadados")
            qc.h(0)
            qc.cx(0, 1)
            qc.cx(1, 2)
            qc.measure_all()
            
            result = self.simulator.run(qc, shots=100).result()
            counts = result.get_counts()
            
            print("   ✅ Sistema quântico: OPERACIONAL")
            print(f"   📊 Teste executado: {counts}")
            return True
            
        except Exception as e:
            print(f"   ❌ Sistema quântico: FALHA - {e}")
            return False
    
    def salvar_metadados_completos(self):
        """Salvar metadados completos em arquivo"""
        nome_arquivo = f"metadados_fundacao_completo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        dados_completos = {
            'metadados': self.metadados_completos,
            'estatisticas': {
                'total_arquivos': len(self.metadados_completos),
                'data_analise': self.data_analise,
                'diretorio_raiz': str(self.raiz)
            },
            'sistema_operacional': self.executar_teste_sistema_operacional()
        }
        
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_completos, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Metadados salvos em: {nome_arquivo}")
        return nome_arquivo
    
    def gerar_relatorio_final(self):
        """Gerar relatório final da análise"""
        print("\n" + "="*70)
        print("🎉 RELATÓRIO FINAL - SISTEMA DE METADADOS DEFINITIVO")
        print("="*70)
        
        total_arquivos = len(self.metadados_completos)
        arquivos_cientificos = sum(1 for m in self.metadados_completos.values() 
                                 if 'fisica_quantica' in m['categorias_cientificas'] or 
                                    'computacao_quantica' in m['categorias_cientificas'])
        
        print(f"📊 RESUMO DA FUNDAÇÃO ALQUIMISTA:")
        print(f"   🌌 Total de componentes: {total_arquivos}")
        print(f"   ⚛️  Arquivos científicos: {arquivos_cientificos}")
        print(f"   🔬 Porcentagem científica: {(arquivos_cientificos/total_arquivos)*100:.1f}%")
        print(f"   🎯 Sistema quântico: {'OPERACIONAL' if self.executar_teste_sistema_operacional() else 'COM PROBLEMAS'}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS RECOMENDADOS:")
        print("   1. Organizar arquivos por categorias científicas")
        print("   2. Criar índice de componentes da Fundação")
        print("   3. Desenvolver sistema de busca inteligente")
        print("   4. Implementar automação de laboratórios")
        
        print(f"\n🌌 FUNDAÇÃO ALQUIMISTA: SISTEMA DE METADADOS ESTABELECIDO!")

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    print("🔧 INICIALIZANDO SISTEMA DE METADADOS DEFINITIVO...")
    
    analisador = AnalisadorMetadadosDefinitivo()
    
    # Executar varredura completa
    total_arquivos, total_diretorios = analisador.executar_varredura_completa()
    
    # Gerar análises
    analisador.gerar_relatorio_estatistico()
    analisador.criar_mapa_interconexoes()
    
    # Salvar e finalizar
    arquivo_metadados = analisador.salvar_metadados_completos()
    analisador.gerar_relatorio_final()
    
    print(f"\n💡 Arquivo de metadados: {arquivo_metadados}")
    print("🚀 Use este arquivo para futuras análises e organizações!")
