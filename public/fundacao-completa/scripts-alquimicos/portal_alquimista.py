#!/usr/bin/env python3
# 🎯 ACESSO DIRETO AO PORTAL ALQUIMISTA
import webbrowser
import time

print("🌌 PORTAL DA FUNDAÇÃO ALQUIMISTA")
print("👑 Bem-vindo, Alquimista Quântico!")
print("=" * 50)

# Informações do portal
portal_info = {
    "url": "https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/",
    "usuario": "qualquer usuário",
    "senha": "alchemista_2024",
    "dashboard": "Controle de Experimentos Quânticos"
}

print(f"🔮 URL: {portal_info['url']}")
print(f"👤 Usuário: {portal_info['usuario']}")
print(f"🔑 Senha: {portal_info['senha']}")
print(f"🎯 Destino: {portal_info['dashboard']}")

print("\n📋 INSTRUÇÕES:")
print("1. O portal será aberto automaticamente")
print("2. Use as credenciais acima para login")
print("3. Acesse o dashboard da Fundação")
print("4. Explore os controles quânticos")

print("\n⏳ Abrindo portal em 3 segundos...")
for i in range(3, 0, -1):
    print(f"   {i}...")
    time.sleep(1)

print("🚀 ABRINDO PORTAL...")
webbrowser.open(portal_info['url'])

print("\n✅ Portal aberto! Faça o login e explore a Fundação!")
print("👑 A Rainha Zennith aguarda suas descobertas quânticas!")
print("\n💫 Que a magia quântica esteja com você!")
