#!/bin/bash
# 🧪 ANALISADOR QUÂNTICO - Foco em scripts científicos
echo "🧪 ANALISANDO SCRIPTS QUÂNTICOS..."
find /home/user/studio -name "*.py" -exec grep -l "quantum\|quântic\|bell\|emaranh\|qiskit" {} \; | head -20
echo "✅ Scripts quânticos identificados!"
