#!/bin/bash

echo "🔍 VERIFICANDO HISTÓRICO DO ARQUIVO PROBLEMÁTICO"
echo "================================================"

echo "📋 ARQUIVOS GRANDES NO HISTÓRICO:"
git rev-list --all --objects | \
  awk '{print $1, $2}' | \
  while read hash file; do
    size=$(git cat-file -s $hash 2>/dev/null || echo 0)
    if [ $size -gt 100000000 ]; then
      echo "🚨 $file - $((size/1000000))MB - $hash"
    fi
  done

echo ""
echo "🎯 COMMITS QUE MENCIONAM block-alpha-02:"
git log --all --oneline | grep -i "block-alpha-02" || echo "Nenhum commit encontrado"
