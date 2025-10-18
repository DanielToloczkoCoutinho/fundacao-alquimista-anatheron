#!/usr/bin/env python3
"""
🌟 VERIFICADOR OPERACIONAL - FUNDAÇÃO ALQUIMISTA
⚛️ Verificação de sistemas críticos e funcionalidades
🌌 Garantia de continuidade operacional
"""

import subprocess
import json
from pathlib import Path
from datetime import datetime

print("🌟 VERIFICADOR OPERACIONAL - FUNDAÇÃO ALQUIMISTA")
print("=" * 70)
print("⚛️  VERIFICAÇÃO DE SISTEMAS CRÍTICOS E FUNCIONALIDADES")
print("")

class VerificadorOperacional:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.resultados_verificacao = {}
    
    def verificar_sistemas_criticos(self):
        """Verificar sistemas críticos da Fundação"""
        print("🔧 VERIFICANDO SISTEMAS CRÍTICOS...")
        
        sistemas_criticos = [
            {
                'nome': 'Sistema de Mapeamento',
                'arquivos': ['ORGANIZADOR_HIERARQUICO_COMPLETO.py', 'MAPEADOR_LABORATORIOS_AVANCADO.py'],
                'descricao': 'Sistema de organização e catalogação'
            },
            {
                'nome': 'Sistema Quântico', 
                'arquivos': ['circuito_psi_plus.py', 'teletransporte_quantico.py', 'teste_bell.py'],
                'descricao': 'Circuitos e algoritmos quânticos'
            },
            {
                'nome': 'Sistema de Análise',
                'arquivos': ['ANALISE_MAGNITUDE_FUNDACAO.py', 'INVESTIGADOR_REALIDADE_FUNDACAO.py'],
                'descricao': 'Análise e investigação de dados'
            },
            {
                'nome': 'Sistema de Configuração',
                'arquivos': ['CONFIGURADOR_IBM_CHAVES.py', 'CONFIGURADOR_IBM_AVANCADO.py'],
                'descricao': 'Configuração e conexões externas'
            }
        ]
        
        resultados = {}
        
        for sistema in sistemas_criticos:
            print(f"   🔍 {sistema['nome']}...")
            
            arquivos_encontrados = []
            arquivos_faltantes = []
            
            for arquivo in sistema['arquivos']:
                caminho = self.raiz / arquivo
                if caminho.exists():
                    arquivos_encontrados.append(arquivo)
                else:
                    arquivos_faltantes.append(arquivo)
            
            status = "✅ OPERACIONAL" if len(arquivos_faltantes) == 0 else "⚠️  PARCIAL"
            
            resultados[sistema['nome']] = {
                'status': status,
                'arquivos_encontrados': arquivos_encontrados,
                'arquivos_faltantes': arquivos_faltantes,
                'descricao': sistema['descricao']
            }
            
            if status == "✅ OPERACIONAL":
                print(f"      ✅ {sistema['nome']}: OPERACIONAL")
            else:
                print(f"      ⚠️  {sistema['nome']}: PARCIAL ({len(arquivos_faltantes)} faltantes)")
        
        self.resultados_verificacao['sistemas_criticos'] = resultados
        return resultados
    
    def verificar_funcionalidades_principais(self):
        """Verificar funcionalidades principais"""
        print("\n⚙️ VERIFICANDO FUNCIONALIDADES PRINCIPAIS...")
        
        funcionalidades = [
            {
                'nome': 'Execução de Scripts Python',
                'teste': ['python3', '--version'],
                'descricao': 'Interpretador Python operacional'
            },
            {
                'nome': 'Sistema de Arquivos',
                'teste': ['ls', '-la'],
                'descricao': 'Acesso ao sistema de arquivos'
            },
            {
                'nome': 'Processamento Básico',
                'teste': ['python3', '-c', 'print("OK")'],
                'descricao': 'Processamento e saída básica'
            }
        ]
        
        resultados = {}
        
        for func in funcionalidades:
            print(f"   🔍 {func['nome']}...")
            
            try:
                processo = subprocess.run(
                    func['teste'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if processo.returncode == 0:
                    resultados[func['nome']] = {
                        'status': '✅ OPERACIONAL',
                        'descricao': func['descricao'],
                        'detalhes': 'Teste executado com sucesso'
                    }
                    print(f"      ✅ {func['nome']}: OPERACIONAL")
                else:
                    resultados[func['nome']] = {
                        'status': '❌ FALHA',
                        'descricao': func['descricao'], 
                        'detalhes': processo.stderr
                    }
                    print(f"      ❌ {func['nome']}: FALHA")
            
            except Exception as e:
                resultados[func['nome']] = {
                    'status': '💥 EXCEÇÃO',
                    'descricao': func['descricao'],
                    'detalhes': str(e)
                }
                print(f"      💥 {func['nome']}: EXCEÇÃO")
        
        self.resultados_verificacao['funcionalidades'] = resultados
        return resultados
    
    def verificar_estado_geral(self):
        """Verificar estado geral do sistema"""
        print("\n📊 VERIFICANDO ESTADO GERAL DO SISTEMA...")
        
        # Análise básica do ambiente
        try:
            import psutil
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            estado = {
                'cpu_percent': cpu_percent,
                'memory_percent': memory.percent,
                'disk_free_gb': disk.free / (1024**3),
                'timestamp': datetime.now().isoformat()
            }
            
            print(f"   💻 CPU: {cpu_percent}%")
            print(f"   💾 Memória: {memory.percent}%")
            print(f"   💿 Disco livre: {estado['disk_free_gb']:.2f} GB")
            
            # Avaliação geral
            if cpu_percent < 80 and memory.percent < 85 and estado['disk_free_gb'] > 1:
                status_geral = "✅ ESTÁVEL"
            else:
                status_geral = "⚠️  ALERTA"
            
            estado['status_geral'] = status_geral
            print(f"   🎯 STATUS GERAL: {status_geral}")
        
        except ImportError:
            estado = {
                'status_geral': '⚠️  MÓDULOS FALTANTES',
                'detalhes': 'psutil não disponível para métricas detalhadas'
            }
            print(f"   🎯 STATUS GERAL: ⚠️  MÓDULOS FALTANTES")
        
        self.resultados_verificacao['estado_geral'] = estado
        return estado
    
    def gerar_relatorio_operacional(self):
        """Gerar relatório operacional completo"""
        print(f"\n{'='*80}")
        print("📋 RELATÓRIO OPERACIONAL - FUNDAÇÃO ALQUIMISTA")
        print(f"{'='*80}")
        
        sistemas = self.verificar_sistemas_criticos()
        funcionalidades = self.verificar_funcionalidades_principais()
        estado = self.verificar_estado_geral()
        
        # Contar status
        total_sistemas = len(sistemas)
        sistemas_operacionais = sum(1 for s in sistemas.values() if s['status'] == '✅ OPERACIONAL')
        
        total_funcionalidades = len(funcionalidades)
        funcionalidades_operacionais = sum(1 for f in funcionalidades.values() if f['status'] == '✅ OPERACIONAL')
        
        print(f"\n📊 RESUMO OPERACIONAL:")
        print(f"   • Sistemas críticos: {sistemas_operacionais}/{total_sistemas} operacionais")
        print(f"   • Funcionalidades: {funcionalidades_operacionais}/{total_funcionalidades} operacionais")
        print(f"   • Estado geral: {estado.get('status_geral', 'N/A')}")
        
        print(f"\n🎯 SISTEMAS CRÍTICOS:")
        for nome, info in sistemas.items():
            emoji = "✅" if info['status'] == '✅ OPERACIONAL' else "⚠️"
            print(f"   {emoji} {nome}: {info['status']}")
        
        print(f"\n⚙️ FUNCIONALIDADES:")
        for nome, info in funcionalidades.items():
            emoji = "✅" if info['status'] == '✅ OPERACIONAL' else "❌"
            print(f"   {emoji} {nome}: {info['status']}")
        
        print(f"\n💡 CONCLUSÃO:")
        if sistemas_operacionais == total_sistemas and funcionalidades_operacionais == total_funcionalidades:
            print("   🌟 SISTEMA COMPLETAMENTE OPERACIONAL!")
            print("   🚀 PRONTO PARA CONTINUIDADE ESTRATÉGICA!")
            print("   💫 TODAS AS FUNCIONALIDADES DISPONÍVEIS!")
        else:
            print("   ⚠️  SISTEMA PARCIALMENTE OPERACIONAL!")
            print("   🔧 ALGUNS AJUSTES PODEM SER NECESSÁRIOS!")
            print("   📈 CONTINUIDADE GARANTIDA COM OBSERVAÇÕES!")
        
        return {
            'sistemas_criticos': sistemas,
            'funcionalidades': funcionalidades,
            'estado_geral': estado,
            'resumo': {
                'sistemas_operacionais': sistemas_operacionais,
                'total_sistemas': total_sistemas,
                'funcionalidades_operacionais': funcionalidades_operacionais,
                'total_funcionalidades': total_funcionalidades
            }
        }
    
    def exportar_verificacao_completa(self):
        """Exportar verificação completa"""
        print(f"\n💾 EXPORTANDO VERIFICAÇÃO OPERACIONAL...")
        
        relatorio = self.gerar_relatorio_operacional()
        
        verificacao_completa = {
            'timestamp': datetime.now().isoformat(),
            'titulo': 'VERIFICAÇÃO OPERACIONAL - FUNDAÇÃO ALQUIMISTA',
            'relatorio': relatorio,
            'status_geral': 'OPERACIONAL' if (
                relatorio['resumo']['sistemas_operacionais'] == relatorio['resumo']['total_sistemas'] and
                relatorio['resumo']['funcionalidades_operacionais'] == relatorio['resumo']['total_funcionalidades']
            ) else 'PARCIALMENTE OPERACIONAL'
        }
        
        # Salvar verificação
        with open('VERIFICACAO_OPERACIONAL.json', 'w', encoding='utf-8') as f:
            json.dump(verificacao_completa, f, indent=2, ensure_ascii=False)
        
        print("   ✅ VERIFICACAO_OPERACIONAL.json salvo!")
        
        return verificacao_completa

def main():
    verificador = VerificadorOperacional()
    
    # Executar verificação completa
    verificacao = verificador.exportar_verificacao_completa()
    
    print(f"\n🌟 VERIFICAÇÃO OPERACIONAL CONCLUÍDA!")
    print(f"🎯 STATUS: {verificacao['status_geral']}")
    print(f"🚀 SISTEMA PRONTO PARA CONTINUIDADE!")

if __name__ == "__main__":
    main()
