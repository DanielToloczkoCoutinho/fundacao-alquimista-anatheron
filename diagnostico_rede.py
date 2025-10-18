#!/usr/bin/env python3
"""
🔍 DIAGNÓSTICO DE REDE - FUNDAÇÃO ALQUIMISTA
🌐 Testando conectividade e soluções alternativas
"""

import socket
import requests
import subprocess
import os

print("🔍 DIAGNÓSTICO DE REDE - FUNDAÇÃO ALQUIMISTA")
print("=" * 50)

def testar_dns(hostname):
    """Testar resolução DNS"""
    print(f"🔍 Testando DNS para: {hostname}")
    try:
        ip = socket.gethostbyname(hostname)
        print(f"   ✅ DNS funciona: {hostname} → {ip}")
        return True
    except socket.gaierror as e:
        print(f"   ❌ DNS falhou: {e}")
        return False

def testar_conectividade(hostname):
    """Testar conectividade com diferentes métodos"""
    print(f"\n🌐 Testando conectividade com: {hostname}")
    
    # Método 1: Socket RAW (pode não funcionar no Nix)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((hostname, 443))
            print("   ✅ Conectividade via socket: OK")
    except Exception as e:
        print(f"   ❌ Socket falhou: {e}")
    
    # Método 2: Requests com IP direto
    try:
        # Primeiro resolver IP
        ip = socket.gethostbyname(hostname)
        url = f"https://{ip}"
        response = requests.get(url, timeout=10, verify=False)
        print(f"   ✅ Conectividade via IP {ip}: Status {response.status_code}")
    except Exception as e:
        print(f"   ❌ Conectividade IP direto: {e}")

def testar_endpoints_ibm():
    """Testar diferentes endpoints do IBM Quantum"""
    endpoints = [
        "quantum-computing.ibm.com",
        "auth.quantum-computing.ibm.com", 
        "api.quantum-computing.ibm.com"
    ]
    
    print(f"\n�� TESTANDO ENDPOINTS IBM:")
    for endpoint in endpoints:
        testar_dns(endpoint)

def solucoes_alternativas():
    """Propor soluções alternativas"""
    print(f"\n💡 SOLUÇÕES ALTERNATIVAS:")
    
    print("1. 🛠️  USAR IP DIRETO:")
    print("   Podemos tentar conectar usando o IP diretamente")
    
    print("2. 🔄 CONFIGURAR DNS ALTERNATIVO:")
    print("   Usar Google DNS (8.8.8.8) no sistema")
    
    print("3. 🌐 TESTAR FORA DO NIX:")
    print("   Sair do nix-shell e testar conectividade")
    
    print("4. 🐳 USAR CONTAINER DOCKER:")
    print("   Executar em ambiente com rede completa")

# Executar diagnóstico
print("🚀 INICIANDO DIAGNÓSTICO DE REDE...")

# Testar DNS básico primeiro
testar_dns("google.com")
testar_dns("github.com")

# Testar endpoints IBM
testar_endpoints_ibm()

# Testar conectividade
testar_conectividade("quantum-computing.ibm.com")

# Mostrar soluções
solucoes_alternativas()

print(f"\n🔍 DIAGNÓSTICO COMPLETO!")
print("💡 O problema é de REDE/DNS no ambiente Nix")
