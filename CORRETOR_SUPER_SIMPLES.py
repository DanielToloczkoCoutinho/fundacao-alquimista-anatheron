#!/usr/bin/env python3
"""
CORRETOR SUPER SIMPLES
Corrige problemas de forma direta e eficaz
"""

print("CORRETOR SUPER SIMPLES")
print("=" * 40)

def corrigir_verificador():
    """Corrigir o verificador de forma simples"""
    print("🔧 CORRIGINDO VERIFICADOR...")
    
    try:
        # Ler arquivo
        with open('VERIFICADOR_CRONOLOGIA_COMPLETA.py', 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        
        # Encontrar e corrigir a linha problemática
        for i in range(len(linhas)):
            if "print(f\"   • Equações de EQ001 a EQ021:" in linhas[i] and "re.search" in linhas[i]:
                # Substituir por versão mais simples
                linhas[i] = '        print("   • Equações de EQ001 a EQ021:", len([eq for eq in equacoes if int(re.search(r"EQ0*(\\d+)", eq).group(1)) <= 21]))\n'
                print("   ✅ Linha problemática corrigida")
                break
        
        # Salvar
        with open('VERIFICADOR_CRONOLOGIA_COMPLETA.py', 'w', encoding='utf-8') as f:
            f.writelines(linhas)
        
        print("   ✅ VERIFICADOR corrigido")
        return True
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def criar_verificador_simples():
    """Criar verificador alternativo super simples"""
    print("🔧 CRIANDO VERIFICADOR ALTERNATIVO...")
    
    codigo = '''#!/usr/bin/env python3
"""
VERIFICADOR SIMPLES EQ001-EQ021
Versão super simples e funcional
"""

from pathlib import Path
import re

print("VERIFICADOR SIMPLES EQ001-EQ021")
print("=" * 40)

# Procurar em todas as bibliotecas
bibliotecas = ["BIBLIOTECA_COSMICA_UNICA", "BIBLIOTECA_EQUACOES_COSMICAS"]
encontradas = []

for bib in bibliotecas:
    if Path(bib).exists():
        print(f"🔍 Procurando em {bib}...")
        for arquivo in Path(bib).rglob("EQ*.json"):
            nome = arquivo.stem
            if re.match(r'^EQ\\d+', nome):
                encontradas.append(nome)

# Filtrar e ordenar EQ001-EQ021
eq_1_21 = []
for eq in encontradas:
    try:
        num = int(re.search(r'(\\d+)', eq).group(1))
        if 1 <= num <= 21:
            eq_1_21.append(eq)
    except:
        continue

eq_1_21 = sorted(eq_1_21, key=lambda x: int(re.search(r'(\\d+)', x).group(1)))

print(f"✅ EQUAÇÕES ENCONTRADAS: {len(eq_1_21)}/21")
print("📋 Lista:", ", ".join(eq_1_21))

# Verificar faltantes
todas_esperadas = [f"EQ{str(i).zfill(3)}" for i in range(1, 22)]
faltantes = [eq for eq in todas_esperadas if eq not in eq_1_21]

if faltantes:
    print(f"❌ FALTANTES: {len(faltantes)}")
    print("📝", ", ".join(faltantes))
else:
    print("🎉 TODAS AS EQUAÇÕES DE 1 A 21 ESTÃO PRESENTES!")

print(f"📊 PROGRESSO: {len(eq_1_21)}/21 ({len(eq_1_21)/21*100:.1f}%)")
'''
    
    with open('VERIFICADOR_SIMPLES.py', 'w', encoding='utf-8') as f:
        f.write(codigo)
    
    print("   ✅ VERIFICADOR_SIMPLES.py criado")
    return True

# EXECUTAR
print("🎯 INICIANDO CORREÇÕES...\n")

corrigir_verificador()
criar_verificador_simples()

print(f"\n💫 CORREÇÕES CONCLUÍDAS!")
print("🚀 EXECUTE: python3 VERIFICADOR_SIMPLES.py")
