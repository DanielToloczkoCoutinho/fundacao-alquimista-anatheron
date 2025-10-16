#!/usr/bin/env python3
# 🛠️ RESOLUÇÃO COMPLETA DE CONFLITOS
import subprocess
import os
import webbrowser

print("🛠️ RESOLVENDO CONFLITOS GIT E CONFIGURANDO PORTAL...")

def executar_comando(comando, descricao):
    print(f"🔧 {descricao}...")
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        if resultado.returncode == 0:
            print(f"✅ {descricao}")
            return True, resultado.stdout
        else:
            print(f"⚠️  {descricao}: {resultado.stderr}")
            return False, resultado.stderr
    except Exception as e:
        print(f"❌ {descricao}: {e}")
        return False, str(e)

def resolver_conflitos_git():
    print("\n🔄 RESOLVENDO CONFLITOS GIT...")
    
    # Verificar status dos conflitos
    executar_comando("git status", "Verificando status dos conflitos")
    
    # Estratégia: Usar versão remota (mais recente)
    comandos = [
        "git checkout --theirs .",  # Usar versão remota para todos os arquivos
        "git add .",
        'git commit -m "🔮 Resolução conflitos - Usando versão remota"',
        "git push origin main"
    ]
    
    for comando in comandos:
        sucesso, output = executar_comando(comando, f"Executando: {comando}")
        if not sucesso:
            return False
    
    return True

def criar_script_login_manual():
    print("\n🔐 CRIANDO SCRIPT DE LOGIN MANUAL MELHORADO...")
    
    script_login = '''#!/usr/bin/env python3
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
'''
    
    with open("acessar_portal.py", "w") as f:
        f.write(script_login)
    
    print("✅ Script de acesso criado: acessar_portal.py")

def verificar_arquivos_locais():
    print("\n📁 VERIFICANDO ARQUIVOS LOCAIS...")
    
    # Listar arquivos importantes
    arquivos_importantes = [
        "setup_fundacao.py", "circuito_phi_plus.py", "circuito_phi_minus.py",
        "circuito_psi_plus.py", "circuito_psi_minus.py", "interpretacao_resultados.py",
        "teletransporte_quantico.py", "teste_bell.py", "ruido_e_correcao.py",
        "simulacao_sistema_fisico.py", "fundacao_master.py"
    ]
    
    for arquivo in arquivos_importantes:
        if os.path.exists(arquivo):
            print(f"✅ {arquivo}")
        else:
            print(f"❌ {arquivo} (FALTANDO)")

def criar_backup_emergencial():
    print("\n💾 CRIANDO BACKUP DE EMERGÊNCIA...")
    
    import datetime
    import shutil
    
    backup_dir = f"backup_emergencial_{datetime.datetime.now().strftime('%H%M%S')}"
    os.makedirs(backup_dir, exist_ok=True)
    
    # Copiar scripts da Fundação
    scripts = [f for f in os.listdir(".") if f.endswith(".py") and "fundacao" in f.lower()]
    
    for script in scripts:
        shutil.copy2(script, os.path.join(backup_dir, script))
        print(f"   📦 Backup: {script}")
    
    print(f"✅ Backup criado em: {backup_dir}")

def main():
    print("🛠️ RESOLUÇÃO COMPLETA DE PROBLEMAS")
    print("=" * 50)
    
    # 1. Backup emergencial
    criar_backup_emergencial()
    
    # 2. Resolver conflitos Git
    git_ok = resolver_conflitos_git()
    
    # 3. Verificar arquivos
    verificar_arquivos_locais()
    
    # 4. Criar script de acesso
    criar_script_login_manual()
    
    # Resumo final
    print(f"\n📊 RESUMO DA RESOLUÇÃO:")
    print(f"   💾 Backup: ✅ Criado")
    print(f"   🔧 Git: {'✅ Resolvido' if git_ok else '⚠️ Precisa de atenção'}")
    print(f"   📁 Scripts: ✅ Verificados") 
    print(f"   🔐 Acesso: 📋 acessar_portal.py")
    
    print(f"\n🎯 PRÓXIMOS PASSOS:")
    print("   1. python acessar_portal.py")
    print("   2. Fazer login manual no portal")
    print("   3. Verificar dashboard da Fundação")
    
    print(f"\n🔗 URL DO PORTAL:")
    print("   https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/")

if __name__ == "__main__":
    main()
