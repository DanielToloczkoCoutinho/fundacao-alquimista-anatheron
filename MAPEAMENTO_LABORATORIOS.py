#!/usr/bin/env python3
"""
🔍 MAPEAMENTO DE LABORATÓRIOS - FUNDAÇÃO ALQUIMISTA
⚛️ Análise completa dos 260+ laboratórios e organização
🎯 Conexão com hierarquia estrutural
"""

import json
import os
from pathlib import Path

print("🔍 MAPEAMENTO DE LABORATÓRIOS - FUNDAÇÃO ALQUIMISTA")
print("=" * 60)

class MapeadorLaboratorios:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.laboratorios = {}
        self.categorias = {}
        
    def descobrir_laboratorios(self):
        """Descobrir todos os laboratórios existentes"""
        print("🔍 DESCOBRINDO LABORATÓRIOS...")
        
        padroes_laboratorios = [
            "laboratorio", "laboratory", "lab", "experimento",
            "teste", "test", "experiment", "estudo", "study"
        ]
        
        laboratorios_encontrados = []
        
        for raiz, dirs, arquivos in os.walk(self.raiz):
            # Verificar diretórios
            for diretorio in dirs:
                dir_lower = diretorio.lower()
                if any(padrao in dir_lower for padrao in padroes_laboratorios):
                    caminho_completo = Path(raiz) / diretorio
                    laboratorios_encontrados.append(caminho_completo)
                    print(f"   ✅ LABORATÓRIO: {caminho_completo}")
            
            # Verificar arquivos
            for arquivo in arquivos:
                arquivo_lower = arquivo.lower()
                if any(padrao in arquivo_lower for padrao in padroes_laboratorios):
                    caminho_completo = Path(raiz) / arquivo
                    laboratorios_encontrados.append(caminho_completo)
                    print(f"   ✅ ARQUIVO DE LABORATÓRIO: {caminho_completo}")
        
        return laboratorios_encontrados
    
    def categorizar_laboratorios(self, laboratorios):
        """Categorizar laboratórios por tipo e função"""
        print("\n📊 CATEGORIZANDO LABORATÓRIOS...")
        
        categorias = {
            'quantico': [],
            'simulacao': [],
            'analise_dados': [],
            'desenvolvimento': [],
            'teste_equacoes': [],
            'interface': [],
            'configuracao': [],
            'outros': []
        }
        
        for lab in laboratorios:
            lab_str = str(lab).lower()
            
            if any(termo in lab_str for termo in ['quant', 'qiskit', 'circuit', 'qubit']):
                categorias['quantico'].append(lab)
            elif any(termo in lab_str for termo in ['simul', 'simulation', 'aer']):
                categorias['simulacao'].append(lab)
            elif any(termo in lab_str for termo in ['analise', 'analysis', 'dados', 'data']):
                categorias['analise_dados'].append(lab)
            elif any(termo in lab_str for termo in ['dev', 'develop', 'script', 'code']):
                categorias['desenvolvimento'].append(lab)
            elif any(termo in lab_str for termo in ['equation', 'equacao', 'formula', 'math']):
                categorias['teste_equacoes'].append(lab)
            elif any(termo in lab_str for termo in ['interface', 'ui', 'web', 'frontend']):
                categorias['interface'].append(lab)
            elif any(termo in lab_str for termo in ['config', 'setup', 'install']):
                categorias['configuracao'].append(lab)
            else:
                categorias['outros'].append(lab)
        
        # Mostrar estatísticas
        for categoria, labs in categorias.items():
            print(f"   📁 {categoria.upper()}: {len(labs)} laboratórios")
        
        return categorias
    
    def analisar_conteudo_laboratorios(self, categorias):
        """Analisar conteúdo dos laboratórios por categoria"""
        print("\n🔬 ANALISANDO CONTEÚDO DOS LABORATÓRIOS...")
        
        analise_conteudo = {}
        
        for categoria, laboratorios in categorias.items():
            print(f"\n   📋 CATEGORIA: {categoria.upper()}")
            analise_conteudo[categoria] = []
            
            for lab in laboratorios[:5]:  # Analisar apenas os 5 primeiros de cada categoria
                try:
                    if lab.is_file():
                        with open(lab, 'r', encoding='utf-8') as f:
                            conteudo = f.read()
                            
                        info = {
                            'caminho': str(lab),
                            'tamanho': len(conteudo),
                            'linhas': conteudo.count('\n') + 1,
                            'tem_equacoes': '=' in conteudo and ('def ' in conteudo or 'import ' in conteudo),
                            'tem_qiskit': 'qiskit' in conteudo.lower(),
                            'tem_ibm': 'ibm' in conteudo.lower() or 'quantum' in conteudo.lower()
                        }
                        
                        analise_conteudo[categoria].append(info)
                        
                        print(f"      📄 {lab.name}")
                        print(f"         • Linhas: {info['linhas']}")
                        print(f"         • Equações: {'✅' if info['tem_equacoes'] else '❌'}")
                        print(f"         • Qiskit: {'✅' if info['tem_qiskit'] else '❌'}")
                        print(f"         • IBM Quantum: {'✅' if info['tem_ibm'] else '❌'}")
                        
                except Exception as e:
                    print(f"      ❌ Erro ao analisar {lab}: {e}")
        
        return analise_conteudo
    
    def executar_mapeamento_completo(self):
        """Executar mapeamento completo de laboratórios"""
        print("🚀 INICIANDO MAPEAMENTO COMPLETO DE LABORATÓRIOS...")
        
        # 1. Descobrir laboratórios
        laboratorios = self.descobrir_laboratorios()
        
        # 2. Categorizar
        categorias = self.categorizar_laboratorios(laboratorios)
        
        # 3. Analisar conteúdo
        analise_conteudo = self.analisar_conteudo_laboratorios(categorias)
        
        # Relatório Final
        print("\n" + "="*70)
        print("🎉 RELATÓRIO DE MAPEAMENTO - LABORATÓRIOS DA FUNDAÇÃO")
        print("="*70)
        
        total_labs = sum(len(labs) for labs in categorias.values())
        print(f"\n📊 ESTATÍSTICAS GERAIS:")
        print(f"   • Total de laboratórios: {total_labs}")
        print(f"   • Categorias identificadas: {len(categorias)}")
        
        print(f"\n🎯 DISTRIBUIÇÃO POR CATEGORIA:")
        for categoria, labs in categorias.items():
            porcentagem = (len(labs) / total_labs) * 100
            print(f"   • {categoria.upper():15} : {len(labs):3d} labs ({porcentagem:5.1f}%)")
        
        print(f"\n🌌 LABORATÓRIOS PRINCIPAIS POR CATEGORIA:")
        for categoria, labs in categorias.items():
            if labs:
                print(f"\n   📁 {categoria.upper()}:")
                for lab in labs[:3]:  # Mostrar 3 principais
                    print(f"      • {lab.name}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS:")
        print("   1. Organizar laboratórios por fluxo de trabalho")
        print("   2. Conectar com hierarquia estrutural")
        print("   3. Implementar sistema de execução unificado")
        print("   4. Preparar para IBM Quantum")
        
        return {
            'total_laboratorios': total_labs,
            'categorias': categorias,
            'analise_conteudo': analise_conteudo
        }

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    mapeador = MapeadorLaboratorios()
    resultados = mapeador.executar_mapeamento_completo()
    
    print(f"\n🌌 MAPEAMENTO DE LABORATÓRIOS CONCLUÍDO!")
    print(f"🎯 {resultados['total_laboratorios']} laboratórios mapeados e categorizados!")
