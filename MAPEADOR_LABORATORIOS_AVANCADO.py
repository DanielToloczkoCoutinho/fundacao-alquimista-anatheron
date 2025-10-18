#!/usr/bin/env python3
"""
🔬 MAPEADOR AVANÇADO DE LABORATÓRIOS - FUNDAÇÃO ALQUIMISTA
⚛️ Catalogo inteligente de 500+ laboratórios
🌌 Análise de produção e relatórios de cada laboratório
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

print("🔬 MAPEADOR AVANÇADO DE LABORATÓRIOS - FUNDAÇÃO ALQUIMISTA")
print("=" * 70)
print("⚛️  CATALOGANDO E ANALISANDO 500+ LABORATÓRIOS")
print("")

class MapeadorLaboratorios:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.laboratorios_mapeados = {}
        self.categorias_laboratorios = {}
        self.relatorios_produzidos = {}
    
    def executar_mapeamento_completo(self):
        """Executar mapeamento completo de todos os laboratórios"""
        print("🔍 INICIANDO MAPEAMENTO DE LABORATÓRIOS...")
        
        padroes_laboratorios = [
            r'.*laboratorio.*', r'.*lab.*', r'.*experimento.*', 
            r'.*pesquisa.*', r'.*estudo.*', r'.*analise.*',
            r'.*teste.*', r'.*simulacao.*', r'.*experiment.*',
            r'.*research.*', r'.*study.*', r'.*analysis.*'
        ]
        
        laboratorios_encontrados = {
            'quanticos': [],
            'computacao': [],
            'pesquisa': [],
            'desenvolvimento': [],
            'analise': [],
            'simulacao': [],
            'outros': []
        }
        
        total_encontrados = 0
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            # Buscar diretórios que são laboratórios
            for diretorio in dirs:
                dir_lower = diretorio.lower()
                
                if any(re.search(padrao, dir_lower) for padrao in padroes_laboratorios):
                    info_lab = self._analisar_laboratorio(Path(raiz) / diretorio, diretorio)
                    categoria = self._classificar_laboratorio(info_lab)
                    
                    laboratorios_encontrados[categoria].append(info_lab)
                    total_encontrados += 1
            
            # Buscar arquivos que representam laboratórios
            for arquivo in arquivos:
                arquivo_lower = arquivo.lower()
                if any(re.search(padrao, arquivo_lower) for padrao in padroes_laboratorios):
                    # Verificar se é um "laboratório virtual" (arquivo principal)
                    info_lab = self._analisar_laboratorio_virtual(Path(raiz) / arquivo, arquivo)
                    categoria = self._classificar_laboratorio(info_lab)
                    
                    laboratorios_encontrados[categoria].append(info_lab)
                    total_encontrados += 1
        
        print(f"   📊 LABORATÓRIOS IDENTIFICADOS: {total_encontrados}")
        
        # Mostrar distribuição
        for categoria, labs in laboratorios_encontrados.items():
            if labs:
                print(f"   📁 {categoria.upper():20}: {len(labs)} laboratórios")
        
        self.laboratorios_mapeados = laboratorios_encontrados
        return laboratorios_encontrados
    
    def _analisar_laboratorio(self, caminho_lab, nome_lab):
        """Analisar um laboratório físico (diretório)"""
        try:
            arquivos = list(caminho_lab.rglob('*'))
            scripts = [f for f in arquivos if f.suffix in ['.py', '.sh', '.js', '.r']]
            relatorios = [f for f in arquivos if any(termo in f.name.lower() for termo in ['relatorio', 'report', 'resultado', 'analise'])]
            dados = [f for f in arquivos if any(termo in f.name.lower() for termo in ['.json', '.csv', '.data', 'dados'])]
            
            info = {
                'nome': nome_lab,
                'caminho': str(caminho_lab),
                'tipo': 'laboratorio_fisico',
                'total_arquivos': len(arquivos),
                'scripts': len(scripts),
                'relatorios': len(relatorios),
                'arquivos_dados': len(dados),
                'tamanho_total': sum(f.stat().st_size for f in arquivos if f.is_file()),
                'ultima_modificacao': self._obter_ultima_modificacao(caminho_lab),
                'descricao': self._extrair_descricao_lab(caminho_lab)
            }
            
            return info
            
        except Exception as e:
            return {
                'nome': nome_lab,
                'caminho': str(caminho_lab),
                'tipo': 'laboratorio_fisico',
                'erro': str(e)
            }
    
    def _analisar_laboratorio_virtual(self, caminho_arquivo, nome_arquivo):
        """Analisar um laboratório virtual (arquivo principal)"""
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            info = {
                'nome': nome_arquivo,
                'caminho': str(caminho_arquivo),
                'tipo': 'laboratorio_virtual',
                'tamanho': caminho_arquivo.stat().st_size,
                'linhas': conteudo.count('\n') + 1,
                'ultima_modificacao': datetime.fromtimestamp(caminho_arquivo.stat().st_mtime).isoformat(),
                'descricao': self._extrair_descricao_arquivo(conteudo),
                'dependencias': self._extrair_dependencias(conteudo),
                'funcoes_principais': self._extrair_funcoes(conteudo)
            }
            
            return info
            
        except Exception as e:
            return {
                'nome': nome_arquivo,
                'caminho': str(caminho_arquivo),
                'tipo': 'laboratorio_virtual',
                'erro': str(e)
            }
    
    def _classificar_laboratorio(self, info_lab):
        """Classificar o laboratório por categoria"""
        nome = info_lab['nome'].lower()
        descricao = info_lab.get('descricao', '').lower()
        
        if any(termo in nome or termo in descricao for termo in ['quant', 'qiskit', 'qubit', 'circuit', 'bell']):
            return 'quanticos'
        elif any(termo in nome or termo in descricao for termo in ['compute', 'algorithm', 'code', 'program']):
            return 'computacao'
        elif any(termo in nome or termo in descricao for termo in ['research', 'study', 'investigate', 'pesquisa']):
            return 'pesquisa'
        elif any(termo in nome or termo in descricao for termo in ['develop', 'build', 'create', 'desenvolvimento']):
            return 'desenvolvimento'
        elif any(termo in nome or termo in descricao for termo in ['analysis', 'analise', 'data', 'dados']):
            return 'analise'
        elif any(termo in nome or termo in descricao for termo in ['simulation', 'simulacao', 'model']):
            return 'simulacao'
        else:
            return 'outros'
    
    def _obter_ultima_modificacao(self, caminho):
        """Obter data da última modificação"""
        try:
            return datetime.fromtimestamp(caminho.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        except:
            return "Desconhecido"
    
    def _extrair_descricao_lab(self, caminho_lab):
        """Extrair descrição do laboratório"""
        # Buscar por README ou arquivos de documentação
        arquivos_desc = ['README.md', 'readme.txt', 'DESCRIPTION', 'SOBRE.md']
        
        for arquivo in arquivos_desc:
            caminho_arquivo = caminho_lab / arquivo
            if caminho_arquivo.exists():
                try:
                    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                        return f.read()[:500] + '...' if len(f.read()) > 500 else f.read()
                except:
                    pass
        
        return "Descrição não disponível"
    
    def _extrair_descricao_arquivo(self, conteudo):
        """Extrair descrição de arquivo de laboratório"""
        # Buscar docstring ou comentários iniciais
        padrao_docstring = r'\"\"\"(.*?)\"\"\"'
        match = re.search(padrao_docstring, conteudo, re.DOTALL)
        if match:
            return match.group(1).strip()[:300]
        
        # Buscar comentários iniciais
        linhas = conteudo.split('\n')[:10]
        comentarios = []
        for linha in linhas:
            linha_limpa = linha.strip()
            if linha_limpa.startswith('#') and not linha_limpa.startswith('#!/'):
                comentarios.append(linha_limpa[1:].strip())
        
        return ' | '.join(comentarios[:3]) if comentarios else "Sem descrição disponível"
    
    def _extrair_dependencias(self, conteudo):
        """Extrair dependências do laboratório"""
        dependencias = []
        bibliotecas = ['qiskit', 'numpy', 'pandas', 'matplotlib', 'tensorflow', 'pytorch', 'scipy']
        
        for lib in bibliotecas:
            if lib in conteudo.lower():
                dependencias.append(lib)
        
        return dependencias[:5]
    
    def _extrair_funcoes(self, conteudo):
        """Extrair funções principais"""
        funcoes = re.findall(r'def\s+(\w+)\s*\(', conteudo)
        return funcoes[:8]
    
    def analisar_producao_relatorios(self):
        """Analisar produção de relatórios dos laboratórios"""
        print("\n📊 ANALISANDO PRODUÇÃO DE RELATÓRIOS...")
        
        relatorios_por_lab = {}
        total_relatorios = 0
        
        for categoria, laboratorios in self.laboratorios_mapeados.items():
            for lab in laboratorios:
                nome_lab = lab['nome']
                relatorios_lab = self._buscar_relatorios_lab(lab)
                
                if relatorios_lab:
                    relatorios_por_lab[nome_lab] = {
                        'categoria': categoria,
                        'total_relatorios': len(relatorios_lab),
                        'relatorios': relatorios_lab,
                        'ultimo_relatorio': max([r['data'] for r in relatorios_lab]) if relatorios_lab else "Nenhum"
                    }
                    total_relatorios += len(relatorios_lab)
        
        print(f"   📈 TOTAL DE RELATÓRIOS PRODUZIDOS: {total_relatorios}")
        print(f"   🔬 LABORATÓRIOS COM RELATÓRIOS: {len(relatorios_por_lab)}")
        
        # Mostrar laboratórios mais produtivos
        labs_mais_produtivos = sorted(relatorios_por_lab.items(), 
                                    key=lambda x: x[1]['total_relatorios'], 
                                    reverse=True)[:10]
        
        print(f"\n   �� TOP 10 LABORATÓRIOS MAIS PRODUTIVOS:")
        for i, (nome, info) in enumerate(labs_mais_produtivos, 1):
            print(f"      {i:2d}. {nome:30} → {info['total_relatorios']:3} relatórios")
        
        self.relatorios_produzidos = relatorios_por_lab
        return relatorios_por_lab
    
    def _buscar_relatorios_lab(self, info_lab):
        """Buscar relatórios produzidos por um laboratório"""
        relatorios = []
        
        if info_lab['tipo'] == 'laboratorio_fisico':
            caminho_lab = Path(info_lab['caminho'])
            try:
                for arquivo in caminho_lab.rglob('*'):
                    if any(termo in arquivo.name.lower() for termo in ['relatorio', 'report', 'resultado', 'analise', 'result']):
                        info_rel = {
                            'nome': arquivo.name,
                            'caminho': str(arquivo),
                            'tamanho': arquivo.stat().st_size,
                            'data': datetime.fromtimestamp(arquivo.stat().st_mtime).strftime('%Y-%m-%d'),
                            'tipo': arquivo.suffix
                        }
                        relatorios.append(info_rel)
            except:
                pass
        
        return relatorios
    
    def gerar_estrategia_organizacao(self):
        """Gerar estratégia de organização para os laboratórios"""
        print(f"\n{'='*80}")
        print("🏗️ ESTRATÉGIA DE ORGANIZAÇÃO - LABORATÓRIOS DA FUNDAÇÃO")
        print(f"{'='*80}")
        
        total_labs = sum(len(labs) for labs in self.laboratorios_mapeados.values())
        total_relatorios = sum(info['total_relatorios'] for info in self.relatorios_produzidos.values())
        
        print(f"\n📊 PANORAMA ATUAL:")
        print(f"   • Total de laboratórios: {total_labs}")
        print(f"   • Relatórios produzidos: {total_relatorios}")
        print(f"   • Categorias ativas: {len([c for c, l in self.laboratorios_mapeados.items() if l])}")
        
        print(f"\n🎯 ESTRATÉGIA DE ORGANIZAÇÃO:")
        
        estrategia = [
            "1. 📂 SISTEMA DE CATEGORIZAÇÃO HIERÁRQUICA",
            "   - Organizar por área de pesquisa principal",
            "   - Subcategorias por metodologia",
            "   - Tags por tecnologias utilizadas",
            "",
            "2. 🔄 SISTEMA DE ROTAÇÃO INTELIGENTE", 
            "   - Laboratórios ativos vs. arquivados",
            "   - Priorização por impacto de pesquisa",
            "   - Alocação dinâmica de recursos",
            "",
            "3. 📊 SISTEMA DE MÉTRICAS DE PRODUTIVIDADE",
            "   - Relatórios produzidos por período",
            "   - Citações e impacto científico",
            "   - Colaborações entre laboratórios",
            "",
            "4. 💾 ESTRATÉGIA DE ARMAZENAMENTO",
            "   - Dados ativos vs. dados arquivados",
            "   - Compressão inteligente de dados",
            "   - Backup estratificado",
            "",
            "5. 🔗 SISTEMA DE INTEGRAÇÃO",
            "   - Conexões entre laboratórios relacionados",
            "   - Compartilhamento de metodologias",
            "   - Colaboração em projetos conjuntos"
        ]
        
        for linha in estrategia:
            print(f"   {linha}")
        
        print(f"\n🚀 PLANO DE AÇÃO IMEDIATO:")
        acoes_imediatas = [
            "• 🔍 CATALOGAR todos os 500+ laboratórios",
            "• 📈 IDENTIFICAR laboratórios mais produtivos", 
            "• 🏷️ IMPLEMENTAR sistema de categorização",
            "• 📊 CRIAR dashboard de métricas",
            "• 💾 OTIMIZAR uso de armazenamento",
            "• 🔗 ESTABELECER conexões estratégicas"
        ]
        
        for acao in acoes_imediatas:
            print(f"   {acao}")
        
        return {
            'total_laboratorios': total_labs,
            'total_relatorios': total_relatorios,
            'categorias_ativas': len([c for c, l in self.laboratorios_mapeados.items() if l]),
            'estrategia_implementada': True
        }
    
    def exportar_catalogo_completo(self):
        """Exportar catálogo completo de laboratórios"""
        print(f"\n💾 EXPORTANDO CATÁLOGO COMPLETO...")
        
        catalogo = {
            'timestamp': datetime.now().isoformat(),
            'estatisticas_gerais': {
                'total_laboratorios': sum(len(labs) for labs in self.laboratorios_mapeados.values()),
                'total_relatorios': sum(info['total_relatorios'] for info in self.relatorios_produzidos.values()),
                'categorias_identificadas': len([c for c, l in self.laboratorios_mapeados.items() if l])
            },
            'laboratorios_por_categoria': self.laboratorios_mapeados,
            'producao_relatorios': self.relatorios_produzidos,
            'estrategia_organizacao': self.gerar_estrategia_organizacao()
        }
        
        # Salvar em JSON
        with open('CATALOGO_LABORATORIOS_FUNDACAO.json', 'w', encoding='utf-8') as f:
            json.dump(catalogo, f, indent=2, ensure_ascii=False)
        
        print("   ✅ CATALOGO_LABORATORIOS_FUNDACAO.json salvo!")
        
        # Gerar relatório resumido
        self._gerar_relatorio_resumido(catalogo)
        
        return catalogo
    
    def _gerar_relatorio_resumido(self, catalogo):
        """Gerar relatório resumido em texto"""
        with open('RELATORIO_LABORATORIOS.txt', 'w', encoding='utf-8') as f:
            f.write("🔬 RELATÓRIO DE LABORATÓRIOS - FUNDAÇÃO ALQUIMISTA\n")
            f.write("=" * 50 + "\n\n")
            
            f.write(f"📊 ESTATÍSTICAS GERAIS:\n")
            f.write(f"• Laboratórios catalogados: {catalogo['estatisticas_gerais']['total_laboratorios']}\n")
            f.write(f"• Relatórios produzidos: {catalogo['estatisticas_gerais']['total_relatorios']}\n")
            f.write(f"• Categorias ativas: {catalogo['estatisticas_gerais']['categorias_identificadas']}\n\n")
            
            f.write("📁 DISTRIBUIÇÃO POR CATEGORIA:\n")
            for categoria, laboratorios in catalogo['laboratorios_por_categoria'].items():
                if laboratorios:
                    f.write(f"• {categoria.title():15}: {len(laboratorios)} laboratórios\n")
            
            f.write("\n🏆 LABORATÓRIOS MAIS PRODUTIVOS:\n")
            labs_produtivos = sorted(catalogo['producao_relatorios'].items(), 
                                   key=lambda x: x[1]['total_relatorios'], 
                                   reverse=True)[:15]
            
            for nome, info in labs_produtivos:
                f.write(f"• {nome:30} → {info['total_relatorios']:3} relatórios\n")
        
        print("   ✅ RELATORIO_LABORATORIOS.txt salvo!")

def main():
    mapeador = MapeadorLaboratorios()
    
    # 1. Mapear laboratórios
    laboratorios = mapeador.executar_mapeamento_completo()
    
    # 2. Analisar produção de relatórios
    mapeador.analisar_producao_relatorios()
    
    # 3. Gerar estratégia
    mapeador.gerar_estrategia_organizacao()
    
    # 4. Exportar catálogo
    catalogo = mapeador.exportar_catalogo_completo()
    
    print(f"\n🔬 MAPEAMENTO DE LABORATÓRIOS CONCLUÍDO!")
    print(f"�� {catalogo['estatisticas_gerais']['total_laboratorios']} laboratórios catalogados!")
    print(f"📈 {catalogo['estatisticas_gerais']['total_relatorios']} relatórios identificados!")
    print(f"🎯 ESTRATÉGIA DE ORGANIZAÇÃO DEFINIDA!")

if __name__ == "__main__":
    main()
