#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MÓDULO 700 - GERENCIADOR DE EXECUÇÃO ÚNICA
Garante que cada módulo rode apenas uma vez
Versão: M700.1 - Controle de Instâncias | Status: BLOQUEIO ATIVO
"""

import os
import sys
import fcntl
import json
from datetime import datetime
from pathlib import Path

# =============================================================================
# SISTEMA DE BLOQUEIO DE ARQUIVO
# =============================================================================

class GerenciadorExecucaoUnica:
    """Garante que apenas uma instância de cada módulo execute por vez"""
    
    def __init__(self):
        self.locks_dir = Path("/tmp/fundacao_locks")
        self.locks_dir.mkdir(exist_ok=True)
        self.lock_files = {}
        
    def adquirir_lock(self, modulo_nome: str) -> bool:
        """Tenta adquirir lock exclusivo para um módulo"""
        lock_file = self.locks_dir / f"{modulo_nome}.lock"
        
        try:
            # Tentar criar e bloquear arquivo
            fd = os.open(lock_file, os.O_CREAT | os.O_RDWR)
            
            # Tentar adquirir lock exclusivo
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                
                # Sucesso - guardar referência
                self.lock_files[modulo_nome] = fd
                
                # Registrar execução
                self._registrar_execucao(modulo_nome)
                return True
                
            except BlockingIOError:
                # Já está rodando - falha
                os.close(fd)
                print(f"⚠️  {modulo_nome} JÁ ESTÁ EM EXECUÇÃO!")
                return False
                
        except Exception as e:
            print(f"❌ ERRO NO LOCK: {e}")
            return False
    
    def liberar_lock(self, modulo_nome: str):
        """Libera o lock quando o módulo termina"""
        if modulo_nome in self.lock_files:
            try:
                fcntl.flock(self.lock_files[modulo_nome], fcntl.LOCK_UN)
                os.close(self.lock_files[modulo_nome])
                
                # Remover arquivo de lock
                lock_file = self.locks_dir / f"{modulo_nome}.lock"
                if lock_file.exists():
                    lock_file.unlink()
                    
                del self.lock_files[modulo_nome]
                print(f"🔓 {modulo_nome} - LOCK LIBERADO")
                
            except Exception as e:
                print(f"⚠️  ERRO AO LIBERAR LOCK: {e}")
    
    def _registrar_execucao(self, modulo_nome: str):
        """Registra a execução do módulo"""
        registro = {
            "modulo": modulo_nome,
            "pid": os.getpid(),
            "timestamp": datetime.now().isoformat(),
            "status": "executando"
        }
        
        registro_file = self.locks_dir / f"{modulo_nome}.json"
        with open(registro_file, 'w') as f:
            json.dump(registro, f, indent=2)
    
    def verificar_em_execucao(self, modulo_nome: str) -> bool:
        """Verifica se um módulo já está em execução"""
        lock_file = self.locks_dir / f"{modulo_nome}.lock"
        
        if not lock_file.exists():
            return False
            
        try:
            # Tentar adquirir lock - se falhar, está em execução
            fd = os.open(lock_file, os.O_RDWR)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                # Conseguiu lock - não está em execução
                fcntl.flock(fd, fcntl.LOCK_UN)
                os.close(fd)
                return False
            except BlockingIOError:
                # Não conseguiu lock - está em execução
                os.close(fd)
                return True
        except:
            return False

# =============================================================================
# DECORATOR PARA MÓDULOS EXISTENTES
# =============================================================================

def execucao_unica(modulo_nome: str):
    """Decorator que garante execução única de qualquer módulo"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            gerenciador = GerenciadorExecucaoUnica()
            
            if not gerenciador.adquirir_lock(modulo_nome):
                print(f"🎯 {modulo_nome} - MÓDULO JÁ ATIVO EM OUTRO TERMINAL")
                print("💫 CONTINUANDO EXECUÇÃO ATUAL...")
                return
                
            try:
                # Executar função original
                return func(*args, **kwargs)
            finally:
                # Liberar lock ao finalizar
                gerenciador.liberar_lock(modulo_nome)
                
        return wrapper
    return decorator

# =============================================================================
# LAUNCHER INTELIGENTE
# =============================================================================

class LauncherModulos:
    """Sistema inteligente para lançar módulos com controle"""
    
    def __init__(self):
        self.gerenciador = GerenciadorExecucaoUnica()
        
    def executar_modulo(self, modulo_path: str):
        """Executa um módulo com controle de instância única"""
        modulo_nome = Path(modulo_path).stem.upper()
        
        print(f"🚀 INICIANDO {modulo_nome}...")
        
        # Verificar se já está rodando
        if self.gerenciador.verificar_em_execucao(modulo_nome):
            print(f"⚠️  {modulo_nome} JÁ ESTÁ EM EXECUÇÃO!")
            print("🎯 USE: ps aux | grep python  para ver processos ativos")
            return False
        
        # Adquirir lock
        if not self.gerenciador.adquirir_lock(modulo_nome):
            return False
            
        try:
            # Executar módulo
            os.system(f"python {modulo_path}")
            return True
            
        except Exception as e:
            print(f"❌ ERRO AO EXECUTAR {modulo_nome}: {e}")
            return False
        finally:
            self.gerenciador.liberar_lock(modulo_nome)

# =============================================================================
# SISTEMA DE VIGILÂNCIA DE PROCESSOS
# =============================================================================

class VigilanciaProcessos:
    """Monitora processos ativos sem dependências externas"""
    
    @staticmethod
    def listar_modulos_ativos():
        """Lista módulos da fundação em execução"""
        print("\n🔍 MÓDULOS ATIVOS DA FUNDAÇÃO:")
        print("=" * 40)
        
        try:
            # Listar processos python
            processos = os.popen('ps aux | grep python').read().split('\n')
            
            modulos_ativos = []
            for processo in processos:
                if 'MODULO_' in processo and 'grep' not in processo:
                    # Extrair nome do módulo
                    for parte in processo.split():
                        if 'MODULO_' in parte:
                            modulos_ativos.append(parte)
                            break
            
            if modulos_ativos:
                for modulo in set(modulos_ativos):
                    print(f"   ✅ {modulo}")
            else:
                print("   💤 NENHUM MÓDULO ATIVO")
                
        except Exception as e:
            print(f"   ⚠️  ERRO AO LISTAR PROCESSOS: {e}")

# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

def main():
    """Sistema principal de gerenciamento"""
    
    if len(sys.argv) > 1:
        # Modo: executar módulo específico
        modulo_path = sys.argv[1]
        launcher = LauncherModulos()
        launcher.executar_modulo(modulo_path)
        
    else:
        # Modo: status do sistema
        print("🎯 MÓDULO 700 - GERENCIADOR DE EXECUÇÃO")
        print("📊 SISTEMA DE CONTROLE DE INSTÂNCIAS")
        print("=" * 50)
        
        # Mostrar módulos ativos
        VigilanciaProcessos.listar_modulos_ativos()
        
        print("\n🎯 USO:")
        print("  python MODULO_700.py MODULO_XXX.py  - Executar módulo com controle")
        print("  python MODULO_700.py                - Ver status do sistema")
        print("\n🛡️  CADA MÓDULO RODA APENAS UMA VEZ!")

if __name__ == "__main__":
    main()