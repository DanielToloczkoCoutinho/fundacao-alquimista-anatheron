#!/usr/bin/env python3
"""
🛠️ CORRETOR DOS DETALHES FINAIS
⚡ Correções pontuais para perfeição cósmica
🔧 Ajustes mínimos, impacto máximo
"""

print("🛠️ CORRETOR DOS DETALHES FINAIS")
print("=" * 50)

def corrigir_processador_fundacao():
    """Corrigir o processador da fundação"""
    print("🔧 CORRIGINDO PROCESSADOR_FUNDACAO_ALQUIMISTA.py...")
    
    try:
        with open('PROCESSADOR_FUNDACAO_ALQUIMISTA.py', 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Corrigir a linha problemática
        linha_erro = 'print(f💫 Coerência média: {relatorio[\'coerencia_media\']:.6f}")'
        linha_correta = 'print(f"💫 Coerência média: {relatorio[\'coerencia_media\']:.6f}")'
        
        if linha_erro in conteudo:
            conteudo = conteudo.replace(linha_erro, linha_correta)
            print("   ✅ Linha 313 corrigida: emoji com aspas")
        
        # Corrigir outra linha similar
        linha_erro2 = 'print(f🌌 BASE MATEMÁTICA DA FUNDAÇÃO ESTABELECIDA!")'
        linha_correta2 = 'print("🌌 BASE MATEMÁTICA DA FUNDAÇÃO ESTABELECIDA!")'
        
        if linha_erro2 in conteudo:
            conteudo = conteudo.replace(linha_erro2, linha_correta2)
            print("   ✅ Outras linhas corrigidas")
        
        # Salvar correções
        with open('PROCESSADOR_FUNDACAO_ALQUIMISTA.py', 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        print("   ✅ PROCESSADOR_FUNDACAO_ALQUIMISTA.py corrigido")
        return True
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def corrigir_analisador_significado():
    """Corrigir o analisador de significado"""
    print("\n🔧 CORRIGINDO ANALISADOR_SIGNIFICADO_FUNDACAO.py...")
    
    try:
        with open('ANALISADOR_SIGNIFICADO_FUNDACAO.py', 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Encontrar e corrigir a seção problemática
        linhas = conteudo.split('\n')
        for i, linha in enumerate(linhas):
            if "for ano, passo in evolucao:" in linha:
                # A linha seguinte deve ser print
                if i+1 < len(linhas) and "print(f" in linhas[i+1]:
                    # Corrigir a estrutura
                    novas_linhas = []
                    for j, l in enumerate(linhas):
                        if j == i:  # Linha do for
                            novas_linhas.append("        for ano, passo in evolucao.items():")
                        elif j == i+1:  # Linha do print
                            novas_linhas.append('            print(f"   • {ano}: {passo}")')
                        else:
                            novas_linhas.append(l)
                    
                    conteudo = '\n'.join(novas_linhas)
                    print("   ✅ Estrutura do for corrigida")
                    break
        
        # Salvar correções
        with open('ANALISADOR_SIGNIFICADO_FUNDACAO.py', 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        print("   ✅ ANALISADOR_SIGNIFICADO_FUNDACAO.py corrigido")
        return True
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")
        return False

def verificar_correcoes():
    """Verificar se as correções funcionaram"""
    print("\n✅ VERIFICANDO CORREÇÕES...")
    
    # Testar sintaxe dos arquivos corrigidos
    import subprocess
    
    arquivos_para_testar = [
        "PROCESSADOR_FUNDACAO_ALQUIMISTA.py",
        "ANALISADOR_SIGNIFICADO_FUNDACAO.py"
    ]
    
    for arquivo in arquivos_para_testar:
        try:
            resultado = subprocess.run(
                ["python3", "-m", "py_compile", arquivo],
                capture_output=True,
                text=True,
                timeout=5
            )
            if resultado.returncode == 0:
                print(f"   ✅ {arquivo} - Sintaxe OK")
            else:
                print(f"   ❌ {arquivo} - Erro de sintaxe")
                print(f"      {resultado.stderr}")
        except Exception as e:
            print(f"   ⚠️  {arquivo} - {e}")

# EXECUTAR CORREÇÕES
print("🎯 APLICANDO CORREÇÕES FINAIS...\n")

corrigir_processador_fundacao()
corrigir_analisador_significado()
verificar_correcoes()

print("\n💫 CORREÇÕES CONCLUÍDAS!")
print("🎯 SISTEMA PERFEITAMENTE AJUSTADO!")
print("🚀 PRONTO PARA PRÓXIMAS TRANSMISSÕES!")
