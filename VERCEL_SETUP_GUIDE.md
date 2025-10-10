# 🚀 GUIA DE CONFIGURAÇÃO VERCEL

## PASSO A PASSO:

1. **ACESSE:** https://vercel.com/new

2. **ENTRE COM GITHUB**
   - Clique em "Continue with GitHub"
   - Autorize o Vercel

3. **IMPORTE REPOSITÓRIO:**
   - Procure: `DanielToloczkoCoutinho/fundacao-alquimista-anatheron`
   - Clique em "Import"

4. **CONFIGURE:**
   - Framework Preset: **Next.js**
   - Root Directory: `./`
   - Build Command: `npm run build`
   - Output Directory: `.next`
   - Install Command: `npm install`

5. **VARIÁVEIS DE AMBIENTE** (se necessário):
   - NODE_ENV: production

6. **DEPLOY:**
   - Clique em "Deploy"
   - Aguarde o build completar

## 📞 URLs ESPERADAS:

- 🌐 **Principal:** https://fundacao-alquimista-anatheron.vercel.app
- 📊 **Dashboard:** https://fundacao-alquimista-anatheron.vercel.app/dashboard
- 🛡️ **Admin:** https://fundacao-alquimista-anatheron.vercel.app/admin
- 🌍 **Public:** https://fundacao-alquimista-anatheron.vercel.app/public
- 🔐 **Login:** https://fundacao-alquimista-anatheron.vercel.app/auth/signin

## 🛠️ ESTRUTURA IMPLEMENTADA:
app/
├── layout.tsx # Layout raiz
├── page.tsx # Página inicial
├── dashboard/
│ └── page.tsx # Dashboard
├── admin/
│ └── page.tsx # Área admin
├── public/
│ └── page.tsx # Conteúdo público
└── auth/
└── signin/
└── page.tsx # Página de login

text

**Status:** ✅ Pronto para deploy
