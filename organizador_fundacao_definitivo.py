#!/usr/bin/env python3
"""
🎯 ORGANIZADOR DEFINITIVO - FUNDAÇÃO ALQUIMISTA
⚛️ Sistema automático de organização baseado em metadados
🌌 Cria estrutura lógica de todos os componentes
"""

import json
import shutil
from pathlib import Path
import datetime

print("🎯 ORGANIZADOR DEFINITIVO - FUNDAÇÃO ALQUIMISTA")
print("=" * 55)

class OrganizadorFundacao:
    def __init__(self, arquivo_metadados):
        self.metadados = self.carregar_metadados(arquivo_metadados)
        self.estrutura_organizada = {}
        
    def carregar_metadados(self, arquivo):
        """Carregar metadados do arquivo"""
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)['metadados']
        except Exception as e:
            print(f"❌ Erro carregando metadados: {e}")
            return {}
    
    def criar_estrutura_categorias(self):
        """Criar estrutura organizada por categorias"""
        print("📁 CRIANDO ESTRUTURA ORGANIZADA...")
        
        categorias_principais = {
            'computacao_quantica': [
                'script_python', 'arquivo_quantico', 'computacao_quantica'
            ],
            'fisica_quantica': [
                'fisica_quantica', 'documentacao'
            ],
            'scripts_shell': [
                'script_shell', 'configuracao'
            ],
            'laboratorios': [
                'laboratorio', 'teste'
            ],
            'relatorios': [
                'relatorio', 'analise_estatistica'
            ],
            'configuracoes': [
                'config_nix', 'config_yaml', 'configuracao'
            ],
            'interface_web': [
                'script_javascript', 'script_typescript', 'react_component',
                'pagina_web', 'estilo'
            ],
            'dados': [
                'dados_json', 'texto'
            ]
        }
        
        for caminho, info in self.metadados.items():
            categorias_arquivo = info['categorias_cientificas']
            tipo_arquivo = info['tipo']
            
            # Encontrar categoria principal
            categoria_destino = 'outros'
            for cat_principal, criterios in categorias_principais.items():
                if (any(crit in categorias_arquivo for crit in criterios) or
                    tipo_arquivo in criterios):
                    categoria_destino = cat_principal
                    break
            
            if categoria_destino not in self.estrutura_organizada:
                self.estrutura_organizada[categoria_destino] = []
            
            self.estrutura_organizada[categoria_destino].append({
                'caminho_original': caminho,
                'tipo': tipo_arquivo,
                'categorias': categorias_arquivo,
                'tamanho_bytes': info['tamanho_bytes']
            })
        
        print("✅ Estrutura criada com sucesso!")
        return self.estrutura_organizada
    
    def gerar_relatorio_organizacao(self):
        """Gerar relatório da organização"""
        print("\n📊 RELATÓRIO DE ORGANIZAÇÃO:")
        print("=" * 40)
        
        total_arquivos = sum(len(arquivos) for arquivos in self.estrutura_organizada.values())
        
        for categoria, arquivos in sorted(self.estrutura_organizada.items(), 
                                        key=lambda x: len(x[1]), reverse=True):
            quantidade = len(arquivos)
            porcentagem = (quantidade / total_arquivos) * 100
            tamanho_total = sum(a['tamanho_bytes'] for a in arquivos) / (1024*1024)
            
            print(f"   {categoria:20} : {quantidade:3d} arquivos ({porcentagem:5.1f}%) - {tamanho_total:.2f} MB")
    
    def criar_indice_buscavel(self):
        """Criar índice buscável da Fundação"""
        print("\n🔍 CRIANDO ÍNDICE BUSCÁVEL...")
        
        indice = {
            'data_criacao': datetime.datetime.now().isoformat(),
            'total_componentes': len(self.metadados),
            'categorias': {},
            'palavras_chave': {}
        }
        
        # Organizar por categorias
        for caminho, info in self.metadados.items():
            for categoria in info['categorias_cientificas']:
                if categoria not in indice['categorias']:
                    indice['categorias'][categoria] = []
                indice['categorias'][categoria].append(caminho)
        
        # Salvar índice
        nome_indice = f"indice_fundacao_buscavel_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(nome_indice, 'w', encoding='utf-8') as f:
            json.dump(indice, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Índice salvo em: {nome_indice}")
        return nome_indice
    
    def executar_organizacao_completa(self):
        """Executar organização completa"""
        print("🚀 EXECUTANDO ORGANIZAÇÃO COMPLETA DA FUNDAÇÃO...")
        
        self.criar_estrutura_categorias()
        self.gerar_relatorio_organizacao()
        indice = self.criar_indice_buscavel()
        
        print("\n🎉 ORGANIZAÇÃO COMPLETA CONCLUÍDA!")
        print("🌌 FUNDAÇÃO ALQUIMISTA: SISTEMA ORGANIZACIONAL ESTABELECIDO!")
        print(f"💡 Índice criado: {indice}")
        
        return indice

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    # Buscar o arquivo de metadados mais recente
    arquivos_metadados = list(Path('.').glob('metadados_fundacao_completo_*.json'))
    
    if not arquivos_metadados:
        print("❌ Nenhum arquivo de metadados encontrado.")
        print("💡 Execute primeiro: python3 sistema_metadados_definitivo.py")
        exit(1)
    
    # Usar o mais recente
    arquivo_recente = max(arquivos_metadados, key=lambda x: x.stat().st_mtime)
    print(f"📁 Usando arquivo: {arquivo_recente}")
    
    organizador = OrganizadorFundacao(arquivo_recente)
    organizador.executar_organizacao_completa()
