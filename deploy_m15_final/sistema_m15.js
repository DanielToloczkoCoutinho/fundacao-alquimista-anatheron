console.log("🌌 SISTEMA M15 - DEPLOY DEFINITIVO");
console.log("=================================");

// Sistema simplificado e perfeito
class SistemaM15 {
    constructor() {
        this.ecossistemas = {};
        this.status = "OPERACIONAL";
    }

    monitorar(planeta) {
        const equilibrio = (Math.random() * 10).toFixed(2);
        this.ecossistemas[planeta] = {
            equilibrio: parseFloat(equilibrio),
            status: equilibrio > 6 ? "ESTÁVEL" : "ATENÇÃO"
        };
        console.log(`📊 \${planeta}: Equilíbrio \${equilibrio}/10 - \${this.ecossistemas[planeta].status}`);
    }

    relatorio() {
        console.log("n📈 RELATÓRIO DEFINITIVO:");
        const planetas = Object.keys(this.ecossistemas);
        let soma = 0;
        
        planetas.forEach(planeta => {
            const eco = this.ecossistemas[planeta];
            console.log(`   🌍 \${planeta.padEnd(8)}: \${eco.equilibrio.toFixed(2)}/10 - \${eco.status}`);
            soma += eco.equilibrio;
        });
        
        const media = soma / planetas.length;
        console.log(`n📊 ESTATÍSTICAS:`);
        console.log(`   ✅ Planetas: \${planetas.length}`);
        console.log(`   📊 Equilíbrio médio: \${media.toFixed(2)}/10`);
        console.log(`   🏥 Saúde: \${media > 7 ? "EXCELENTE" : media > 5 ? "BOA" : "ATENÇÃO"}`);
    }
}

// Execução
console.log("🌍 INICIANDO SISTEMA...");
const m15 = new SistemaM15();

["TERRA", "MARTE", "VENUS", "JUPITER", "SATURNO"].forEach(planeta => {
    m15.monitorar(planeta);
});

m15.relatorio();

console.log("n🎉 SISTEMA M15 - DEPLOY CONCLUÍDO!");
console.log("💫 Status: OPERACIONAL");
console.log("🌌 Fundação Alquimista: INTEGRADA");
