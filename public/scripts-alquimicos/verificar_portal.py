#!/usr/bin/env python3
# 🔮 VERIFICADOR DO PORTAL DA FUNDAÇÃO ALQUIMISTA
import requests
import webbrowser
import time

print("🌐 INICIANDO VERIFICAÇÃO DO PORTAL ALQUIMISTA...")

# URLs do portal
portal_url = "https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/"
github_repo = "https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
firebase_console = "https://console.firebase.google.com/project/studio-4265982502-21871"

credenciais = {
    "usuário": "qualquer usuário",
    "senha": "alchemista_2024"
}

def testar_portal():
    print(f"🔗 Testando acesso ao portal: {portal_url}")
    try:
        response = requests.get(portal_url, timeout=10)
        if response.status_code == 200:
            print("✅ PORTAL ACESSÍVEL - Status 200 OK")
            return True
        else:
            print(f"⚠️  Portal retornou status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ ERRO ao acessar portal: {e}")
        return False

def abrir_navegador():
    print("🌍 Abrindo portal no navegador...")
    webbrowser.open(portal_url)
    print("📋 Credenciais para teste:")
    print(f"   👤 Usuário: {credenciais['usuário']}")
    print(f"   🔑 Senha: {credenciais['senha']}")
    print("   🎯 Destino esperado: Dashboard da Fundação")

def verificar_github():
    print(f"\n🔗 Verificando repositório GitHub...")
    try:
        headers = {
            "Authorization": "token SEU_TOKEN_AQUI",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(
            "https://api.github.com/repos/DanielToloczkoCoutinho/fundacao-alquimista-anatheron",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            repo_data = response.json()
            print(f"✅ REPOSITÓRIO GITHUB ACESSÍVEL")
            print(f"   📁 Nome: {repo_data.get('name', 'N/A')}")
            print(f"   🌟 Stars: {repo_data.get('stargazers_count', 0)}")
            print(f"   🍴 Forks: {repo_data.get('forks_count', 0)}")
            print(f"   📝 URL: {repo_data.get('html_url', 'N/A')}")
            return True
        else:
            print(f"❌ GitHub API retornou status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ ERRO ao acessar GitHub: {e}")
        return False

if __name__ == "__main__":
    print("🔮 VERIFICAÇÃO COMPLETA DO PORTAL ALQUIMISTA")
    print("=" * 50)
    
    # Testar portal
    portal_ok = testar_portal()
    
    # Testar GitHub
    github_ok = verificar_github()
    
    # Abrir navegador
    print(f"\n🎯 ABRINDO PORTAL AUTOMATICAMENTE...")
    abrir_navegador()
    
    # Resumo
    print(f"\n📊 RESUMO DA VERIFICAÇÃO:")
    print(f"   🌐 Portal Web: {'✅ ONLINE' if portal_ok else '❌ OFFLINE'}")
    print(f"   💾 GitHub Repo: {'✅ ACESSÍVEL' if github_ok else '❌ INACESSÍVEL'}")
    print(f"   🔥 Firebase: 🔗 {firebase_console}")
    
    if portal_ok and github_ok:
        print(f"\n🎉 PORTAL DA FUNDAÇÃO OPERACIONAL!")
        print("   👑 A Rainha Zennith aguarda no dashboard...")
    else:
        print(f"\n⚠️  Verifique as configurações do portal")
    
    print(f"\n🔗 LINKS IMPORTANTES:")
    print(f"   📱 Portal: {portal_url}")
    print(f"   💾 Código: {github_repo}")
    print(f"   🛠️  Console: {firebase_console}")
