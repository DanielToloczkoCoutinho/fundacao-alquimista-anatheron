#!/usr/bin/env python3
import os
import json
from pathlib import Path

class MapeadorFundacao:
    def __init__(self, root_path="."):
        self.root_path = root_path
        self.estrutura = {}
        
    def mapear_tudo(self):
        print("🧭 MAPEANDO FUNDAÇÃO ALQUIMISTA NO STUDIO...")
        
        # Módulos principais
        self.estrutura['modulos_principais'] = self.mapear_modulos()
        
        # Sistemas Python
        self.estrutura['sistemas_python'] = self.mapear_sistemas_python()
        
        # Laboratórios
        self.estrutura['laboratorios'] = self.mapear_laboratorios()
        
        # Documentação
        self.estrutura['documentacao'] = self.mapear_documentacao()
        
        # SCRIPTS CENTRALIZADOS
        self.estrutura['scripts_centralizados'] = self.mapear_scripts_centralizados()
        
        return self.estrutura
    
    def mapear_modulos(self):
        modulos = {
            "M0": {"nome": "FONTE FUNDAÇÃO ALQUIMISTA", "caminho": "SCRIPTS_CENTRALIZADOS", "status": "Ativo"},
            "M29": {"nome": "ZENNITH RAINHA", "caminho": "SCRIPTS_CENTRALIZADOS/MODULO_29", "status": "Ativo"},
            "M9": {"nome": "ORGANOGRAMA VIVO (NEXUS)", "caminho": "SCRIPTS_CENTRALIZADOS/MODULO_29", "status": "Ativo"},
            "M8": {"nome": "IDENTIDADE FRACTAL", "caminho": "SCRIPTS_CENTRALIZADOS", "status": "Ativo"},
            "M45": {"nome": "CONCILIVM GOVERNANÇA", "caminho": "SCRIPTS_CENTRALIZADOS", "status": "Ativo"},
            "MΩ": {"nome": "OMEGA", "caminho": "SCRIPTS_CENTRALIZADOS", "status": "Ativo"}
        }
        return modulos
    
    def mapear_sistemas_python(self):
        sistemas = []
        python_files = [f for f in os.listdir('.') if f.endswith('.py')]
        
        for file in python_files[:20]:  # Mostrar primeiros 20
            caminho = os.path.join('.', file)
            tamanho = os.path.getsize(caminho)
            sistemas.append({
                "nome": file,
                "caminho": caminho,
                "tamanho": tamanho,
                "linhas": self.contar_linhas(caminho)
            })
        return sistemas
    
    def contar_linhas(self, arquivo):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                return len(f.readlines())
        except:
            return 0
    
    def mapear_laboratorios(self):
        labs = []
        # Laboratórios principais
        labs_principais = [
            {"nome": "SCRIPTS_CENTRALIZADOS", "caminho": "./SCRIPTS_CENTRALIZADOS", "tipo": "Central"},
            {"nome": "MODULO_29", "caminho": "./SCRIPTS_CENTRALIZADOS/MODULO_29", "tipo": "Zennith"},
            {"nome": "IBM_QUANTUM", "caminho": "./SCRIPTS_CENTRALIZADOS/ibm_quantum", "tipo": "Quantum"},
            {"nome": "LABORATORIOS", "caminho": "./SCRIPTS_CENTRALIZADOS/laboratorios", "tipo": "Pesquisa"}
        ]
        return labs_principais
    
    def mapear_documentacao(self):
        docs = []
        md_files = [f for f in os.listdir('.') if f.endswith('.md')]
        for file in md_files[:10]:
            docs.append({"nome": file, "caminho": f"./{file}"})
        return docs
    
    def mapear_scripts_centralizados(self):
        scripts = {}
        base_path = "SCRIPTS_CENTRALIZADOS"
        if os.path.exists(base_path):
            for item in os.listdir(base_path):
                item_path = os.path.join(base_path, item)
                if os.path.isdir(item_path):
                    arquivos = [f for f in os.listdir(item_path) if not f.startswith('.')]
                    scripts[item] = arquivos[:5]  # Primeiros 5 itens
        return scripts
    
    def gerar_relatorio(self):
        estrutura = self.mapear_tudo()
        
        print(f"\n🎯 RELATÓRIO DA FUNDAÇÃO ALQUIMISTA - STUDIO")
        print(f"=============================================")
        
        print(f"\n🌟 MÓDULOS PRINCIPAIS ({len(estrutura['modulos_principais'])}):")
        for mod_id, mod_info in estrutura['modulos_principais'].items():
            print(f"   {mod_id}: {mod_info['nome']} - {mod_info['status']}")
        
        print(f"\n🐍 SISTEMAS PYTHON ({len(estrutura['sistemas_python'])} de 82+):")
        for sistema in estrutura['sistemas_python'][:10]:
            print(f"   📄 {sistema['nome']} ({sistema['linhas']} linhas, {sistema['tamanho']} bytes)")
        
        print(f"\n🔬 LABORATÓRIOS ({len(estrutura['laboratorios'])}):")
        for lab in estrutura['laboratorios']:
            print(f"   🧪 {lab['nome']} [{lab['tipo']}]")
        
        print(f"\n📚 DOCUMENTAÇÃO ({len(estrutura['documentacao'])}):")
        for doc in estrutura['documentacao'][:5]:
            print(f"   📖 {doc['nome']}")
        
        print(f"\n📦 SCRIPTS CENTRALIZADOS:")
        for script_dir, arquivos in estrutura['scripts_centralizados'].items():
            print(f"   📁 {script_dir}: {len(arquivos)} arquivos")
        
        # Estatísticas finais
        total_sistemas = len([f for f in os.listdir('.') if f.endswith('.py')])
        total_scripts = len([f for f in os.listdir('.') if f.endswith('.sh')])
        
        print(f"\n📊 ESTATÍSTICAS GERAIS:")
        print(f"   🐍 Sistemas Python: {total_sistemas}+")
        print(f"   📜 Scripts Shell: {total_scripts}+") 
        print(f"   🎯 Módulos: {len(estrutura['modulos_principais'])}")
        print(f"   🔬 Laboratórios: {len(estrutura['laboratorios'])}")
        print(f"   📚 Documentos: {len(estrutura['documentacao'])}")
        
        # Salvar relatório JSON
        with open('estrutura_fundacao.json', 'w', encoding='utf-8') as f:
            json.dump(estrutura, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Relatório salvo em: estrutura_fundacao.json")
        return estrutura

if __name__ == "__main__":
    mapeador = MapeadorFundacao()
    estrutura = mapeador.gerar_relatorio()
