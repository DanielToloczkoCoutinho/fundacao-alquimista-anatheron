#!/usr/bin/env python3
import os
import json
import subprocess
from pathlib import Path

class AnalisadorEficienciaZennith:
    def __init__(self):
        self.ineficiencias = {}
        self.recomendacoes = {}
        self.metricas_sistema = {}
        
    def analise_completa(self):
        print("🧠 ZENNITH INICIANDO ANÁLISE DE EFICIÊNCIA COMPLETA...")
        print("=" * 70)
        
        # 1. Análise de Performance do Build
        self.analisar_performance_build()
        
        # 2. Análise de Estrutura de Arquivos
        self.analisar_estrutura_arquivos()
        
        # 3. Análise de Dependências
        self.analisar_dependencias()
        
        # 4. Análise de Interfaces
        self.analisar_interfaces()
        
        # 5. Análise de Configurações
        self.analisar_configuracoes()
        
        # 6. Gerar Relatório Final
        self.gerar_relatorio_eficiencia()
        
        return self.ineficiencias
    
    def analisar_performance_build(self):
        """Analisar performance do build Next.js"""
        print("\n⚡ ANALISANDO PERFORMANCE DO BUILD...")
        
        try:
            # Verificar tamanho do build
            build_dir = ".next"
            if os.path.exists(build_dir):
                tamanho_total = 0
                for root, dirs, files in os.walk(build_dir):
                    for file in files:
                        caminho = os.path.join(root, file)
                        tamanho_total += os.path.getsize(caminho)
                
                tamanho_mb = tamanho_total / (1024 * 1024)
                self.metricas_sistema['tamanho_build'] = f"{tamanho_mb:.2f} MB"
                
                if tamanho_mb > 50:
                    self.ineficiencias['build_grande'] = {
                        "nivel": "ALTO",
                        "descricao": f"Build muito grande: {tamanho_mb:.2f} MB",
                        "impacto": "Performance reduzida"
                    }
                else:
                    print(f"   ✅ Tamanho do build: {tamanho_mb:.2f} MB (Otimizado)")
            
            # Verificar se há análise de bundle
            analise_bundle = os.path.join(build_dir, "analyze")
            if os.path.exists(analise_bundle):
                print("   ✅ Análise de bundle disponível")
            else:
                self.ineficiencias['sem_analise_bundle'] = {
                    "nivel": "BAIXO", 
                    "descricao": "Sem análise de bundle otimizada",
                    "impacto": "Dificuldade na otimização"
                }
                
        except Exception as e:
            print(f"   ⚠️ Erro na análise de build: {e}")
    
    def analisar_estrutura_arquivos(self):
        """Analisar estrutura de arquivos por eficiência"""
        print("\n📁 ANALISANDO ESTRUTURA DE ARQUIVOS...")
        
        # Verificar arquivos desnecessários no deploy
        arquivos_desnecessarios = []
        extensoes_desnecessarias = ['.log', '.tmp', '.backup', '.pre_', '.map']
        
        for root, dirs, files in os.walk('.'):
            for file in files:
                if any(file.endswith(ext) for ext in extensoes_desnecessarias):
                    if 'node_modules' not in root and '.git' not in root:
                        arquivos_desnecessarios.append(os.path.join(root, file))
        
        if arquivos_desnecessarios:
            self.ineficiencias['arquivos_desnecessarios'] = {
                "nivel": "MEDIO",
                "descricao": f"{len(arquivos_desnecessarios)} arquivos desnecessários encontrados",
                "exemplos": arquivos_desnecessarios[:10],
                "impacto": "Deploy mais lento"
            }
        
        # Verificar duplicação de código
        componentes_react = []
        for root, dirs, files in os.walk('./app'):
            for file in files:
                if file.endswith(('.tsx', '.jsx')):
                    componentes_react.append(os.path.join(root, file))
        
        self.metricas_sistema['componentes_react'] = len(componentes_react)
        print(f"   ✅ {len(componentes_react)} componentes React encontrados")
    
    def analisar_dependencias(self):
        """Analisar dependências do projeto"""
        print("\n📦 ANALISANDO DEPENDÊNCIAS...")
        
        try:
            # Verificar package.json
            if os.path.exists('package.json'):
                with open('package.json', 'r') as f:
                    package_data = json.load(f)
                
                dependencias = package_data.get('dependencies', {})
                dev_dependencias = package_data.get('devDependencies', {})
                
                total_deps = len(dependencias) + len(dev_dependencias)
                self.metricas_sistema['total_dependencias'] = total_deps
                
                print(f"   ✅ {total_deps} dependências encontradas")
                
                # Verificar dependências pesadas
                dependencias_pesadas = ['three', '@types/three', 'qiskit', 'tensorflow']
                encontradas = []
                
                for dep in dependencias_pesadas:
                    if dep in dependencias or any(dep in key for key in dependencias.keys()):
                        encontradas.append(dep)
                
                if encontradas:
                    self.ineficiencias['dependencias_pesadas'] = {
                        "nivel": "MEDIO",
                        "descricao": f"Dependências pesadas: {', '.join(encontradas)}",
                        "impacto": "Build mais lento e maior"
                    }
            
        except Exception as e:
            print(f"   ⚠️ Erro na análise de dependências: {e}")
    
    def analisar_interfaces(self):
        """Analisar eficiência das interfaces"""
        print("\n🎨 ANALISANDO EFICIÊNCIA DAS INTERFACES...")
        
        # Verificar componentes não utilizados
        componentes = []
        for root, dirs, files in os.walk('./components'):
            for file in files:
                if file.endswith(('.tsx', '.jsx')):
                    componentes.append(file)
        
        # Verificar páginas
        paginas = []
        for root, dirs, files in os.walk('./app'):
            if 'page.tsx' in files or 'page.jsx' in files:
                paginas.append(root)
        
        self.metricas_sistema['componentes_total'] = len(componentes)
        self.metricas_sistema['paginas_total'] = len(paginas)
        
        print(f"   ✅ {len(componentes)} componentes e {len(paginas)} páginas")
        
        # Verificar se há lazy loading
        arquivos_com_lazy = []
        for componente in componentes:
            try:
                caminho = os.path.join('./components', componente)
                with open(caminho, 'r') as f:
                    conteudo = f.read()
                    if 'lazy' in conteudo or 'dynamic' in conteudo:
                        arquivos_com_lazy.append(componente)
            except:
                pass
        
        if not arquivos_com_lazy:
            self.ineficiencias['sem_lazy_loading'] = {
                "nivel": "MEDIO",
                "descricao": "Sem implementação de lazy loading",
                "impacto": "Carregamento inicial mais lento"
            }
    
    def analisar_configuracoes(self):
        """Analisar configurações do Next.js"""
        print("\n⚙️ ANALISANDO CONFIGURAÇÕES...")
        
        # Verificar next.config.js
        if os.path.exists('next.config.js'):
            try:
                with open('next.config.js', 'r') as f:
                    config_content = f.read()
                
                otimizacoes_encontradas = []
                
                if 'compression' in config_content:
                    otimizacoes_encontradas.append('compressão')
                if 'optimizeFonts' in config_content:
                    otimizacoes_encontradas.append('fontes otimizadas')
                if 'optimizeCss' in config_content:
                    otimizacoes_encontradas.append('CSS otimizado')
                
                if otimizacoes_encontradas:
                    print(f"   ✅ Otimizações encontradas: {', '.join(otimizacoes_encontradas)}")
                else:
                    self.ineficiencias['configuracoes_otimizacao'] = {
                        "nivel": "BAIXO",
                        "descricao": "Configurações de otimização básicas",
                        "impacto": "Performance não maximizada"
                    }
                    
            except Exception as e:
                print(f"   ⚠️ Erro na análise de configurações: {e}")
        
        # Verificar se há PWA configurado
        if not os.path.exists('public/manifest.json'):
            self.ineficiencias['sem_pwa'] = {
                "nivel": "BAIXO",
                "descricao": "Sem configuração PWA",
                "impacto": "Experiência mobile não otimizada"
            }
    
    def gerar_relatorio_eficiencia(self):
        """Gerar relatório completo de eficiência"""
        print("\n" + "=" * 70)
        print("📊 RELATÓRIO ZENNITH - ANÁLISE DE EFICIÊNCIA")
        print("=" * 70)
        
        # Métricas do sistema
        print(f"\n🎯 MÉTRICAS DO SISTEMA:")
        for metrica, valor in self.metricas_sistema.items():
            print(f"   📈 {metrica.replace('_', ' ').title()}: {valor}")
        
        # Ineficiências encontradas
        if self.ineficiencias:
            print(f"\n⚠️  INEFICIÊNCIAS IDENTIFICADAS:")
            
            inef_por_nivel = {"ALTO": [], "MEDIO": [], "BAIXO": []}
            for nome, dados in self.ineficiencias.items():
                inef_por_nivel[dados["nivel"]].append((nome, dados))
            
            for nivel in ["ALTO", "MEDIO", "BAIXO"]:
                if inef_por_nivel[nivel]:
                    print(f"\n   🔴 {nivel} IMPACTO:")
                    for nome, dados in inef_por_nivel[nivel]:
                        print(f"      • {dados['descricao']}")
                        print(f"        Impacto: {dados['impacto']}")
                        
                        if 'exemplos' in dados:
                            print(f"        Exemplos: {', '.join(dados['exemplos'][:3])}")
        else:
            print(f"\n✅ SISTEMA OTIMIZADO - Nenhuma ineficiência crítica encontrada!")
        
        # Recomendações
        print(f"\n💡 RECOMENDAÇÕES ZENNITH:")
        
        recomendacoes = []
        
        if 'build_grande' in self.ineficiencias:
            recomendacoes.append("Implementar code splitting e lazy loading")
        
        if 'arquivos_desnecessarios' in self.ineficiencias:
            recomendacoes.append("Limpar arquivos temporários e de backup")
        
        if 'dependencias_pesadas' in self.ineficiencias:
            recomendacoes.append("Otimizar uso de Three.js e Qiskit")
        
        if 'sem_lazy_loading' in self.ineficiencias:
            recomendacoes.append("Implementar lazy loading para componentes pesados")
        
        if 'sem_analise_bundle' in self.ineficiencias:
            recomendacoes.append("Adicionar análise de bundle @next/bundle-analyzer")
        
        if 'sem_pwa' in self.ineficiencias:
            recomendacoes.append("Configurar PWA para melhor experiência mobile")
        
        if not recomendacoes:
            recomendacoes.append("Sistema bem otimizado! Manter monitoramento contínuo")
        
        for i, recomendacao in enumerate(recomendacoes, 1):
            print(f"   {i}. {recomendacao}")
        
        # Status geral
        total_ineficiencias = len(self.ineficiencias)
        if total_ineficiencias == 0:
            status = "✅ OTIMIZADO"
        elif total_ineficiencias <= 2:
            status = "🟡 BOM" 
        else:
            status = "🔴 ATENÇÃO"
        
        print(f"\n🏆 STATUS GERAL: {status}")
        print(f"   Ineficiências encontradas: {total_ineficiencias}")
        
        # Salvar relatório detalhado
        relatorio = {
            "metricas": self.metricas_sistema,
            "ineficiencias": self.ineficiencias,
            "recomendacoes": recomendacoes,
            "status_geral": status
        }
        
        with open('relatorio_eficiencia_zennith.json', 'w', encoding='utf-8') as f:
            json.dump(relatorio, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Relatório salvo em: relatorio_eficiencia_zennith.json")

# Executar análise
if __name__ == "__main__":
    analisador = AnalisadorEficienciaZennith()
    analisador.analise_completa()
