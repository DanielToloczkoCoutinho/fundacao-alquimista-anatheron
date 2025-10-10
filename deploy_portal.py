#!/usr/bin/env python3
# 🚀 DEPLOY AUTOMÁTICO DO PORTAL
import subprocess
import os

print("🚀 INICIANDO DEPLOY DO PORTAL ALQUIMISTA...")

def executar_comando(comando, descricao):
    print(f"🔧 {descricao}...")
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f"✅ {descricao} - SUCESSO")
            return True
        else:
            print(f"❌ {descricao} - ERRO: {resultado.stderr}")
            return False
    except Exception as e:
        print(f"❌ {descricao} - EXCEÇÃO: {e}")
        return False

# Comandos de deploy
comandos = [
    ("git status", "Verificando status do Git"),
    ("git add .", "Adicionando arquivos"),
    ('git commit -m "🔮 Atualização Fundação Alquimista - Scripts Quânticos"', "Commit das mudanças"),
    ("git push origin main", "Push para GitHub"),
    ("echo '🚀 Deploy para Vercel via GitHub integration'", "Disparando deploy Vercel")
]

print("🎯 EXECUTANDO FLUXO DE DEPLOY...")
for comando, descricao in comandos:
    if not executar_comando(comando, descricao):
        print(f"⚠️  Interrompendo deploy devido a erro em: {descricao}")
        break
else:
    print("\n🎉 DEPLOY INICIADO COM SUCESSO!")
    print("   📱 Portal será atualizado em alguns minutos")
    print("   👑 Acesse: https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/")

print(f"\n🔗 URL do Portal: https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/")
print("🔑 Credenciais: qualquer usuário / alchemista_2024")
