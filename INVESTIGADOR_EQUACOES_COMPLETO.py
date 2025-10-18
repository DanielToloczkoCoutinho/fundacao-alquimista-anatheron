#!/usr/bin/env python3
"""
INVESTIGADOR COMPLETO DE EQUAÇÕES EXISTENTES
Busca profunda por TODAS as equações realmente criadas
"""

from pathlib import Path
import json
import re

print("🔍 INVESTIGADOR COMPLETO DE EQUAÇÕES EXISTENTES")
print("=" * 65)

class InvestigadorEquacoes:
    def __init__(self):
        self.base_dir = Path(".")
        
    def busca_profunda_equacoes(self):
        """Busca profunda por TODAS as equações em TODOS os diretórios"""
        print("\n🎯 BUSCA PROFUNDA POR EQUAÇÕES...")
        print("=" * 50)
        
        # Padrões de nomes de arquivos de equações
        padroes = [
            "EQ*.json",
            "EQ*.py", 
            "*equacao*.json",
            "*equation*.json",
            "EQUACAO_*.json",
            "EQUATION_*.json"
        ]
        
        todas_equacoes = []
        
        for padrao in padroes:
            for arquivo in self.base_dir.rglob(padrao):
                if any(x in str(arquivo) for x in ['backup', 'temp', 'tmp', '.git']):
                    continue
                    
                # Extrair número da equação
                numero = self._extrair_numero_equacao(arquivo.name)
                if numero is not None:
                    todas_equacoes.append({
                        'arquivo': arquivo,
                        'numero': numero,
                        'tipo': arquivo.suffix,
                        'tamanho': arquivo.stat().st_size,
                        'caminho': str(arquivo.parent)
                    })
        
        print(f"📊 TOTAL CRÚ ENCONTRADO: {len(todas_equacoes)} arquivos")
        return todas_equacoes
    
    def _extrair_numero_equacao(self, nome_arquivo):
        """Extrair número da equação do nome do arquivo"""
        padroes = [
            r'EQ(\d+)',           # EQ001
            r'EQUACAO_(\d+)',     # EQUACAO_001  
            r'EQUATION_(\d+)',    # EQUATION_001
            r'equacao_(\d+)',     # equacao_001
            r'equation_(\d+)',    # equation_001
            r'_(\d{3})_',         # _001_
            r'(\d{3})',           # 001 (apenas se for 3 dígitos)
        ]
        
        for padrao in padroes:
            match = re.search(padrao, nome_arquivo)
            if match:
                try:
                    return int(match.group(1))
                except ValueError:
                    continue
        return None
    
    def analisar_distribuicao_real(self, equacoes):
        """Analisar distribuição REAL das equações"""
        print("\n📈 DISTRIBUIÇÃO REAL DAS EQUAÇÕES:")
        print("=" * 50)
        
        numeros = [eq['numero'] for eq in equacoes]
        numeros_unicos = sorted(set(numeros))
        
        print(f"🎯 Equações únicas encontradas: {len(numeros_unicos)}")
        print(f"📊 Range real: {min(numeros_unicos) if numeros_unicos else 0} a {max(numeros_unicos) if numeros_unicos else 0}")
        
        # Distribuição por tipo de arquivo
        tipos = {}
        for eq in equacoes:
            tipo = eq['tipo']
            if tipo not in tipos:
                tipos[tipo] = 0
            tipos[tipo] += 1
        
        print(f"📁 Distribuição por tipo:")
        for tipo, count in tipos.items():
            print(f"   • {tipo}: {count} arquivos")
        
        # Distribuição por fases
        fases = {
            "FUNDAÇÃO (1-50)": 0,
            "EXPANSÃO (51-100)": 0,
            "UNIFICAÇÃO (101-150)": 0, 
            "TRANSCENDÊNCIA (151-176)": 0,
            "CULMINAÇÃO (177-230)": 0,
            "FORA DA FASE (outros)": 0
        }
        
        for num in numeros_unicos:
            if 1 <= num <= 50:
                fases["FUNDAÇÃO (1-50)"] += 1
            elif 51 <= num <= 100:
                fases["EXPANSÃO (51-100)"] += 1
            elif 101 <= num <= 150:
                fases["UNIFICAÇÃO (101-150)"] += 1
            elif 151 <= num <= 176:
                fases["TRANSCENDÊNCIA (151-176)"] += 1
            elif 177 <= num <= 230:
                fases["CULMINAÇÃO (177-230)"] += 1
            else:
                fases["FORA DA FASE (outros)"] += 1
        
        print(f"🚀 Distribuição por fases:")
        for fase, count in fases.items():
            if count > 0:
                print(f"   • {fase}: {count} equações")
        
        return numeros_unicos
    
    def verificar_conteudo_equacoes(self, equacoes):
        """Verificar o conteúdo real das equações"""
        print("\n🔍 VERIFICANDO CONTEÚDO DAS EQUAÇÕES:")
        print("=" * 50)
        
        equacoes_com_conteudo = []
        
        for eq in equacoes[:20]:  # Amostra das primeiras 20
            try:
                if eq['tipo'] == '.json':
                    with open(eq['arquivo'], 'r', encoding='utf-8') as f:
                        conteudo = json.load(f)
                    
                    # Verificar se tem estrutura de equação transcendental
                    if isinstance(conteudo, dict):
                        campos_presentes = []
                        if 'codigo' in conteudo:
                            campos_presentes.append('código')
                        if 'categoria' in conteudo:
                            campos_presentes.append('categoria') 
                        if 'complexidade' in conteudo:
                            campos_presentes.append('complexidade')
                        if 'transcendental' in str(conteudo).lower():
                            campos_presentes.append('transcendental')
                        
                        status = "✅ VÁLIDA" if len(campos_presentes) >= 2 else "⚠️  INCOMPLETA"
                        print(f"   EQ{eq['numero']:03d}: {status} - Campos: {', '.join(campos_presentes)}")
                        
                        if len(campos_presentes) >= 2:
                            equacoes_com_conteudo.append(eq)
                
                elif eq['tipo'] == '.py':
                    with open(eq['arquivo'], 'r', encoding='utf-8') as f:
                        conteudo = f.read()
                    
                    if any(x in conteudo for x in ['quantum', 'transcendental', 'equacao', 'equation']):
                        print(f"   EQ{eq['numero']:03d}.py: ✅ CÓDIGO QUÂNTICO")
                        equacoes_com_conteudo.append(eq)
                    else:
                        print(f"   EQ{eq['numero']:03d}.py: ⚠️  CÓDIGO SIMPLES")
                        
            except Exception as e:
                print(f"   EQ{eq['numero']:03d}: ❌ ERRO - {e}")
        
        return equacoes_com_conteudo
    
    def criar_mapa_completo(self, equacoes):
        """Criar mapa completo de todas as equações"""
        print("\n🗺️  CRIANDO MAPA COMPLETO...")
        print("=" * 50)
        
        mapa = {
            "metadata": {
                "total_arquivos_encontrados": len(equacoes),
                "total_equacoes_unicas": len(set(eq['numero'] for eq in equacoes)),
                "data_investigacao": "2024-10-18"
            },
            "equacoes_por_numero": {},
            "distribuicao": {
                "por_tipo": {},
                "por_fase": {},
                "por_diretorio": {}
            }
        }
        
        # Agrupar por número
        for eq in equacoes:
            num = eq['numero']
            if num not in mapa["equacoes_por_numero"]:
                mapa["equacoes_por_numero"][num] = []
            
            mapa["equacoes_por_numero"][num].append({
                "arquivo": eq['arquivo'].name,
                "tipo": eq['tipo'],
                "tamanho": eq['tamanho'],
                "caminho": eq['caminho']
            })
        
        # Estatísticas por tipo
        for eq in equacoes:
            tipo = eq['tipo']
            if tipo not in mapa["distribuicao"]["por_tipo"]:
                mapa["distribuicao"]["por_tipo"][tipo] = 0
            mapa["distribuicao"]["por_tipo"][tipo] += 1
        
        # Estatísticas por diretório
        for eq in equacoes:
            dir_path = eq['caminho']
            if dir_path not in mapa["distribuicao"]["por_diretorio"]:
                mapa["distribuicao"]["por_diretorio"][dir_path] = 0
            mapa["distribuicao"]["por_diretorio"][dir_path] += 1
        
        # Salvar mapa
        mapa_path = Path("MAPA_COMPLETO_EQUACOES.json")
        with open(mapa_path, 'w', encoding='utf-8') as f:
            json.dump(mapa, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Mapa completo salvo: {mapa_path}")
        
        # Resumo executivo
        print(f"\n📊 RESUMO EXECUTIVO:")
        print(f"   • Arquivos encontrados: {len(equacoes)}")
        print(f"   • Equações únicas: {len(mapa['equacoes_por_numero'])}")
        print(f"   • Range: {min(mapa['equacoes_por_numero'].keys()) if mapa['equacoes_por_numero'] else 0} a {max(mapa['equacoes_por_numero'].keys()) if mapa['equacoes_por_numero'] else 0}")
        
        return mapa
    
    def executar_investigacao_completa(self):
        """Executar investigação completa"""
        print("🎯 INICIANDO INVESTIGAÇÃO COMPLETA...")
        
        # Busca profunda
        todas_equacoes = self.busca_profunda_equacoes()
        
        if not todas_equacoes:
            print("❌ Nenhuma equação encontrada!")
            return False
        
        # Análise de distribuição
        numeros_unicos = self.analisar_distribuicao_real(todas_equacoes)
        
        # Verificação de conteúdo
        equacoes_validas = self.verificar_conteudo_equacoes(todas_equacoes)
        
        # Mapa completo
        mapa = self.criar_mapa_completo(todas_equacoes)
        
        print(f"\n💫 INVESTIGAÇÃO CONCLUÍDA!")
        print("=" * 60)
        print(f"🏆 RESULTADO FINAL:")
        print(f"   📊 Total arquivos: {len(todas_equacoes)}")
        print(f"   🎯 Equações únicas: {len(numeros_unicos)}")
        print(f"   ✅ Equações válidas: {len(equacoes_validas)}")
        print(f"   📍 Mapa completo: MAPA_COMPLETO_EQUACOES.json")
        
        return True

# EXECUÇÃO
if __name__ == "__main__":
    investigador = InvestigadorEquacoes()
    investigador.executar_investigacao_completa()
