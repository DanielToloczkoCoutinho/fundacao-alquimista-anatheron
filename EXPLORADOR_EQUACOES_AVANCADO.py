#!/usr/bin/env python3
"""
🧮 EXPLORADOR AVANÇADO DE EQUAÇÕES - FUNDAÇÃO ALQUIMISTA
⚛️ Análise profunda das equações matemáticas encontradas
🌌 Classificação por tipo e complexidade
"""

import re
import json
from pathlib import Path
from datetime import datetime

print("🧮 EXPLORADOR AVANÇADO DE EQUAÇÕES - FUNDAÇÃO ALQUIMISTA")
print("=" * 70)
print("⚛️  ANÁLISE PROFUNDA DAS EQUAÇÕES MATEMÁTICAS")
print("")

class ExploradorEquacoes:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.equacoes_classificadas = {}
        self.tipos_equacoes = {}
    
    def carregar_catalogo_cientifico(self):
        """Carregar catálogo científico existente"""
        try:
            with open('CATALOGO_CIENTIFICO_LABORATORIOS.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None
    
    def analisar_equacoes_profundamente(self):
        """Analisar equações de forma profunda"""
        print("🔍 ANALISANDO EQUAÇÕES MATEMÁTICAS...")
        
        catalogo = self.carregar_catalogo_cientifico()
        if not catalogo:
            print("   ❌ Catálogo científico não encontrado")
            return
        
        todas_equacoes = []
        for area, laboratorios in catalogo['laboratorios_detalhados'].items():
            for lab in laboratorios:
                todas_equacoes.extend(lab['equacoes_identificadas'])
        
        equacoes_unicas = list(set(todas_equacoes))
        print(f"   📊 Equações únicas identificadas: {len(equacoes_unicas)}")
        
        # Classificar equações por tipo
        for equacao in equacoes_unicas:
            tipo = self._classificar_equacao(equacao)
            complexidade = self._calcular_complexidade(equacao)
            
            if tipo not in self.equacoes_classificadas:
                self.equacoes_classificadas[tipo] = []
            
            self.equacoes_classificadas[tipo].append({
                'equacao': equacao,
                'complexidade': complexidade,
                'ocorrencias': todas_equacoes.count(equacao)
            })
        
        return equacoes_unicas
    
    def _classificar_equacao(self, equacao):
        """Classificar equação por tipo"""
        if 'ψ' in equacao or 'φ' in equacao or '⟨' in equacao:
            return 'mecanica_quantica'
        elif '∂' in equacao or '∇' in equacao or '∫' in equacao:
            return 'calculus_avancado'
        elif '∑' in equacao or '∏' in equacao:
            return 'algebra_superior'
        elif '_{' in equacao and '}^{' in equacao:
            return 'tensores_relatividade'
        elif '\\frac' in equacao:
            return 'algebra_basica'
        elif 'e^{' in equacao or 'ln' in equacao:
            return 'funcoes_especiais'
        elif '√' in equacao or '\\sqrt' in equacao:
            return 'radicais'
        else:
            return 'outras'
    
    def _calcular_complexidade(self, equacao):
        """Calcular complexidade da equação"""
        fatores = [
            len(equacao) * 0.1,
            equacao.count('{') * 2,
            equacao.count('_') * 1.5,
            equacao.count('^') * 1.5,
            len(re.findall(r'[α-ω]', equacao)) * 3,  # Letras gregas
            len(re.findall(r'[∫∑∏∂∇]', equacao)) * 5  # Símbolos avançados
        ]
        
        complexidade = sum(fatores)
        
        if complexidade < 5:
            return 'simples'
        elif complexidade < 15:
            return 'moderada'
        elif complexidade < 30:
            return 'complexa'
        else:
            return 'muito_complexa'
    
    def gerar_relatorio_equacoes(self):
        """Gerar relatório detalhado das equações"""
        print(f"\n{'='*80}")
        print("📊 RELATÓRIO DE EQUAÇÕES - FUNDAÇÃO ALQUIMISTA")
        print(f"{'='*80}")
        
        equacoes_unicas = self.analisar_equacoes_profundamente()
        
        print(f"\n🧮 ESTATÍSTICAS DAS EQUAÇÕES:")
        print(f"   • Total de equações únicas: {len(equacoes_unicas)}")
        
        total_ocorrencias = sum(sum(eq['ocorrencias'] for eq in eqs) for eqs in self.equacoes_classificadas.values())
        print(f"   • Total de ocorrências: {total_ocorrencias}")
        
        print(f"\n📈 DISTRIBUIÇÃO POR TIPO:")
        for tipo, equacoes in sorted(self.equacoes_classificadas.items(), key=lambda x: len(x[1]), reverse=True):
            ocorrencias_tipo = sum(eq['ocorrencias'] for eq in equacoes)
            print(f"   • {tipo.replace('_', ' ').title():25}: {len(equacoes):3} eq | {ocorrencias_tipo:3} ocorrências")
        
        print(f"\n🎯 COMPLEXIDADE DAS EQUAÇÕES:")
        complexidades = {}
        for tipo, equacoes in self.equacoes_classificadas.items():
            for eq in equacoes:
                if eq['complexidade'] not in complexidades:
                    complexidades[eq['complexidade']] = 0
                complexidades[eq['complexidade']] += 1
        
        for complexidade, quantidade in sorted(complexidades.items(), key=lambda x: ['simples', 'moderada', 'complexa', 'muito_complexa'].index(x[0])):
            print(f"   • {complexidade.replace('_', ' ').title():20}: {quantidade:3} equações")
        
        print(f"\n🌟 EQUAÇÕES MAIS FREQUENTES:")
        todas_equacoes_com_ocorrencias = []
        for tipo, equacoes in self.equacoes_classificadas.items():
            for eq in equacoes:
                todas_equacoes_com_ocorrencias.append((eq['equacao'], eq['ocorrencias'], tipo, eq['complexidade']))
        
        equacoes_frequentes = sorted(todas_equacoes_com_ocorrencias, key=lambda x: x[1], reverse=True)[:15]
        
        for i, (equacao, ocorrencias, tipo, complexidade) in enumerate(equacoes_frequentes, 1):
            print(f"   {i:2d}. {equacao:40} → {ocorrencias:2} labs ({tipo}, {complexidade})")
        
        return {
            'total_equacoes_unicas': len(equacoes_unicas),
            'distribuicao_tipos': {tipo: len(equacoes) for tipo, equacoes in self.equacoes_classificadas.items()},
            'complexidade_geral': complexidades,
            'equacoes_mais_frequentes': equacoes_frequentes
        }
    
    def exportar_analise_equacoes(self):
        """Exportar análise completa das equações"""
        print(f"\n💾 EXPORTANDO ANÁLISE DE EQUAÇÕES...")
        
        relatorio = self.gerar_relatorio_equacoes()
        
        analise_equacoes = {
            'timestamp': datetime.now().isoformat(),
            'titulo': 'ANÁLISE AVANÇADA DE EQUAÇÕES - FUNDAÇÃO ALQUIMISTA',
            'relatorio_geral': relatorio,
            'equacoes_detalhadas': self.equacoes_classificadas,
            'resumo_matematico': {
                'diversidade_tipos': len(self.equacoes_classificadas),
                'complexidade_media': self._calcular_complexidade_media(),
                'tipos_mais_comuns': [tipo for tipo, _ in sorted(relatorio['distribuicao_tipos'].items(), key=lambda x: x[1], reverse=True)[:3]]
            }
        }
        
        # Salvar análise
        with open('ANALISE_EQUACOES_AVANCADA.json', 'w', encoding='utf-8') as f:
            json.dump(analise_equacoes, f, indent=2, ensure_ascii=False)
        
        print("   ✅ ANALISE_EQUACOES_AVANCADA.json salvo!")
        
        return analise_equacoes
    
    def _calcular_complexidade_media(self):
        """Calcular complexidade média das equações"""
        complexidades = []
        for tipo, equacoes in self.equacoes_classificadas.items():
            for eq in equacoes:
                peso = {'simples': 1, 'moderada': 2, 'complexa': 3, 'muito_complexa': 4}
                complexidades.append(peso[eq['complexidade']])
        
        return sum(complexidades) / len(complexidades) if complexidades else 0

def main():
    explorador = ExploradorEquacoes()
    
    # Executar análise de equações
    analise = explorador.exportar_analise_equacoes()
    
    print(f"\n🧮 ANÁLISE DE EQUAÇÕES CONCLUÍDA!")
    print(f"📊 {analise['relatorio_geral']['total_equacoes_unicas']} equações únicas analisadas!")
    print(f"🎯 {len(analise['relatorio_geral']['distribuicao_tipos'])} tipos matemáticos identificados!")
    print(f"🌟 COMPLEXIDADE MÉDIA: {analise['resumo_matematico']['complexidade_media']:.2f}")

if __name__ == "__main__":
    main()
