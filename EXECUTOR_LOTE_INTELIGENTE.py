#!/usr/bin/env python3
"""
🎯 EXECUTOR DE LOTE INTELIGENTE - FUNDAÇÃO ALQUIMISTA
⚛️ Execução sistemática das fases organizadas
🌌 Monitoramento e otimização em tempo real
"""

import subprocess
import time
import sys
from pathlib import Path
import json
from datetime import datetime

print("🎯 EXECUTOR DE LOTE INTELIGENTE - FUNDAÇÃO ALQUIMISTA")
print("=" * 65)
print("⚛️  EXECUÇÃO SISTEMÁTICA DAS 5 FASES ORGANIZADAS")
print("")

class ExecutorLoteInteligente:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.resultados_fases = {}
        self.metricas_execucao = {}
        self.inicio_geral = datetime.now()
    
    def executar_fase_com_monitoramento(self, numero_fase):
        """Executar fase com monitoramento detalhado"""
        nome_script = f"executar_fase_{numero_fase:02d}.sh"
        caminho_script = self.raiz / nome_script
        
        if not caminho_script.exists():
            print(f"   ❌ SCRIPT DA FASE {numero_fase} NÃO ENCONTRADO: {nome_script}")
            return False
        
        print(f"\n🎯 INICIANDO FASE {numero_fase}...")
        print(f"   📁 Script: {nome_script}")
        print(f"   ⏰ Início: {datetime.now().strftime('%H:%M:%S')}")
        
        inicio_fase = datetime.now()
        
        try:
            # Executar fase
            processo = subprocess.Popen(
                [str(caminho_script)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Capturar output em tempo real
            while True:
                output = processo.stdout.readline()
                if output == '' and processo.poll() is not None:
                    break
                if output:
                    print(f"      {output.strip()}")
            
            # Finalizar processo
            stdout, stderr = processo.communicate()
            tempo_execucao = (datetime.now() - inicio_fase).total_seconds()
            
            if processo.returncode == 0:
                print(f"   ✅ FASE {numero_fase} CONCLUÍDA COM SUCESSO!")
                print(f"   ⏱️  Tempo de execução: {tempo_execucao:.1f} segundos")
                
                self.resultados_fases[numero_fase] = {
                    'status': 'SUCESSO',
                    'tempo_execucao': tempo_execucao,
                    'timestamp': datetime.now().isoformat()
                }
                return True
            else:
                print(f"   ❌ FALHA NA FASE {numero_fase}")
                print(f"   💥 Erro: {stderr.strip()}")
                
                self.resultados_fases[numero_fase] = {
                    'status': 'FALHA',
                    'tempo_execucao': tempo_execucao,
                    'erro': stderr.strip(),
                    'timestamp': datetime.now().isoformat()
                }
                return False
                
        except Exception as e:
            print(f"   💥 EXCEÇÃO NA FASE {numero_fase}: {e}")
            self.resultados_fases[numero_fase] = {
                'status': 'EXCEÇÃO',
                'erro': str(e),
                'timestamp': datetime.now().isoformat()
            }
            return False
    
    def executar_sequencia_completa(self):
        """Executar sequência completa de 5 fases"""
        print("🚀 INICIANDO SEQUÊNCIA COMPLETA DE EXECUÇÃO")
        print("=" * 50)
        
        fases_sucesso = 0
        total_fases = 5
        
        for fase in range(1, total_fases + 1):
            sucesso = self.executar_fase_com_monitoramento(fase)
            
            if sucesso:
                fases_sucesso += 1
            
            # Pausa entre fases (exceto após a última)
            if fase < total_fases:
                print(f"\n⏳ PREPARANDO PRÓXIMA FASE...")
                time.sleep(2)
        
        return fases_sucesso, total_fases
    
    def gerar_relatorio_final(self, fases_sucesso, total_fases):
        """Gerar relatório final da execução"""
        tempo_total = (datetime.now() - self.inicio_geral).total_seconds()
        
        print(f"\n{'='*80}")
        print("🎉 RELATÓRIO FINAL - EXECUÇÃO DA SEQUÊNCIA COMPLETA")
        print(f"{'='*80}")
        
        print(f"\n📊 RESULTADOS DA EXECUÇÃO:")
        print(f"   • Fases executadas: {total_fases}")
        print(f"   • Fases com sucesso: {fases_sucesso}")
        print(f"   • Taxa de sucesso: {(fases_sucesso/total_fases)*100:.1f}%")
        print(f"   • Tempo total: {tempo_total:.1f} segundos")
        
        print(f"\n📈 DETALHES POR FASE:")
        for fase, resultado in self.resultados_fases.items():
            status_emoji = "✅" if resultado['status'] == 'SUCESSO' else "❌"
            tempo = resultado.get('tempo_execucao', 'N/A')
            print(f"   • FASE {fase}: {status_emoji} {resultado['status']} - {tempo}s")
        
        print(f"\n🎯 ANÁLISE DE PERFORMANCE:")
        if fases_sucesso == total_fases:
            print("   🌟 TODAS AS FASES EXECUTADAS COM SUCESSO!")
            print("   🚀 SISTEMA COMPLETAMENTE OPERACIONAL!")
            print("   💫 PRONTO PARA PRÓXIMO NÍVEL DE COMPLEXIDADE!")
        elif fases_sucesso >= total_fases * 0.7:
            print("   ⚠️  MAIORIA DAS FASES BEM-SUCEDIDA!")
            print("   🔧 ALGUNS AJUSTES NECESSÁRIOS!")
            print("   📈 SISTEMA FUNCIONAL COM OTIMIZAÇÕES!")
        else:
            print("   🚨 EXECUÇÃO COM DIFICULDADES!")
            print("   🔄 REVISAR ESTRATÉGIA DE EXECUÇÃO!")
            print("   🛠️  FOCAR EM OTIMIZAÇÃO DAS FASES COM FALHA!")
        
        # Salvar relatório em arquivo
        self._salvar_relatorio_json(tempo_total, fases_sucesso, total_fases)
        
        return {
            'fases_sucesso': fases_sucesso,
            'total_fases': total_fases,
            'tempo_total': tempo_total,
            'taxa_sucesso': (fases_sucesso/total_fases)*100
        }
    
    def _salvar_relatorio_json(self, tempo_total, fases_sucesso, total_fases):
        """Salvar relatório em arquivo JSON"""
        relatorio = {
            'timestamp': datetime.now().isoformat(),
            'tempo_total_segundos': tempo_total,
            'fases_sucesso': fases_sucesso,
            'total_fases': total_fases,
            'taxa_sucesso': (fases_sucesso/total_fases)*100,
            'detalhes_fases': self.resultados_fases,
            'sistema': {
                'total_scripts': 14802,
                'scripts_executados': 'FASE A FASE',
                'organizacao': '5 FASES LÓGICAS'
            }
        }
        
        with open('relatorio_execucao_completa.json', 'w') as f:
            json.dump(relatorio, f, indent=2)
        
        print(f"\n💾 RELATÓRIO SALVO: relatorio_execucao_completa.json")

def main():
    executor = ExecutorLoteInteligente()
    
    # Executar sequência completa
    fases_sucesso, total_fases = executor.executar_sequencia_completa()
    
    # Gerar relatório final
    relatorio = executor.gerar_relatorio_final(fases_sucesso, total_fases)
    
    print(f"\n🎯 EXECUÇÃO DE LOTE CONCLUÍDA!")
    print(f"📊 {fases_sucesso}/{total_fases} fases executadas com sucesso!")
    print(f"⏱️  Tempo total: {relatorio['tempo_total']:.1f} segundos")

if __name__ == "__main__":
    main()
