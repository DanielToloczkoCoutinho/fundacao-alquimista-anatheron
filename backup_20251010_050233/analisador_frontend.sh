#!/bin/bash  
# 🎨 ANALISADOR FRONTEND - Foco em interface
echo "🎨 ANALISANDO FRONTEND..."
find /home/user/studio -name "*.tsx" -o -name "*.jsx" -o -name "*.css" | head -15
echo "✅ Frontend analisado!"
