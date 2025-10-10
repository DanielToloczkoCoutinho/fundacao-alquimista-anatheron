#!/usr/bin/env python3
import os
import json

class AnalisadorOmega:
    def __init__(self):
        self.visao_holistica = {}
    
    def analise_omega(self):
        print("🌀 MÓDULO OMEGA - ATIVANDO VISÃO HOLÍSTICA...")
        print("=" * 60)
        
        # 1. Mapear todos os sistemas por complexidade
        self.mapear_sistemas_complexidade()
        
        # 2. Identificar padrões de interface
        self.identificar_padroes_interfaces()
        
        # 3. Gerar arquitetura ideal
        self.gerar_arquitetura_ideal()
        
        return self.visao_holistica
    
    def mapear_sistemas_complexidade(self):
        """Mapear sistemas por nível de complexidade e tecnologia"""
        print("\n📊 MAPEANDO SISTEMAS POR COMPLEXIDADE...")
        
        sistemas = {
            "alta_complexidade": [],
            "media_complexidade": [], 
            "baixa_complexidade": []
        }
        
        # Analisar arquivos Python para complexidade
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.py') and 'node_modules' not in root:
                    caminho = os.path.join(root, file)
                    complexidade = self.analisar_complexidade_python(caminho)
                    
                    sistema_info = {
                        "nome": file,
                        "caminho": caminho,
                        "complexidade": complexidade,
                        "tecnologias": self.identificar_tecnologias_arquivo(caminho)
                    }
                    
                    if complexidade == "alta":
                        sistemas["alta_complexidade"].append(sistema_info)
                    elif complexidade == "media":
                        sistemas["media_complexidade"].append(sistema_info)
                    else:
                        sistemas["baixa_complexidade"].append(sistema_info)
        
        self.visao_holistica['sistemas_complexidade'] = sistemas
        
        print(f"   ✅ Sistemas de Alta Complexidade: {len(sistemas['alta_complexidade'])}")
        print(f"   ✅ Sistemas de Média Complexidade: {len(sistemas['media_complexidade'])}") 
        print(f"   ✅ Sistemas de Baixa Complexidade: {len(sistemas['baixa_complexidade'])}")
    
    def analisar_complexidade_python(self, arquivo):
        """Analisar complexidade de arquivo Python"""
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                linhas = f.readlines()
                
            num_linhas = len(linhas)
            
            # Contar imports e funções complexas
            imports = sum(1 for linha in linhas if linha.strip().startswith('import') or linha.strip().startswith('from'))
            funcoes = sum(1 for linha in linhas if linha.strip().startswith('def '))
            classes = sum(1 for linha in linhas if linha.strip().startswith('class '))
            
            if num_linhas > 200 or imports > 10 or funcoes > 15:
                return "alta"
            elif num_linhas > 50 or imports > 5 or funcoes > 5:
                return "media"
            else:
                return "baixa"
                
        except:
            return "desconhecida"
    
    def identificar_tecnologias_arquivo(self, arquivo):
        """Identificar tecnologias usadas no arquivo"""
        tecnologias = []
        
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                conteudo = f.read().lower()
                
            tech_mapping = {
                "qiskit": "IBM Quantum",
                "quantum": "Computação Quântica", 
                "tensorflow": "Machine Learning",
                "keras": "Deep Learning",
                "numpy": "Computação Científica",
                "matplotlib": "Visualização",
                "flask": "Web Framework",
                "fastapi": "API Moderna",
                "blockchain": "Blockchain",
                "crypto": "Criptografia"
            }
            
            for termo, tech in tech_mapping.items():
                if termo in conteudo:
                    tecnologias.append(tech)
                    
        except:
            pass
            
        return list(set(tecnologias))
    
    def identificar_padroes_interfaces(self):
        """Identificar padrões de interfaces existentes"""
        print("\n🎨 IDENTIFICANDO PADRÕES DE INTERFACE...")
        
        padroes = {
            "dashboard_central": False,
            "laboratorios_especializados": False,
            "realidade_virtual": False,
            "interfaces_neurais": False,
            "visualizacao_3d": False
        }
        
        # Verificar componentes existentes
        componentes_react = []
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith(('.tsx', '.jsx')) and 'node_modules' not in root:
                    componentes_react.append(os.path.join(root, file))
        
        # Analisar padrões nos componentes
        for componente in componentes_react:
            comp_lower = componente.lower()
            
            if any(term in comp_lower for term in ['dashboard', 'metric']):
                padroes["dashboard_central"] = True
            elif any(term in comp_lower for term in ['lab', 'laborator']):
                padroes["laboratorios_especializados"] = True  
            elif any(term in comp_lower for term in ['vr', 'virtual', 'three']):
                padroes["realidade_virtual"] = True
            elif any(term in comp_lower for term in ['neural', 'brain']):
                padroes["interfaces_neurais"] = True
            elif any(term in comp_lower for term in ['3d', 'fractal', 'webgl']):
                padroes["visualizacao_3d"] = True
        
        self.visao_holistica['padroes_interfaces'] = padroes
        
        print("   📊 Padrões identificados:")
        for padrao, existe in padroes.items():
            status = "✅" if existe else "❌"
            print(f"      {status} {padrao}")
    
    def gerar_arquitetura_ideal(self):
        """Gerar arquitetura ideal baseada na análise"""
        print("\n🏗️ GERANDO ARQUITETURA IDEAL OMEGA...")
        
        arquitetura = {
            "nucleo_central": {
                "zennith_core": "Módulo 29 - Governança",
                "nexus_interface": "Módulo 9 - Interconexões", 
                "omega_dashboard": "Visão Holística"
            },
            "laboratorios_especializados": [],
            "interfaces_avancadas": [],
            "sistemas_autonomos": []
        }
        
        # Baseado nos padrões identificados
        if self.visao_holistica.get('padroes_interfaces', {}).get('realidade_virtual'):
            arquitetura["interfaces_avancadas"].append("Hub de Realidade Virtual")
        
        if self.visao_holistica.get('padroes_interfaces', {}).get('laboratorios_especializados'):
            arquitetura["laboratorios_especializados"].extend([
                "EnergyLab (Energia Quântica)",
                "QuantumLab (Computação Quântica)", 
                "NeuralLab (Interfaces Neurais)",
                "HealingLab (Biorressonância)"
            ])
        
        # Adicionar sistemas complexos como autônomos
        sistemas_complexos = self.visao_holistica.get('sistemas_complexidade', {}).get('alta_complexidade', [])
        for sistema in sistemas_complexos[:5]:  # Top 5 mais complexos
            arquitetura["sistemas_autonomos"].append(sistema["nome"])
        
        self.visao_holistica['arquitetura_ideal'] = arquitetura
        
        print("   🎯 Arquitetura Omega Recomendada:")
        for categoria, itens in arquitetura.items():
            print(f"      📁 {categoria.replace('_', ' ').title()}:")
            for item in itens if isinstance(itens, list) else [itens]:
                if isinstance(item, dict):
                    for k, v in item.items():
                        print(f"         • {k}: {v}")
                else:
                    print(f"         • {item}")
        
        # Salvar arquitetura
        with open('arquitetura_omega_ideal.json', 'w', encoding='utf-8') as f:
            json.dump(arquitetura, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Arquitetura ideal salva em: arquitetura_omega_ideal.json")

# Executar análise Omega
if __name__ == "__main__":
    analisador_omega = AnalisadorOmega()
    analisador_omega.analise_omega()
