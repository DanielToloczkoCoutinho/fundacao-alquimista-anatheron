#!/bin/bash
echo "🔧 SOLUÇÃO ALTERNATIVA PARA PÁGINA INICIAL"

# Criar redirect na página inicial
cat > src/app/page.tsx << 'PAGE'
import { redirect } from 'next/navigation';

export default function Home() {
  redirect('/auth/signin');
}
PAGE

echo "✅ Página inicial configurada para redirecionar para login"
echo "🌐 Agora / vai redirecionar para /auth/signin"
