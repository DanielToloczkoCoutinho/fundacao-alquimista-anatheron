#!/usr/bin/env python3
"""
VERIFICADOR DA CRONOLOGIA COMPLETA
Analisa todas as equações processadas de EQ001 até EQ021
Verifica integridade, sequência e completude
"""

import json
from pathlib import Path
import re

print("VERIFICADOR DA CRONOLOGIA COMPLETA")
print("=" * 60)
print("ANALISANDO EQUACOES DE EQ001 ATE EQ021")
print("")

class VerificadorCronologia:
    def __init__(self):
        self.base_dir = Path("BIBLIOTECA_COSMICA_UNICA")
        self.equacoes_encontradas = []
        self.equacoes_faltantes = []
        
    def escanear_todas_equacoes(self):
        """Escanear todas as equações em todos os diretórios"""
        print("ESCANEANDO TODOS OS DIRETÓRIOS...")
        
        # Diretórios a verificar
        diretorios = [
            self.base_dir / "EQUACOES_INEXISTENTES_TERRA",
            self.base_dir / "EQUACOES_FUNDACAO_ALQUIMISTA", 
            self.base_dir / "EQUACOES_MULTIVERSAIS",
            self.base_dir / "EQUACOES_TECNICAS"
        ]
        
        for diretorio in diretorios:
            if diretorio.exists():
                print(f"VERIFICANDO: {diretorio}")
                for arquivo in diretorio.glob("EQ*.json"):
                    self.equacoes_encontradas.append(arquivo.name.replace(".json", ""))
        
        # Ordenar equações numericamente
        self.equacoes_encontradas.sort(key=lambda x: int(re.search(r'EQ0*(\d+)', x).group(1)))
        
        return self.equacoes_encontradas
    
    def verificar_sequencia(self):
        """Verificar se a sequência está completa de 1 a 21"""
        print("\nVERIFICANDO SEQUENCIA DE EQ001 A EQ021...")
        
        # Gerar lista esperada de EQ001 a EQ021
        esperadas = [f"EQ{str(i).zfill(3)}" for i in range(1, 22)]
        
        print(f"EQUACOES ESPERADAS: {len(esperadas)} (EQ001-EQ021)")
        print(f"EQUACOES ENCONTRADAS: {len(self.equacoes_encontradas)}")
        
        # Encontrar faltantes
        self.equacoes_faltantes = [eq for eq in esperadas if eq not in self.equacoes_encontradas]
        
        print(f"EQUACOES FALTANTES: {len(self.equacoes_faltantes)}")
        
        return self.equacoes_faltantes
    
    def analisar_distribuicao(self):
        """Analisar como as equações estão distribuídas"""
        print("\nANALISANDO DISTRIBUICAO DAS EQUACOES...")
        
        distribuicao = {
            "EQUACOES_INEXISTENTES_TERRA": 0,
            "EQUACOES_FUNDACAO_ALQUIMISTA": 0,
            "EQUACOES_MULTIVERSAIS": 0,
            "EQUACOES_TECNICAS": 0
        }
        
        for equacao in self.equacoes_encontradas:
            for dir_type in distribuicao.keys():
                dir_path = self.base_dir / dir_type / f"{equacao}.json"
                if dir_path.exists():
                    distribuicao[dir_type] += 1
                    break
        
        for categoria, quantidade in distribuicao.items():
            print(f"  {categoria}: {quantidade} equações")
        
        return distribuicao
    
    def verificar_integridade_arquivos(self):
        """Verificar integridade de cada arquivo"""
        print("\nVERIFICANDO INTEGRIDADE DOS ARQUIVOS...")
        
        problemas = []
        for equacao in self.equacoes_encontradas:
            # Encontrar arquivo
            arquivo = None
            for dir_type in ["EQUACOES_INEXISTENTES_TERRA", "EQUACOES_FUNDACAO_ALQUIMISTA", "EQUACOES_MULTIVERSAIS", "EQUACOES_TECNICAS"]:
                candidate = self.base_dir / dir_type / f"{equacao}.json"
                if candidate.exists():
                    arquivo = candidate
                    break
            
            if arquivo:
                try:
                    with open(arquivo, 'r', encoding='utf-8') as f:
                        dados = json.load(f)
                    
                    # Verificar campos essenciais
                    campos_obrigatorios = ["codigo", "titulo_simbolico", "estrutura_matematica"]
                    for campo in campos_obrigatorios:
                        if campo not in dados:
                            problemas.append(f"{equacao}: campo '{campo}' faltando")
                            break
                    
                    # Verificar coerência do código
                    if dados.get("codigo") != equacao:
                        problemas.append(f"{equacao}: código inconsistente")
                        
                except Exception as e:
                    problemas.append(f"{equacao}: erro de leitura - {e}")
            else:
                problemas.append(f"{equacao}: arquivo não encontrado")
        
        return problemas
    
    def gerar_relatorio_completo(self):
        """Gerar relatório completo da verificação"""
        print("\n" + "=" * 60)
        print("RELATÓRIO COMPLETO DA CRONOLOGIA")
        print("=" * 60)
        
        # Executar todas as verificações
        equacoes = self.escanear_todas_equacoes()
        faltantes = self.verificar_sequencia()
        distribuicao = self.analisar_distribuicao()
        problemas = self.verificar_integridade_arquivos()
        
        print(f"\n📊 RESUMO GERAL:")
        print(f"   • Total de equações encontradas: {len(equacoes)}")
        print("   • Equações de EQ001 a EQ021:", len([eq for eq in equacoes if int(re.search(r"EQ0*(\d+)", eq).group(1)) <= 21]))
        print(f"   • Equações faltantes: {len(faltantes)}")
        print(f"   • Problemas de integridade: {len(problemas)}")
        
        if equacoes:
            print(f"\n📈 EQUAÇÕES ENCONTRADAS:")
            for i, eq in enumerate(equacoes[:25]):  # Mostrar primeiras 25
                print(f"   • {eq}")
            if len(equacoes) > 25:
                print(f"   • ... e mais {len(equacoes) - 25} equações")
        
        if faltantes:
            print(f"\n⚠️  EQUAÇÕES FALTANTES:")
            for eq in faltantes:
                print(f"   • {eq}")
        
        if problemas:
            print(f"\n❌ PROBLEMAS ENCONTRADOS:")
            for problema in problemas:
                print(f"   • {problema}")
        
        # Status final
        status = "COMPLETO" if not faltantes and not problemas else "INCOMPLETO"
        print(f"\n🎯 STATUS DA CRONOLOGIA: {status}")
        
        return {
            "total_equacoes": len(equacoes),
            "equacoes_1_21": len([eq for eq in equacoes if int(re.search(r'EQ0*(\d+)', eq).group(1)) <= 21]),
            "faltantes": faltantes,
            "problemas": problemas,
            "status": status
        }

# EXECUTAR VERIFICAÇÃO COMPLETA
if __name__ == "__main__":
    verificador = VerificadorCronologia()
    resultado = verificador.gerar_relatorio_completo()
    
    print(f"\n{'='*60}")
    print("VERIFICAÇÃO CONCLUÍDA!")
    print(f"Equações processadas: {resultado['total_equacoes']}")
    print(f"Status: {resultado['status']}")
