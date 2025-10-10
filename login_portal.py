#!/usr/bin/env python3
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
