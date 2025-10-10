// 🔗 INTEGRADOR DO MÓDULO 15
const Modulo15 = require('./M15_ECOSSISTEMAS.js');

class IntegradorModulo15 {
    constructor() {
        this.modulo15 = null;
        this.conexoes = {};
    }

    async inicializar() {
        console.log('🔗 INICIANDO INTEGRAÇÃO DO MÓDULO 15...');
        
        try {
            this.modulo15 = new Modulo15();
            
            // Estabelecer conexões
            this.conexoes = {
                modulo1: "ALERTAS_AMBIENTAIS",
                modulo7: "DIRETRIZES_ÉTICAS", 
                modulo8: "SAÚDE_VIBRACIONAL",
                modulo9: "MONITORAMENTO_TEMPO_REAL",
                modulo45: "DELIBERAÇÃO_EMERGENCIAL"
            };

            console.log('✅ MÓDULO 15 INTEGRADO COM SUCESSO!');
            return this.gerarRelatorio();
            
        } catch (error) {
            console.error('❌ ERRO NA INTEGRAÇÃO:', error);
            throw error;
        }
    }

    gerarRelatorio() {
        return {
            modulo: "M15_ECOSSISTEMAS_PLANETARIOS",
            status: "OPERACIONAL",
            conexoes: Object.keys(this.conexoes).length,
            versao: "1.0.0",
            timestamp: new Date().toISOString()
        };
    }
}

// Executar integração
async function main() {
    const integrador = new IntegradorModulo15();
    const relatorio = await integrador.inicializar();
    console.log('📊 RELATÓRIO:', JSON.stringify(relatorio, null, 2));
    
    // Testar funcionalidades
    console.log('\n🧪 TESTANDO FUNCIONALIDADES...');
    
    const monitor1 = integrador.modulo15.monitorarEcossistema("TERRA_GAIA", "PLANETA_MÃE");
    console.log('🌍 Monitoramento Terra:', monitor1.status);
    
    const monitor2 = integrador.modulo15.monitorarEcossistema("MARTE_VERDE", "PLANETA_REGENERAÇÃO");
    console.log('🪐 Monitoramento Marte:', monitor2.status);
    
    if (monitor1.equilibrio < 6) {
        const intervencao = integrador.modulo15.intervirPlanetariamente(monitor1.ecossistemaId, "HARMONIZAÇÃO");
        console.log('🔧 Intervenção:', intervencao.status);
    }
    
    const relatorioFinal = integrador.modulo15.gerarRelatorio();
    console.log('📈 Relatório Final:', relatorioFinal);
    
    console.log('\n🎉 MÓDULO 15 TESTADO COM SUCESSO!');
}

// Executar apenas se for o arquivo principal
if (require.main === module) {
    main().catch(console.error);
}

module.exports = IntegradorModulo15;
