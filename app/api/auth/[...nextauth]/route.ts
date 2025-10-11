import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

const authOptions = {
  providers: [
    CredentialsProvider({
      name: 'Fundação Alquimista',
      credentials: {
        username: { label: "Usuário", type: "text" },
        password: { label: "Senha", type: "password" }
      },
      async authorize(credentials) {
        // Sistema de autenticação simplificado para desenvolvimento
        const users = [
          { id: "1", username: "zennith", password: "quantum966", role: "admin" },
          { id: "2", username: "fundador", password: "alquimia2025", role: "founder" },
          { id: "3", username: "operador", password: "nexus111", role: "operator" }
        ];

        const user = users.find(u => 
          u.username === credentials?.username && 
          u.password === credentials?.password
        );

        if (user) {
          return {
            id: user.id,
            name: user.username,
            role: user.role,
            email: `${user.username}@fundacao-alquimista.quantum`
          };
        }
        return null;
      }
    })
  ],
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.role = user.role;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.role = token.role;
      }
      return session;
    }
  },
  pages: {
    signIn: '/auth/signin',
    signOut: '/auth/signout'
  },
  secret: process.env.NEXTAUTH_SECRET || 'fundacao-alquimista-quantum-secret-2025'
};

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };
