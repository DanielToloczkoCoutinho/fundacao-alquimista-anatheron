#!/usr/bin/env python3
"""
🎨 EXECUÇÃO VISUAL ORGANIZADA - FUNDAÇÃO ALQUIMISTA
⚛️ Sistema de execução sequencial com visualização clara
🌌 Cada circuito executado isoladamente sem sobreposição
"""

import subprocess
import sys
import time
from pathlib import Path

print("🎨 EXECUÇÃO VISUAL ORGANIZADA - FUNDAÇÃO ALQUIMISTA")
print("=" * 60)
print("⚛️  EXECUÇÃO SEQUENCIAL ISOLADA - SEM SOBREPOSIÇÃO")
print("")

class ExecutorVisualOrganizado:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.resultados_detalhados = {}
    
    def executar_circuito_isolado(self, nome_arquivo, numero_execucao, total_execucoes):
        """Executar um circuito de forma completamente isolada"""
        print(f"\n{'='*70}")
        print(f"🔬 [{numero_execucao}/{total_execucoes}] EXECUTANDO: {nome_arquivo}")
        print(f"{'='*70}")
        
        caminho_arquivo = self.raiz / nome_arquivo
        
        if not caminho_arquivo.exists():
            print(f"   🚫 ARQUIVO NÃO ENCONTRADO: {nome_arquivo}")
            return f"🚫 NÃO ENCONTRADO"
        
        try:
            # Executar em processo completamente isolado
            processo = subprocess.Popen(
                [sys.executable, str(caminho_arquivo)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Coletar saída em tempo real
            saida_completa = []
            for linha in processo.stdout:
                linha_limpa = linha.rstrip()
                saida_completa.append(linha_limpa)
                print(f"   {linha_limpa}")
            
            # Esperar processo terminar
            processo.wait(timeout=30)
            
            if processo.returncode == 0:
                print(f"   ✅ {nome_arquivo} - EXECUTADO COM SUCESSO")
                return "✅ SUCESSO"
            else:
                erro = processo.stderr.read()
                print(f"   ❌ {nome_arquivo} - ERRO: {erro[:100]}...")
                return f"❌ ERRO: {erro[:100]}"
                
        except subprocess.TimeoutExpired:
            print(f"   ⏰ {nome_arquivo} - TIMEOUT")
            processo.kill()
            return "⏰ TIMEOUT"
        except Exception as e:
            print(f"   💥 {nome_arquivo} - EXCEÇÃO: {e}")
            return f"💥 EXCEÇÃO: {e}"
    
    def executar_sequencia_visual_organizada(self):
        """Executar sequência visualmente organizada"""
        print("🚀 INICIANDO SEQUÊNCIA VISUALMENTE ORGANIZADA...")
        print("💡 Cada circuito executado ISOLADAMENTE sem sobreposição")
        print("")
        
        # Sequência organizada de execução
        sequencia_execucao = [
            {
                "nome": "🌌 CONFIGURAÇÃO INICIAL",
                "arquivo": "VERIFICAR_AMBIENTE.sh",
                "tipo": "configuracao"
            },
            {
                "nome": "🔧 CIRCUITO |Ψ⁺⟩ (PSI PLUS)",
                "arquivo": "circuito_psi_plus.py", 
                "tipo": "circuito_basico"
            },
            {
                "nome": "🔧 CIRCUITO |Φ⁻⟩ (PHI MINUS)",
                "arquivo": "circuito_phi_minus.py",
                "tipo": "circuito_basico" 
            },
            {
                "nome": "🚀 TELETRANSPORTE QUÂNTICO",
                "arquivo": "teletransporte_quantico.py",
                "tipo": "circuito_avancado"
            },
            {
                "nome": "🔔 TESTE DE BELL",
                "arquivo": "teste_bell.py",
                "tipo": "teste_avancado"
            },
            {
                "nome": "⚡ CIRCUITOS UNIFICADOS",
                "arquivo": "CIRCUITOS_UNIFICADOS.py",
                "tipo": "circuito_unificado"
            },
            {
                "nome": "👑 MÓDULO 29 - RAINHA ZENNITH",
                "arquivo": "explorar_modulo_29.py",
                "tipo": "modulo_rainha"
            }
        ]
        
        tempo_inicio_total = time.time()
        resultados_sequencia = {}
        
        # Executar cada item da sequência
        for i, item in enumerate(sequencia_execucao, 1):
            resultado = self.executar_circuito_isolado(
                item["arquivo"], 
                i, 
                len(sequencia_execucao)
            )
            resultados_sequencia[item["nome"]] = resultado
            
            # Pequena pausa entre execuções para evitar sobreposição
            if i < len(sequencia_execucao):
                print(f"\n⏳ PREPARANDO PRÓXIMA EXECUÇÃO...")
                time.sleep(1)
        
        tempo_total = time.time() - tempo_inicio_total
        
        # Relatório Final Organizado
        print(f"\n{'='*70}")
        print("🎉 RELATÓRIO FINAL - EXECUÇÃO VISUALMENTE ORGANIZADA")
        print(f"{'='*70}")
        
        print(f"\n�� RESUMO DA EXECUÇÃO:")
        for nome, resultado in resultados_sequencia.items():
            emoji = "✅" if "✅" in resultado else "❌" if "❌" in resultado else "⚠️"
            print(f"   {emoji} {nome}: {resultado}")
        
        print(f"\n⏱️  ESTATÍSTICAS:")
        print(f"   • Total de execuções: {len(sequencia_execucao)}")
        print(f"   • Tempo total: {tempo_total:.2f} segundos")
        print(f"   • Tempo médio por execução: {tempo_total/len(sequencia_execucao):.2f} segundos")
        
        sucessos = sum(1 for r in resultados_sequencia.values() if "✅" in r)
        print(f"   • Taxa de sucesso: {sucessos}/{len(sequencia_execucao)} ({sucessos/len(sequencia_execucao)*100:.1f}%)")
        
        print(f"\n🚀 PRÓXIMOS PASSOS:")
        if sucessos == len(sequencia_execucao):
            print("   ✅ TODOS OS CIRCUITOS EXECUTADOS COM SUCESSO!")
            print("   🌌 PRONTO PARA IBM QUANTUM REAL!")
            print("   📊 EXECUÇÃO PERFEITAMENTE ORGANIZADA!")
        else:
            print("   ⚠️  ALGUNS CIRCUITOS PRECISAM DE AJUSTES")
            print("   🔧 VERIFICAR SCRIPTS COM FALHA")
            print("   🔄 RE-EXECUTAR COM CORREÇÕES")
        
        return resultados_sequencia

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    executor = ExecutorVisualOrganizado()
    resultados = executor.executar_sequencia_visual_organizada()
    
    print(f"\n🎨 EXECUÇÃO VISUALMENTE ORGANIZADA CONCLUÍDA!")
    print("⚛️  CIRCUITOS EXECUTADOS SEM SOBREPOSIÇÃO!")
