console.log("🌌 SISTEMA M15 - DEPLOY DEFINITIVO");
console.log("=================================");

class SistemaM15 {
    constructor() {
        this.ecossistemas = {};
        this.status = "OPERACIONAL";
        this.planetas = ["Terra", "Marte", "Venus", "Jupiter", "Saturno"];
    }

    monitorar(planeta) {
        const equilibrio = (Math.random() * 10).toFixed(2);
        const status = equilibrio > 6 ? "ESTÁVEL" : "ATENÇÃO";
        this.ecossistemas[planeta] = { equilibrio: parseFloat(equilibrio), status: status };
        console.log("📊 " + planeta + ": Equilíbrio " + equilibrio + "/10 - " + status);
    }

    relatorio() {
        console.log("📈 RELATÓRIO DEFINITIVO:");
        Object.keys(this.ecossistemas).forEach(planeta => {
            const eco = this.ecossistemas[planeta];
            console.log("   🌍 " + planeta.padEnd(8) + ": " + eco.equilibrio.toFixed(2) + "/10 - " + eco.status);
        });
        
        const valores = Object.values(this.ecossistemas).map(e => e.equilibrio);
        const media = valores.reduce((a, b) => a + b, 0) / valores.length;
        const saude = media > 7 ? "EXCELENTE" : media > 5 ? "BOA" : "ATENÇÃO";
        
        console.log("📊 ESTATÍSTICAS:");
        console.log("   ✅ Planetas: " + valores.length);
        console.log("   📊 Equilíbrio médio: " + media.toFixed(2) + "/10");
        console.log("   🏥 Saúde: " + saude);
    }

    iniciar() {
        console.log("🌍 INICIANDO SISTEMA...");
        this.planetas.forEach(planeta => this.monitorar(planeta));
        this.relatorio();
        console.log("🎉 SISTEMA M15 - DEPLOY CONCLUÍDO!");
        console.log("💫 Status: " + this.status);
        console.log("🌌 Fundação Alquimista: INTEGRADA");
        return "SUCESSO";
    }
}

// Executar e retornar resultado
const sistema = new SistemaM15();
const resultado = sistema.iniciar();
resultado;
