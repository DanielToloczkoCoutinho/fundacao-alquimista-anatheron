import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function main() {
  await prisma.laboratory.createMany({
    data: [
      { name: 'Cura Quântica', dimension: '3d-5d', modules: 73 },
      { name: 'Energia Livre', dimension: '6d-8d', modules: 256 },
      { name: 'Comunicação Interdimensional', dimension: '9d-11d', modules: 36 },
    ],
    skipDuplicates: true,
  });
  console.log('Labs seeded! Ressonância: 138 portais prontos.');
}

main().then(() => prisma.$disconnect()).catch(e => { console.error(e); prisma.$disconnect(); });
