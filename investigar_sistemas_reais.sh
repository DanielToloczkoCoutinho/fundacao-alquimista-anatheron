#!/bin/bash
echo "🔍 INVESTIGANDO SISTEMAS REAIS NO BACKEND"
echo "=========================================="

echo "🎯 O PROBLEMA:"
echo "   Estamos mostrando 'QUE existe' mas não 'O QUE existe'"
echo ""

# 1. ENCONTRAR SISTEMAS REAIS DE QISKIT
echo "1. ⚛️ SISTEMAS QISKIT REAIS:"
find /home/user -name "*.py" -exec grep -l "qiskit" {} \; 2>/dev/null | head -5 | while read file; do
    echo "   📄 $(basename $file)"
    echo "      🗂️  $file"
    # Verificar se tem funções reais
    grep -c "def " "$file" 2>/dev/null | xargs echo "      🔧 Funções:"
    grep -c "QuantumCircuit" "$file" 2>/dev/null | xargs echo "      ⚛️ Circuitos:"
done

echo ""
# 2. ENCONTRAR SISTEMAS 3D REAIS
echo "2. 🎮 SISTEMAS THREE.JS REAIS:"
find /home/user -name "*.js" -o -name "*.ts" -o -name "*.tsx" | xargs grep -l "three" 2>/dev/null | head -3 | while read file; do
    echo "   📄 $(basename $file)"
    echo "      🗂️  $file"
    grep -c "Scene\\|Mesh\\|Camera" "$file" 2>/dev/null | xargs echo "      🎨 Elementos 3D:"
done

echo ""
# 3. VERIFICAR SE HÁ APIs OU DADOS REAIS
echo "3. 📡 DADOS REAIS PARA MOSTRAR:"
echo "   🐍 Python com dados:"
find /home/user -name "*.py" -exec grep -l "import.*qiskit" {} \; 2>/dev/null | wc -l | xargs echo "      Qiskit imports:"
find /home/user -name "*.py" -exec grep -l "QuantumCircuit" {} \; 2>/dev/null | wc -l | xargs echo "      Circuitos:"
find /home/user -name "*.py" -exec grep -l "execute\\|run" {} \; 2>/dev/null | wc -l | xargs echo "      Execuções:"

echo ""
echo "🎯 DIAGNÓSTICO:"
echo "   ❌ Backend tem sistemas REAIS"
echo "   ❌ Frontend mostra apenas 'letras'"
echo "   ❌ FALTA: Conexão real backend → frontend"
echo "   ❌ FALTA: Dados reais sendo mostrados"
echo "   ❌ FALTA: Visualizações reais"
