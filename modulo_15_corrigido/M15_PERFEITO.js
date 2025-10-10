console.log("🌍 MÓDULO 15 - ECOSSISTEMAS PLANETÁRIOS");
console.log("======================================");

class Modulo15 {
    constructor() {
        this.nome = "Gerenciamento de Ecossistemas Planetários";
        this.status = "OPERACIONAL";
        this.ecossistemas = [];
        console.log("✅ M15: Sistema de Proteção Planetária Ativado!");
    }

    monitorar(planeta) {
        const equilibrio = (Math.random() * 10).toFixed(2);
        const ecossistema = { planeta, equilibrio };
        this.ecossistemas.push(ecossistema);
        console.log(`📊 ${planeta}: Equilíbrio ${equilibrio}`);
        return { status: "SUCESSO", equilibrio: parseFloat(equilibrio) };
    }

    relatorio() {
        console.log("📈 RELATÓRIO PLANETÁRIO COMPLETO:");
        this.ecossistemas.forEach(eco => {
            console.log(`   🌍 ${eco.planeta}: ${eco.equilibrio}/10`);
        });
        console.log(`   ✅ Total monitorado: ${this.ecossistemas.length} ecossistemas`);
        
        const media = this.ecossistemas.reduce((acc, eco) => acc + parseFloat(eco.equilibrio), 0) / this.ecossistemas.length;
        console.log(`   📊 Equilíbrio médio: ${media.toFixed(2)}/10`);
        console.log(`   🏥 Saúde geral: ${media > 7 ? "EXCELENTE" : media > 5 ? "BOA" : "ATENÇÃO"}`);
    }

    intervir(planeta) {
        const eco = this.ecossistemas.find(e => e.planeta === planeta);
        if (eco) {
            const melhoria = (Math.random() * 3 + 1).toFixed(2);
            eco.equilibrio = Math.min(10, (parseFloat(eco.equilibrio) + parseFloat(melhoria)).toFixed(2));
            console.log(`🔧 Intervenção em ${planeta}: +${melhoria} pontos`);
            console.log(`   Novo equilíbrio: ${eco.equilibrio}/10`);
            return { status: "SUCESSO", melhoria: parseFloat(melhoria) };
        }
        return { status: "FALHA", mensagem: "Planeta não encontrado" };
    }
}

// ==================== EXECUÇÃO PRINCIPAL ====================
console.log("🚀 INICIANDO SISTEMA M15...");

const m15 = new Modulo15();

// Monitorar planetas
console.log("\n🌐 INICIANDO MONITORAMENTO PLANETÁRIO:");
m15.monitorar("TERRA");
m15.monitorar("MARTE");
m15.monitorar("VENUS");
m15.monitorar("JUPITER");

// Gerar relatório
console.log("\n📊 GERANDO RELATÓRIO:");
m15.relatorio();

// Intervir se necessário
console.log("\n🔧 VERIFICANDO INTERVENÇÕES:");
m15.ecossistemas.forEach(eco => {
    if (parseFloat(eco.equilibrio) < 6) {
        console.log(`⚠️  ${eco.planeta} precisa de intervenção!`);
        m15.intervir(eco.planeta);
    }
});

// Relatório final
console.log("\n🎯 RELATÓRIO FINAL:");
m15.relatorio();

console.log("\n💫 MÓDULO 15 - MISSÃO CUMPRIDA!");
console.log("🌌 Integrado com a Fundação Alquimista");
console.log("🔮 Status: OPERACIONAL E SINCRONIZADO");
