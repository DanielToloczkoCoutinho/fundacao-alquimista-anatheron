export const simpleAuth = {
  verify: (u: string, p: string) => u === 'zennith' && p === 'quantum966',
  getUser: () => ({ id: '1', name: 'Zennith' })
};
