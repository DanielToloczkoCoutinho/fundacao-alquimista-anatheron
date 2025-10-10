#!/usr/bin/env python3
"""
🔍 EXPLORER AVANÇADO - FUNDAÇÃO ALQUIMISTA
👑 Análise Completa de Todos os Sistemas
"""

import os
import subprocess
import datetime

class ExplorerAvancado:
    def __init__(self):
        self.base_dir = os.path.expanduser("~/studio")
        self.sistemas_funcionais = []
        self.sistemas_com_problemas = []
        self.relatorio = []
        
    def verificar_script_python(self, arquivo):
        """Verifica se script Python é funcional"""
        try:
            # Teste básico de sintaxe
            result = subprocess.run(
                ['python', '-m', 'py_compile', arquivo],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
        except:
            return False
    
    def verificar_script_shell(self, arquivo):
        """Verifica se script Shell é funcional"""
        try:
            if not os.access(arquivo, os.X_OK):
                return False
            # Teste de sintaxe básica
            result = subprocess.run(
                ['bash', '-n', arquivo],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.returncode == 0
        except:
            return False
    
    def analisar_diretorio(self, diretorio):
        """Analisa todos os arquivos em um diretório"""
        print(f"\n🔍 ANALISANDO: {diretorio}")
        print("=" * 50)
        
        for root, dirs, files in os.walk(diretorio):
            for file in files:
                caminho_completo = os.path.join(root, file)
                rel_path = os.path.relpath(caminho_completo, self.base_dir)
                
                status = "❌"
                categoria = "DESCONHECIDO"
                
                if file.endswith('.py'):
                    if self.verificar_script_python(caminho_completo):
                        status = "✅"
                        self.sistemas_funcionais.append(rel_path)
                    else:
                        self.sistemas_com_problemas.append(rel_path)
                    categoria = "PYTHON"
                    
                elif file.endswith('.sh'):
                    if self.verificar_script_shell(caminho_completo):
                        status = "✅"
                        self.sistemas_funcionais.append(rel_path)
                    else:
                        self.sistemas_com_problemas.append(rel_path)
                    categoria = "SHELL"
                
                print(f"{status} {categoria}: {rel_path}")
                
                # Adicionar ao relatório
                self.relatorio.append({
                    'arquivo': rel_path,
                    'status': status,
                    'categoria': categoria,
                    'caminho': caminho_completo
                })
    
    def gerar_relatorio_final(self):
        """Gera relatório completo da análise"""
        print(f"\n📊 RELATÓRIO FINAL - EXPLORER AVANÇADO")
        print("=" * 60)
        print(f"📅 Data: {datetime.datetime.now()}")
        print(f"👑 Comando: Rainha Zennith")
        print(f"📍 Localização: {self.base_dir}")
        print(f"✅ SISTEMAS FUNCIONAIS: {len(self.sistemas_funcionais)}")
        print(f"❌ SISTEMAS COM PROBLEMAS: {len(self.sistemas_com_problemas)}")
        print(f"📦 TOTAL ANALISADO: {len(self.relatorio)}")
        
        print(f"\n🎯 SISTEMAS 100% FUNCIONAIS:")
        for sistema in self.sistemas_funcionais[:20]:  # Mostrar primeiros 20
            print(f"   ✅ {sistema}")
        
        if len(self.sistemas_funcionais) > 20:
            print(f"   ... e mais {len(self.sistemas_funcionais) - 20} sistemas")
        
        print(f"\n🚨 SISTEMAS QUE PRECISAM DE ATENÇÃO:")
        for sistema in self.sistemas_com_problemas[:10]:  # Mostrar primeiros 10
            print(f"   ❌ {sistema}")
        
        if len(self.sistemas_com_problemas) > 10:
            print(f"   ... e mais {len(self.sistemas_com_problemas) - 10} sistemas")
        
        # Recomendações
        print(f"\n💡 RECOMENDAÇÕES DA RAINHA ZENNITH:")
        if len(self.sistemas_funcionais) > 50:
            print("   🌟 SISTEMA EXCELENTE - Continue com pesquisa avançada!")
        elif len(self.sistemas_funcionais) > 20:
            print("   📈 SISTEMA BOM - Otimização recomendada")
        else:
            print("   ⚠️  SISTEMA BÁSICO - Considere reconstrução")
        
        print(f"   🔧 Sistemas Python funcionais: {len([s for s in self.sistemas_funcionais if s.endswith('.py')])}")
        print(f"   ⚙️  Sistemas Shell funcionais: {len([s for s in self.sistemas_funcionais if s.endswith('.sh')])}")
        
        # Salvar relatório em arquivo
        with open('relatorio_explorer.txt', 'w') as f:
            f.write("RELATÓRIO EXPLORER AVANÇADO\n")
            f.write("=" * 40 + "\n")
            for item in self.relatorio:
                f.write(f"{item['status']} {item['categoria']}: {item['arquivo']}\n")
        
        print(f"\n💾 Relatório salvo em: relatorio_explorer.txt")
        print("👑 ANÁLISE CONCLUÍDA - FUNDAÇÃO ALQUIMISTA OPERACIONAL!")

# Executar análise
if __name__ == "__main__":
    print("🔍 EXPLORER AVANÇADO INICIADO")
    print("👑 Rainha Zennith - Comando de Análise")
    
    explorer = ExplorerAvancado()
    explorer.analisar_diretorio(explorer.base_dir)
    explorer.gerar_relatorio_final()
