console.log("🌍 MÓDULO 15 ATIVADO - ECOSSISTEMAS PLANETÁRIOS");
console.log("==============================================");

class Modulo15 {
    constructor() {
        this.nome = "Gerenciamento de Ecossistemas";
        this.status = "OPERACIONAL";
        this.ecossistemas = [];
    }

    monitorar(planeta) {
        const equilibrio = (Math.random() * 10).toFixed(2);
        this.ecossistemas.push({ planeta, equilibrio });
        console.log(`📊 ${planeta}: Equilíbrio ${equilibrio}`);
        return { status: "SUCESSO", equilibrio };
    }

    relatorio() {
        console.log("📈 RELATÓRIO PLANETÁRIO:");
        this.ecossistemas.forEach(eco => {
            console.log(`   🌍 ${eco.planeta}: ${eco.equilíbrio}`);
        });
        console.log(`   ✅ Total: ${this.ecossistemas.length} ecossistemas`);
    }
}

// Usar o módulo
const m15 = new Modulo15();
m15.monitorar("TERRA");
m15.monitorar("MARTE"); 
m15.monitorar("VENUS");
m15.relatorio();

console.log("🎉 MÓDULO 15 OPERACIONAL!");
