#!/usr/bin/env python3
"""
🔬 ANALISADOR CIENTÍFICO DE LABORATÓRIOS - FUNDAÇÃO ALQUIMISTA
⚛️ Classificação por área científica específica
🌌 Identificação de equações e fórmulas especializadas
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

print("🔬 ANALISADOR CIENTÍFICO DE LABORATÓRIOS - FUNDAÇÃO ALQUIMISTA")
print("=" * 70)
print("⚛️  CLASSIFICAÇÃO POR ÁREA CIENTÍFICA ESPECÍFICA")
print("")

class AnalisadorCientifico:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.laboratorios_classificados = {}
        self.equacoes_identificadas = {}
        self.areas_cientificas = {}
    
    def executar_analise_cientifica_completa(self):
        """Executar análise científica completa dos laboratórios"""
        print("🔍 INICIANDO ANÁLISE CIENTÍFICA AVANÇADA...")
        
        # Áreas científicas para classificação
        areas_cientificas = {
            'fisica_quantica': {
                'termos': ['qubit', 'quantum', 'circuit', 'bell', 'emaranhamento', 'superposicao', 'hadamard', 'cnot'],
                'equacoes': ['ψ', 'φ', '⟨ψ|φ⟩', 'ħ', 'H|ψ⟩=E|ψ⟩']
            },
            'quimica_computacional': {
                'termos': ['molecula', 'atom', 'orbital', 'binding', 'energy', 'reaction', 'compound'],
                'equacoes': ['HΨ=EΨ', 'e^{-βH}', '⟨ϕ|H|ψ⟩']
            },
            'biologia_molecular': {
                'termos': ['protein', 'dna', 'rna', 'gene', 'cell', 'enzyme', 'metabolism'],
                'equacoes': ['k_{cat}', 'K_m', 'ΔG']
            },
            'medicina_quantica': {
                'termos': ['medical', 'health', 'therapy', 'diagnosis', 'treatment', 'patient', 'clinical'],
                'equacoes': ['PD', 'AUC', 'IC50']
            },
            'cosmologia': {
                'termos': ['cosmos', 'universe', 'blackhole', 'gravity', 'relativity', 'spacetime'],
                'equacoes': ['G_{\\mu\\nu}=8πT_{\\mu\\nu}', 'ds^2=g_{\\mu\\nu}dx^\\mu dx^\\nu']
            },
            'matematica_avancada': {
                'termos': ['equation', 'formula', 'theorem', 'proof', 'matrix', 'tensor', 'manifold'],
                'equacoes': ['e^{iπ}+1=0', '∇·E=ρ/ε_0', 'F=ma']
            },
            'computacao_avancada': {
                'termos': ['algorithm', 'compute', 'process', 'data', 'analysis', 'simulation', 'model'],
                'equacoes': ['O(n)', 'P=NP?', 'f(x)=∫_{-∞}^{∞}F(ξ)e^{2πiξx}dξ']
            }
        }
        
        laboratorios_analisados = 0
        equacoes_encontradas = 0
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            # Analisar diretórios de laboratórios
            for diretorio in dirs:
                if any(termo in diretorio.lower() for termo in ['lab', 'experiment', 'research', 'study']):
                    info_lab = self._analisar_laboratorio_cientifico(Path(raiz) / diretorio, diretorio, areas_cientificas)
                    if info_lab:
                        laboratorios_analisados += 1
                        equacoes_encontradas += len(info_lab.get('equacoes', []))
            
            # Analisar arquivos de laboratórios virtuais
            for arquivo in arquivos:
                if any(termo in arquivo.lower() for termo in ['experiment', 'research', 'study', 'analysis']):
                    caminho_arquivo = Path(raiz) / arquivo
                    if caminho_arquivo.suffix in ['.py', '.ipynb', '.r', '.m']:
                        info_lab = self._analisar_arquivo_cientifico(caminho_arquivo, arquivo, areas_cientificas)
                        if info_lab:
                            laboratorios_analisados += 1
                            equacoes_encontradas += len(info_lab.get('equacoes', []))
        
        print(f"   📊 LABORATÓRIOS ANALISADOS: {laboratorios_analisados}")
        print(f"   🧮 EQUAÇÕES IDENTIFICADAS: {equacoes_encontradas}")
        
        return laboratorios_analisados, equacoes_encontradas
    
    def _analisar_laboratorio_cientifico(self, caminho_lab, nome_lab, areas_cientificas):
        """Analisar laboratório físico com foco científico"""
        try:
            arquivos = list(caminho_lab.rglob('*'))
            scripts = [f for f in arquivos if f.suffix in ['.py', '.ipynb', '.r', '.m', '.cpp']]
            
            conteudo_total = ""
            equacoes_encontradas = []
            areas_detectadas = set()
            
            for script in scripts[:10]:  # Analisar até 10 scripts por laboratório
                try:
                    with open(script, 'r', encoding='utf-8') as f:
                        conteudo = f.read()
                        conteudo_total += conteudo + "\n"
                        
                        # Buscar equações
                        equacoes = self._extrair_equacoes(conteudo)
                        equacoes_encontradas.extend(equacoes)
                        
                        # Identificar áreas científicas
                        for area, dados in areas_cientificas.items():
                            if any(termo in conteudo.lower() for termo in dados['termos']):
                                areas_detectadas.add(area)
                            
                except:
                    continue
            
            # Classificar laboratório
            area_principal = self._determinar_area_principal(areas_detectadas, conteudo_total)
            
            info = {
                'nome': nome_lab,
                'caminho': str(caminho_lab),
                'tipo': 'laboratorio_fisico',
                'area_principal': area_principal,
                'areas_detectadas': list(areas_detectadas),
                'total_scripts': len(scripts),
                'equacoes_identificadas': equacoes_encontradas[:10],  # Limitar a 10
                'descricao_cientifica': self._gerar_descricao_cientifica(area_principal, equacoes_encontradas)
            }
            
            # Atualizar estatísticas
            if area_principal not in self.laboratorios_classificados:
                self.laboratorios_classificados[area_principal] = []
            self.laboratorios_classificados[area_principal].append(info)
            
            return info
            
        except Exception as e:
            return None
    
    def _analisar_arquivo_cientifico(self, caminho_arquivo, nome_arquivo, areas_cientificas):
        """Analisar arquivo de laboratório virtual"""
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Buscar equações
            equacoes_encontradas = self._extrair_equacoes(conteudo)
            
            # Identificar áreas científicas
            areas_detectadas = set()
            for area, dados in areas_cientificas.items():
                if any(termo in conteudo.lower() for termo in dados['termos']):
                    areas_detectadas.add(area)
            
            area_principal = self._determinar_area_principal(areas_detectadas, conteudo)
            
            info = {
                'nome': nome_arquivo,
                'caminho': str(caminho_arquivo),
                'tipo': 'laboratorio_virtual',
                'area_principal': area_principal,
                'areas_detectadas': list(areas_detectadas),
                'equacoes_identificadas': equacoes_encontradas[:10],
                'descricao_cientifica': self._gerar_descricao_cientifica(area_principal, equacoes_encontradas),
                'linhas_codigo': conteudo.count('\n') + 1
            }
            
            # Atualizar estatísticas
            if area_principal not in self.laboratorios_classificados:
                self.laboratorios_classificados[area_principal] = []
            self.laboratorios_classificados[area_principal].append(info)
            
            return info
            
        except:
            return None
    
    def _extrair_equacoes(self, conteudo):
        """Extrair equações matemáticas do conteúdo"""
        equacoes = []
        
        # Padrões para equações matemáticas
        padroes_equacoes = [
            r'\\[\\[].*?\\[\\]]',  # LaTeX: \[ \]
            r'\$.*?\$',            # LaTeX: $ $
            r'ψ|φ|Ψ',              # Símbolos quânticos
            r'α|β|γ|δ|ε',          # Letras gregas
            r'∑|∫|∏|∂',            # Símbolos matemáticos
            r'[A-Z]_{[^}]+}',      # Subscritos
            r'[A-Z]^{[^}]+}',      # Sobrescritos
            r'\\frac{.*?}{.*?}',   # Frações LaTeX
            r'\\sqrt{.*?}',        # Raízes LaTeX
        ]
        
        for padrao in padroes_equacoes:
            matches = re.findall(padrao, conteudo)
            equacoes.extend(matches)
        
        return list(set(equacoes))[:20]  # Limitar a 20 equações únicas
    
    def _determinar_area_principal(self, areas_detectadas, conteudo):
        """Determinar área científica principal"""
        if not areas_detectadas:
            return 'outros'
        
        # Contar ocorrências de termos por área
        contagem_areas = {}
        for area in areas_detectadas:
            # Contar ocorrências de termos da área no conteúdo
            termos_area = [
                'qubit', 'quantum', 'molecule', 'protein', 
                'medical', 'cosmos', 'equation', 'algorithm'
            ]
            contagem = sum(conteudo.lower().count(termo) for termo in termos_area)
            contagem_areas[area] = contagem
        
        return max(contagem_areas, key=contagem_areas.get, default='outros')
    
    def _gerar_descricao_cientifica(self, area_principal, equacoes):
        """Gerar descrição científica baseada na área e equações"""
        descricoes = {
            'fisica_quantica': f"Laboratório de Física Quântica com {len(equacoes)} equações especializadas",
            'quimica_computacional': f"Laboratório de Química Computacional com {len(equacoes)} modelos moleculares",
            'biologia_molecular': f"Laboratório de Biologia Molecular com {len(equacoes)} equações bioquímicas",
            'medicina_quantica': f"Laboratório de Medicina Quântica com {len(equacoes)} modelos médicos",
            'cosmologia': f"Laboratório de Cosmologia com {len(equacoes)} equações do universo",
            'matematica_avancada': f"Laboratório de Matemática Avançada com {len(equacoes)} teoremas",
            'computacao_avancada': f"Laboratório de Computação Avançada com {len(equacoes)} algoritmos"
        }
        
        return descricoes.get(area_principal, f"Laboratório científico com {len(equacoes)} equações identificadas")
    
    def gerar_relatorio_cientifico(self):
        """Gerar relatório científico completo"""
        print(f"\n{'='*80}")
        print("📊 RELATÓRIO CIENTÍFICO - LABORATÓRIOS DA FUNDAÇÃO")
        print(f"{'='*80}")
        
        total_labs = sum(len(labs) for labs in self.laboratorios_classificados.values())
        total_equacoes = sum(len(lab['equacoes_identificadas']) for labs in self.laboratorios_classificados.values() for lab in labs)
        
        print(f"\n🌌 VISÃO GERAL CIENTÍFICA:")
        print(f"   • Laboratórios classificados: {total_labs}")
        print(f"   • Equações identificadas: {total_equacoes}")
        print(f"   • Áreas científicas ativas: {len(self.laboratorios_classificados)}")
        
        print(f"\n🔬 DISTRIBUIÇÃO POR ÁREA CIENTÍFICA:")
        for area, laboratorios in sorted(self.laboratorios_classificados.items(), key=lambda x: len(x[1]), reverse=True):
            if laboratorios:
                equacoes_area = sum(len(lab['equacoes_identificadas']) for lab in laboratorios)
                print(f"   • {area.replace('_', ' ').title():25}: {len(laboratorios):3} labs | {equacoes_area:3} equações")
        
        print(f"\n🧮 EQUAÇÕES MAIS FREQUENTES:")
        todas_equacoes = []
        for laboratorios in self.laboratorios_classificados.values():
            for lab in laboratorios:
                todas_equacoes.extend(lab['equacoes_identificadas'])
        
        from collections import Counter
        equacoes_comuns = Counter(todas_equacoes).most_common(10)
        
        for equacao, frequencia in equacoes_comuns:
            print(f"   • {equacao:30} → {frequencia:2} laboratórios")
        
        print(f"\n🎯 LABORATÓRIOS MAIS ESPECIALIZADOS:")
        labs_especializados = []
        for area, laboratorios in self.laboratorios_classificados.items():
            for lab in laboratorios:
                if len(lab['equacoes_identificadas']) >= 5:  # Labs com pelo menos 5 equações
                    labs_especializados.append((lab['nome'], len(lab['equacoes_identificadas']), area))
        
        labs_especializados.sort(key=lambda x: x[1], reverse=True)
        for nome, num_equacoes, area in labs_especializados[:10]:
            print(f"   • {nome:40} → {num_equacoes:2} equações ({area})")
        
        return {
            'total_laboratorios': total_labs,
            'total_equacoes': total_equacoes,
            'distribuicao_areas': {area: len(labs) for area, labs in self.laboratorios_classificados.items()},
            'equacoes_comuns': dict(equacoes_comuns),
            'laboratorios_especializados': labs_especializados[:10]
        }
    
    def exportar_catalogo_cientifico(self):
        """Exportar catálogo científico completo"""
        print(f"\n💾 EXPORTANDO CATÁLOGO CIENTÍFICO...")
        
        relatorio = self.gerar_relatorio_cientifico()
        
        catalogo_cientifico = {
            'timestamp': datetime.now().isoformat(),
            'titulo': 'CATÁLOGO CIENTÍFICO - LABORATÓRIOS DA FUNDAÇÃO ALQUIMISTA',
            'relatorio_geral': relatorio,
            'laboratorios_detalhados': self.laboratorios_classificados,
            'resumo_cientifico': {
                'diversidade_areas': len(self.laboratorios_classificados),
                'intensidade_matematica': relatorio['total_equacoes'] / relatorio['total_laboratorios'] if relatorio['total_laboratorios'] > 0 else 0,
                'areas_mais_ativas': [area for area, _ in sorted(relatorio['distribuicao_areas'].items(), key=lambda x: x[1], reverse=True)[:3]]
            }
        }
        
        # Salvar catálogo
        with open('CATALOGO_CIENTIFICO_LABORATORIOS.json', 'w', encoding='utf-8') as f:
            json.dump(catalogo_cientifico, f, indent=2, ensure_ascii=False)
        
        print("   ✅ CATALOGO_CIENTIFICO_LABORATORIOS.json salvo!")
        
        # Gerar relatório em texto
        self._gerar_relatorio_cientifico_texto(catalogo_cientifico)
        
        return catalogo_cientifico
    
    def _gerar_relatorio_cientifico_texto(self, catalogo):
        """Gerar relatório científico em texto"""
        with open('RELATORIO_CIENTIFICO_LABORATORIOS.txt', 'w', encoding='utf-8') as f:
            f.write("🔬 RELATÓRIO CIENTÍFICO - LABORATÓRIOS DA FUNDAÇÃO\n")
            f.write("=" * 50 + "\n\n")
            
            f.write(f"📊 ESTATÍSTICAS GERAIS:\n")
            f.write(f"• Laboratórios analisados: {catalogo['relatorio_geral']['total_laboratorios']}\n")
            f.write(f"• Equações identificadas: {catalogo['relatorio_geral']['total_equacoes']}\n")
            f.write(f"• Áreas científicas: {catalogo['resumo_cientifico']['diversidade_areas']}\n")
            f.write(f"• Intensidade matemática: {catalogo['resumo_cientifico']['intensidade_matematica']:.2f} eq/lab\n\n")
            
            f.write("🔬 DISTRIBUIÇÃO POR ÁREA:\n")
            for area, quantidade in catalogo['relatorio_geral']['distribuicao_areas'].items():
                f.write(f"• {area.replace('_', ' ').title()}: {quantidade} laboratórios\n")
            
            f.write("\n🧮 EQUAÇÕES MAIS COMUNS:\n")
            for equacao, frequencia in catalogo['relatorio_geral']['equacoes_comuns'].items():
                f.write(f"• {equacao}: {frequencia} labs\n")
            
            f.write("\n🎯 LABORATÓRIOS MAIS ESPECIALIZADOS:\n")
            for nome, equacoes, area in catalogo['relatorio_geral']['laboratorios_especializados']:
                f.write(f"• {nome}: {equacoes} equações ({area})\n")
        
        print("   ✅ RELATORIO_CIENTIFICO_LABORATORIOS.txt salvo!")

def main():
    analisador = AnalisadorCientifico()
    
    # Executar análise científica
    labs_analisados, equacoes_encontradas = analisador.executar_analise_cientifica_completa()
    
    # Gerar relatório
    analisador.gerar_relatorio_cientifico()
    
    # Exportar catálogo
    catalogo = analisador.exportar_catalogo_cientifico()
    
    print(f"\n🔬 ANÁLISE CIENTÍFICA CONCLUÍDA!")
    print(f"📊 {labs_analisados} laboratórios classificados cientificamente!")
    print(f"🧮 {equacoes_encontradas} equações matemáticas identificadas!")
    print(f"🎯 ESPECIALIDADES CIENTÍFICAS REVELADAS!")

if __name__ == "__main__":
    main()
