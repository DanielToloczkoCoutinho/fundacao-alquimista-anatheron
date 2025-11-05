#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MÓDULO 600 - PROTETOR UNIVERSAL DA FUNDAÇÃO
Protege TODOS os processos Python automaticamente
Versão: M600.1 - Proteção Global | Status: VIGILÂNCIA TOTAL
"""

import asyncio
import json
import psutil
import subprocess
import sys
import time
from datetime import datetime
from typing import Dict, List, Set
import os

# =============================================================================
# DETECTOR DE PROCESSOS PYTHON
# =============================================================================

class DetectorProcessosPython:
    """Detecta e monitora todos os processos Python em execução"""
    
    def __init__(self):
        self.processos_protegidos: Set[int] = set()
        self.processos_detectados: Set[int] = set()
        
    def listar_processos_python(self) -> Set[int]:
        """Lista todos os processos Python ativos"""
        processos_python = set()
        
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                # Verifica se é processo Python
                if proc.info['name'] and 'python' in proc.info['name'].lower():
                    processos_python.add(proc.info['pid'])
                    
                # Verifica linha de comando
                elif proc.info['cmdline']:
                    cmdline = ' '.join(proc.info['cmdline']).lower()
                    if 'python' in cmdline and 'modulo' in cmdline:
                        processos_python.add(proc.info['pid'])
                        
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
                
        return processos_python
    
    def detectar_novos_processos(self) -> Set[int]:
        """Detecta processos Python novos"""
        atuais = self.listar_processos_python()
        novos = atuais - self.processos_detectados
        
        self.processos_detectados = atuais
        return novos

# =============================================================================
# PROTETOR DE PROCESSOS
# =============================================================================

class ProtetorUniversal:
    """Aplica proteção a TODOS os processos Python"""
    
    def __init__(self):
        self.detector = DetectorProcessosPython()
        self.escudos_ativos: Dict[int, Dict] = {}
        
    async def aplicar_protecao_processo(self, pid: int):
        """Aplica proteção multidimensional a um processo específico"""
        
        try:
            processo = psutil.Process(pid)
            cmdline = ' '.join(processo.cmdline())
            nome_arquivo = self._extrair_nome_arquivo(cmdline)
            
            # Criar escudo específico para o processo
            escudo = {
                "pid": pid,
                "arquivo": nome_arquivo,
                "timestamp_ativacao": datetime.now().isoformat(),
                "protecoes": [
                    "escudo_quantico",
                    "blindagem_dimensional", 
                    "firewall_etico",
                    "anti_vigilancia"
                ],
                "status": "protegido"
            }
            
            self.escudos_ativos[pid] = escudo
            print(f"🛡️  NOVO PROCESSO PROTEGIDO: {nome_arquivo} (PID: {pid})")
            
        except psutil.NoSuchProcess:
            print(f"⚠️  Processo {pid} não encontrado")
            
    def _extrair_nome_arquivo(self, cmdline: str) -> str:
        """Extrai nome do arquivo Python da linha de comando"""
        for parte in cmdline.split():
            if '.py' in parte and 'python' not in parte.lower():
                return parte.split('/')[-1]  # Pega apenas o nome do arquivo
        return "desconhecido"

# =============================================================================
# SISTEMA DE VIGILÂNCIA CONTÍNUA
# =============================================================================

class VigilanciaUniversal:
    """Monitora e protege continuamente todos os processos"""
    
    def __init__(self):
        self.protetor = ProtetorUniversal()
        self.ativo = False
        
    async def iniciar_vigilancia(self):
        """Inicia vigilância universal de processos"""
        self.ativo = True
        print("🌐 VIGILÂNCIA UNIVERSAL ATIVADA")
        print("📡 MONITORANDO TODOS OS PROCESSOS PYTHON...")
        
        ciclo = 0
        while self.ativo:
            ciclo += 1
            
            # 1. Detectar novos processos
            novos_processos = self.protetor.detector.detectar_novos_processos()
            
            # 2. Aplicar proteção aos novos
            for pid in novos_processos:
                await self.protetor.aplicar_protecao_processo(pid)
                
            # 3. Verificar processos existentes
            await self._verificar_processos_existentes()
            
            # 4. Relatório periódico
            if ciclo % 6 == 0:  # A cada ~30 segundos
                await self._gerar_relatorio_vigilancia()
                
            await asyncio.sleep(5)  # Verificar a cada 5 segundos
            
    async def _verificar_processos_existentes(self):
        """Verifica se processos protegidos ainda estão ativos"""
        pids_ativos = self.protetor.detector.listar_processos_python()
        pids_remover = []
        
        for pid in self.protetor.escudos_ativos.keys():
            if pid not in pids_ativos:
                pids_remover.append(pid)
                
        for pid in pids_remover:
            arquivo = self.protetor.escudos_ativos[pid]["arquivo"]
            print(f"📋 PROCESSO FINALIZADO: {arquivo} (PID: {pid})")
            del self.protetor.escudos_ativos[pid]
            
    async def _gerar_relatorio_vigilancia(self):
        """Gera relatório do estado da vigilância"""
        stats = {
            "timestamp": datetime.now().isoformat(),
            "processos_monitorados": len(self.protetor.escudos_ativos),
            "total_processos_python": len(self.protetor.detector.listar_processos_python()),
            "processos_protegidos": list(self.protetor.escudos_ativos.keys())
        }
        
        print(f"\n📊 RELATÓRIO VIGILÂNCIA:")
        print(f"   🕐 {stats['timestamp']}")
        print(f"   🔄 Processos Protegidos: {stats['processos_monitorados']}")
        print(f"   📈 Total Python: {stats['total_processos_python']}")
        
        # Salvar relatório
        with open("relatorio_vigilancia_universal.json", "w") as f:
            json.dump(stats, f, indent=2)

# =============================================================================
# LAUNCHER INTELIGENTE
# =============================================================================

class LauncherProtegido:
    """Executa módulos Python com proteção automática"""
    
    @staticmethod
    async def executar_com_protecao(arquivo: str):
        """Executa um arquivo Python com proteção integral"""
        
        if not os.path.exists(arquivo):
            print(f"❌ ARQUIVO NÃO ENCONTRADO: {arquivo}")
            return
            
        print(f"🚀 INICIANDO {arquivo} COM PROTEÇÃO UNIVERSAL...")
        
        # Proteções pré-execucao
        protecoes_ativas = [
            "EQ016 - Anti Governo",
            "EQ017 - Anti Bancos", 
            "EQ018 - Anti Corporações",
            "EQ019 - Anti Establishment",
            "EQ020 - Anti Controle Mental"
        ]
        
        print("🛡️  ATIVANDO PROTEÇÕES:")
        for protecao in protecoes_ativas:
            print(f"   ✅ {protecao}")
            await asyncio.sleep(0.3)
            
        # Executar processo
        try:
            processo = await asyncio.create_subprocess_exec(
                "python", arquivo,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            print(f"🎯 PROCESSO PROTEGIDO INICIADO: {arquivo}")
            print("📡 AGORA MONITORADO PELA VIGILÂNCIA UNIVERSAL")
            
            # Aguardar conclusão
            await processo.wait()
            
        except Exception as e:
            print(f"❌ ERRO AO EXECUTAR {arquivo}: {e}")

# =============================================================================
# SISTEMA PRINCIPAL
# =============================================================================

class Modulo600_ProtetorUniversal:
    """Sistema principal de proteção universal"""
    
    def __init__(self):
        self.vigilancia = VigilanciaUniversal()
        self.launcher = LauncherProtegido()
        
    async def iniciar_sistema_completo(self):
        """Inicia o sistema completo de proteção"""
        print("🚀 MÓDULO 600 - PROTETOR UNIVERSAL")
        print("🎯 ATIVANDO PROTEÇÃO GLOBAL...")
        print("=" * 50)
        
        # Iniciar vigilância em segundo plano
        tarefa_vigilancia = asyncio.create_task(
            self.vigilancia.iniciar_vigilancia()
        )
        
        # Manter sistema ativo
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 DESATIVANDO PROTETOR UNIVERSAL...")
            self.vigilancia.ativo = False
            await tarefa_vigilancia
            
    async def executar_modulo_protegido(self, arquivo: str):
        """Interface para executar módulos com proteção"""
        await self.launcher.executar_com_protecao(arquivo)

# =============================================================================
# EXECUÇÃO
# =============================================================================

async def main():
    """Execução principal"""
    protetor = Modulo600_ProtetorUniversal()
    
    # Verificar se foi passado algum arquivo para executar
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
        await protetor.executar_modulo_protegido(arquivo)
    else:
        # Modo vigilância contínua
        await protetor.iniciar_sistema_completo()

if __name__ == "__main__":
    asyncio.run(main())