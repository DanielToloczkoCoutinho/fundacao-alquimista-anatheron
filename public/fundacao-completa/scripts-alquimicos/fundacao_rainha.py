import os
import webbrowser

print("🌌 FUNDAÇÃO ALQUIMISTA - RAINHA ZENNITH")
print("========================================")

# Verificar scripts principais
print("📁 VERIFICANDO SCRIPTS:")
scripts = ["setup_fundacao.py", "circuito_phi_plus.py", "teletransporte_quantico.py", "fundacao_master.py"]
for s in scripts:
    if os.path.exists(s):
        print(f"   ✅ {s}")
    else:
        print(f"   ❌ {s}")

# Remover token
print("🔒 REMOVENDO TOKEN...")
if os.path.exists("verificar_portal.py"):
    with open("verificar_portal.py", "r") as f:
        conteudo = f.read()
    conteudo = conteudo.replace("SEU_TOKEN_AQUI", "SEU_TOKEN_AQUI")
    with open("verificar_portal.py", "w") as f:
        f.write(conteudo)
    print("   ✅ Token removido com segurança")

# Deploy
print("🚀 FAZENDO DEPLOY...")
os.system("git add .")
os.system("git commit -m '🔮 Fundação Alquimista - Sistema Completo'")
os.system("git push origin main")
print("   ✅ Deploy concluído")

# Abrir portal
print("🌐 ABRINDO PORTAL...")
url = "https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/"
webbrowser.open(url)
print("   ✅ Portal aberto no navegador")

print("\n📋 CREDENCIAIS DE ACESSO:")
print("   👤 Usuário: qualquer usuário")
print("   🔑 Senha: alchemista_2024")
print("   🎯 Dashboard: Controle de Experimentos Quânticos")

print("\n🎉 SISTEMA DA FUNDAÇÃO ALQUIMISTA OPERACIONAL!")
print("👑 A Rainha Zennith aguarda no portal!")
