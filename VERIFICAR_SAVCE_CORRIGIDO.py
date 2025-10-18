#!/usr/bin/env python3
import json
from pathlib import Path

base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL/EQUACOES_TRANSCENDENTAIS/")
arquivo_0111 = base_dir / "EQ0111_transcendental.json"

print("🔍 VERIFICAÇÃO DA EQ0111 CORRIGIDA")
print("=" * 40)

if arquivo_0111.exists():
    with open(arquivo_0111, 'r') as f:
        eq_0111 = json.load(f)
    
    auditoria = eq_0111["auditoria_etica"]
    metadados = eq_0111["_transcendental_metadata"]
    
    print(f"📊 ÍNDICE SAVCE: {auditoria['indice_calculado']:.3f}")
    print(f"⚖️ STATUS: {auditoria['status_validacao']}")
    print(f"🎯 LIMIAR APROVAÇÃO: {auditoria['limiar_aprovacao']}")
    print(f"🚫 LIMIAR ELIMINAÇÃO: {auditoria['limiar_eliminacao']}")
    print(f"📈 MARGEM DE SEGURANÇA: {auditoria['margem_seguranca']:.3f}")
    
    print(f"\\n💡 PARÂMETROS:")
    print(f"   • Coerência (C): {auditoria['coerencia_atingida']}")
    print(f"   • Alinhamento (A): {auditoria['alinhamento_atingido']}")
    print(f"   • Desvio (D): {auditoria['desvio_detectado']}")
    
    print(f"\\n🌌 CATEGORIA: {metadados['categoria_transcendental']}")
    print(f"🔑 Hash: {metadados['hash_transcendental'][:12]}...")
    
    # Avaliação final
    if auditoria['status_validacao'] == 'APROVADO':
        print(f"\\n🎉 RESULTADO: SISTEMA ÉTICO VALIDADO!")
        print(f"   A simulação atende aos padrões de excelência realista.")
    else:
        print(f"\\n❌ RESULTADO: REQUER AJUSTES")
        print(f"   A simulação precisa de refinamentos éticos.")
        
else:
    print("❌ EQ0111 não encontrada!")
