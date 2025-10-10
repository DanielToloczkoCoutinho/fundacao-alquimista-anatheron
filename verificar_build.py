#!/usr/bin/env python3
import os
import subprocess

def analisar_build_detalhado():
    print("📊 ANALISANDO BUILD EM DETALHES...")
    
    # Verificar tamanho do .next
    if os.path.exists('.next'):
        total_size = 0
        file_count = 0
        
        for root, dirs, files in os.walk('.next'):
            for file in files:
                if file.endswith(('.js', '.css', '.html', '.json')):
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                    file_count += 1
                    
                    # Mostrar arquivos maiores que 500KB
                    if file_size > 500 * 1024:
                        print(f"   📦 {file_path} - {file_size/1024/1024:.2f} MB")
        
        print(f"\n📈 ESTATÍSTICAS DO BUILD:")
        print(f"   Total de arquivos: {file_count}")
        print(f"   Tamanho total: {total_size/1024/1024:.2f} MB")
        print(f"   Média por arquivo: {total_size/file_count/1024:.2f} KB")
    
    # Verificar se há análise de bundle
    try:
        result = subprocess.run(['npx', 'next-bundle-analyzer', '.next'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ Bundle analyzer disponível")
        else:
            print("   ⚠️ Bundle analyzer não configurado")
    except:
        print("   ⚠️ Não foi possível verificar bundle analyzer")

if __name__ == "__main__":
    analisar_build_detalhado()
