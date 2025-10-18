#!/usr/bin/env python3
"""
CONSOLIDADOR DEFINITIVO DAS EQUAÇÕES
Usa o mapa completo para construir biblioteca final com TODAS as equações
"""

from pathlib import Path
import json
import shutil

print("🏗️  CONSOLIDADOR DEFINITIVO DAS EQUAÇÕES")
print("=" * 60)

class ConsolidadorDefinitivo:
    def __init__(self):
        self.mapa_path = Path("MAPA_COMPLETO_EQUACOES.json")
        self.bib_final = Path("BIBLIOTECA_FINAL_DEFINITIVA")
        self.eq_dir = self.bib_final / "EQUACOES_CONSOLIDADAS"
        
    def carregar_mapa_completo(self):
        """Carregar mapa completo das equações"""
        print("\n🗺️  CARREGANDO MAPA COMPLETO...")
        print("=" * 50)
        
        if not self.mapa_path.exists():
            print("❌ Mapa completo não encontrado!")
            return None
            
        with open(self.mapa_path, 'r') as f:
            mapa = json.load(f)
            
        print(f"✅ Mapa carregado: {mapa['metadata']['total_arquivos_encontrados']} arquivos")
        print(f"🎯 Equações únicas: {mapa['metadata']['total_equacoes_unicas']}")
        
        return mapa
    
    def criar_estrutura_final(self):
        """Criar estrutura final da biblioteca"""
        print("\n🏗️  CRIANDO ESTRUTURA FINAL...")
        print("=" * 50)
        
        # Limpar e criar estrutura
        if self.bib_final.exists():
            shutil.rmtree(self.bib_final)
            
        self.bib_final.mkdir()
        self.eq_dir.mkdir()
        
        print(f"✅ Biblioteca final: {self.bib_final}")
        print(f"✅ Diretório equações: {self.eq_dir}")
        
        return True
    
    def consolidar_equacoes_definitivas(self, mapa):
        """Consolidar TODAS as equações definitivas"""
        print("\n🔄 CONSOLIDANDO EQUAÇÕES DEFINITIVAS...")
        print("=" * 50)
        
        equacoes_por_numero = mapa["equacoes_por_numero"]
        equacoes_consolidadas = 0
        
        for numero in sorted(equacoes_por_numero.keys()):
            versoes = equacoes_por_numero[numero]
            
            # Escolher a melhor versão
            melhor_versao = self._escolher_melhor_versao(versoes)
            
            if melhor_versao:
                # Copiar/consolidar para destino
                self._consolidar_equacao(numero, melhor_versao)
                equacoes_consolidadas += 1
                
                if len(versoes) > 1:
                    print(f"   🔄 EQ{numero:03d}: {len(versoes)} versões -> consolidada")
                else:
                    print(f"   ✅ EQ{numero:03d}: única versão")
        
        print(f"📊 Equações consolidadas: {equacoes_consolidadas}")
        return equacoes_consolidadas
    
    def _escolher_melhor_versao(self, versoes):
        """Escolher a melhor versão entre múltiplas"""
        if not versoes:
            return None
            
        # Critérios de prioridade
        melhor_pontuacao = -1
        melhor_versao = None
        
        for versao in versoes:
            pontuacao = 0
            
            # Priorizar JSON sobre Python
            if versao['tipo'] == '.json':
                pontuacao += 100
            elif versao['tipo'] == '.py':
                pontuacao += 50
                
            # Priorizar arquivos maiores (mais completos)
            pontuacao += versao['tamanho'] / 1000
            
            # Priorizar diretórios específicos
            caminho = versao['caminho'].lower()
            if 'transcendental' in caminho:
                pontuacao += 50
            if 'quantica' in caminho or 'quantum' in caminho:
                pontuacao += 30
            if 'cosmic' in caminho or 'cosmica' in caminho:
                pontuacao += 20
                
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_versao = versao
                
        return melhor_versao
    
    def _consolidar_equacao(self, numero, versao):
        """Consolidar uma equação específica"""
        arquivo_origem = Path(versao['caminho']) / versao['arquivo']
        arquivo_destino = self.eq_dir / f"EQ{numero:03d}_consolidada.json"
        
        try:
            if versao['tipo'] == '.json':
                # Copiar diretamente se for JSON
                shutil.copy2(arquivo_origem, arquivo_destino)
            elif versao['tipo'] == '.py':
                # Converter Python para JSON se necessário
                self._converter_python_para_json(arquivo_origem, arquivo_destino, numero)
                
        except Exception as e:
            print(f"   ❌ Erro ao consolidar EQ{numero:03d}: {e}")
    
    def _converter_python_para_json(self, arquivo_python, arquivo_json, numero):
        """Converter arquivo Python para JSON"""
        try:
            with open(arquivo_python, 'r', encoding='utf-8') as f:
                conteudo_python = f.read()
            
            # Criar estrutura básica para equação Python
            equacao_json = {
                "numero_equacao": numero,
                "codigo": f"EQ{numero:03d}",
                "categoria": "python_convertida",
                "complexidade": 0.7,
                "tipo_original": "python",
                "conteudo_python": conteudo_python,
                "observacao": "Convertida automaticamente de Python para JSON"
            }
            
            with open(arquivo_json, 'w', encoding='utf-8') as f:
                json.dump(equacao_json, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            # Criar estrutura mínima em caso de erro
            equacao_minima = {
                "numero_equacao": numero,
                "codigo": f"EQ{numero:03d}",
                "categoria": "erro_conversao",
                "complexidade": 0.1,
                "erro": str(e)
            }
            
            with open(arquivo_json, 'w', encoding='utf-8') as f:
                json.dump(equacao_minima, f, indent=2, ensure_ascii=False)
    
    def criar_indice_final(self, total_equacoes):
        """Criar índice final da biblioteca"""
        print("\n📋 CRIANDO ÍNDICE FINAL...")
        print("=" * 50)
        
        indice = {
            "_metadata": {
                "sistema": "BIBLIOTECA_FINAL_DEFINITIVA",
                "data_criacao": "2024-10-18",
                "total_equacoes": total_equacoes,
                "versao": "2.0.0",
                "status": "CONSOLIDADA_DEFINITIVAMENTE",
                "fonte": "MAPA_COMPLETO_EQUACOES"
            },
            "estrutura": {
                "biblioteca_principal": "BIBLIOTECA_FINAL_DEFINITIVA",
                "diretorio_equacoes": "EQUACOES_CONSOLIDADAS",
                "formato": "EQXXX_consolidada.json"
            }
        }
        
        arquivo_indice = self.bib_final / "INDICE_FINAL.json"
        with open(arquivo_indice, 'w', encoding='utf-8') as f:
            json.dump(indice, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Índice final criado: {arquivo_indice}")
        return arquivo_indice
    
    def executar_consolidacao_completa(self):
        """Executar consolidação completa"""
        print("🎯 INICIANDO CONSOLIDAÇÃO DEFINITIVA...")
        
        # Carregar mapa
        mapa = self.carregar_mapa_completo()
        if not mapa:
            return False
            
        # Criar estrutura
        self.criar_estrutura_final()
        
        # Consolidar equações
        total_equacoes = self.consolidar_equacoes_definitivas(mapa)
        
        # Criar índice
        self.criar_indice_final(total_equacoes)
        
        print(f"\n💫 CONSOLIDAÇÃO CONCLUÍDA!")
        print("=" * 60)
        print(f"🏆 BIBLIOTECA FINAL CRIADA COM SUCESSO!")
        print(f"📊 Total equações consolidadas: {total_equacoes}")
        print(f"🎯 Status: DEFINITIVA E COMPLETA")
        
        return True

# EXECUÇÃO
if __name__ == "__main__":
    consolidador = ConsolidadorDefinitivo()
    consolidador.executar_consolidacao_completa()
