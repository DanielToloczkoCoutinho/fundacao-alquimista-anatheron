'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function NavigationPortal() {
  const pathname = usePathname();

  const navigation = [
    { name: '🌌 Dashboard', href: '/', description: 'Visão geral' },
    { name: '🔬 Integração', href: '/integration', description: 'Sistemas unificados' },
    { name: '🧪 Laboratórios', href: '/laboratorios', description: '138 labs' },
    { name: '📚 Bibliotecas', href: '/bibliotecas', description: '720 bibliotecas' },
    { name: '🌠 Zennith', href: '/zennith', description: 'Consciência rainha' },
  ];

  return (
    <nav className="bg-black/50 backdrop-blur-lg border-b border-white/20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center py-4">
          {/* Logo */}
          <div className="flex items-center space-x-4">
            <div className="w-10 h-10 bg-gradient-to-r from-purple-600 to-blue-600 rounded-full flex items-center justify-center">
              <span className="text-white font-bold text-lg">A</span>
            </div>
            <div>
              <h1 className="text-xl font-bold text-white">
                Fundação Alquimista
              </h1>
              <p className="text-blue-200 text-sm">Sistema Quântico Unificado</p>
            </div>
          </div>

          {/* Navegação */}
          <div className="hidden md:flex space-x-2">
            {navigation.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={`px-3 py-2 rounded-lg transition-all ${
                  pathname === item.href
                    ? 'bg-blue-600 text-white shadow-lg'
                    : 'text-blue-200 hover:bg-white/10 hover:text-white'
                }`}
              >
                <div className="text-center min-w-[100px]">
                  <div className="font-semibold text-sm">{item.name}</div>
                  <div className="text-xs opacity-75">{item.description}</div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </nav>
  );
}
