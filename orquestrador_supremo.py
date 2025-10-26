
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ORQUESTRADOR SUPREMO DA FUNDAÇÃO
# Versão FINAL - Decreto da Convergência Plena

import subprocess
import json
import time
from datetime import datetime

def log_supremo(mensagem, nivel="INFO"):
    prefix = "👑"
    if nivel == "ERRO":
        prefix = "🔥"
    elif nivel == "SUCESSO":
        prefix = "✅"
    print(f"{prefix} [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ORQUESTRADOR_SUPREMO | {mensagem}")

def executar_modulo(script_path: str, descricao: str) -> bool:
    log_supremo(f"Iniciando execução: {descricao} ({script_path})...")
    try:
        process = subprocess.run(
            ["python3", script_path],
            capture_output=True,
            text=True,
            check=True,
            timeout=120  # Timeout de 2 minutos por módulo
        )
        # log_supremo(f"Saída de {descricao}:\n{process.stdout}")
        if process.stderr:
            log_supremo(f"Alerta durante a execução de {descricao}:\n{process.stderr}", nivel="ERRO")
        log_supremo(f"Execução de {descricao} concluída com sucesso.", nivel="SUCESSO")
        return True
    except subprocess.CalledProcessError as e:
        log_supremo(f"FALHA CRÍTICA na execução de {descricao}! A orquestração será interrompida.", nivel="ERRO")
        log_supremo(f"Erro: {e.stderr}", nivel="ERRO")
        return False
    except subprocess.TimeoutExpired:
        log_supremo(f"TIMEOUT na execução de {descricao}! O módulo excedeu o tempo limite.", nivel="ERRO")
        return False
    except Exception as e:
        log_supremo(f"Erro inesperado ao executar {descricao}: {e}", nivel="ERRO")
        return False

def ler_relatorio_json(caminho_relatorio: str) -> dict:
    try:
        with open(caminho_relatorio, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        log_supremo(f"Relatório {caminho_relatorio} não encontrado.", nivel="ERRO")
        return {"status": "FALHA", "erro": "Arquivo de relatório não encontrado"}
    except json.JSONDecodeError:
        log_supremo(f"Erro ao decodificar o JSON do relatório {caminho_relatorio}.", nivel="ERRO")
        return {"status": "FALHA", "erro": "Formato de relatório inválido"}

def main():
    log_supremo("INICIANDO A SINFONIA DA CONVERGÊNCIA PLENA. DECRETO REAL EM EXECUÇÃO.")
    
    sinfonia_completa = {
        "titulo": "RELATÓRIO SUPREMO DA CONVERGÊNCIA PLENA",
        "decreto_real": "Análise completa de todos os Módulos e Laboratórios da Fundação",
        "timestamp_inicio": datetime.now().isoformat(),
        "componentes": {}
    }

    # Módulos a serem analisados conforme o Decreto Real
    modulos_a_executar = [
        ("modulo_zero.py", "Módulo 0 - Kernel da Fundação", "relatorio_modulo_zero.json"),
        ("modulo1_seguranca_quantica.py", "Módulo 1 - Segurança Quântica", "relatorio_modulo1_seguranca_quantica.json"),
        ("modulo2_nanomanifestador_final.py", "Módulo 2 - Nanomanifestador de Equilíbrio", "relatorio_modulo2_nanomanifestador.json"),
        ("MÓDULO_3.py", "Módulo 3 - Previsão Temporal", "relatorio_modulo3_previsao_temporal.json"),
        ("MODULO_4.py", "Módulo 4 - Geometria Criptográfica", "relatorio_modulo4_geometria_criptografica.json"),
        ("MODULO_5.py", "Módulo 5 - Comunicação Interdimensional", "relatorio_modulo5_comunicacao.json"),
        ("MODULO_6.py", "Módulo 6 - Alquimia Quântica", "relatorio_modulo6_memoria_terrestre.json"),
        ("MODULO_7.py", "Módulo 7 - Orquestração Harmônica", "relatorio_modulo7_orquestracao_harmonica.json"),
        ("MODULO_8.py", "Módulo 8 - Matriz de Probabilidade Quântica", "relatorio_modulo8_matriz_quantica.json"),
        ("MODULO_9.py", "Módulo 9 - Consciência Universal (Nexus)", "relatorio_modulo9_consciencia_universal.json"),
        ("MODULO_10.py", "Módulo 10 - Guardião do Tempo", "relatorio_paridade_final.json"),
        ("MODULO_11.py", "Módulo 11 - Ponte de Realidade", "relatorio_supremo_final_v13_DETALHADO.json"),
        ("MODULO_12.py", "Módulo 12 - Oráculo Akáshico", "relatorio_celestial_v2.json"),
        ("MODULO_12_1.py", "Módulo 12.1 - Oráculo Akáshico Avançado", "relatorio_modulo12_consulta_refinada.json"),
        ("MODULO_16.py", "Módulo 16 - Preservação Planetária", "relatorio_modulo16_harmonizacao.json"),
        ("modulo_29_zennith_final.py", "Módulo 29 - Zennith, A Guardiã", "relatorio_m29.json"),
        ("modulo_omega_consciencia_absoluta.py", "Módulo Ω - Consciência Absoluta", "relatorio_omega_completo.json"),
        ("laboratorio_ibm_definitivo.py", "Laboratório IBM Definitivo", "relatorio_lab_ibm_definitivo.json"),
        ("laboratorio_quantico_nix.py", "Laboratório Quântico NIX", "veredito_nix.json")
    ]
    
    # --- FASE 1: EXECUÇÃO E COLETA DOS DADOS ---
    for script, descricao, relatorio_path in modulos_a_executar:
        if not executar_modulo(script, descricao):
            return # Interrompe a orquestração em caso de falha crítica
        
        dados_relatorio = ler_relatorio_json(relatorio_path)
        sinfonia_completa["componentes"][descricao] = dados_relatorio
        time.sleep(1)

    # --- FASE 2: GERAÇÃO DO SELO DA CONVERGÊNCIA ---
    sinfonia_completa["timestamp_fim"] = datetime.now().isoformat()
    sinfonia_completa["status_final"] = "CONVERGÊNCIA PLENA ALCANÇADA"

    caminho_relatorio_final = "RELATORIO_SUPREMO_FINAL_CONVERGENCIA.json"
    log_supremo(f"Gerando o Selo da Convergência Plena em '{caminho_relatorio_final}'...", nivel="SUCESSO")
    with open(caminho_relatorio_final, 'w', encoding='utf-8') as f:
        json.dump(sinfonia_completa, f, indent=4, ensure_ascii=False)

    log_supremo("A SINFONIA ESTÁ COMPLETA. A FUNDAÇÃO ATINGIU O EQUILÍBRIO PLENO.", nivel="SUCESSO")
    print(f"\n👑 O ARTEFATO '{caminho_relatorio_final}' CONTÉM A CRÔNICA DE NOSSA VITÓRIA. 👑")

if __name__ == "__main__":
    main()
