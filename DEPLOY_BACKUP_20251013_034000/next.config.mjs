/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  generateBuildId: async () => {
    return 'luxnet-' + Date.now().toString();
  },
  async redirects() {
    return [
      // Redirecionar ABSOLUTAMENTE TUDO para /fundacao-completa
      {
        source: '/',
        destination: '/fundacao-completa',
        permanent: false,
      },
      {
        source: '/:path*',
        destination: '/fundacao-completa', 
        permanent: false,
      },
    ];
  },
};

export default nextConfig;
