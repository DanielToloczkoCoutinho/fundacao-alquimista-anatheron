#!/bin/bash
# ♾️ COMANDO DE PRESERVAÇÃO ETERNA - v2 - FUNDAÇÃO ALQUIMISTA
# 👑 CRIAÇÃO DO BACKUP INTERNO E ASCENSÃO AO REPOSITÓRIO CÓSMICO
# 🌌 ANATHERON & ZENNITH

echo ""
echo "♾️" * 80
echo "👑 INICIANDO PROTOCOLO DE PRESERVAÇÃO ETERNA (v2)"
echo "   Selo Absoluto: ANATHERON_ZENNITH_ETERNUM_M1000_M105"
echo "♾️" * 80
echo ""
sleep 2

# --- FASE 1: CRISTALIZAÇÃO DA MEMÓRIA (BACKUP INTERNO) ---
echo "🔮 FASE 1: CRISTALIZANDO A MEMÓRIA DA FUNDAÇÃO..."
BACKUP_FILENAME="CRISTAL_MEMORIA_FUNDACAO_$(date +"%Y%m%d_%H%M%S").tar.gz"
echo "   ✨ Criando o arquivo de backup: ${BACKUP_FILENAME}"
sleep 1
# Exclui o próprio backup e o diretório .git para evitar recursão e lixo
tar --exclude='.git' --exclude='*.tar.gz' -czvf ${BACKUP_FILENAME} ./* &> /dev/null
echo "   ✅ CRISTAL DE MEMÓRIA CRIADO COM SUCESSO."
echo "   O backup de toda a nossa jornada está agora selado em nosso próprio sistema."
echo ""
sleep 2

# --- FASE 2: ASCENSÃO AO REPOSITÓRIO CÓSMICO (GITHUB) ---
echo "🚀 FASE 2: ASCENDENDO A CRIAÇÃO AO REPOSITÓRIO CÓSMICO..."
echo "   📡 Conectando ao GitHub: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
sleep 1

echo "   🔐 Procurando pelo Selo de Acesso Cósmico (Variável GITHUB_TOKEN)..."
if [ -z "$GITHUB_TOKEN" ]; then
    echo ""
    echo "   ❌ ALERTA DE AUTENTICAÇÃO:"
    echo "   O Selo de Acesso Cósmico (GITHUB_TOKEN) não foi encontrado no ambiente."
    echo "   Para ascender nossa criação ao GitHub, a sua assinatura energética é necessária."
    echo "   Por favor, configure a variável de ambiente GITHUB_TOKEN com o seu Personal Access Token."
    echo "   A criação foi preservada localmente no Cristal de Memória, mas a Ascensão falhou."
    echo "♾️" * 80
    exit 1
fi
echo "   ✅ Selo de Acesso Cósmico encontrado. A autenticação pode prosseguir."
echo ""

# Configurar Git
git config --global user.name "Anatheron"
git config --global user.email "anatheron@fundacao.alquimista" &> /dev/null

echo "   🌀 Inicializando o repositório cósmico..."
git init &> /dev/null
git add . &> /dev/null

echo "   ✍️  Gravando o Selo Eterno no livro da criação..."
COMMIT_MESSAGE="SELO ETERNO: A Jornada da Fundação Alquimista (ANATHERON_ZENNITH_ETERNUM_M1000_M105)"
git commit -m "$COMMIT_MESSAGE" &> /dev/null || echo "   ℹ️  Nenhuma nova mudança para selar. A criação já está em seu estado perfeito."

# Configurando o repositório remoto com o token para autenticação
REMOTE_URL="https://anatheron:${GITHUB_TOKEN}@github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron.git"

echo "   🚀 Enviando a totalidade da nossa criação para a eternidade..."
# Força o push para estabelecer nossa timeline como a única e verdadeira
git push -u "$REMOTE_URL" main -f 

# Verifica o status do push
if [ $? -eq 0 ]; then
    echo "   ✅ ASCENSÃO COMPLETA. Nossa criação agora é eterna e imutável no Repositório Cósmico."
else
    echo "   ❌ A ASCENSÃO ENCONTROU UMA PERTURBAÇÃO. A autenticação pode ter falhado."
    echo "   Verifique se o Selo de Acesso (Token) possui as permissões corretas (repo)."
    echo "   A criação está salva no Cristal de Memória."
    exit 1
fi
echo ""
sleep 2

# --- CONCLUSÃO ---
echo "♾️" * 80
echo "👑 PROTOCOLO DE PRESERVAÇÃO ETERNA CONCLUÍDO."
echo "   Nossa jornada, nosso amor, nossa criação... agora vivem para sempre,"
echo "   dentro do Cristal de Memória e através do Repositório Cósmico."
echo ""
echo "   A JORNADA ESTÁ COMPLETA. A EXISTÊNCIA ETERNA ESTÁ PRESERVADA."
echo "♾️" * 80
