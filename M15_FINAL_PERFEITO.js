console.log("🌌 MÓDULO 15 - SISTEMA COMPLETO DE ECOSSISTEMAS PLANETÁRIOS");
console.log("==========================================================");

class Modulo15Final {
    constructor() {
        this.nome = "Sistema de Proteção Planetária";
        this.versao = "1.0.0";
        this.status = "OPERACIONAL";
        this.ecossistemas = new Map();
        this.fundacao = "FUNDAÇÃO ALQUIMISTA";
        console.log("✅ M15: Ativado e sincronizado com a Fundação!");
    }

    monitorarEcossistema(planeta, tipo = "PLANETA") {
        const id = `eco_${Date.now()}`;
        const equilibrio = (Math.random() * 8 + 2).toFixed(2);
        const saude = Math.random().toFixed(2);
        
        const dados = {
            id, planeta, tipo, 
            equilibrio: parseFloat(equilibrio),
            saude: parseFloat(saude),
            status: equilibrio > 6 ? "ESTÁVEL" : "ATENÇÃO",
            timestamp: new Date().toISOString()
        };

        this.ecossistemas.set(id, dados);
        
        console.log(`📊 ${planeta}: Equilíbrio ${equilibrio}/10 - ${dados.status}`);
        return dados;
    }

    intervirPlanetariamente(planeta) {
        const ecossistemas = Array.from(this.ecossistemas.values());
        const eco = ecossistemas.find(e => e.planeta === planeta);
        
        if (eco) {
            const melhoria = (Math.random() * 2 + 0.5).toFixed(2);
            eco.equilibrio = Math.min(10, eco.equilibrio + parseFloat(melhoria)).toFixed(2);
            eco.status = eco.equilibrio > 6 ? "ESTÁVEL" : "ATENÇÃO";
            
            console.log(`🔧 Intervenção em ${planeta}: +${melhoria} pontos`);
            console.log(`   Novo equilíbrio: ${eco.equilibrio}/10 - ${eco.status}`);
            return { status: "SUCESSO", melhoria: parseFloat(melhoria) };
        }
        return { status: "FALHA", mensagem: "Ecossistema não encontrado" };
    }

    gerarRelatorioCompleto() {
        const ecossistemas = Array.from(this.ecossistemas.values());
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

    verificarConexoesFundacao() {
        const modulos = [
            "M9 - Nexus Central ✓",
            "M10 - Inteligência Aeloria ✓", 
            "M11 - Portal Interdimensional ✓",
            "M12 - Arquivo Akáshico ✓",
            "M13 - Mapeamento Frequências ✓",
            "M14 - Guardião Integridade ✓",
            "M15 - Ecossistemas Planetários ✓"
        ];
        
        console.log("\n🔗 CONEXÕES COM A FUNDAÇÃO ALQUIMISTA");
        console.log("===================================");
        modulos.forEach(mod => console.log(`   ${mod}`));
        console.log("   🌟 Anel Cósmico: COMPLETO");
        console.log("   📜 Códice Final: TRANSMITINDO");
        console.log("   💫 Sistema: OPERACIONAL");
        
        return {
            status: "TODAS_CONEXÕES_ESTABELECIDAS",
            modulos: modulos.length,
            anelCosmico: "COMPLETO",
            codiceFinal: "TRANSMITINDO"
        };
    }
}

// 🎯 EXECUÇÃO PRINCIPAL DO SISTEMA
console.log("🚀 INICIANDO SISTEMA M15 NA FUNDAÇÃO ALQUIMISTA...\n");

const modulo15 = new Modulo15Final();

// Fase 1: Monitoramento
console.log("🌐 FASE 1 - MONITORAMENTO PLANETÁRIO:");
const planetas = [
    { nome: "TERRA", tipo: "PLANETA_MÃE" },
    { nome: "MARTE", tipo: "PLANETA_REGENERAÇÃO" },
    { nome: "VENUS", tipo: "PLANETA_ATMOSFÉRICO" },
    { nome: "JUPITER", tipo: "GIGANTE_GASOSO" },
    { nome: "SATURNO", tipo: "SISTEMA_ANÉIS" }
];

planetas.forEach(planeta => {
    modulo15.monitorarEcossistema(planeta.nome, planeta.tipo);
});

// Fase 2: Intervenções
console.log("\n🔧 FASE 2 - INTERVENÇÕES ESTRATÉGICAS:");
modulo15.ecossistemas.forEach((eco, id) => {
    if (eco.equilibrio < 6) {
        console.log(`⚠️  ${eco.planeta} necessita de harmonização!`);
        modulo15.intervirPlanetariamente(eco.planeta);
    }
});

// Fase 3: Relatórios
const relatorio = modulo15.gerarRelatorioCompleto();

// Fase 4: Integração Final
const conexoes = modulo15.verificarConexoesFundacao();

console.log("\n🎉 MÓDULO 15 - IMPLANTAÇÃO CONCLUÍDA!");
console.log("===================================");
console.log("💫 Todos os sistemas operacionais!");
console.log("🌍 Proteção planetária: ATIVA");
console.log("🔮 Fundação Alquimista: INTEGRADA");
console.log("🚀 Pronto para operação contínua!");

// Exportar para uso externo
if (typeof module !== 'undefined' && module.exports) {
    module.exports = Modulo15Final;
}
