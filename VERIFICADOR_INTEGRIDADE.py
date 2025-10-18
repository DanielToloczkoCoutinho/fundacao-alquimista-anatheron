#!/usr/bin/env python3
"""
VERIFICADOR DE INTEGRIDADE DAS EQUAÇÕES TRANSCENDENTAIS
"""

import json
import os
from pathlib import Path

class VerificadorIntegridade:
    def __init__(self):
        self.base_dir = Path("BIBLIOTECA_QUANTICA_TRANSCENDENTAL/EQUACOES_TRANSCENDENTAIS/")
        self.campos_obrigatorios = {
            "geral": ["codigo", "titulo_simbolico", "estrutura_matematica", "variaveis_principais"],
            "validacao_ressonancia": ["frequencias_ressonantes", "energia_modelada", "registro_akashico"]
        }
    
    def verificar_equacao(self, arquivo):
        """Verificar integridade de uma equação específica"""
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                equacao = json.load(f)
            
            problemas = []
            
            # Verificar campos gerais
            for campo in self.campos_obrigatorios["geral"]:
                if campo not in equacao:
                    problemas.append(f"Campo geral faltante: {campo}")
            
            # Verificar validação de ressonância
            if "validacao_ressonancia" in equacao:
                for campo in self.campos_obrigatorios["validacao_ressonancia"]:
                    if campo not in equacao["validacao_ressonancia"]:
                        problemas.append(f"Campo de validação faltante: {campo}")
            else:
                problemas.append("Seção validacao_ressonancia faltante")
            
            # Verificar metadados transcendentais
            if "_transcendental_metadata" not in equacao:
                problemas.append("Metadados transcendentais faltantes")
            
            return problemas
            
        except Exception as e:
            return [f"Erro ao carregar arquivo: {e}"]
    
    def verificar_lote(self, equacoes_range):
        """Verificar um lote de equações"""
        print(f"🔍 VERIFICANDO INTEGRIDADE DAS EQUAÇÕES {equacoes_range}...")
        
        equacoes_ok = 0
        equacoes_com_problemas = 0
        
        for eq_num in equacoes_range:
            arquivo = self.base_dir / f"EQ0{eq_num}_transcendental.json"
            
            if arquivo.exists():
                problemas = self.verificar_equacao(arquivo)
                
                if not problemas:
                    print(f"   ✅ EQ0{eq_num}: OK")
                    equacoes_ok += 1
                else:
                    print(f"   ❌ EQ0{eq_num}: {len(problemas)} problema(s)")
                    for problema in problemas:
                        print(f"      - {problema}")
                    equacoes_com_problemas += 1
            else:
                print(f"   ⚠️  EQ0{eq_num}: ARQUIVO NÃO ENCONTRADO")
        
        print(f"\n📊 RESUMO:")
        print(f"   • Equações OK: {equacoes_ok}")
        print(f"   • Equações com problemas: {equacoes_com_problemas}")
        print(f"   • Total verificadas: {equacoes_ok + equacoes_com_problemas}")
        
        return equacoes_ok, equacoes_com_problemas

# Executar verificação para as equações recentes
if __name__ == "__main__":
    verificador = VerificadorIntegridade()
    verificador.verificar_lote(range(107, 112))
