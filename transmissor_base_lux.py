import requests
import json
import os
import gzip
import time

def transmit_batch(data, url, batch_size=2, max_payload_size=2_000_000, max_retries=3):
    if isinstance(data, dict):
        data = list(data.items())
        print(f"🔄 Dados convertidos de dicionário para lista de itens: {len(data)} itens")
    if not isinstance(data, list):
        print(f"❌ Dados inválidos: esperado lista, recebido {type(data)}")
        return
    total = len(data)
    headers = {
        "Authorization": "Bearer fundacao-alquimista-quantum-secret-2025-966hz-luxnet",
        "Content-Type": "application/json",
        "Content-Encoding": "gzip"
    }
    for i in range(0, total, batch_size):
        batch = data[i:i + batch_size]
        payload = json.dumps(batch, separators=(',', ':'))
        compressed_payload = gzip.compress(payload.encode('utf-8'), compresslevel=9)
        payload_size = len(compressed_payload)
        if payload_size > max_payload_size:
            print(f"⚠️ Lote {i//batch_size + 1} excede o limite de {max_payload_size} bytes: {payload_size} bytes")
            smaller_batch_size = batch_size // 2
            if smaller_batch_size < 1:
                print(f"❌ Lote {i//batch_size + 1} não pode ser dividido mais. Abortando.")
                continue
            print(f"🔄 Reduzindo batch_size para {smaller_batch_size}")
            transmit_batch(data[i:i + batch_size], url, smaller_batch_size, max_payload_size, max_retries)
            continue
        for attempt in range(1, max_retries + 1):
            try:
                print(f"📤 Enviando lote {i//batch_size + 1} ({payload_size} bytes, tentativa {attempt}/{max_retries})")
                response = requests.post(url, data=compressed_payload, headers=headers, timeout=10)
                if response.status_code == 200:
                    print(f"✅ Lote {i//batch_size + 1} transmitido com sucesso")
                    break
                else:
                    print(f"⚠️ Erro no lote {i//batch_size + 1}: {response.status_code} - {response.text}")
                    if attempt == max_retries:
                        with open(f"/home/user/logs/transmissao_lux_20251012_batch_{i//batch_size + 1}.json", "w") as f:
                            json.dump(batch, f, indent=2)
                    time.sleep(2 ** attempt)
            except Exception as e:
                print(f"⚠️ Falha no lote {i//batch_size + 1}: {e}")
                if attempt == max_retries:
                    with open(f"/home/user/logs/transmissao_lux_20251012_batch_{i//batch_size + 1}.json", "w") as f:
                        json.dump(batch, f, indent=2)
                time.sleep(2 ** attempt)

if __name__ == "__main__":
    log_file = "/home/user/logs/transmissao_lux_20251012_013752.json"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)
        print(f"📄 Conteúdo do arquivo {log_file}: {json.dumps(data, indent=2)}")
        transmit_batch(data, "https://fundacao-alquimista-pdvlacpuf.vercel.app/api/fundacao-completa", 2, 2_000_000)
    else:
        print(f"❌ Arquivo {log_file} não encontrado")
