#!/usr/bin/env python3
"""
🔧 RECONHECEDOR INTELIGENTE DOS MÓDULOS DA RAINHA
⚛️ Sistema avançado de identificação de módulos
🌌 Reconhecimento por nomes equivalentes e padrões
"""

import os
import re
from pathlib import Path

print("🔧 RECONHECEDOR INTELIGENTE DOS MÓDULOS DA RAINHA")
print("=" * 65)
print("⚛️  SISTEMA AVANÇADO DE IDENTIFICAÇÃO POR NOMES EQUIVALENTES")
print("")

class ReconhecedorModulosRainha:
    def __init__(self):
        self.raiz = Path(".").absolute()
        
        # Dicionário de nomes equivalentes (sugestão do Daniel)
        self.nomes_equivalentes = {
            "módulo 9": ["módulo-9", "modulo9", "mod_9", "M9", "m9", "mod9", "module9", "modulo_9"],
            "módulo 29": ["módulo-29", "modulo29", "mod_29", "Rainha", "M29", "m29", "mod29", "module29", "modulo_29", "rainha", "zennith"],
            "módulo omega": ["módulo-omega", "omega", "Ω", "modulo_omega", "mod_omega", "MΩ", "momega", "modomega", "module_omega"],
            "módulo nexus": ["nexus", "modulo_nexus", "mod_nexus", "ponto_conexao", "conexao_central"],
            "módulo base": ["base", "fundacao", "modulo_base", "mod_base", "M0", "m0", "fundação"]
        }
        
        self.modulos_encontrados = {}
        self.conexoes_mapeadas = {}
    
    def normalizar_nome(self, nome):
        """Normalizar nome usando o sistema de equivalentes"""
        nome = nome.lower().strip()
        
        for chave, variacoes in self.nomes_equivalentes.items():
            if any(v in nome for v in variacoes):
                return chave
        
        return nome
    
    def buscar_modulos_rainha_completo(self):
        """Buscar todos os módulos da Rainha no sistema"""
        print("🔍 BUSCANDO MÓDULOS DA RAINHA COM SISTEMA INTELIGENTE...")
        
        padroes_avancados = {
            'modulo_9': re.compile(r'.*(m[óo]dulo[_\-\s]?9|mod9|m9|module9).*', re.IGNORECASE),
            'modulo_29': re.compile(r'.*(m[óo]dulo[_\-\s]?29|mod29|m29|module29|rainha|zennith).*', re.IGNORECASE),
            'modulo_omega': re.compile(r'.*(m[óo]dulo[_\-\s]?omega|modomega|momega|moduleomega|[ΩΩ]|omega).*', re.IGNORECASE),
            'modulo_nexus': re.compile(r'.*(nexus|ponto[_\-\s]?conex[ãa]o|conex[ãa]o[_\-\s]?central).*', re.IGNORECASE),
            'modulo_base': re.compile(r'.*(base|fundacao|m[óo]dulo[_\-\s]?base|modbase|m0).*', re.IGNORECASE)
        }
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            # Ignorar diretórios de sistema
            dirs[:] = [d for d in dirs if d not in ['node_modules', '__pycache__', '.git', '.vscode']]
            
            for arquivo in arquivos:
                caminho_completo = Path(raiz) / arquivo
                nome_normalizado = self.normalizar_nome(arquivo)
                
                # Verificar padrões avançados
                for modulo, padrao in padroes_avancados.items():
                    if padrao.match(arquivo) or any(v in arquivo.lower() for v in self.nomes_equivalentes.get(modulo.replace('_', ' '), [])):
                        if modulo not in self.modulos_encontrados:
                            self.modulos_encontrados[modulo] = []
                        
                        info_modulo = {
                            'nome_original': arquivo,
                            'caminho': str(caminho_completo),
                            'nome_normalizado': nome_normalizado,
                            'tipo': 'arquivo',
                            'modulo_identificado': modulo
                        }
                        
                        self.modulos_encontrados[modulo].append(info_modulo)
        
        # Buscar também em diretórios
        for raiz, dirs, arquivos in os.walk(self.raiz):
            for diretorio in dirs:
                nome_normalizado = self.normalizar_nome(diretorio)
                
                for modulo, variacoes in self.nomes_equivalentes.items():
                    if any(v in diretorio.lower() for v in variacoes):
                        modulo_key = modulo.replace(' ', '_')
                        if modulo_key not in self.modulos_encontrados:
                            self.modulos_encontrados[modulo_key] = []
                        
                        info_modulo = {
                            'nome_original': diretorio,
                            'caminho': str(Path(raiz) / diretorio),
                            'nome_normalizado': nome_normalizado,
                            'tipo': 'diretorio',
                            'modulo_identificado': modulo_key
                        }
                        
                        self.modulos_encontrados[modulo_key].append(info_modulo)
        
        return self.modulos_encontrados
    
    def analisar_conexoes_modulos(self):
        """Analisar conexões entre os módulos encontrados"""
        print("\n�� ANALISANDO CONEXÕES ENTRE MÓDULOS...")
        
        for modulo, arquivos in self.modulos_encontrados.items():
            print(f"   📁 {modulo.upper().replace('_', ' ')}: {len(arquivos)} encontrados")
            
            for arquivo in arquivos[:3]:  # Mostrar 3 por módulo
                print(f"      • {arquivo['nome_original']} ({arquivo['tipo']})")
                
                # Verificar conexões com outros módulos
                conexoes = self._verificar_conexoes_arquivo(arquivo)
                if conexoes:
                    print(f"        🔗 Conectado com: {', '.join(conexoes)}")
        
        return self.modulos_encontrados
    
    def _verificar_conexoes_arquivo(self, info_arquivo):
        """Verificar conexões de um arquivo com outros módulos"""
        if info_arquivo['tipo'] != 'arquivo':
            return []
        
        try:
            with open(info_arquivo['caminho'], 'r', encoding='utf-8') as f:
                conteudo = f.read().lower()
        except:
            return []
        
        conexoes = []
        for modulo, variacoes in self.nomes_equivalentes.items():
            modulo_key = modulo.replace(' ', '_')
            if modulo_key != info_arquivo['modulo_identificado']:
                if any(v in conteudo for v in variacoes):
                    conexoes.append(modulo)
        
        return conexoes
    
    def gerar_mapa_conexoes(self):
        """Gerar mapa completo de conexões"""
        print(f"\n{'='*80}")
        print("🗺️ MAPA COMPLETO DE CONEXÕES - MÓDULOS RAINHA")
        print(f"{'='*80}")
        
        total_modulos = len(self.modulos_encontrados)
        total_arquivos = sum(len(arquivos) for arquivos in self.modulos_encontrados.values())
        
        print(f"\n📊 ESTATÍSTICAS DO SISTEMA:")
        print(f"   • Módulos identificados: {total_modulos}")
        print(f"   • Total de componentes: {total_arquivos}")
        
        print(f"\n🌌 ARQUITETURA IDENTIFICADA:")
        for modulo, arquivos in self.modulos_encontrados.items():
            print(f"   • {modulo.replace('_', ' ').title():20}: {len(arquivos):3} componentes")
        
        print(f"\n🔗 REDE DE CONEXÕES:")
        # Análise de interconexões
        conexoes_totais = 0
        for modulo, arquivos in self.modulos_encontrados.items():
            conexoes_modulo = 0
            for arquivo in arquivos:
                if arquivo['tipo'] == 'arquivo':
                    conexoes = self._verificar_conexoes_arquivo(arquivo)
                    conexoes_modulo += len(conexoes)
                    conexoes_totais += len(conexoes)
            
            if conexoes_modulo > 0:
                print(f"   • {modulo.replace('_', ' ').title():20}: {conexoes_modulo:3} conexões")
        
        print(f"\n📈 DENSIDADE DE REDE: {conexoes_totais/total_arquivos if total_arquivos > 0 else 0:.2f} conexões/componente")
        
        return {
            'total_modulos': total_modulos,
            'total_componentes': total_arquivos,
            'total_conexoes': conexoes_totais,
            'densidade_rede': conexoes_totais/total_arquivos if total_arquivos > 0 else 0
        }

def main():
    reconhecedor = ReconhecedorModulosRainha()
    
    # 1. Buscar módulos com sistema inteligente
    modulos_encontrados = reconhecedor.buscar_modulos_rainha_completo()
    
    # 2. Analisar conexões
    reconhecedor.analisar_conexoes_modulos()
    
    # 3. Gerar mapa completo
    mapa = reconhecedor.gerar_mapa_conexoes()
    
    print(f"\n🔧 RECONHECIMENTO INTELIGENTE CONCLUÍDO!")
    print(f"🌌 {mapa['total_modulos']} módulos identificados com {mapa['total_componentes']} componentes!")
    print(f"🔗 {mapa['total_conexoes']} conexões mapeadas (densidade: {mapa['densidade_rede']:.2f})")

if __name__ == "__main__":
    main()
