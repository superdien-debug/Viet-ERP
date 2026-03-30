import urllib.request
import json
import time
import ssl
import sys
import subprocess

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

import os
HEADERS = {'Authorization': f'token {os.environ.get("GITHUB_TOKEN", "")}'}

print("=> Đang theo dõi tiến trình GitHub Actions (CI Pipeline) trên github.com...")

while True:
    try:
        req = urllib.request.Request('https://api.github.com/repos/superdien-debug/Viet-ERP/actions/runs', headers=HEADERS)
        runs = json.loads(urllib.request.urlopen(req, context=ctx).read())['workflow_runs']
        ci_run = next((r for r in runs if r['name'] == 'CI Pipeline'), runs[0])
        
        if ci_run['status'] == 'completed':
            if ci_run['conclusion'] == 'success':
                print("\n✅ GitHub Actions đã chạy THÀNH CÔNG! Đang khởi động deploy-superdien.py...\n")
                break
            else:
                print(f"\n❌ GitHub Actions đã THẤT BẠI với mã: {ci_run['conclusion']}")
                print("Vui lòng truy cập github.com để xem log lỗi.")
                sys.exit(1)
                
        print(f'⏳ Tiến trình đang build Docker Images. Vui lòng chờ... ({ci_run["status"]})')
        time.sleep(15)
    except Exception as e:
        print(f"Lỗi: {e}")
        time.sleep(15)

# Deploy
subprocess.run([sys.executable, "deploy-superdien.py"])
