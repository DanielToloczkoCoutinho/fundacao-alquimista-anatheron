#!/bin/bash
echo "🔍 VERIFICANDO DEPLOY..."
curl -I https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app
curl -I https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/fundacao-completa
curl -I https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/api/fundacao-completa
echo "✅ Verificação concluída!"
