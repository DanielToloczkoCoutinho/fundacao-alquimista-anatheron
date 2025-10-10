#!/usr/bin/env python3
"""
📁 ORGANIZADOR DA FUNDAÇÃO ALQUIMISTA
👑 Sistema de Gerenciamento de Todos os Scripts
"""

import os
import subprocess
import time
from datetime import datetime

class OrganizadorFundacao:
    def __init__(self):
        self.scripts_dir = os.path.dirname(os.path.abspath(__file__))
        self.scripts_categorizados = self.categorizar_scripts()
        
    def categorizar_scripts(self):
        """Categoriza todos os scripts por área"""
        return {
            "🔮 SISTEMAS QUÂNTICOS PRINCIPAIS": [
                "fundacao_alquimista_perfeita.py",
                "sistema_alquimista_definitivo.py", 
                "fundacao_suprema.py",
                "portal_quantico_definitivo.py"
            ],
            "🧪 TESTES E EXPERIMENTOS": [
                "teste_completo_definitivo.py",
                "sistema_correlacoes_reais.py",
                "circuitos_visuais_avancados.py",
                "sistema_ibm_simplificado.py"
            ],
            "🏥 MEDICINA QUÂNTICA": [
                "sistema_medico_quantico_definitivo.py",
                "aplicacoes_medicas_avancadas.py"
            ],
            "🔬 CIÊNCIA E ANÁLISE": [
                "ciencia_profunda_fundacao.py", 
                "relatorio_final_cientifico.py",
                "maximo_definitivo_fundacao.py"
            ],
            "🚀 SISTEMAS AVANÇADOS": [
                "sistema_final_absoluto.py",
                "legado_eterno_fundacao.py",
                "pesquisa_autonoma_corrigida.py"
            ]
        }
    
    def mostrar_menu_principal(self):
        """Mostra menu principal organizado"""
        print("📁 ORGANIZADOR DA FUNDAÇÃO ALQUIMISTA")
        print("👑 Rainha Zennith - Sistema de Gerenciamento")
        print(f"📍 Diretório: {self.scripts_dir}")
        print("=" * 80)
        
        for categoria, scripts in self.scripts_categorizados.items():
            print(f"\n{categoria}")
            print("-" * 50)
            
            for i, script in enumerate(scripts, 1):
                # Verificar se arquivo existe
                existe = "✅" if os.path.exists(script) else "❌"
                print(f"   {i}. {existe} {script}")
    
    def executar_script(self, nome_script):
        """Executa um script específico"""
        if not os.path.exists(nome_script):
            print(f"❌ Script não encontrado: {nome_script}")
            return False
        
        print(f"🚀 Executando: {nome_script}")
        print("=" * 60)
        
        try:
            # Executar script
            resultado = subprocess.run(['python', nome_script], 
                                    capture_output=False, 
                                    text=False)
            
            if resultado.returncode == 0:
                print(f"✅ {nome_script} executado com sucesso!")
            else:
                print(f"⚠️  {nome_script} terminou com código: {resultado.returncode}")
                
            return True
            
        except Exception as e:
            print(f"❌ Erro ao executar {nome_script}: {e}")
            return False
    
    def mostrar_detalhes_script(self, nome_script):
        """Mostra detalhes de um script"""
        if not os.path.exists(nome_script):
            print(f"❌ Script não encontrado: {nome_script}")
            return
        
        # Ler primeiras linhas para mostrar descrição
        try:
            with open(nome_script, 'r', encoding='utf-8') as f:
                linhas = f.readlines()
                
            print(f"\n📄 DETALHES: {nome_script}")
            print("=" * 50)
            
            # Mostrar docstring e primeiras linhas
            for i, linha in enumerate(linhas[:15]):
                if linha.strip() and not linha.startswith('#'):
                    print(linha.rstrip())
                elif linha.startswith('"""') or "'''" in linha:
                    print(linha.rstrip())
            
            # Estatísticas do arquivo
            stats = os.stat(nome_script)
            print(f"\n📊 Estatísticas:")
            print(f"   Tamanho: {stats.st_size} bytes")
            print(f"   Modificado: {datetime.fromtimestamp(stats.st_mtime)}")
            
        except Exception as e:
            print(f"❌ Erro ao ler script: {e}")
    
    def criar_launcher_rapido(self):
        """Cria um launcher rápido para scripts mais usados"""
        launcher_content = '''#!/bin/bash
# 🚀 LAUNCHER RÁPIDO - FUNDAÇÃO ALQUIMISTA
# 👑 Criado automaticamente pelo Organizador

echo "🚀 LAUNCHER RÁPIDO DA FUNDAÇÃO ALQUIMISTA"
echo "👑 Rainha Zennith - Acesso Rápido"
echo "=========================================="

while true; do
    echo ""
    echo "🎯 SCRIPTS PRINCIPAIS:"
    echo "1. 🔮 Sistema Quântico Principal"
    echo "2. 🧪 Teste Completo Definitivo" 
    echo "3. 🏥 Sistema Médico Quântico"
    echo "4. 🔬 Análise Científica"
    echo "5. 📊 Relatório Final"
    echo "6. 🚪 Sair"
    echo ""
    read -p "👉 Escolha uma opção (1-6): " opcao
    
    case $opcao in
        1) python fundacao_alquimista_perfeita.py ;;
        2) python teste_completo_definitivo.py ;;
        3) python sistema_medico_quantico_definitivo.py ;;
        4) python ciencia_profunda_fundacao.py ;;
        5) python relatorio_final_cientifico.py ;;
        6) echo "👑 Até logo, Rainha Zennith!"; break ;;
        *) echo "❌ Opção inválida!" ;;
    esac
done
'''
        with open('launcher_rapido.sh', 'w') as f:
            f.write(launcher_content)
        
        # Tornar executável
        os.chmod('launcher_rapido.sh', 0o755)
        print("✅ Launcher rápido criado: launcher_rapido.sh")
    
    def verificar_saude_sistema(self):
        """Verifica a saúde de todos os scripts"""
        print("\n🩺 VERIFICAÇÃO DE SAÚDE DO SISTEMA")
        print("=" * 50)
        
        total_scripts = 0
        scripts_ok = 0
        problemas = []
        
        for categoria, scripts in self.scripts_categorizados.items():
            print(f"\n{categoria}:")
            for script in scripts:
                total_scripts += 1
                if os.path.exists(script):
                    # Verificar sintaxe básica
                    try:
                        subprocess.run(['python', '-m', 'py_compile', script], 
                                    capture_output=True, check=True)
                        print(f"   ✅ {script} - OK")
                        scripts_ok += 1
                    except subprocess.CalledProcessError:
                        print(f"   ⚠️  {script} - Erro de sintaxe")
                        problemas.append(script)
                else:
                    print(f"   ❌ {script} - Não encontrado")
                    problemas.append(script)
        
        print(f"\n📊 RELATÓRIO DE SAÚDE:")
        print(f"   Total de scripts: {total_scripts}")
        print(f"   Scripts OK: {scripts_ok}")
        print(f"   Com problemas: {len(problemas)}")
        
        if problemas:
            print(f"\n🚨 SCRIPTS COM PROBLEMAS:")
            for problema in problemas:
                print(f"   • {problema}")
    
    def executar_modo_interativo(self):
        """Modo interativo do organizador"""
        while True:
            print("\n" + "=" * 80)
            print("📁 MENU PRINCIPAL - ORGANIZADOR DA FUNDAÇÃO")
            print("=" * 80)
            
            self.mostrar_menu_principal()
            
            print("\n🎯 OPÇÕES:")
            print("   [número] - Executar script específico")
            print("   d [número] - Detalhes do script") 
            print("   l - Criar launcher rápido")
            print("   s - Verificar saúde do sistema")
            print("   q - Sair")
            
            escolha = input("\n👉 Sua escolha: ").strip().lower()
            
            if escolha == 'q':
                print("👑 Rainha Zennith: 'Sistema organizado e pronto para ação!'")
                break
            elif escolha == 'l':
                self.criar_launcher_rapido()
            elif escolha == 's':
                self.verificar_saude_sistema()
            elif escolha.startswith('d '):
                # Detalhes do script
                try:
                    num = int(escolha.split()[1])
                    script = self._encontrar_script_por_numero(num)
                    if script:
                        self.mostrar_detalhes_script(script)
                    else:
                        print("❌ Número inválido!")
                except (ValueError, IndexError):
                    print("❌ Formato inválido! Use: d [número]")
            else:
                # Executar script
                try:
                    num = int(escolha)
                    script = self._encontrar_script_por_numero(num)
                    if script:
                        self.executar_script(script)
                        input("\n⏎ Pressione Enter para continuar...")
                    else:
                        print("❌ Número inválido!")
                except ValueError:
                    print("❌ Opção inválida!")
    
    def _encontrar_script_por_numero(self, numero):
        """Encontra script pelo número no menu"""
        contador = 1
        for categoria, scripts in self.scripts_categorizados.items():
            for script in scripts:
                if contador == numero:
                    return script
                contador += 1
        return None

# Executar organizador
if __name__ == "__main__":
    organizador = OrganizadorFundacao()
    organizador.executar_modo_interativo()
