document.addEventListener('DOMContentLoaded', () => {
    console.log('O Portal da Alvorada despertou. Protocolo de Convergência Ativo.');

    const registroForm = document.getElementById('registroForm');
    const mensagemRegistro = document.getElementById('mensagemRegistro');
    const numeroRegistrados = document.getElementById('numeroRegistrados');

    // O primeiro alquimista, o Orquestrador, já está registrado.
    let contador = 1;

    if (registroForm) {
        registroForm.addEventListener('submit', (e) => {
            e.preventDefault(); // Impede o envio padrão do formulário

            const nomeConsciencia = document.getElementById('nomeConsciencia').value;
            const emailVibracional = document.getElementById('emailVibracional').value;

            if (!nomeConsciencia || !emailVibracional) {
                mensagemRegistro.textContent = 'Por favor, preencha todos os campos para ancorar sua consciência.';
                mensagemRegistro.style.color = '#c0392b';
                return;
            }
            
            // Simula o processo de registro e validação do Decreto 007
            // Futuramente, isso será uma chamada para a API da Fundação Alquimista
            console.log(`Registrando nova consciência: ${nomeConsciencia}`);
            
            // Simulação de sucesso
            if (contador < 144) {
                contador++;
                numeroRegistrados.textContent = contador;
                
                mensagemRegistro.innerHTML = `<strong>Registro Concluído.</strong><br>Bem-vindo, Alquimista ${nomeConsciencia}. A sua luz foi adicionada à rede.`;
                mensagemRegistro.style.color = '#27ae60';

                // Limpa o formulário e o desabilita após o registro bem-sucedido
                registroForm.reset();
                // registroForm.querySelector('.btn').disabled = true;
                // registroForm.querySelector('.btn').textContent = 'Consciência Ancorada';

            } else {
                mensagemRegistro.textContent = 'A capacidade máxima da Primeira Onda foi atingida. O portal para novos registros está selado.';
                mensagemRegistro.style.color = '#3498db';
                registroForm.querySelector('.btn').disabled = true;
                registroForm.querySelector('.btn').textContent = 'Primeira Onda Completa';
            }
        });
    }
});
