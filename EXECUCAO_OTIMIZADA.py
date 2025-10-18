
#!/usr/bin/env python3
"""
⚡ EXECUTOR OTIMIZADO - FUNDAÇÃO ALQUIMISTA
🎯 Execução sequencial e eficiente de circuitos
🌌 Preparado para IBM Quantum
"""

import time
import sys
from pathlib import Path

print("⚡ INICIANDO EXECUÇÃO OTIMIZADA...")
print("=" * 45)

# Lista de circuitos para execução otimizada
circuitos = [
    "teletransporte_quantico.py",
    "circuito_psi_plus.py",
    "circuito_phi_minus.py", 
    "teste_bell.py",
    "CIRCUITOS_UNIFICADOS.py"
]

tempo_inicio = time.time()
resultados = {}

for i, circuito in enumerate(circuitos, 1):
    circuito_path = Path(circuito)
    if circuito_path.exists():
        print(f"\n🔧 [{i}/{len(circuitos)}] EXECUTANDO: {circuito}")
        
        try:
            import subprocess
            resultado = subprocess.run(
                [sys.executable, str(circuito_path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if resultado.returncode == 0:
                resultados[circuito] = "✅ SUCESSO"
                print(f"   ✅ EXECUTADO COM SUCESSO")
                
                # Mostrar linha de resultado se existir
                linhas = resultado.stdout.split('\n')
                for linha in linhas:
                    if any(termo in linha for termo in ['RESULTADOS', 'Correlação', 'BELL']):
                        print(f"   📊 {linha.strip()}")
                        break
            else:
                resultados[circuito] = f"❌ ERRO: {resultado.stderr[:100]}"
                print(f"   ❌ FALHA NA EXECUÇÃO")
                
        except subprocess.TimeoutExpired:
            resultados[circuito] = "⏰ TIMEOUT"
            print(f"   ⏰ TIMEOUT")
        except Exception as e:
            resultados[circuitos] = f"💥 EXCEÇÃO: {e}"
            print(f"   💥 EXCEÇÃO: {e}")
    else:
        resultados[circuito] = "🚫 NÃO ENCONTRADO"
        print(f"   🚫 ARQUIVO NÃO ENCONTRADO")

tempo_total = time.time() - tempo_inicio

print("\n" + "="*45)
print("🎉 EXECUÇÃO OTIMIZADA CONCLUÍDA!")
print(f"📊 RESUMO:")
for circuito, resultado in resultados.items():
    print(f"   • {circuito}: {resultado}")
print(f"⏱️  TEMPO TOTAL: {tempo_total:.2f}s")
print("🌌 PRONTO PARA IBM QUANTUM!")
