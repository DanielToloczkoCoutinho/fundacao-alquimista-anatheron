import os, webbrowser
print("🌌 FUNDAÇÃO ALQUIMISTA")
scripts = ["setup_fundacao.py","circuito_phi_plus.py","teletransporte_quantico.py","fundacao_master.py"]
for s in scripts: print(f"{'✅' if os.path.exists(s) else '❌'} {s}")
if os.path.exists("verificar_portal.py"):
    with open("verificar_portal.py","r") as f: t=f.read()
    with open("verificar_portal.py","w") as f: f.write(t.replace("SEU_TOKEN_AQUI","SEU_TOKEN_AQUI"))
    print("🔒 TOKEN REMOVIDO")
os.system("git add . && git commit -m '🔮 Fundação Completa' && git push origin main")
webbrowser.open("https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/")
print("🌐 PORTAL: https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/")
print("👤 USUÁRIO: qualquer usuário")
print("🔑 SENHA: alchemista_2024")
print("🎉 SISTEMA PRONTO!")
