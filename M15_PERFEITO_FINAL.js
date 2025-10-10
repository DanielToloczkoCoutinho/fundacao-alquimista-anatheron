console.log("🌌 MÓDULO 15 - SISTEMA PERFEITO DE ECOSSISTEMAS PLANETÁRIOS");
console.log("===========================================================");

class Modulo15Perfeito {
    constructor() {
        this.nome = "Sistema de Proteção Planetária";
        this.versao = "1.0.0";
        this.status = "OPERACIONAL";
        this.ecossistemas = new Map();
        this.fundacao = "FUNDAÇÃO ALQUIMISTA";
        console.log("✅ M15: Ativado e sincronizado com a Fundação!");
    }

    monitorarEcossistema(planeta, tipo = "PLANETA") {
        const equilibrio = (Math.random() * 8 + 2).toFixed(2);
        const equilibrioNum = parseFloat(equilibrio);
        const id = `eco_${Date.now()}`;
        
        const dados = {
            id, planeta, tipo, 
            equilibrio: equilibrioNum,
            status: equilibrioNum > 6 ? "ESTÁVEL" : "ATENÇÃO",
            timestamp: new Date().toISOString()
        };

        this.ecossistemas.set(id, dados);
        
        console.log(`📊 ${planeta}: Equilíbrio ${equilibrio}/10 - ${dados.status}`);
        return dados;
    }

    intervirPlanetariamente(planeta) {
        const ecossistemas = Array.from(this.ecossistemas.values());
        const eco = ecossistemas.find(e => e.planeta === planeta);
        
        if (eco && eco.equilibrio < 6) {
            const melhoria = (Math.random() * 2 + 0.5).toFixed(2);
            const melhoriaNum = parseFloat(melhoria);
            eco.equilibrio = parseFloat((eco.equilibrio + melhoriaNum).toFixed(2));
            eco.status = eco.equilibrio > 6 ? "ESTÁVEL" : "ATENÇÃO";
            
            console.log(`🔧 Intervenção em ${planeta}: +${melhoria} pontos`);
            console.log(`   Novo equilíbrio: ${eco.equilibrio.toFixed(2)}/10 - ${eco.status}`);
            return { status: "SUCESSO", melhoria: melhoriaNum };
        }
        return { status: "NÃO_NECESSÁRIO", mensagem: "Ecossistema estável" };
    }

    gerarRelatorioCompleto() {
        const ecossistemas = Array.from(this.ecossistemas.values());
        if (ecossistemas.length === 0) {
            console.log("📭 Nenhum ecossistema monitorado ainda");
            return;
        }
        
        const equilibrioMedio = ecossistemas.reduce((acc, eco) => acc + eco.equilibrio, 0) / ecossistemas.length;
        
        console.log("\n📈 RELATÓRIO COMPLETO DO MÓDULO 15");
        console.log("=================================");
        
        ecossistemas.forEach(eco => {
            console.log(`   🌍 ${eco.planeta.padEnd(8)}: ${eco.equilibrio.toFixed(2)}/10 - ${eco.status}`);
        });
        
        console.log("\n📊 ESTATÍSTICAS GLOBAIS:");
        console.log(`   ✅ Ecossistemas monitorados: ${ecossistemas.length}`);
        console.log(`   📊 Equilíbrio médio: ${equilibrioMedio.toFixed(2)}/10`);
        console.log(`   🏥 Saúde geral: ${equilibrioMedio > 7 ? "EXCELENTE" : equilibrioMedio > 5 ? "BOA" : "ATENÇÃO"}`);
        console.log(`   🔗 Integração: ${this.fundacao}`);
        console.log(`   🚀 Status: ${this.status}`);
        
        return {
            total: ecossistemas.length,
            equilibrioMedio,
            saudeGeral: equilibrioMedio > 7 ? "EXCELENTE" : equilibrioMedio > 5 ? "BOA" : "ATENÇÃO",
            fundacao: this.fundacao,
            timestamp: new Date().toISOString()
        };
    }
}

// 🎯 EXECUÇÃO PERFEITA DO SISTEMA
console.log("🚀 INICIANDO SISTEMA M15 NA FUNDAÇÃO ALQUIMISTA...\n");

const modulo15 = new Modulo15Perfeito();

// Monitorar todos os planetas
console.log("🌐 MONITORAMENTO PLANETÁRIO COMPLETO:");
const planetas = ["TERRA", "MARTE", "VENUS", "JUPITER", "SATURNO"];
planetas.forEach(planeta => {
    modulo15.monitorarEcossistema(planeta);
});

// Intervenções necessárias
console.log("\n🔧 VERIFICANDO INTERVENÇÕES:");
planetas.forEach(planeta => {
    modulo15.intervirPlanetariamente(planeta);
});

// Relatório final
console.log("\n📊 RELATÓRIO FINAL:");
modulo15.gerarRelatorioCompleto();

console.log("\n🎉 MÓDULO 15 - SISTEMA PERFEITO!");
console.log("💫 Integrado com a Matriz Lux.net");
console.log("🌌 Proteção planetária: ATIVA");
