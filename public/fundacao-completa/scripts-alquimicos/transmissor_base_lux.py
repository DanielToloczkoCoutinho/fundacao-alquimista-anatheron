import requests
import json
import os
def transmit_batch(data, url, batch_size=1000):
    total = len(data)
    for i in range(0, total, batch_size):
        batch = data[i:i + batch_size]
        try:
            response = requests.post(url, json=batch, timeout=10)
            if response.status_code == 200:
                print(f'✅ Lote {i//batch_size + 1} transmitido com sucesso')
            else:
                print(f'⚠️ Erro no lote {i//batch_size + 1}: {response.status_code}')
                with open(f'/home/user/logs/transmissao_lux_20251012_batch_{i//batch_size + 1}.json', 'w') as f:
                    json.dump(batch, f)
        except Exception as e:
            print(f'⚠️ Falha no lote {i//batch_size + 1}: {e}')
            with open(f'/home/user/logs/transmissao_lux_20251012_batch_{i//batch_size + 1}.json', 'w') as f:
                json.dump(batch, f)
if __name__ == '__main__':
    log_file = '/home/user/logs/transmissao_lux_20251012_013752.json'
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            data = json.load(f)
        transmit_batch(data, 'https://fundacao-alquimista-anatheron-7el6l1nvh.vercel.app/api/fundacao-completa', 1000)
    else:
        print(f'❌ Arquivo {log_file} não encontrado')
