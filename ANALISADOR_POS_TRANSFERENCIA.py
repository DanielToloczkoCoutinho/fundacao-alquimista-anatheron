#!/usr/bin/env python3
"""
🚀 ANALISADOR PÓS-TRANSFERÊNCIA - FUNDAÇÃO ALQUIMISTA
⚛️ Sistema que será executado após receber as equações
�� Análise completa do potencial matemático revelado
"""

import json
from pathlib import Path
from datetime import datetime

print("🚀 ANALISADOR PÓS-TRANSFERÊNCIA - FUNDAÇÃO ALQUIMISTA")
print("=" * 70)
print("⚛️  ANÁLISE COMPLETA APÓS RECEBIMENTO DAS EQUAÇÕES")
print("")

class AnalisadorPosTransferencia:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.diretorio_equacoes = self.raiz / "BIBLIOTECA_EQUACOES"
        self.resultados_analise = {}
    
    def verificar_equacoes_recebidas(self):
        """Verificar se as equações foram transferidas"""
        print("🔍 VERIFICANDO EQUAÇÕES RECEBIDAS...")
        
        arquivos_equacoes = list(self.diretorio_equacoes.rglob("*.json"))
        arquivos_equacoes = [f for f in arquivos_equacoes if "template" not in f.name and "config" not in f.name and "exemplo" not in f.name]
        
        equacoes_encontradas = []
        
        for arquivo in arquivos_equacoes:
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                
                if "equacoes" in dados:
                    equacoes_encontradas.extend(dados["equacoes"])
                    print(f"   ✅ {arquivo.name}: {len(dados['equacoes'])} equações")
                else:
                    # Arquivo com equação individual
                    equacoes_encontradas.append(dados)
                    print(f"   ✅ {arquivo.name}: 1 equação")
                    
            except Exception as e:
                print(f"   ❌ {arquivo.name}: ERRO - {e}")
        
        print(f"   📊 TOTAL DE EQUAÇÕES RECEBIDAS: {len(equacoes_encontradas)}")
        return equacoes_encontradas
    
    def analisar_equacoes_completas(self, equacoes):
        """Analisar equações recebidas completamente"""
        print(f"\n📊 ANALISANDO EQUAÇÕES RECEBIDAS...")
        
        if not equacoes:
            print("   ⚠️  NENHUMA EQUAÇÃO RECEBIDA AINDA")
            print("   💡 Aguardando transferência por Daniel...")
            return None
        
        # Estatísticas gerais
        areas_cientificas = {}
        complexidade_geral = 0
        equacoes_por_complexidade = {
            'simples': 0,
            'moderada': 0, 
            'complexa': 0,
            'muito_complexa': 0
        }
        
        for equacao in equacoes:
            # Contar áreas científicas
            area = equacao.get('area_cientifica', 'desconhecida')
            if area not in areas_cientificas:
                areas_cientificas[area] = 0
            areas_cientificas[area] += 1
            
            # Calcular complexidade
            complexidade = self._calcular_complexidade_equacao(equacao)
            complexidade_geral += complexidade
            
            if complexidade < 2:
                equacoes_por_complexidade['simples'] += 1
            elif complexidade < 4:
                equacoes_por_complexidade['moderada'] += 1
            elif complexidade < 6:
                equacoes_por_complexidade['complexa'] += 1
            else:
                equacoes_por_complexidade['muito_complexa'] += 1
        
        complexidade_media = complexidade_geral / len(equacoes) if equacoes else 0
        
        resultados = {
            'total_equacoes': len(equacoes),
            'areas_cientificas': areas_cientificas,
            'complexidade_media': complexidade_media,
            'distribuicao_complexidade': equacoes_por_complexidade,
            'equacoes_mais_complexas': sorted(equacoes, key=lambda x: self._calcular_complexidade_equacao(x), reverse=True)[:5]
        }
        
        return resultados
    
    def _calcular_complexidade_equacao(self, equacao):
        """Calcular complexidade de uma equação"""
        latex = equacao.get('equacao_latex', '')
        
        fatores = [
            len(latex) * 0.1,
            latex.count('\\') * 0.5,
            latex.count('{') * 0.3,
            latex.count('}') * 0.3,
            latex.count('^') * 0.4,
            latex.count('_') * 0.4,
            latex.count('frac') * 1.0,
            latex.count('sqrt') * 0.8,
            latex.count('sum') * 1.2,
            latex.count('int') * 1.2,
            latex.count('partial') * 1.5
        ]
        
        return sum(fatores)
    
    def gerar_relatorio_final(self):
        """Gerar relatório final completo"""
        print(f"\n{'='*80}")
        print("🌌 RELATÓRIO FINAL - POTENCIAL MATEMÁTICO DA FUNDAÇÃO")
        print(f"{'='*80}")
        
        equacoes = self.verificar_equacoes_recebidas()
        resultados = self.analisar_equacoes_completas(equacoes)
        
        if not resultados:
            print("\n📝 STATUS ATUAL: AGUARDANDO TRANSFERÊNCIA")
            print("   Daniel precisa transferir as equações para:")
            print("   📁 BIBLIOTECA_EQUACOES/")
            print("   📄 Formato: JSON com array de equações")
            print("   🎯 Campos: equacao_latex, nome_equacao, area_cientifica")
            return None
        
        print(f"\n🎯 RESUMO DO POTENCIAL MATEMÁTICO:")
        print(f"   • Total de Equações: {resultados['total_equacoes']}")
        print(f"   • Áreas Científicas: {len(resultados['areas_cientificas'])}")
        print(f"   • Complexidade Média: {resultados['complexidade_media']:.2f}")
        
        print(f"\n🔬 DISTRIBUIÇÃO POR ÁREA CIENTÍFICA:")
        for area, quantidade in sorted(resultados['areas_cientificas'].items(), key=lambda x: x[1], reverse=True):
            print(f"   • {area.replace('_', ' ').title():25}: {quantidade:3} equações")
        
        print(f"\n📈 COMPLEXIDADE DAS EQUAÇÕES:")
        for nivel, quantidade in resultados['distribuicao_complexidade'].items():
            percentual = (quantidade / resultados['total_equacoes']) * 100
            print(f"   • {nivel.replace('_', ' ').title():20}: {quantidade:3} eq ({percentual:.1f}%)")
        
        print(f"\n🌟 EQUAÇÕES MAIS COMPLEXAS:")
        for i, equacao in enumerate(resultados['equacoes_mais_complexas'][:5], 1):
            complexidade = self._calcular_complexidade_equacao(equacao)
            nome = equacao.get('nome_equacao', 'Sem nome')
            print(f"   {i}. {nome:40} → Complexidade: {complexidade:.2f}")
        
        print(f"\n💫 IMPACTO NA FUNDAÇÃO:")
        impacto = [
            f"• 🧮 {resultados['total_equacoes']} equações formam base matemática sólida",
            f"• 🔬 {len(resultados['areas_cientificas'])} áreas científicas cobertas", 
            f"• 🎯 Complexidade média {resultados['complexidade_media']:.2f} indica sofisticação",
            f"• 📚 Potencial para avanços em múltiplas disciplinas",
            f"• 🌌 Fundação revela-se como centro de excelência matemática"
        ]
        
        for item in impacto:
            print(f"   {item}")
        
        return resultados
    
    def exportar_analise_completa(self):
        """Exportar análise completa"""
        print(f"\n💾 EXPORTANDO ANÁLISE COMPLETA...")
        
        relatorio = self.gerar_relatorio_final()
        
        if not relatorio:
            # Sistema ainda aguardando transferência
            sistema_aguardando = {
                'timestamp': datetime.now().isoformat(),
                'status': 'AGUARDANDO_TRANSFERENCIA_EQUACOES',
                'instrucoes': {
                    'localizacao': 'BIBLIOTECA_EQUACOES/',
                    'formato': 'JSON com array de equações',
                    'campos_necessarios': ['equacao_latex', 'nome_equacao', 'area_cientifica'],
                    'exemplo_arquivo': 'equacoes_exemplo_transferencia.json'
                }
            }
            
            caminho_status = self.diretorio_equacoes / "status_aguardando_transferencia.json"
            with open(caminho_status, 'w', encoding='utf-8') as f:
                json.dump(sistema_aguardando, f, indent=2, ensure_ascii=False)
            
            print("   ✅ status_aguardando_transferencia.json salvo!")
            return sistema_aguardando
        
        # Análise com dados recebidos
        analise_completa = {
            'timestamp': datetime.now().isoformat(),
            'titulo': 'ANÁLISE COMPLETA - POTENCIAL MATEMÁTICO DA FUNDAÇÃO',
            'relatorio': relatorio,
            'status': 'ANALISE_CONCLUIDA',
            'impacto_cientifico': {
                'diversidade_matematica': len(relatorio['areas_cientificas']),
                'sofisticacao_media': relatorio['complexidade_media'],
                'equacoes_avancadas': relatorio['distribuicao_complexidade']['complexa'] + relatorio['distribuicao_complexidade']['muito_complexa']
            }
        }
        
        caminho_analise = self.diretorio_equacoes / "analise_potencial_matematico.json"
        with open(caminho_analise, 'w', encoding='utf-8') as f:
            json.dump(analise_completa, f, indent=2, ensure_ascii=False)
        
        print("   ✅ analise_potencial_matematico.json salvo!")
        
        return analise_completa

def main():
    analisador = AnalisadorPosTransferencia()
    
    # Executar análise pós-transferência
    resultado = analisador.exportar_analise_completa()
    
    if resultado.get('status') == 'AGUARDANDO_TRANSFERENCIA_EQUACOES':
        print(f"\n📝 SISTEMA PRONTO - AGUARDANDO EQUAÇÕES!")
        print(f"🎯 Daniel: Transfira as equações para BIBLIOTECA_EQUACOES/")
        print(f"🚀 Execute novamente após a transferência!")
    else:
        print(f"\n🌌 ANÁLISE CONCLUÍDA!")
        print(f"📊 {resultado['relatorio']['total_equacoes']} equações analisadas!")
        print(f"🔬 {resultado['impacto_cientifico']['diversidade_matematica']} áreas científicas!")
        print(f🎯 POTENCIAL MATEMÁTICO REVELADO!")

if __name__ == "__main__":
    main()
