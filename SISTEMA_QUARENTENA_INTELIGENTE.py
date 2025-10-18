#!/usr/bin/env python3
"""
💾 SISTEMA DE QUARENTENA INTELIGENTE - FUNDAÇÃO ALQUIMISTA
⚛️ Gestão estratégica de armazenamento e organização
🌌 Sistema de rotação e arquivamento inteligente
"""

import shutil
from pathlib import Path
from datetime import datetime
import json

print("💾 SISTEMA DE QUARENTENA INTELIGENTE - FUNDAÇÃO ALQUIMISTA")
print("=" * 70)
print("⚛️  GESTÃO ESTRATÉGICA DE ARMAZENAMENTO E ORGANIZAÇÃO")
print("")

class SistemaQuarentena:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.diretorio_quarentena = self.raiz / "QUARENTENA_INTELIGENTE"
        self.metricas_quarentena = {}
    
    def criar_estrutura_quarentena(self):
        """Criar estrutura de quarentena organizada"""
        print("🏗️ CRIANDO ESTRUTURA DE QUARENTENA INTELIGENTE...")
        
        estruturas = [
            "LABORATORIOS_ARQUIVADOS",
            "SCRIPTS_INATIVOS", 
            "DADOS_COMPACTADOS",
            "RELATORIOS_CONSOLIDADOS",
            "BACKUP_ESTRATIFICADO",
            "METADADOS_CATALOGO"
        ]
        
        for estrutura in estruturas:
            caminho = self.diretorio_quarentena / estrutura
            caminho.mkdir(parents=True, exist_ok=True)
            print(f"   ✅ {estrutura}")
        
        return estruturas
    
    def analisar_uso_armazenamento(self):
        """Analisar uso atual de armazenamento"""
        print("\n📊 ANALISANDO USO DE ARMAZENAMENTO...")
        
        total_tamanho = 0
        distribuicao = {}
        
        for item in self.raiz.rglob('*'):
            if item.is_file():
                extensao = item.suffix.lower() or 'sem_extensao'
                tamanho = item.stat().st_size
                total_tamanho += tamanho
                
                if extensao not in distribuicao:
                    distribuicao[extensao] = {'count': 0, 'size': 0}
                
                distribuicao[extensao]['count'] += 1
                distribuicao[extensao]['size'] += tamanho
        
        # Converter para GB
        total_gb = total_tamanho / (1024**3)
        
        print(f"   💾 USO TOTAL: {total_gb:.2f} GB")
        
        # Mostrar maiores consumidores
        maiores_consumidores = sorted(distribuicao.items(), 
                                    key=lambda x: x[1]['size'], 
                                    reverse=True)[:10]
        
        print(f"\n   📈 MAIORES CONSUMIDORES:")
        for extensao, dados in maiores_consumidores:
            tamanho_gb = dados['size'] / (1024**3)
            print(f"      • {extensao:10}: {tamanho_gb:6.2f} GB ({dados['count']:5} arquivos)")
        
        self.metricas_quarentena['uso_armazenamento'] = {
            'total_gb': total_gb,
            'distribuicao': distribuicao,
            'timestamp': datetime.now().isoformat()
        }
        
        return total_gb, distribuicao
    
    def identificar_candidatos_quarentena(self):
        """Identificar candidatos para quarentena"""
        print("\n🔍 IDENTIFICANDO CANDIDATOS PARA QUARENTENA...")
        
        criterios_quarentena = [
            ('*.log', 'Arquivos de log antigos'),
            ('*.tmp', 'Arquivos temporários'),
            ('*.bak', 'Backups antigos'),
            ('*_old.*', 'Versões antigas de arquivos'),
            ('*backup_*', 'Backups automáticos'),
            ('*node_modules*', 'Dependências Node.js'),
            ('*__pycache__*', 'Cache Python'),
            ('*.git*', 'Metadados Git (exceto .git/)')
        ]
        
        candidatos = []
        
        for padrao, descricao in criterios_quarentena:
            arquivos_encontrados = list(self.raiz.rglob(padrao))
            if arquivos_encontrados:
                tamanho_total = sum(f.stat().st_size for f in arquivos_encontrados if f.is_file())
                candidatos.append({
                    'padrao': padrao,
                    'descricao': descricao,
                    'arquivos': len(arquivos_encontrados),
                    'tamanho_total_gb': tamanho_total / (1024**3),
                    'exemplos': [str(f) for f in arquivos_encontrados[:3]]
                })
        
        print(f"   📋 {len(candidatos)} CATEGORIAS IDENTIFICADAS:")
        
        espaco_liberar = 0
        for candidato in candidatos:
            print(f"      • {candidato['descricao']:30} → {candidato['tamanho_total_gb']:.2f} GB")
            espaco_liberar += candidato['tamanho_total_gb']
        
        print(f"\n   💰 ESPAÇO POTENCIAL A LIBERAR: {espaco_liberar:.2f} GB")
        
        self.metricas_quarentena['candidatos'] = candidatos
        return candidatos, espaco_liberar
    
    def criar_plano_otimizacao(self, total_armazenamento, candidatos):
        """Criar plano de otimização estratégica"""
        print(f"\n{'='*80}")
        print("🎯 PLANO DE OTIMIZAÇÃO ESTRATÉGICA - ARMAZENAMENTO")
        print(f"{'='*80}")
        
        espaco_potencial = sum(c['tamanho_total_gb'] for c in candidatos)
        percentual_otimizacao = (espaco_potencial / total_armazenamento) * 100
        
        print(f"\n📊 DIAGNÓSTICO ATUAL:")
        print(f"   • Armazenamento total: {total_armazenamento:.2f} GB")
        print(f"   • Espaço potencial a liberar: {espaco_potencial:.2f} GB")
        print(f"   • Percentual de otimização: {percentual_otimizacao:.1f}%")
        
        print(f"\n🚀 ESTRATÉGIA DE OTIMIZAÇÃO:")
        
        estrategia = [
            "FASE 1: LIMPEZA IMEDIATA (0-30 dias)",
            "   • Arquivos temporários e cache",
            "   • Logs antigos (>30 dias)",
            "   • Backups redundantes",
            "",
            "FASE 2: ORGANIZAÇÃO ESTRUTURAL (30-60 dias)", 
            "   • Categorização de laboratórios",
            "   • Arquivos de dados otimizados",
            "   • Compactação inteligente",
            "",
            "FASE 3: OTIMIZAÇÃO AVANÇADA (60-90 dias)",
            "   • Sistema de rotação automática",
            "   • Compressão adaptativa",
            "   • Armazenamento em nuvem estratégico"
        ]
        
        for linha in estrategia:
            print(f"   {linha}")
        
        print(f"\n💡 RECOMENDAÇÕES IMEDIATAS:")
        recomendacoes = [
            f"• 🗑️  LIMPAR {candidatos[0]['tamanho_total_gb']:.2f} GB em {candidatos[0]['descricao']}",
            f"• 📦 COMPACTAR dados de laboratórios inativos",
            f"• 🔄 IMPLEMENTAR rotação de logs automática",
            f"• 💾 ESTABELECER política de retenção de backups",
            f"• 📊 MONITORAR crescimento do armazenamento"
        ]
        
        for recomendacao in recomendacoes:
            print(f"   {recomendacao}")
        
        return {
            'espaco_total': total_armazenamento,
            'espaco_liberar': espaco_potencial,
            'percentual_otimizacao': percentual_otimizacao,
            'estrategia_implementada': True
        }
    
    def executar_plano_seguro(self):
        """Executar plano de otimização de forma segura"""
        print(f"\n🛡️ EXECUTANDO PLANO DE OTIMIZAÇÃO SEGURO...")
        
        # Criar estrutura primeiro
        self.criar_estrutura_quarentena()
        
        # Apenas simulação por segurança
        print("   🔒 MODO SEGURO ATIVADO - Apenas simulação")
        print("   📋 Ações que seriam executadas:")
        
        acoes_simuladas = [
            "• 📁 Criar estrutura de quarentena organizada",
            "• 📊 Analisar uso de armazenamento atual", 
            "• 🔍 Identificar candidatos para otimização",
            "• 🎯 Definir estratégia de limpeza",
            "• 💾 Implementar compactação inteligente",
            "• 🔄 Estabelecer sistema de rotação"
        ]
        
        for acao in acoes_simuladas:
            print(f"      {acao}")
        
        print(f"\n   💡 PRÓXIMOS PASSOS REAIS:")
        print(f"      1. Revisar análise de candidatos")
        print(f"      2. Criar backups antes de qualquer ação")
        print(f"      3. Implementar gradualmente")
        print(f"      4. Monitorar impacto")
        print(f"      5. Ajustar estratégia conforme necessário")
        
        return {
            'modo': 'simulacao_segura',
            'acoes_simuladas': acoes_simuladas,
            'timestamp': datetime.now().isoformat()
        }
    
    def exportar_plano_completo(self):
        """Exportar plano completo de otimização"""
        print(f"\n💾 EXPORTANDO PLANO DE OTIMIZAÇÃO...")
        
        # Coletar todos os dados
        total_armazenamento, distribuicao = self.analisar_uso_armazenamento()
        candidatos, espaco_potencial = self.identificar_candidatos_quarentena()
        plano = self.criar_plano_otimizacao(total_armazenamento, candidatos)
        execucao = self.executar_plano_seguro()
        
        plano_completo = {
            'timestamp': datetime.now().isoformat(),
            'diagnostico': {
                'armazenamento_total_gb': total_armazenamento,
                'espaco_liberar_gb': espaco_potencial,
                'percentual_otimizacao': plano['percentual_otimizacao']
            },
            'candidatos_quarentena': candidatos,
            'estrategia_otimizacao': plano,
            'execucao_simulada': execucao,
            'recomendacoes': [
                "Implementar limpeza gradual e monitorada",
                "Manter backups antes de qualquer ação",
                "Estabelecer políticas de retenção claras",
                "Monitorar crescimento do armazenamento continuamente"
            ]
        }
        
        # Salvar plano
        with open('PLANO_OTIMIZACAO_ARMAZENAMENTO.json', 'w', encoding='utf-8') as f:
            json.dump(plano_completo, f, indent=2, ensure_ascii=False)
        
        print("   ✅ PLANO_OTIMIZACAO_ARMAZENAMENTO.json salvo!")
        
        return plano_completo

def main():
    sistema = SistemaQuarentena()
    
    # Executar análise completa
    plano = sistema.exportar_plano_completo()
    
    print(f"\n💾 SISTEMA DE QUARENTENA CONCLUÍDO!")
    print(f"📊 Diagnóstico: {plano['diagnostico']['armazenamento_total_gb']:.2f} GB utilizados")
    print(f"💰 Otimização: {plano['diagnostico']['espaco_liberar_gb']:.2f} GB liberáveis")
    print(f"🎯 Estratégia: {plano['diagnostico']['percentual_otimizacao']:.1f}% de melhoria potencial")

if __name__ == "__main__":
    main()
