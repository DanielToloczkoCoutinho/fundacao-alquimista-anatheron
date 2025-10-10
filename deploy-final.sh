#!/bin/bash
echo "🚀 Deploy rápido - Fundação Alquimista"
npm run build && npx vercel --prod --force
echo "🌐 URL: https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app"
