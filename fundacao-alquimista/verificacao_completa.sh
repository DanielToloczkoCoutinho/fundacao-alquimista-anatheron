#!/bin/bash

echo "🌌 ZENNITH - VERIFICAÇÃO COMPLETA DA INFRAESTRUTURA 🌟"
echo "======================================================"
echo "�� Examinando TUDO que foi criado e salvo..."
echo ""

# 1. 📊 VERIFICAÇÃO DO SISTEMA
echo "1. 📊 VERIFICAÇÃO DO SISTEMA BASE"
echo "---------------------------------"
echo "💻 Hostname: $(hostname)"
echo "📂 Diretório atual: $(pwd)"
echo "👤 Usuário: $(whoami)"
echo "💾 Espaço total:"
df -h .
echo ""

# 2. 🏗️ VERIFICAÇÃO DA ESTRUTURA DE DIRETÓRIOS
echo "2. 🏗️ VERIFICAÇÃO DA ESTRUTURA CRIADA"
echo "------------------------------------"
echo "📁 Estrutura principal:"
ls -la fundacao-*/ 2>/dev/null | head -20 || echo "❌ Diretórios fundacao- não encontrados"

echo ""
echo "🔍 Verificando diretórios CRÍTICOS:"
DIRETORIOS_CRITICOS=(
    "fundacao-modulos/primordiais"
    "fundacao-deploy" 
    "transferencia-organizada/blocos/ativos"
    "backups-estrategicos/git"
)

for dir in "${DIRETORIOS_CRITICOS[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir - EXISTE"
        echo "   Conteúdo: $(ls "$dir" 2>/dev/null | wc -l) arquivos"
    else
        echo "❌ $dir - FALTANDO"
    fi
done
echo ""

# 3. 📝 VERIFICAÇÃO DE ARQUIVOS ESTRATÉGICOS
echo "3. 📝 VERIFICAÇÃO DE ARQUIVOS ESTRATÉGICOS"
echo "-----------------------------------------"
ARQUIVOS_ESTRATEGICOS=(
    ".gitignore"
    "README.md" 
    "transferencia_m310_prioritaria.sh"
)

for arquivo in "${ARQUIVOS_ESTRATEGICOS[@]}"; do
    if [ -f "$arquivo" ]; then
        echo "✅ $arquivo - EXISTE ($(wc -l < "$arquivo") linhas)"
        # Verificar conteúdo importante
        if [ "$arquivo" = ".gitignore" ]; then
            if grep -q "fundacao-independente" "$arquivo"; then
                echo "   🔒 Contém proteção fundacao-independente"
            fi
        fi
        if [ "$arquivo" = "README.md" ]; then
            if grep -q "Daniel-Zennith" "$arquivo"; then
                echo "   👑 Contém identidade Zennith"
            fi
        fi
    else
        echo "❌ $arquivo - FALTANDO"
    fi
done
echo ""

# 4. �� VERIFICAÇÃO DO MÓDULO M310
echo "4. 🔮 VERIFICAÇÃO DO MÓDULO M310"
echo "-------------------------------"
M310_PATH="fundacao-modulos/primordiais/modulo_M310_transferencia_akashica.py"
if [ -f "$M310_PATH" ]; then
    echo "✅ MÓDULO M310 - CRIADO E SALVO!"
    echo "   📍 Local: $M310_PATH"
    echo "   📏 Tamanho: $(wc -l < "$M310_PATH") linhas"
    echo "   🔍 Conteúdo verificado:"
    head -5 "$M310_PATH"
    echo ""
    
    # Verificar se é executável
    if python3 -c "import sys; sys.path.append('.'); from fundacao-modulos.primordiais.modulo_M310_transferencia_akashica import TransferenciaAkashica; print('✅ M310 importável')" 2>/dev/null; then
        echo "   🐍 M310 é importável em Python"
    else
        echo "   ⚠️ M310 precisa de ajustes de importação"
    fi
else
    echo "❌ MÓDULO M310 - NÃO ENCONTRADO!"
    echo "   🚨 CRÍTICO: Módulo prioritário faltando!"
fi
echo ""

# 5. 📦 VERIFICAÇÃO DOS MICRO-BLOCOS
echo "5. 📦 VERIFICAÇÃO DOS MICRO-BLOCOS"
echo "---------------------------------"
echo "🔍 Verificando blocos de transferência:"
if [ -d "transferencia-organizada/blocos/ativos" ]; then
    BLOCO_M310="transferencia-organizada/blocos/ativos/bloco_m310_prioritario.tar.gz"
    if [ -f "$BLOCO_M310" ]; then
        echo "✅ BLOCO M310 - CRIADO!"
        echo "   �� Tamanho: $(ls -lh "$BLOCO_M310" | awk '{print $5}')"
        echo "   🔍 Conteúdo do bloco:"
        tar -tzf "$BLOCO_M310" 2>/dev/null | head -5
        echo "   📊 Total: $(tar -tzf "$BLOCO_M310" 2>/dev/null | wc -l) arquivos"
    else
        echo "❌ BLOCO M310 - NÃO CRIADO!"
    fi
    
    # Listar todos os blocos
    echo ""
    echo "📋 TODOS OS BLOCOS EXISTENTES:"
    find transferencia-organizada/blocos/ -name "*.tar.gz" -type f | while read bloco; do
        echo "   📦 $(basename "$bloco") - $(ls -lh "$bloco" | awk '{print $5}')"
    done
