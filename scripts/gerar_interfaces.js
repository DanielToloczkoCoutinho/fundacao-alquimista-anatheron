const fs = require('fs/promises');
const path = require('path');

async function generateInterfaces() {
  const routes = [
    'fundacao-completa', 'fundacao-completa/docs', 'fundacao-completa/scripts',
    'fundacao-completa/modulos', 'painel-interativo', 'mapa-dimensional',
    'relatorio-sinergia', 'nexus', 'dashboard-completo', 'status-urls', 'vr',
    'luxnet', 'integration', 'auth/signin', 'organograma', 'metricas',
    'docs/interfaces', 'docs/manifesto_quantico', 'laboratorios', 'interfaces'
  ];
  const interfaces = await Promise.all(routes.map(async (route) => {
    const filePath = path.join('app', route, 'page.tsx');
    const exists = await fs.access(filePath).then(() => true).catch(() => false);
    return { route, status: exists ? 'online' : 'offline' };
  }));
  await fs.writeFile('public/interfaces.json', JSON.stringify(interfaces, null, 2));
  console.log('✅ interfaces.json gerado');
}

generateInterfaces();
