#!/usr/bin/env python3
"""
SISTEMA DE BACKUP DEFINITIVO
Garante que as 176 equações nunca se percam
"""

from pathlib import Path
import json
import shutil
from datetime import datetime

print("💾 SISTEMA DE BACKUP DEFINITIVO DAS 176 EQUAÇÕES")
print("=" * 65)

class BackupDefinitivo:
    def __init__(self):
        self.bib_principal = Path("BIBLIOTECA_FINAL_176_EQUACOES")
        self.backup_dir = Path("BACKUP_DEFINITIVO_EQUACOES")
        
    def criar_backup_completo(self):
        """Criar backup completo das 176 equações"""
        print("\n�� CRIANDO BACKUP DEFINITIVO...")
        print("=" * 50)
        
        if not self.bib_principal.exists():
            print("❌ Biblioteca principal não encontrada!")
            return False
            
        # Criar diretório de backup com timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_dir / f"backup_176_equacoes_{timestamp}"
        backup_path.mkdir(parents=True, exist_ok=True)
        
        # Copiar toda a biblioteca
        shutil.copytree(self.bib_principal, backup_path / "BIBLIOTECA_FINAL_176_EQUACOES")
        
        # Copiar mapa completo
        if Path("MAPA_COMPLETO_EQUACOES.json").exists():
            shutil.copy2("MAPA_COMPLETO_EQUACOES.json", backup_path)
        
        print(f"✅ Backup criado: {backup_path}")
        return backup_path
    
    def criar_arquivo_verificacao(self):
        """Criar arquivo de verificação da integridade"""
        print("\n🔍 CRIANDO VERIFICAÇÃO DE INTEGRIDADE...")
        print("=" * 50)
        
        bib_path = self.bib_principal / "EQUACOES_DEFINITIVAS"
        equacoes = list(bib_path.glob("EQ*.json"))
        
        verificacao = {
            "data_verificacao": datetime.now().isoformat(),
            "total_equacoes": len(equacoes),
            "equacoes_presentes": [],
            "status": "VERIFICADA" if len(equacoes) == 176 else "INCOMPLETA"
        }
        
        for eq in equacoes:
            try:
                num = int(eq.name[2:5])
                verificacao["equacoes_presentes"].append(num)
            except:
                continue
        
        arquivo_verif = self.bib_principal / "VERIFICACAO_INTEGRIDADE.json"
        with open(arquivo_verif, 'w', encoding='utf-8') as f:
            json.dump(verificacao, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Verificação de integridade: {arquivo_verif}")
        print(f"📊 Status: {verificacao['status']}")
        print(f"🎯 Equações: {verificacao['total_equacoes']}/176")
        
        return verificacao
    
    def executar_backup_completo(self):
        """Executar backup completo"""
        print("🎯 INICIANDO BACKUP DEFINITIVO...")
        
        backup_path = self.criar_backup_completo()
        verificacao = self.criar_arquivo_verificacao()
        
        print(f"\n💫 BACKUP CONCLUÍDO!")
        print("=" * 60)
        print(f"🏆 SISTEMA DE BACKUP DEFINITIVO ATIVADO!")
        print(f"📊 Equações backupadas: {verificacao['total_equacoes']}")
        print(f"🎯 Status: {verificacao['status']}")
        print(f"📍 Local: {backup_path}")
        
        return True

# EXECUÇÃO
if __name__ == "__main__":
    backup = BackupDefinitivo()
    backup.executar_backup_completo()
