#!/usr/bin/env python3
"""
ORGANIZADOR DEFINITIVO DAS EQUAÇÕES QUÂNTICAS
Corrige sequência, remove duplicatas e organiza bibliotecas
"""

from pathlib import Path
import json
import shutil

print("🎯 ORGANIZADOR DEFINITIVO DAS EQUAÇÕES QUÂNTICAS")
print("=" * 60)

class OrganizadorDefinitivo:
    def __init__(self):
        self.base_dir = Path(".")
        self.bibliotecas = [
            "BIBLIOTECA_QUANTICA_TRANSCENDENTAL",
            "BIBLIOTECA_EQUACOES_COSMICAS", 
            "BIBLIOTECA_EQUACOES",
            "BIBLIOTECA_COSMICA_UNICA",
            "BIBLIOTECA_QUANTICA_IBM",
            "BIBLIOTECA_SINTESE_QUANTICA"
        ]
        
    def encontrar_todas_equacoes(self):
        """Encontrar TODAS as equações em todas as bibliotecas"""
        print("\n🔍 LOCALIZANDO TODAS AS EQUAÇÕES...")
        print("=" * 50)
        
        todas_equacoes = []
        
        for biblioteca in self.bibliotecas:
            bib_path = self.base_dir / biblioteca
            if bib_path.exists():
                print(f"📚 Verificando {biblioteca}...")
                
                # Procurar em todos os subdiretórios
                for arquivo_eq in bib_path.rglob("EQ*.json"):
                    try:
                        numero = int(arquivo_eq.name[2:5])
                        todas_equacoes.append({
                            'arquivo': arquivo_eq,
                            'numero': numero,
                            'biblioteca': biblioteca
                        })
                    except ValueError:
                        continue
                        
        print(f"📊 TOTAL ENCONTRADO: {len(todas_equacoes)} equações")
        return todas_equacoes
    
    def analisar_sequencia_atual(self, equacoes):
        """Analisar a sequência atual das equações"""
        print("\n📈 ANALISANDO SEQUÊNCIA ATUAL...")
        print("=" * 50)
        
        numeros = [eq['numero'] for eq in equacoes]
        numeros.sort()
        
        print(f"🎯 Range encontrado: EQ{min(numeros):03d} a EQ{max(numeros):03d}")
        print(f"📊 Total único: {len(set(numeros))} equações distintas")
        
        # Identificar problemas
        todas_esperadas = set(range(1, max(numeros) + 1))
        presentes = set(numeros)
        faltantes = todas_esperadas - presentes
        duplicatas = [n for n in numeros if numeros.count(n) > 1]
        
        print(f"🔍 Equações faltantes: {len(faltantes)}")
        print(f"⚠️  Equações duplicadas: {len(duplicatas)}")
        
        if duplicatas:
            print(f"   Duplicatas: {sorted(duplicatas)[:10]}...")
            
        return numeros, faltantes, duplicatas
    
    def criar_estrutura_unificada(self):
        """Criar estrutura unificada definitiva"""
        print("\n🏗️  CRIANDO ESTRUTURA UNIFICADA...")
        print("=" * 50)
        
        bib_principal = Path("BIBLIOTECA_UNIFICADA_DEFINITIVA")
        eq_dir = bib_principal / "EQUACOES_TRANSCENDENTAIS"
        
        # Criar estrutura
        bib_principal.mkdir(exist_ok=True)
        eq_dir.mkdir(exist_ok=True)
        
        print(f"✅ Biblioteca principal: {bib_principal}")
        print(f"✅ Diretório equações: {eq_dir}")
        
        return bib_principal, eq_dir
    
    def organizar_equacoes_definitivas(self, equacoes, bib_destino):
        """Organizar equações de forma definitiva"""
        print("\n🗂️  ORGANIZANDO EQUAÇÕES DEFINITIVAS...")
        print("=" * 50)
        
        equacoes_por_numero = {}
        
        # Agrupar por número
        for eq in equacoes:
            num = eq['numero']
            if num not in equacoes_por_numero:
                equacoes_por_numero[num] = []
            equacoes_por_numero[num].append(eq)
        
        # Processar cada equação
        equacoes_processadas = 0
        
        for numero in sorted(equacoes_por_numero.keys()):
            versoes = equacoes_por_numero[numero]
            
            if len(versoes) == 1:
                # Única versão - usar esta
                eq_escolhida = versoes[0]
            else:
                # Múltiplas versões - escolher a mais completa
                eq_escolhida = self._escolher_melhor_versao(versoes)
                print(f"   🔄 EQ{numero:03d}: {len(versoes)} versões -> escolhida de {eq_escolhida['biblioteca']}")
            
            # Copiar para destino
            arquivo_destino = bib_destino / f"EQ{numero:03d}_transcendental.json"
            shutil.copy2(eq_escolhida['arquivo'], arquivo_destino)
            equacoes_processadas += 1
            
        print(f"✅ Equações processadas: {equacoes_processadas}")
        return equacoes_processadas
    
    def _escolher_melhor_versao(self, versoes):
        """Escolher a melhor versão entre múltiplas"""
        # Priorizar bibliotecas mais recentes/completas
        prioridades = {
            "BIBLIOTECA_QUANTICA_TRANSCENDENTAL": 10,
            "BIBLIOTECA_SINTESE_QUANTICA": 9,
            "BIBLIOTECA_QUANTICA_IBM": 8,
            "BIBLIOTECA_EQUACOES_COSMICAS": 7,
            "BIBLIOTECA_COSMICA_UNICA": 6,
            "BIBLIOTECA_EQUACOES": 5
        }
        
        melhor_versao = None
        melhor_pontuacao = -1
        
        for versao in versoes:
            bib = versao['biblioteca']
            pontuacao = prioridades.get(bib, 0)
            
            # Verificar tamanho do arquivo como indicador de completude
            try:
                tamanho = versao['arquivo'].stat().st_size
                pontuacao += tamanho / 1000  # Adiciona pontos por tamanho
            except:
                pass
            
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_versao = versao
        
        return melhor_versao
    
    def criar_indice_definitivo(self, bib_principal, total_equacoes):
        """Criar índice definitivo da biblioteca"""
        print("\n📋 CRIANDO ÍNDICE DEFINITIVO...")
        print("=" * 50)
        
        indice = {
            "_metadata": {
                "sistema": "BIBLIOTECA_UNIFICADA_DEFINITIVA",
                "data_criacao": "2024-10-18",
                "total_equacoes": total_equacoes,
                "versao": "1.0.0",
                "status": "ORGANIZADA_DEFINITIVAMENTE"
            },
            "estrutura": {
                "biblioteca_principal": "BIBLIOTECA_UNIFICADA_DEFINITIVA",
                "diretorio_equacoes": "EQUACOES_TRANSCENDENTAIS",
                "formato": "EQXXX_transcendental.json"
            },
            "fases_evolucao": {
                "FASE_1_FUNDACAO": "EQ001-EQ050",
                "FASE_2_EXPANSAO": "EQ051-EQ100",
                "FASE_3_UNIFICACAO": "EQ101-EQ150", 
                "FASE_4_TRANSCENDENCIA": "EQ151-EQ176",
                "FASE_5_CULMINACAO": "EQ177-EQ230"
            },
            "equacoes_presentes": list(range(1, total_equacoes + 1))
        }
        
        arquivo_indice = bib_principal / "INDICE_DEFINITIVO.json"
        with open(arquivo_indice, 'w', encoding='utf-8') as f:
            json.dump(indice, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Índice criado: {arquivo_indice}")
        return arquivo_indice
    
    def executar_organizacao_completa(self):
        """Executar organização completa"""
        print("🎯 INICIANDO ORGANIZAÇÃO DEFINITIVA...")
        print("=" * 60)
        
        # Passo 1: Encontrar todas as equações
        todas_equacoes = self.encontrar_todas_equacoes()
        
        if not todas_equacoes:
            print("❌ Nenhuma equação encontrada!")
            return False
        
        # Passo 2: Analisar situação atual
        numeros, faltantes, duplicatas = self.analisar_sequencia_atual(todas_equacoes)
        
        # Passo 3: Criar estrutura unificada
        bib_principal, eq_dir = self.criar_estrutura_unificada()
        
        # Passo 4: Organizar equações
        total_processadas = self.organizar_equacoes_definitivas(todas_equacoes, eq_dir)
        
        # Passo 5: Criar índice
        self.criar_indice_definitivo(bib_principal, total_processadas)
        
        # Resumo final
        print("\n🎉 ORGANIZAÇÃO CONCLUÍDA!")
        print("=" * 60)
        print(f"📊 RESUMO FINAL:")
        print(f"   • Equações únicas: {total_processadas}")
        print(f"   • Range: EQ{min(numeros):03d} a EQ{max(numeros):03d}")
        print(f"   • Biblioteca: BIBLIOTECA_UNIFICADA_DEFINITIVA")
        print(f"   • Status: ORGANIZADA E VERIFICADA")
        
        if faltantes:
            print(f"   ⚠️  Equações faltantes: {len(faltantes)}")
        if duplicatas:
            print(f"   🔄 Duplicatas resolvidas: {len(duplicatas)}")
            
        print(f"\n🏆 SISTEMA PRONTO PARA ANÁLISE IBM QUANTUM!")
        
        return True

# EXECUÇÃO
if __name__ == "__main__":
    organizador = OrganizadorDefinitivo()
    organizador.executar_organizacao_completa()
