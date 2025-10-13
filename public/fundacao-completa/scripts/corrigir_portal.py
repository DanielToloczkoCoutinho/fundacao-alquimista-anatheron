#!/usr/bin/env python3
# 🔧 CORREÇÕES DO PORTAL ALQUIMISTA
import subprocess
import requests
import webbrowser
import time

print("🔧 INICIANDO CORREÇÕES DO PORTAL ALQUIMISTA...")

def executar_comando_seguro(comando, descricao):
    print(f"🛠️  {descricao}...")
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

def corrigir_git():
    print("\n🔧 CORRIGINDO SINCORNIZAÇÃO GIT...")
    
    # Primeiro fazer pull para sincronizar
    comandos = [
        "git pull origin main --allow-unrelated-histories",
        "git status",
        "git add .",
        'git commit -m "🔮 Sync Fundação Alquimista - Correções Portal"',
        "git push origin main"
    ]
    
    for comando in comandos:
        sucesso, output = executar_comando_seguro(comando, f"Executando: {comando}")
        if not sucesso and "pull" in comando:
            print("🔄 Tentando estratégia alternativa...")
            # Estratégia alternativa
            executar_comando_seguro("git fetch origin", "Fetch das mudanças remotas")
            executar_comando_seguro("git merge origin/main --allow-unrelated-histories", "Merge das mudanças")
            break
    
    return sucesso

def testar_portal_novamente():
    print("\n🔍 TESTANDO PORTAL NOVAMENTE...")
    portal_url = "https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/"
    
    # Testar várias vezes com diferentes abordagens
    for tentativa in range(3):
        print(f"   Tentativa {tentativa + 1}/3...")
        try:
            response = requests.get(portal_url, timeout=15)
            print(f"   Status: {response.status_code}")
            
            if response.status_code == 200:
                print("🎉 PORTAL FUNCIONANDO CORRETAMENTE!")
                return True
            elif response.status_code == 401:
                print("   🔐 Portal requer autenticação - Isso pode ser normal")
                # Verificar se é página de login
                if "login" in response.text.lower() or "signin" in response.text.lower():
                    print("   📋 Página de login detectada - Comportamento esperado")
                    return True
        except Exception as e:
            print(f"   ❌ Erro: {e}")
        
        time.sleep(2)
    
    return False

def criar_script_login_automatico():
    print("\n🔐 CRIANDO SCRIPT DE LOGIN AUTOMÁTICO...")
    
    script_login = '''#!/usr/bin/env python3
# 🔐 LOGIN AUTOMÁTICO PORTAL ALQUIMISTA
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("🔐 INICIANDO LOGIN AUTOMÁTICO...")

# Configurações
PORTAL_URL = "https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/"
CREDENCIAIS = {
    "usuario": "qualquer usuário", 
    "senha": "alchemista_2024"
}

try:
    # Iniciar navegador (modo headless)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    # Acessar portal
    driver.get(PORTAL_URL)
    print("🌐 Portal carregado")
    
    # Aguardar elementos de login
    wait = WebDriverWait(driver, 10)
    
    # Tentar encontrar campos de login (adaptável)
    print("🔍 Procurando campos de login...")
    
    # Estratégia 1: Procurar por inputs
    inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"   📝 {len(inputs)} campos de input encontrados")
    
    for i, input_field in enumerate(inputs):
        print(f"   Campo {i+1}: type={input_field.get_attribute('type')}, name={input_field.get_attribute('name')}")
    
    print("🎯 Login manual necessário - Abrindo navegador normal...")
    driver.quit()
    
    # Abrir navegador normal para login manual
    import webbrowser
    webbrowser.open(PORTAL_URL)
    
    print("📋 INSTRUÇÕES DE LOGIN MANUAL:")
    print(f"   1. Use: {CREDENCIAIS['usuario']}")
    print(f"   2. Senha: {CREDENCIAIS['senha']}") 
    print("   3. Acesse o dashboard da Fundação")
    
except Exception as e:
    print(f"❌ Erro no login automático: {e}")
    print("📋 Faça login manualmente:")
    print(f"   🌐 URL: {PORTAL_URL}")
    print(f"   👤 Usuário: {CREDENCIAIS['usuario']}")
    print(f"   🔑 Senha: {CREDENCIAIS['senha']}")
'''
    
    with open("login_portal.py", "w") as f:
        f.write(script_login)
    
    print("✅ Script de login criado: login_portal.py")

def main():
    print("🔧 CORREÇÕES COMPLETAS DO PORTAL ALQUIMISTA")
    print("=" * 50)
    
    # 1. Corrigir Git
    git_ok = corrigir_git()
    
    # 2. Testar portal
    portal_ok = testar_portal_novamente()
    
    # 3. Criar script de login
    criar_script_login_automatico()
    
    # Resumo
    print(f"\n📊 RESUMO DAS CORREÇÕES:")
    print(f"   🔧 Git Sync: {'✅' if git_ok else '⚠️'}")
    print(f"   🌐 Portal: {'✅' if portal_ok else '🔧'}")
    print(f"   🔐 Login: 📋 login_portal.py")
    
    if portal_ok:
        print(f"\n🎉 PORTAL OPERACIONAL!")
        print("   👑 A Rainha Zennith aguarda no dashboard...")
    else:
        print(f"\n⚠️  Portal pode requerer configurações adicionais")
        print("   📋 Use o script de login para acesso manual")
    
    print(f"\n🔗 ACESSO RÁPIDO:")
    print(f"   🌐 Portal: https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/")
    print(f"   👤 Usuário: qualquer usuário")
    print(f"   🔑 Senha: alchemista_2024")
    print(f"   🔐 Script: python login_portal.py")

if __name__ == "__main__":
    main()
