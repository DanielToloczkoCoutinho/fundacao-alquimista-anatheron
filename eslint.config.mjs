/** @type {import('eslint').Linter.Config} */
const config = {
  extends: 'next/core-web-vitals',
  ignorePatterns: [
    'node_modules/',
    '.next/',
    'out/',
    'dist/',
    'build/',
    'prisma/generated/',
    'src/generated/',
    '*.d.ts',  // Ignora declaration files como next-auth.d.ts
    '**/wasm.js'  // Ignora Prisma wasm require()
  ],
  rules: {
    '@typescript-eslint/no-require-imports': 'off',  // Permite require() em generated
    '@typescript-eslint/no-unused-vars': 'warn'  // Leniente para unused em generated
  }
};

export default config;
