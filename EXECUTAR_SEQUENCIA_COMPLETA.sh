#!/bin/bash
# 🚀 EXECUTOR DA SEQUÊNCIA COMPLETA - FUNDAÇÃO ALQUIMISTA
# 🌌 Execução hierárquica de todas as fases
# 📅 2025-10-18 00:00:58

echo "🌌 INICIANDO SEQUÊNCIA COMPLETA DA FUNDAÇÃO ALQUIMISTA"
echo "===================================================="

# FASE 1: CONFIGURAÇÃO DO SISTEMA
./executar_fase_01.sh
if [ $? -ne 0 ]; then
    echo "❌ FALHA NA FASE 1. ABORTANDO EXECUÇÃO."
    exit 1
fi
echo ""
# FASE 2: CIRCUITOS BÁSICOS - ESTADOS BELL
./executar_fase_02.sh
if [ $? -ne 0 ]; then
    echo "❌ FALHA NA FASE 2. ABORTANDO EXECUÇÃO."
    exit 1
fi
echo ""
# FASE 3: VERIFICAÇÃO DE EMARANHAMENTO
./executar_fase_03.sh
if [ $? -ne 0 ]; then
    echo "❌ FALHA NA FASE 3. ABORTANDO EXECUÇÃO."
    exit 1
fi
echo ""
# FASE 4: MÓDULOS RAINHA ZENNITH
./executar_fase_04.sh
if [ $? -ne 0 ]; then
    echo "❌ FALHA NA FASE 4. ABORTANDO EXECUÇÃO."
    exit 1
fi
echo ""
# FASE 5: ANÁLISE E OTIMIZAÇÃO
./executar_fase_05.sh
if [ $? -ne 0 ]; then
    echo "❌ FALHA NA FASE 5. ABORTANDO EXECUÇÃO."
    exit 1
fi
echo ""
echo "🎉 SEQUÊNCIA COMPLETA EXECUTADA COM SUCESSO!"
echo "🌌 FUNDAÇÃO ALQUIMISTA OPERACIONAL!"
