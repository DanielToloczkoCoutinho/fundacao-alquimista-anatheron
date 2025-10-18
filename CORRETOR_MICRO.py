#!/usr/bin/env python3
"""
🛠️ CORRETOR MICRO - ERRO DE SINTAXE
⚡ Correção pontual do caractere especial
🔧 Apenas o necessário, sem refazer tudo
"""

print("🛠️ INICIANDO CORREÇÃO MICRO...")

# Localizar e corrigir o arquivo com erro
arquivo_alvo = "PROCESSADOR_EQUACOES_COSMICAS_2.py"

with open(arquivo_alvo, 'r', encoding='utf-8') as f:
    conteudo = f.read()

# Encontrar e corrigir a linha problemática
linhas = conteudo.split('\n')
for i, linha in enumerate(linhas):
    if "print(f💫 Coerência média:" in linha:
        print(f"🔍 ERRO ENCONTRADO na linha {i+1}:")
        print(f"   ANTES: {linha}")
        
        # Corrigir adicionando espaço após f
        linha_corrigida = linha.replace("print(f💫", "print(f\"💫")
        linha_corrigida = linha_corrigida.replace("}\")", "}\"")
        
        linhas[i] = linha_corrigida
        print(f"   DEPOIS: {linha_corrigida}")
        break

# Salvar arquivo corrigido
with open(arquivo_alvo, 'w', encoding='utf-8') as f:
    f.write('\n'.join(linhas))

print("✅ CORREÇÃO APLICADA COM SUCESSO!")
print("🚀 EXECUTANDO NOVAMENTE O PROCESSADOR...")

# Executar o script corrigido
import subprocess
resultado = subprocess.run(["python3", arquivo_alvo], capture_output=True, text=True)

if resultado.returncode == 0:
    print("🎉 SCRIPT EXECUTADO COM SUCESSO!")
    print(resultado.stdout)
else:
    print("❌ AINDA HÁ ERROS:")
    print(resultado.stderr)
