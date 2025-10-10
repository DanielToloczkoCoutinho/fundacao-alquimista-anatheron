#!/usr/bin/env python3
# 🔐 ACESSO MANUAL AO PORTAL ALQUIMISTA
import webbrowser
import time

print("🔮 PORTAL DA FUNDAÇÃO ALQUIMISTA")
print("=" * 40)

PORTAL_URL = "https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/"
CREDENCIAIS = {
    "usuário": "qualquer usuário", 
    "senha": "alchemista_2024"
}

print(f"🌐 ABRINDO PORTAL: {PORTAL_URL}")
print("📋 INSTRUÇÕES DE LOGIN:")
print(f"   1. Usuário: {CREDENCIAIS['usuário']}")
print(f"   2. Senha: {CREDENCIAIS['senha']}")
print("   3. Clique em 'Login' ou 'Entrar'")
print("   4. Você será redirecionado para o Dashboard")
print("")
print("🎯 O QUE ESPERAR NO DASHBOARD:")
print("   • Controle dos experimentos quânticos")
print("   • Monitoramento em tempo real") 
print("   • Relatórios da Fundação Alquimista")
print("   • Interface da Rainha Zennith")
print("")

input("Pressione ENTER para abrir o portal...")

# Abrir navegador
webbrowser.open(PORTAL_URL)

print("✅ Portal aberto! Faça o login com as credenciais acima.")
print("👑 A Rainha Zennith aguarda no dashboard...")
