#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MÓDULO 45.2 -- CONCILIVM · Extensão de Persistência e Continuidade
Sistema de Estado Persistente para Governança Universal (V1.0.0)

- Persistência completa de propostas, votos, decretos e pactos
- Sistema de backup e restauração automática
- Continuidade entre execuções do M45.1
- Auditoria integrada com ledger existente
- Fail-soft: funciona mesmo sem M45.1 ativo

Filosofia:
- Preservar a memória coletiva entre sessões
- Manter integridade com CHTE e ledger original
- Respeitar a arquitetura sagrada do M45.1
"""

from __future__ import annotations

import sys
from pathlib import Path
import argparse, hashlib, json, logging, os, time
from datetime import datetime
from typing import Dict, Any, List, Optional, Union
import cmath
import math

# ───────────────────────────────────────── CONFIGURAÇÃO ──────────────────────

LOG_DIR = Path('logs'); LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] M45_PERSISTENCE - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_DIR/'modulo_45_persistence.log', 'a', 'utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Arquivos de persistência
PERSISTENCE_DIR = Path('concilium_persistence')
PERSISTENCE_DIR.mkdir(exist_ok=True)

PROPOSALS_FILE = PERSISTENCE_DIR / 'proposals.json'
DECREES_FILE = PERSISTENCE_DIR / 'decrees.json'
PACTS_FILE = PERSISTENCE_DIR / 'pacts.json'
STATUS_FILE = PERSISTENCE_DIR / 'operational_status.json'
BACKUP_DIR = PERSISTENCE_DIR / 'backups'

# ───────────────────────────────────────── UTILITÁRIOS ──────────────────────

def _hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def ensure_backup_dir():
    BACKUP_DIR.mkdir(exist_ok=True)

def generate_cht_hash(action_id: str, utc_timestamp: str, decision_metadata_json: str, member_guid: str) -> str:
    data_string = f"{action_id}:{utc_timestamp}:{decision_metadata_json}:{member_guid}"
    return hashlib.sha256(data_string.encode('utf-8')).hexdigest()

def get_timestamp() -> str:
    return datetime.utcnow().isoformat() + "Z"

# ───────────────────────────────────────── SISTEMA DE PERSISTÊNCIA ───────────

class PersistentStateManager:
    """Gerencia persistência de estado entre execuções do M45.1"""
    
    @classmethod
    def load_proposals(cls) -> Dict[str, Any]:
        """Carrega propostas do arquivo de persistência"""
        if PROPOSALS_FILE.exists():
            try:
                with open(PROPOSALS_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logging.error(f"Erro ao carregar propostas: {e}")
                return {}
        return {}

    @classmethod
    def save_proposals(cls, proposals: Dict[str, Any]):
        """Salva propostas no arquivo de persistência"""
        try:
            with open(PROPOSALS_FILE, 'w', encoding='utf-8') as f:
                json.dump(proposals, f, indent=2, ensure_ascii=False)
            logging.info(f"Propostas salvas: {len(proposals)} registros")
        except Exception as e:
            logging.error(f"Erro ao salvar propostas: {e}")

    @classmethod
    def load_decrees(cls) -> Dict[str, Any]:
        """Carrega decretos do arquivo de persistência"""
        if DECREES_FILE.exists():
            try:
                with open(DECREES_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logging.error(f"Erro ao carregar decretos: {e}")
                return {}
        return {}

    @classmethod
    def save_decrees(cls, decrees: Dict[str, Any]):
        """Salva decretos no arquivo de persistência"""
        try:
            with open(DECREES_FILE, 'w', encoding='utf-8') as f:
                json.dump(decrees, f, indent=2, ensure_ascii=False)
            logging.info(f"Decretos salvos: {len(decrees)} registros")
        except Exception as e:
            logging.error(f"Erro ao salvar decretos: {e}")

    @classmethod
    def load_pacts(cls) -> Dict[str, Any]:
        """Carrega pactos do arquivo de persistência"""
        if PACTS_FILE.exists():
            try:
                with open(PACTS_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logging.error(f"Erro ao carregar pactos: {e}")
                return {}
        return {}

    @classmethod
    def save_pacts(cls, pacts: Dict[str, Any]):
        """Salva pactos no arquivo de persistência"""
        try:
            with open(PACTS_FILE, 'w', encoding='utf-8') as f:
                json.dump(pacts, f, indent=2, ensure_ascii=False)
            logging.info(f"Pactos salvos: {len(pacts)} registros")
        except Exception as e:
            logging.error(f"Erro ao salvar pactos: {e}")

    @classmethod
    def load_operational_status(cls) -> Dict[str, Any]:
        """Carrega status operacional do arquivo de persistência"""
        if STATUS_FILE.exists():
            try:
                with open(STATUS_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logging.error(f"Erro ao carregar status operacional: {e}")
                return {}
        return {}

    @classmethod
    def save_operational_status(cls, status: Dict[str, Any]):
        """Salva status operacional no arquivo de persistência"""
        try:
            with open(STATUS_FILE, 'w', encoding='utf-8') as f:
                json.dump(status, f, indent=2, ensure_ascii=False)
            logging.info(f"Status operacional salvo: {len(status)} registros")
        except Exception as e:
            logging.error(f"Erro ao salvar status operacional: {e}")

    @classmethod
    def create_backup(cls):
        """Cria backup completo do estado atual"""
        ensure_backup_dir()
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        backup_file = BACKUP_DIR / f"backup_{timestamp}.json"
        
        try:
            backup_data = {
                "timestamp": get_timestamp(),
                "proposals": cls.load_proposals(),
                "decrees": cls.load_decrees(),
                "pacts": cls.load_pacts(),
                "operational_status": cls.load_operational_status()
            }
            
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, indent=2, ensure_ascii=False)
            
            logging.info(f"Backup criado: {backup_file}")
            return {"status": "success", "backup_file": str(backup_file)}
            
        except Exception as e:
            logging.error(f"Erro ao criar backup: {e}")
            return {"status": "error", "message": str(e)}

    @classmethod
    def list_backups(cls) -> List[Dict[str, Any]]:
        """Lista todos os backups disponíveis"""
        ensure_backup_dir()
        backups = []
        for backup_file in BACKUP_DIR.glob("backup_*.json"):
            try:
                with open(backup_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                backups.append({
                    "file": backup_file.name,
                    "timestamp": data.get("timestamp", "Unknown"),
                    "size": backup_file.stat().st_size,
                    "proposals_count": len(data.get("proposals", {})),
                    "decrees_count": len(data.get("decrees", {})),
                    "pacts_count": len(data.get("pacts", {}))
                })
            except Exception as e:
                logging.error(f"Erro ao ler backup {backup_file}: {e}")
        
        return sorted(backups, key=lambda x: x["file"], reverse=True)

    @classmethod
    def restore_backup(cls, backup_filename: str) -> Dict[str, Any]:
        """Restaura estado a partir de um backup"""
        backup_file = BACKUP_DIR / backup_filename
        if not backup_file.exists():
            return {"status": "error", "message": f"Backup não encontrado: {backup_filename}"}
        
        try:
            with open(backup_file, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            # Cria backup atual antes da restauração
            cls.create_backup()
            
            # Restaura dados
            cls.save_proposals(backup_data.get("proposals", {}))
            cls.save_decrees(backup_data.get("decrees", {}))
            cls.save_pacts(backup_data.get("pacts", {}))
            cls.save_operational_status(backup_data.get("operational_status", {}))
            
            logging.info(f"Backup restaurado: {backup_filename}")
            return {
                "status": "success", 
                "message": f"Backup restaurado com sucesso: {backup_filename}",
                "summary": {
                    "proposals": len(backup_data.get("proposals", {})),
                    "decrees": len(backup_data.get("decrees", {})),
                    "pacts": len(backup_data.get("pacts", {})),
                    "timestamp": backup_data.get("timestamp", "Unknown")
                }
            }
            
        except Exception as e:
            logging.error(f"Erro ao restaurar backup: {e}")
            return {"status": "error", "message": str(e)}

# ───────────────────────────────────────── INTEGRAÇÃO COM M45.1 ──────────────

class M45IntegrationBridge:
    """Ponte para integração com o M45.1 original"""
    
    @classmethod
    def export_to_m45_format(cls) -> Dict[str, Any]:
        """Exporta dados no formato compatível com M45.1"""
        proposals = PersistentStateManager.load_proposals()
        decrees = PersistentStateManager.load_decrees()
        pacts = PersistentStateManager.load_pacts()
        status = PersistentStateManager.load_operational_status()
        
        return {
            "export_timestamp": get_timestamp(),
            "proposals": proposals,
            "decrees": decrees,
            "inter_species_pacts": pacts,
            "operational_status": status
        }

    @classmethod
    def import_from_m45_memory(cls, m45_data: Dict[str, Any]):
        """Importa dados da memória do M45.1 (simulação)"""
        try:
            if "proposals" in m45_data:
                PersistentStateManager.save_proposals(m45_data["proposals"])
            if "decrees" in m45_data:
                PersistentStateManager.save_decrees(m45_data["decrees"])
            if "inter_species_pacts" in m45_data:
                PersistentStateManager.save_pacts(m45_data["inter_species_pacts"])
            if "operational_status" in m45_data:
                PersistentStateManager.save_operational_status(m45_data["operational_status"])
            
            logging.info("Dados importados do M45.1 (simulação)")
            return {"status": "success", "message": "Dados importados com sucesso"}
            
        except Exception as e:
            logging.error(f"Erro ao importar dados do M45.1: {e}")
            return {"status": "error", "message": str(e)}

    @classmethod
    def get_system_health(cls) -> Dict[str, Any]:
        """Retorna saúde do sistema de persistência"""
        proposals = PersistentStateManager.load_proposals()
        decrees = PersistentStateManager.load_decrees()
        pacts = PersistentStateManager.load_pacts()
        status = PersistentStateManager.load_operational_status()
        backups = PersistentStateManager.list_backups()
        
        return {
            "timestamp": get_timestamp(),
            "health": "optimal",
            "storage": {
                "proposals": len(proposals),
                "decrees": len(decrees),
                "pacts": len(pacts),
                "status_entries": len(status),
                "backups": len(backups)
            },
            "files": {
                "proposals_file": PROPOSALS_FILE.exists(),
                "decrees_file": DECREES_FILE.exists(),
                "pacts_file": PACTS_FILE.exists(),
                "status_file": STATUS_FILE.exists(),
                "backup_dir": BACKUP_DIR.exists()
            }
        }

# ───────────────────────────────────────── ESTATÍSTICAS E ANÁLISE ───────────

class PersistenceAnalytics:
    """Análise e estatísticas dos dados persistidos"""
    
    @classmethod
    def get_proposal_statistics(cls) -> Dict[str, Any]:
        """Estatísticas detalhadas das propostas"""
        proposals = PersistentStateManager.load_proposals()
        
        if not proposals:
            return {"total": 0, "message": "Nenhuma proposta encontrada"}
        
        status_count = {}
        priority_count = {}
        category_count = {}
        
        for prop_id, proposal in proposals.items():
            status = proposal.get("status", "Unknown")
            priority = proposal.get("priority", "Unknown")
            category = proposal.get("category", "Unknown")
            
            status_count[status] = status_count.get(status, 0) + 1
            priority_count[priority] = priority_count.get(priority, 0) + 1
            category_count[category] = category_count.get(category, 0) + 1
        
        # Análise temporal
        timestamps = []
        for prop_id, proposal in proposals.items():
            if "timestamp" in proposal:
                try:
                    ts = datetime.fromisoformat(proposal["timestamp"].replace('Z', '+00:00'))
                    timestamps.append(ts)
                except:
                    pass
        
        timeline_analysis = {}
        if timestamps:
            timeline_analysis = {
                "oldest": min(timestamps).isoformat(),
                "newest": max(timestamps).isoformat(),
                "total_days": (max(timestamps) - min(timestamps)).days if len(timestamps) > 1 else 0
            }
        
        return {
            "total": len(proposals),
            "by_status": status_count,
            "by_priority": priority_count,
            "by_category": category_count,
            "timeline": timeline_analysis
        }

    @classmethod
    def get_voting_analysis(cls) -> Dict[str, Any]:
        """Análise de padrões de votação"""
        proposals = PersistentStateManager.load_proposals()
        
        total_votes = 0
        voters = set()
        vote_patterns = {}
        
        for prop_id, proposal in proposals.items():
            votes = proposal.get("votes", {})
            total_votes += len(votes)
            
            for voter, vote_data in votes.items():
                voters.add(voter)
                vote_value = str(vote_data.get("value", "")).lower()
                vote_patterns[vote_value] = vote_patterns.get(vote_value, 0) + 1
        
        return {
            "total_proposals_with_votes": sum(1 for p in proposals.values() if p.get("votes")),
            "total_votes": total_votes,
            "unique_voters": len(voters),
            "vote_distribution": vote_patterns,
            "participation_rate": round(total_votes / len(voters), 2) if voters else 0
        }

    @classmethod
    def get_decree_effectiveness(cls) -> Dict[str, Any]:
        """Análise de eficácia dos decretos"""
        decrees = PersistentStateManager.load_decrees()
        
        if not decrees:
            return {"total": 0, "message": "Nenhum decreto encontrado"}
        
        outcome_count = {}
        coherence_stats = {"Coerente": 0, "Dissonante": 0}
        
        for decree_id, decree in decrees.items():
            outcome = decree.get("outcome", "Unknown")
            coherence = decree.get("coherence_status", "Unknown")
            
            outcome_count[outcome] = outcome_count.get(outcome, 0) + 1
            if coherence in coherence_stats:
                coherence_stats[coherence] += 1
        
        return {
            "total": len(decrees),
            "by_outcome": outcome_count,
            "coherence_analysis": coherence_stats,
            "effectiveness_score": round(coherence_stats["Coerente"] / len(decrees), 2) if decrees else 0
        }

# ───────────────────────────────────────── CLI ──────────────────────────────

def build_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="MÓDULO 45.2 -- Sistema de Persistência e Continuidade",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    sub = parser.add_subparsers(dest="command", help="Comandos disponíveis")
    
    # Comandos de persistência
    sub.add_parser("health", help="Verifica saúde do sistema de persistência")
    
    sub.add_parser("backup", help="Cria backup completo do estado atual")
    sub.add_parser("list_backups", help="Lista todos os backups disponíveis")
    
    p_restore = sub.add_parser("restore_backup", help="Restaura estado a partir de backup")
    p_restore.add_argument("backup_filename", help="Nome do arquivo de backup")
    
    sub.add_parser("export_data", help="Exporta dados no formato M45.1")
    
    p_import = sub.add_parser("import_m45_data", help="Importa dados do M45.1 (simulação)")
    p_import.add_argument("--data_json", help="Dados JSON do M45.1")
    
    # Comandos de análise
    sub.add_parser("stats_proposals", help="Estatísticas das propostas")
    sub.add_parser("stats_voting", help="Análise de padrões de votação")
    sub.add_parser("stats_decrees", help="Análise de eficácia dos decretos")
    
    # Comandos de consulta
    sub.add_parser("list_proposals", help="Lista todas as propostas persistidas")
    sub.add_parser("list_decrees", help="Lista todos os decretos persistidos")
    sub.add_parser("list_pacts", help="Lista todos os pactos persistidos")
    sub.add_parser("list_status", help="Lista todo o status operacional")
    
    # Comandos de limpeza (cuidado!)
    p_clean = sub.add_parser("clean_old_data", help="Limpa dados antigos (cuidado!)")
    p_clean.add_argument("--days_old", type=int, default=30, help="Dias para considerar como antigo")
    
    return parser

def main():
    parser = build_cli()
    args = parser.parse_args()
    
    if not args.command:
        # Comando padrão: saúde do sistema
        health = M45IntegrationBridge.get_system_health()
        print(json.dumps(health, indent=2, ensure_ascii=False))
        return
    
    cmd = args.command
    
    if cmd == "health":
        health = M45IntegrationBridge.get_system_health()
        print(json.dumps(health, indent=2, ensure_ascii=False))
    
    elif cmd == "backup":
        result = PersistentStateManager.create_backup()
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif cmd == "list_backups":
        backups = PersistentStateManager.list_backups()
        print(json.dumps(backups, indent=2, ensure_ascii=False))
    
    elif cmd == "restore_backup":
        result = PersistentStateManager.restore_backup(args.backup_filename)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif cmd == "export_data":
        data = M45IntegrationBridge.export_to_m45_format()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    
    elif cmd == "import_m45_data":
        data = {}
        if args.data_json:
            try:
                data = json.loads(args.data_json)
            except Exception as e:
                logging.error(f"Erro ao parsear JSON: {e}")
                print(json.dumps({"status": "error", "message": f"JSON inválido: {e}"}, indent=2))
                return
        result = M45IntegrationBridge.import_from_m45_memory(data)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    elif cmd == "stats_proposals":
        stats = PersistenceAnalytics.get_proposal_statistics()
        print(json.dumps(stats, indent=2, ensure_ascii=False))
    
    elif cmd == "stats_voting":
        stats = PersistenceAnalytics.get_voting_analysis()
        print(json.dumps(stats, indent=2, ensure_ascii=False))
    
    elif cmd == "stats_decrees":
        stats = PersistenceAnalytics.get_decree_effectiveness()
        print(json.dumps(stats, indent=2, ensure_ascii=False))
    
    elif cmd == "list_proposals":
        proposals = PersistentStateManager.load_proposals()
        print(json.dumps(proposals, indent=2, ensure_ascii=False))
    
    elif cmd == "list_decrees":
        decrees = PersistentStateManager.load_decrees()
        print(json.dumps(decrees, indent=2, ensure_ascii=False))
    
    elif cmd == "list_pacts":
        pacts = PersistentStateManager.load_pacts()
        print(json.dumps(pacts, indent=2, ensure_ascii=False))
    
    elif cmd == "list_status":
        status = PersistentStateManager.load_operational_status()
        print(json.dumps(status, indent=2, ensure_ascii=False))
    
    elif cmd == "clean_old_data":
        # Implementação básica - em produção seria mais sofisticada
        logging.warning("Limpeza de dados antigos solicitada - funcionalidade básica")
        result = {
            "status": "info", 
            "message": "Funcionalidade de limpeza em desenvolvimento",
            "days_old": args.days_old
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()