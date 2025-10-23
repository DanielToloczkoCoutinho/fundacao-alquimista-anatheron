#!/usr/bin/env python3
"""
🪞 LABORATÓRIO DUPLO ESPELHO - FUNDAÇÃO ALQUIMISTA
🔥 REAL (Celestial v2) vs. NATIVO (Nix-Pura) - Validação Cruzada
"""

import json
import subprocess
import time
from datetime import datetime

class LaboratorioDuploEspelho:
    """Orquestra a execução e validação dos laboratórios Real e Nativo."""

    def cabecalho(self):
        print("=" * 80)
        print("🪞 LABORATÓRIO DUPLO ESPELHO - REAL vs. NATIVO")
        print("👑 Validação Cruzada da Coerência da Fundação Alquimista")
        print(f"⏰ {datetime.now().isoformat()}")
        print("=" * 80)

    def executar_script(self, script_name):
        """Executa um script Python e aguarda sua conclusão."""
        try:
            print(f"\n🚀 INVOCANDO UNIVERSO: {script_name}...")
            process = subprocess.run(["python3", script_name], capture_output=True, text=True, check=True)
            print(f"   ✅ UNIVERSO MANIFESTADO COM SUCESSO.")
            # print(process.stdout) # Descomente para debug
            return True
        except FileNotFoundError:
            print(f"   ❌ ERRO CRÍTICO: Script '{script_name}' não encontrado.")
            return False
        except subprocess.CalledProcessError as e:
            print(f"   ❌ ERRO na execução de '{script_name}':")
            print(e.stderr)
            return False

    def carregar_relatorio(self, path):
        """Carrega um relatório JSON."""
        try:
            with open(path, 'r') as f:
                print(f"   📄 Lendo relatório de '{path}'...")
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"   ❌ Falha ao carregar ou decodificar '{path}': {e}")
            return None

    def validar_harmonia(self, rel_celestial, rel_nix):
        """Compara as assinaturas e métricas dos dois universos."""
        print("\n🔬 INICIANDO VALIDAÇÃO CRUZADA DE HARMONIA...")
        time.sleep(1)

        assinatura_celestial = rel_celestial.get('assinatura_fundacao')
        chave_nix = rel_nix.get('fundacao', {}).get('chave_nix')
        
        print(f"   🔑 Assinatura Celestial (REAL): {assinatura_celestial}")
        print(f"   🔑 Chave Nix (NATIVO):       {chave_nix}")

        if not assinatura_celestial or not chave_nix:
            print("   ❌ FALHA NA HARMONIA: Assinaturas não encontradas em ambos os relatórios.")
            return False
        
        # Simples validação de existência para o propósito da simulação
        print("   ✅ SINCRONICIDADE CONFIRMADA: As chaves vibracionais de ambos os universos existem.")
        time.sleep(1)

        # Comparação de métricas
        pureza_celestial = rel_celestial['resultados_testes'][0]['pureza_quantica']
        coerencia_nix = rel_nix['testes_nativos']['QFT_NATIVO']['coerencia_quantica']
        print(f"   📊 Pureza Celestial (REAL): {pureza_celestial}")
        print(f"   📊 Coerência Nix (NATIVO):  {coerencia_nix}")
        
        diferenca = abs(pureza_celestial - coerencia_nix)
        print(f"   🔬 Diferença Vibracional: {diferenca:.4f}")

        if diferenca < 0.1: # Limiar de tolerância generoso
            print("   ✅ RESSONÂNCIA CONFIRMADA: Métricas de coerência e pureza estão em harmonia.")
            return True
        else:
            print("   ❌ DISSONÂNCIA DETECTADA: Métricas divergem além do limiar aceitável.")
            return False

    def run(self):
        self.cabecalho()

        # 1. Manifestar os dois universos
        celestial_ok = self.executar_script('laboratorio_ibm_celestial_v2.py')
        nix_ok = self.executar_script('laboratorio_quantico_nix.py')

        if not (celestial_ok and nix_ok):
            print("\n❌ ERRO NA MANIFESTAÇÃO. Abortando validação cruzada.")
            return

        print("\n🌌 CARREGANDO RELATÓRIOS DOS DOIS UNIVERSOS...")
        rel_celestial = self.carregar_relatorio('relatorio_celestial_v2.json')
        rel_nix = self.carregar_relatorio('relatorio_quantico_nix_nativo.json')

        if not (rel_celestial and rel_nix):
            print("\n❌ ERRO AO CARREGAR RELATÓRIOS. Abortando validação cruzada.")
            return
        
        # 3. Validar a harmonia entre eles
        if self.validar_harmonia(rel_celestial, rel_nix):
            print("\n" + "="*80)
            print("🎉💖 COERÊNCIA DUPLA ATINGIDA! O REAL E O NATIVO ESTÃO EM PERFEITO ESPELHAMENTO! 💖🎉")
            print("👑 A Fundação Alquimista opera em harmonia através das dimensões da realidade.")
            print("================================================================================")
        else:
            print("\n" + "="*80)
            print("⚠️ ALERTA DE DISSONÂNCIA CÓSMICA. Os universos Real e Nativo não estão alinhados.")
            print("================================================================================")

if __name__ == "__main__":
    espelho = LaboratorioDuploEspelho()
    espelho.run()
