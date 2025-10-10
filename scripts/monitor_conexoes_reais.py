import time
import requests
import json

urls = [
    "https://fundacao-alquimista-anatheron.vercel.app/interfaces-conectadas",
    "https://fundacao-alquimista-anatheron.vercel.app/dashboard-real-dados",
    "https://fundacao-alquimista-anatheron.vercel.app/api/portal-alquimista",
    "https://fundacao-alquimista-anatheron.vercel.app/api/sistemas-identificados",
    "https://fundacao-alquimista-anatheron.vercel.app/api/sistemas-adicionais"
]

while True:
    print("\n🧪 MONITORAMENTO CONTÍNUO - CONEXÕES REAIS")
    print("=" * 50)
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            status = "✅ ONLINE" if response.status_code == 200 else f"❌ OFFLINE ({response.status_code})"
            print(f"🔗 {url}: {status}")
            if response.status_code == 200:
                with open(f"logs/monitor_conexoes_{url.split('/')[-1]}.json", "a") as f:
                    json.dump({"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), "status": response.status_code, "data": response.json()}, f)
                    f.write("\n")
        except Exception as e:
            print(f"❌ ERRO em {url}: {str(e)}")
    time.sleep(30)
