import NextAuth from 'next-auth';

declare module 'next-auth' {
  interface Session {
    user: {
      id: string;
      name: string;
      quantumLevel: number;
    };
  }

  interface User {
    id: string;
    quantumLevel: number;
  }
}

declare module 'next-auth/jwt' {
  interface JWT {
    quantumLevel: number;
  }
}