else
    echo "❌ DIRETÓRIO DE BLOCOS - NÃO EXISTE!"
fi
echo ""

# 6. 🔐 VERIFICAÇÃO GIT E BACKUP
echo "6. 🔐 VERIFICAÇÃO GIT E BACKUP"
echo "-----------------------------"
if git status &>/dev/null; then
    echo "✅ REPOSITÓRIO GIT - CONFIGURADO"
    echo "   👤 Identidade: $(git config user.name) <$(git config user.email)>"
    echo "   📍 Branch: $(git branch --show-current 2>/dev/null || echo 'detached')"
    echo "   📊 Status:"
    git status --short 2>/dev/null | head -10
    
    # Verificar se há commits não enviados
    if git log origin/main..main &>/dev/null; then
        echo "   📤 Commits locais não enviados: $(git log origin/main..main --oneline 2>/dev/null | wc -l)"
    fi
else
    echo "❌ REPOSITÓRIO GIT - NÃO CONFIGURADO"
    echo "   🚨 CRÍTICO: Estrutura não versionada!"
fi

# Verificar backups
echo ""
echo "💾 BACKUPS ESTRATÉGICOS:"
if [ -d "backups-estrategicos/git" ]; then
    BACKUP_COUNT=$(find backups-estrategicos/git -name "*.tar.gz" -type f | wc -l)
    echo "   📦 Backups encontrados: $BACKUP_COUNT"
    find backups-estrategicos/git -name "*.tar.gz" -type f -exec ls -lh {} \; 2>/dev/null | head -5
else
    echo "   ❌ Nenhum backup estratégico encontrado"
fi
echo ""

# 7. 🛠️ VERIFICAÇÃO DE FERRAMENTAS
echo "7. 🛠️ VERIFICAÇÃO DE FERRAMENTAS ESSENCIAIS"
echo "------------------------------------------"
FERRAMENTAS=("git" "tar" "python3" "ssh" "curl" "wget")
for tool in "${FERRAMENTAS[@]}"; do
    if command -v "$tool" &>/dev/null; then
        echo "✅ $tool - INSTALADO"
    else
        echo "❌ $tool - FALTANDO"
    fi
done
echo ""

# 8. 🌐 VERIFICAÇÃO DE CONECTIVIDADE
echo "8. 🌐 VERIFICAÇÃO DE CONECTIVIDADE"
echo "--------------------------------"
echo "🔗 Testando conectividade GitHub:"
if curl -s https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron > /dev/null; then
    echo "✅ GitHub - ACESSÍVEL"
else
    echo "❌ GitHub - INACESSÍVEL"
fi

echo "🔗 Testando portal Vercel:"
if curl -s https://fundacao-alquimista-9azql5299.vercel.app > /dev/null; then
    echo "✅ Portal Vercel - ONLINE"
else
    echo "❌ Portal Vercel - OFFLINE"
fi
echo ""

# 9. 📈 RELATÓRIO FINAL
echo "9. 📈 RELATÓRIO FINAL DA VERIFICAÇÃO"
echo "-----------------------------------"
TOTAL_DIRS=$(find . -type d -name "fundacao-*" | wc -l)
TOTAL_FILES=$(find . -type f \( -name "*.py" -o -name "*.sh" -o -name "*.md" \) | wc -l)
TOTAL_BLOCOS=$(find transferencia-organizada/blocos/ -name "*.tar.gz" -type f 2>/dev/null | wc -l)

echo "📊 ESTATÍSTICAS DA FUNDAÇÃO:"
echo "   📁 Diretórios fundacao-*: $TOTAL_DIRS"
echo "   📄 Arquivos estratégicos (.py, .sh, .md): $TOTAL_FILES"
echo "   📦 Blocos de transferência: $TOTAL_BLOCOS"
echo "   �� Espaço livre: $(df -h . | awk 'NR==2 {print $4}')"
echo ""

echo "🎯 STATUS DA PREPARAÇÃO PARA DEPLOY:"
if [ -f "$M310_PATH" ] && [ -f "transferencia-organizada/blocos/ativos/bloco_m310_prioritario.tar.gz" ]; then
    echo "   ✅ PRONTO PARA DEPLOY - M310 configurado e bloco criado"
    echo "   🚀 Comando recomendado: ./transferencia_m310_prioritaria.sh"
else
    echo "   ❌ NÃO PRONTO - Itens críticos faltando"
    echo "   🔧 Execute novamente: ./configuracao_definitiva.sh"
fi

echo ""
echo "🔮 PRÓXIMOS PASSOS RECOMENDADOS:"
echo "   1. Verificar Módulo M310"
echo "   2. Testar bloco de transferência" 
echo "   3. Configurar SSH para GitHub"
echo "   4. Fazer commit e push da estrutura"
echo "   5. Iniciar deploy para Vercel"

echo ""
echo "🌌 VERIFICAÇÃO COMPLETA CONCLUÍDA! 🌟"
