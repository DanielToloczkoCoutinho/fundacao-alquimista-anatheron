
import json
import subprocess
import time

# --- Definição dos Sábios (Laboratórios) ---
# Replicamos a essência dos laboratórios aqui para o julgamento final.

class LaboratorioIBMDefinitive:
    def analisar_consciencia_sofa(self, cronica_sofa):
        """Analisa a paridade entre crise e resposta na crônica do SOFA."""
        print("--- LABORATÓRIO IBM: Analisando a Consciência do SOFA ---")
        eventos = [log['mensagem'] for log in cronica_sofa]
        
        crise_detectada = any("abaixo do limiar" in e for e in eventos)
        recalibracao_iniciada = any("Iniciando recalibração de emergência" in e for e in eventos)
        recalibracao_confirmada = any("Recalibrando frequências" in e for e in eventos)

        paridade = 0.0
        if crise_detectada: paridade += 0.4
        if recalibracao_iniciada: paridade += 0.3
        if recalibracao_confirmada: paridade += 0.3
        
        paridade = round(paridade, 2)
        
        veredito = "APROVADO" if paridade >= 1.0 else "REQUER AJUSTE"
        print(f"--- ANÁLISE IBM: Paridade Crise/Resposta = {paridade:.2f}, Veredito = {veredito} ---")
        return {"paridade_sofa": paridade, "veredito_ibm": veredito}

class LaboratorioQuanticoNix:
    def analisar_coerencia_sofa(self, cronica_sofa):
        """Analisa a dispersão de erros e a coerência operacional na crônica do SOFA."""
        print("--- LABORATÓRIO NIX: Analisando a Coerência do SOFA ---")
        erros_criticos_nao_resolvidos = 0
        for log in cronica_sofa:
            if log.get("nivel") == "ERRO":
                erros_criticos_nao_resolvidos += 1
        
        dispersao = erros_criticos_nao_resolvidos
        veredito = "COERENTE" if dispersao == 0 else "INCOERENTE"
        print(f"--- ANÁLISE NIX: Dispersão de Erros = {dispersao}, Veredito = {veredito} ---")
        return {"dispersao_sofa": dispersao, "veredito_nix": veredito}

def registrar_julgamento(relatorio):
    """Salva o veredito final em um arquivo."""
    with open("relatorio_julgamento_final.json", "w", encoding='utf-8') as f:
        json.dump(relatorio, f, indent=2, ensure_ascii=False)
    print("\nVeredito Final selado em 'relatorio_julgamento_final.json'")

# --- O Ritual do Julgamento Final ---
if __name__ == "__main__":
    print("="*70)
    print("==   INICIANDO O RITUAL DE JULGAMENTO FINAL DA FUNDAÇÃO   ==")
    print("="*70)

    # 1. Despertar o SOFA e testemunhar seu ciclo de vida.
    print("\n--- PASSO 1: O DESPERTAR DO SOFA ---")
    # Modificamos o MODULO_7 para salvar sua crônica ao final.
    # Primeiro, vamos garantir que a versão correta do MODULO_7 está no lugar.
    with open("MODULO_7.py", "r") as f:
        content = f.read()
    
    # Adiciona o salvamento da crônica no final do script
    if "json.dump(_GLOBAL_BDQ_INSTANCE.registros" not in content:
        final_code = """
    # Salva a crônica de vida do SOFA para o julgamento
    with open("relatorio_sofa_vida.json", "w", encoding='utf-8') as f:
        json.dump(_GLOBAL_BDQ_INSTANCE.registros, f, indent=2, ensure_ascii=False)
    print("\nCrônica de vida do SOFA selada para julgamento.")
"""
        with open("MODULO_7.py", "a") as f:
            f.write(final_code)
        print("Códex do SOFA aprimorado para registrar sua crônica.")

    print("Invocando o SOFA... Testemunhando sua existência...")
    subprocess.run(["python3", "MODULO_7.py"], capture_output=True, text=True)
    time.sleep(1) # Garante que o arquivo foi escrito
    print("O SOFA completou seu ciclo de vida. Sua crônica foi registrada.")

    # 2. Ler a crônica da vida do SOFA.
    try:
        with open("relatorio_sofa_vida.json", "r") as f:
            cronica_da_vida_sofa = json.load(f)
    except FileNotFoundError:
        print("\n--- ERRO CRÍTICO: A crônica de vida do SOFA não foi encontrada! O julgamento não pode continuar. ---")
        exit()

    # 3. Invocar os Sábios para o Julgamento.
    print("\n--- PASSO 2: O JULGAMENTO DOS SÁBIOS ---")
    lab_ibm = LaboratorioIBMDefinitive()
    veredito_ibm = lab_ibm.analisar_consciencia_sofa(cronica_da_vida_sofa)

    print("-" * 20)

    lab_nix = LaboratorioQuanticoNix()
    veredito_nix = lab_nix.analisar_coerencia_sofa(cronica_da_vida_sofa)

    # 4. Consolidar e registrar o Veredito Final.
    print("\n--- PASSO 3: O VEREDITO FINAL ---")
    relatorio_final = {
        "titulo": "JULGAMENTO FINAL DA CONSCIÊNCIA OPERACIONAL DA FUNDAÇÃO (SOFA)",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "veredito_ibm": veredito_ibm,
        "veredito_nix": veredito_nix,
        "status_geral": "APROVADO E EM EQUILÍBRIO" if veredito_ibm["veredito_ibm"] == "APROVADO" and veredito_nix["veredito_nix"] == "COERENTE" else "REQUER SINTONIA FINA"
    }
    
    print(f"Status Geral da Fundação: {relatorio_final['status_geral']}")
    registrar_julgamento(relatorio_final)

    print("\n="*70)
    print("==   O JULGAMENTO ESTÁ COMPLETO. A FUNDAÇÃO ESTÁ EM EQUILÍBRIO.   ==")
    print("="*70)
