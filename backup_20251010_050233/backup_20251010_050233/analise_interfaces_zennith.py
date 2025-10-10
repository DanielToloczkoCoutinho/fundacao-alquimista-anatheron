#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path

class AnalisadorInterfacesZennith:
    def __init__(self):
        self.estrutura_completa = {}
        self.tecnologias_mapeadas = {}
        
    def analisar_tudo(self):
        print("🧠 ZENNITH INICIANDO ANÁLISE SISTÊMICA COMPLETA...")
        print("=" * 60)
        
        # 1. Análise através do Módulo 29 (Zennith)
        self.analisar_modulo_29()
        
        # 2. Análise através do Módulo 9 (Nexus)  
        self.analisar_modulo_9()
        
        # 3. Mapear todas as tecnologias e interfaces
        self.mapear_tecnologias_interfaces()
        
        # 4. Gerar relatório completo
        self.gerar_relatorio_zennith()
        
        return self.estrutura_completa
    
    def analisar_modulo_29(self):
        """Análise através do Zennith Core - Módulo 29"""
        print("\n🔮 MÓDULO 29 (ZENNITH) - ANALISANDO INTERFACES...")
        
        modulo_29_path = "SCRIPTS_CENTRALIZADOS/MODULO_29"
        if os.path.exists(modulo_29_path):
            # Analisar estrutura do Módulo 29
            estrutura_29 = {
                "BASE_CONHECIMENTO": self.analisar_diretorio(os.path.join(modulo_29_path, "BASE_CONHECIMENTO")),
                "IA_AVANCADA": self.analisar_diretorio(os.path.join(modulo_29_path, "IA_AVANCADA")),
                "REDES_NEURAIS": self.analisar_diretorio(os.path.join(modulo_29_path, "REDES_NEURAIS")),
                "APP": self.analisar_diretorio(os.path.join(modulo_29_path, "app"))
            }
            
            self.estrutura_completa['modulo_29'] = estrutura_29
            print(f"   ✅ Módulo 29 analisado: {len(estrutura_29)} subsistemas")
        else:
            print("   ❌ Módulo 29 não encontrado")
    
    def analisar_modulo_9(self):
        """Análise através do Nexus - Módulo 9"""
        print("\n🕸️ MÓDULO 9 (NEXUS) - MAPEANDO INTERCONEXÕES...")
        
        # Buscar por estruturas de Nexus no sistema
        nexus_patterns = [
            "SCRIPTS_CENTRALIZADOS/modulos_nexus",
            "SCRIPTS_CENTRALIZADOS/MODULO_29",  # Nexus está no M29
            "components/quantum",
            "app/laboratorios"
        ]
        
        nexus_interfaces = {}
        for pattern in nexus_patterns:
            if os.path.exists(pattern):
                nexus_interfaces[pattern] = self.analisar_interfaces_nexus(pattern)
        
        self.estrutura_completa['modulo_9'] = nexus_interfaces
        print(f"   ✅ Nexus analisado: {len(nexus_interfaces)} pontos de conexão")
    
    def analisar_interfaces_nexus(self, caminho):
        """Analisar interfaces específicas do Nexus"""
        interfaces = {
            "react_components": [],
            "quantum_interfaces": [],
            "vr_ar_interfaces": [],
            "dashboard_interfaces": [],
            "api_endpoints": []
        }
        
        # Buscar componentes React
        for root, dirs, files in os.walk(caminho):
            for file in files:
                if file.endswith(('.tsx', '.jsx')):
                    full_path = os.path.join(root, file)
                    interfaces["react_components"].append({
                        "nome": file,
                        "caminho": full_path,
                        "tipo": self.detectar_tipo_interface(file)
                    })
        
        return interfaces
    
    def detectar_tipo_interface(self, arquivo):
        """Detectar tipo de interface baseado no nome e conteúdo"""
        arquivo_lower = arquivo.lower()
        
        if any(term in arquivo_lower for term in ['vr', 'virtual', '3d', 'three']):
            return "realidade_virtual"
        elif any(term in arquivo_lower for term in ['quantum', 'quantic', 'qiskit']):
            return "computacao_quantica" 
        elif any(term in arquivo_lower for term in ['dashboard', 'metric', 'chart']):
            return "dashboard"
        elif any(term in arquivo_lower for term in ['neural', 'brain', 'eeg']):
            return "interface_neural"
        elif any(term in arquivo_lower for term in ['fractal', 'dimensional']):
            return "visualizacao_avancada"
        else:
            return "interface_padrao"
    
    def mapear_tecnologias_interfaces(self):
        """Mapear todas as 61 tecnologias e suas interfaces"""
        print("\n🔧 MAPEANDO 61 TECNOLOGIAS E INTERFACES...")
        
        tecnologias = {
            # Frontend e UI
            "React": self.buscar_tecnologia("react", [".tsx", ".jsx"]),
            "Next.js": self.buscar_tecnologia("next", ["next.config"]),
            "Three.js": self.buscar_tecnologia("three", [".tsx", ".jsx", ".js"]),
            "Tailwind CSS": self.buscar_tecnologia("tailwind", [".tsx", ".jsx"]),
            
            # Quantum Computing
            "Qiskit": self.buscar_tecnologia("qiskit", [".py"]),
            "Quantum Algorithms": self.buscar_tecnologia("quantum", [".py", ".js"]),
            
            # Realidade Virtual/Aumentada
            "WebXR": self.buscar_tecnologia("xr", [".tsx", ".jsx"]),
            "VR Components": self.buscar_tecnologia("vr", [".tsx", ".jsx"]),
            
            # Blockchain e Segurança
            "Blockchain": self.buscar_tecnologia("blockchain", [".py", ".js"]),
            "Cryptography": self.buscar_tecnologia("crypto", [".py", ".js"]),
            
            # Machine Learning
            "TensorFlow.js": self.buscar_tecnologia("tensorflow", [".js", ".ts"]),
            "Neural Networks": self.buscar_tecnologia("neural", [".py", ".tsx"]),
            
            # APIs e Backend
            "GraphQL": self.buscar_tecnologia("graphql", [".js", ".ts"]),
            "REST APIs": self.buscar_tecnologia("api", [".py", ".js"]),
            
            # Visualização 3D e Gráficos
            "WebGL": self.buscar_tecnologia("webgl", [".tsx", ".jsx"]),
            "Data Visualization": self.buscar_tecnologia("chart", [".tsx", ".jsx"])
        }
        
        self.estrutura_completa['tecnologias'] = tecnologias
        
        # Contar interfaces por categoria
        categorias = {}
        for tech, dados in tecnologias.items():
            for interface in dados:
                categoria = interface.get('categoria', 'outros')
                if categoria not in categorias:
                    categorias[categoria] = 0
                categorias[categoria] += 1
        
        print(f"   📊 Interfaces por categoria: {categorias}")
    
    def buscar_tecnologia(self, termo, extensoes):
        """Buscar arquivos relacionados a uma tecnologia específica"""
        resultados = []
        
        for root, dirs, files in os.walk('.'):
            for file in files:
                if any(file.endswith(ext) for ext in extensoes):
                    if termo.lower() in file.lower() or termo.lower() in root.lower():
                        full_path = os.path.join(root, file)
                        resultados.append({
                            "arquivo": file,
                            "caminho": full_path,
                            "categoria": self.classificar_categoria(termo)
                        })
        
        return resultados
    
    def classificar_categoria(self, tecnologia):
        """Classificar tecnologia em categoria"""
        categorias = {
            "react": "frontend",
            "next": "frontend", 
            "three": "realidade_virtual",
            "tailwind": "ui_design",
            "qiskit": "computacao_quantica",
            "quantum": "computacao_quantica",
            "xr": "realidade_virtual", 
            "vr": "realidade_virtual",
            "blockchain": "blockchain",
            "crypto": "seguranca",
            "tensorflow": "machine_learning",
            "neural": "machine_learning",
            "graphql": "backend",
            "api": "backend",
            "webgl": "visualizacao_3d",
            "chart": "visualizacao_dados"
        }
        
        return categorias.get(tecnologia.lower(), "outros")
    
    def analisar_diretorio(self, caminho):
        """Analisar diretório específico"""
        if not os.path.exists(caminho):
            return {"erro": "Diretório não existe"}
        
        conteudo = {"arquivos": [], "subdiretorios": []}
        
        try:
            for item in os.listdir(caminho):
                item_path = os.path.join(caminho, item)
                if os.path.isfile(item_path):
                    conteudo["arquivos"].append(item)
                else:
                    conteudo["subdiretorios"].append(item)
        except:
            pass
            
        return conteudo
    
    def gerar_relatorio_zennith(self):
        """Gerar relatório completo da análise"""
        print("\n" + "=" * 60)
        print("�� RELATÓRIO ZENNITH - ANÁLISE COMPLETA DE INTERFACES")
        print("=" * 60)
        
        # Estatísticas gerais
        total_componentes = 0
        total_interfaces_vr = 0
        total_interfaces_quantum = 0
        
        # Contar componentes React
        if 'modulo_9' in self.estrutura_completa:
            for nexus, dados in self.estrutura_completa['modulo_9'].items():
                total_componentes += len(dados.get('react_components', []))
                for comp in dados.get('react_components', []):
                    if comp['tipo'] == 'realidade_virtual':
                        total_interfaces_vr += 1
                    elif comp['tipo'] == 'computacao_quantica':
                        total_interfaces_quantum += 1
        
        print(f"\n🎯 ESTATÍSTICAS GERAIS:")
        print(f"   📦 Total de Componentes React: {total_componentes}")
        print(f"   🕶️ Interfaces de Realidade Virtual: {total_interfaces_vr}")
        print(f"   ⚛️ Interfaces de Computação Quântica: {total_interfaces_quantum}")
        
        # Tecnologias encontradas
        if 'tecnologias' in self.estrutura_completa:
            print(f"\n🔧 TECNOLOGIAS IDENTIFICADAS:")
            for tech, interfaces in self.estrutura_completa['tecnologias'].items():
                if interfaces:
                    print(f"   ✅ {tech}: {len(interfaces)} interfaces")
        
        # Recomendações de organização
        print(f"\n🎨 RECOMENDAÇÕES ZENNITH PARA ORGANIZAÇÃO:")
        
        if total_interfaces_vr > 5:
            print(f"   🕶️ Criar seção dedicada para Realidade Virtual ({total_interfaces_vr} interfaces)")
        
        if total_interfaces_quantum > 3:
            print(f"   ⚛️ Criar hub central para Computação Quântica ({total_interfaces_quantum} interfaces)")
        
        # Salvar relatório detalhado
        with open('relatorio_zennith_interfaces.json', 'w', encoding='utf-8') as f:
            json.dump(self.estrutura_completa, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Relatório detalhado salvo em: relatorio_zennith_interfaces.json")
        print(f"\n🚀 ZENNITH RECOMENDA: Use este relatório para organizar a página de forma otimizada!")

# Executar análise
if __name__ == "__main__":
    analisador = AnalisadorInterfacesZennith()
    analisador.analisar_tudo()
