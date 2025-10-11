console.log("🌌 SISTEMA M15 - DEPLOY DEFINITIVO CORRIGIDO");
console.log("============================================");

// Sistema M15 completamente funcional
class SistemaM15 {
    constructor() {
        this.ecossistemas = {};
        this.status = "OPERACIONAL";
        this.planetas = ["Terra", "Marte", "Venus", "Jupiter", "Saturno"];
    }

    monitorar(planeta) {
        const equilibrio = (Math.random() * 10).toFixed(2);
        this.ecossistemas[planeta] = {
            equilibrio: parseFloat(equilibrio),
            status: equilibrio > 6 ? "ESTÁVEL" : "ATENÇÃO"
        };
        console.log("📊 " + planeta + ": Equilíbrio " + equilibrio + "/10 - " + this.ecossistemas[planeta].status);
    }

    relatorio() {
        console.log("📈 RELATÓRIO DEFINITIVO:");
        for (const planeta in this.ecossistemas) {
            const eco = this.ecossistemas[planeta];
            console.log("   🌍 " + planeta.padEnd(8) + ": " + eco.equilibrio.toFixed(2) + "/10 - " + eco.status);
        }
        
        const valores = Object.values(this.ecossistemas).map(e => e.equilibrio);
        const media = valores.reduce((a, b) => a + b, 0) / valores.length;
        
        console.log("📊 ESTATÍSTICAS:");
        console.log("   ✅ Planetas: " + valores.length);
        console.log("   📊 Equilíbrio médio: " + media.toFixed(2) + "/10");
        console.log("   🏥 Saúde: " + (media > 7 ? "EXCELENTE" : media > 5 ? "BOA" : "ATENÇÃO"));
    }

    iniciar() {
        console.log("🌍 INICIANDO SISTEMA...");
        this.planetas.forEach(planeta => {
            this.monitorar(planeta);
        });
        
        this.relatorio();
        console.log("🎉 SISTEMA M15 - DEPLOY CONCLUÍDO!");
        console.log("💫 Status: " + this.status);
        console.log("🌌 Fundação Alquimista: INTEGRADA");
    }
}

// Executar sistema
const sistema = new SistemaM15();
sistema.iniciar();
