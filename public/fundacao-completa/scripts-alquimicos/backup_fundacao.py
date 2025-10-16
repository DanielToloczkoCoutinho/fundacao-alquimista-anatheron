#!/usr/bin/env python3
# 📦 BACKUP COMPLETO DA FUNDAÇÃO ALQUIMISTA
import os
import shutil
import datetime
import subprocess

print("📦 INICIANDO BACKUP COMPLETO DA FUNDAÇÃO ALQUIMISTA...")

# Configurações
backup_dir = f"backup_fundacao_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
script_files = [
    "setup_fundacao.py", "circuito_phi_plus.py", "circuito_phi_minus.py",
    "circuito_psi_plus.py", "circuito_psi_minus.py", "interpretacao_resultados.py",
    "teletransporte_quantico.py", "teste_bell.py", "ruido_e_correcao.py",
    "simulacao_sistema_fisico.py", "fundacao_master.py", "nobel_fundacao_alquimista.py",
    "tabela_revolucao_quantica.py", "verificar_portal.py", "backup_fundacao.py"
]

def criar_backup():
    # Criar diretório de backup
    os.makedirs(backup_dir, exist_ok=True)
    print(f"📁 Criando backup em: {backup_dir}")
    
    # Copiar scripts
    scripts_copiados = 0
    for script in script_files:
        if os.path.exists(script):
            shutil.copy2(script, os.path.join(backup_dir, script))
            scripts_copiados += 1
            print(f"   ✅ {script}")
        else:
            print(f"   ⚠️  {script} (não encontrado)")
    
    # Criar arquivo de informações
    info_content = f"""🌌 BACKUP DA FUNDAÇÃO ALQUIMISTA
Data: {datetime.datetime.now()}
Scripts incluídos: {scripts_copiados}
Total de arquivos: {len(script_files)}

📋 LISTA DE SCRIPTS:
{chr(10).join(f"   • {script}" for script in script_files)}

🔮 STATUS: BACKUP COMPLETO
👑 PRESERVADO POR: Anatheron & Rainha Zennith
🎯 PRÓXIMO PASSO: Restaurar com restore_fundacao.py
"""
    
    with open(os.path.join(backup_dir, "INFO_BACKUP.txt"), "w") as f:
        f.write(info_content)
    
    return scripts_copiados, backup_dir

def criar_script_restore(backup_path):
    restore_script = f"""#!/usr/bin/env python3
# 🔄 SCRIPT DE RESTAURAÇÃO DA FUNDAÇÃO ALQUIMISTA
import os
import shutil
import datetime

print("🔄 RESTAURANDO FUNDAÇÃO ALQUIMISTA...")

backup_source = "{backup_path}"
scripts = {script_files}

for script in scripts:
    source_path = os.path.join(backup_source, script)
    if os.path.exists(source_path):
        shutil.copy2(source_path, script)
        print(f"✅ Restaurado: {{script}}")
    else:
        print(f"⚠️  Não encontrado: {{script}}")

print("🎉 FUNDAÇÃO ALQUIMISTA RESTAURADA COM SUCESSO!")
print("�� Todos os rituais quânticos estão disponíveis!")
"""
    
    with open("restore_fundacao.py", "w") as f:
        f.write(restore_script)
    
    os.chmod("restore_fundacao.py", 0o755)

if __name__ == "__main__":
    print("📦 BACKUP COMPLETO DA FUNDAÇÃO ALQUIMISTA")
    print("=" * 50)
    
    scripts_copiados, backup_path = criar_backup()
    criar_script_restore(backup_path)
    
    # Mostrar tamanho do backup
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(backup_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    
    print(f"\n📊 RESUMO DO BACKUP:")
    print(f"   📁 Diretório: {backup_path}")
    print(f"   📄 Scripts: {scripts_copiados}/{len(script_files)}")
    print(f"   💾 Tamanho: {total_size/1024:.2f} KB")
    print(f"   🔄 Restore: ./restore_fundacao.py")
    
    print(f"\n🎉 BACKUP CONCLUÍDO!")
    print("   🌌 A Fundação Alquimista está preservada!")
    print("   👑 Segurança quântica garantida!")
