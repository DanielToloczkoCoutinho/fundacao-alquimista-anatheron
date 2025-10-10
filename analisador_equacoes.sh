#!/bin/bash
# 🧮 ANALISADOR DE EQUAÇÕES - Foco matemático
echo "🧮 BUSCANDO EQUAÇÕES..."
find /home/user/studio -name "*.py" -exec grep -l "import math\|import numpy\|def.*equation" {} \; | head -10
echo "✅ Equações identificadas!"
