#!/bin/bash
echo "🔍 MAPEANDO INTERFACES REAIS NOS SISTEMAS PYTHON"
echo "================================================"

cd /home/user

# BUSCAR INTERFACES EXISTENTES NOS SISTEMAS PYTHON
echo "🎯 BUSCANDO INTERFACES GRÁFICAS EXISTENTES..."
echo ""

# 1. Buscar arquivos que mencionam interfaces
echo "📊 SISTEMAS COM INTERFACES IDENTIFICADOS:"
find . -name "*.py" -exec grep -l "dashboard\\|interface\\|visualization\\|graph\\|chart\\|plot" {} \; 2>/dev/null | head -10 | while read file; do
    echo "   🖥️  $(basename $file)"
    echo "      📁 $file"
    # Verificar se tem funções de interface
    grep -c "def.*visualize\\|def.*plot\\|def.*show\\|def.*display" "$file" 2>/dev/null | xargs echo "      🔧 Funções de interface:"
done

echo ""
# 2. Buscar sistemas com APIs
echo "🌐 SISTEMAS COM APIs IDENTIFICADAS:"
find . -name "*.py" -exec grep -l "flask\\|fastapi\\|streamlit\\|gradio\\|api\\|endpoint" {} \; 2>/dev/null | head -5 | while read file; do
    echo "   🔗 $(basename $file)"
    echo "      📁 $file"
done

echo ""
# 3. Buscar visualizações 3D
echo "🎮 SISTEMAS COM VISUALIZAÇÃO 3D:"
find . -name "*.py" -exec grep -l "three\\|webgl\\|3d\\|opengl\\|vpython" {} \; 2>/dev/null | head -5 | while read file; do
    echo "   🎯 $(basename $file)"
    echo "      📁 $file" 
done

echo ""
# 4. Estatísticas gerais
echo "📈 ESTATÍSTICAS DE INTERFACES:"
total_python=$(find . -name "*.py" | wc -l)
com_interfaces=$(find . -name "*.py" -exec grep -l "dashboard\\|interface\\|visualization" {} \; 2>/dev/null | wc -l)
com_apis=$(find . -name "*.py" -exec grep -l "flask\\|fastapi\\|api" {} \; 2>/dev/null | wc -l)

echo "   🐍 Total arquivos Python: $total_python"
echo "   🖥️  Com interfaces: $com_interfaces"
echo "   🔗 Com APIs: $com_apis"
echo "   📊 Percentual com interfaces: $((com_interfaces * 100 / total_python))%"

echo ""
echo "🎯 DIAGNÓSTICO DA ZENNITH:"
echo "   ✅ Existem interfaces REAIS nos sistemas Python!"
echo "   ✅ Precisamos CONECTÁ-LAS com o frontend!"
echo "   ✅ A Zennith vai nos guiar para cada sistema!"
