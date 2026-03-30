import paramiko
import sys
import time

def run_cmd(ssh, cmd):
    print(f"Running: {cmd}")
    stdout = ssh.exec_command(cmd)[1]
    status = stdout.channel.recv_exit_status()
    out = stdout.read().decode().strip()
    return status, out

def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect('14.225.224.203', username='root', password='fs7RS1FuvrJ9jgKDJcNp', timeout=10)
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    print("Authenticating with GHCR...")
    import os
    github_token = os.environ.get("GITHUB_TOKEN", "")
    status, _ = run_cmd(ssh, f"echo {github_token} | docker login ghcr.io -u superdien-debug --password-stdin")
    if status != 0:
        print("Failed to authenticate with GitHub Container Registry.")
        return

    print("Fetching services list from docker-compose.prod.yml...")
    _, out = run_cmd(ssh, "cd /opt/viet-erp && docker compose -f docker-compose.prod.yml --env-file .env.production config --services")
    services = [s for s in out.split('\n') if s.strip()]

    working = []
    failed = []

    print(f"Found {len(services)} services. Attempting to pull images...")
    for svc in services:
        print(f"Pulling {svc}...")
        status, _ = run_cmd(ssh, f"cd /opt/viet-erp && docker compose -f docker-compose.prod.yml --env-file .env.production pull {svc}")
        if status == 0:
            working.append(svc)
        else:
            failed.append(svc)

    print(f"\nPull Results:")
    print(f"Working ({len(working)}): {' '.join(working)}")
    print(f"Failed  ({len(failed)}): {' '.join(failed)}")

    if working:
        print("\nStarting Working Services...")
        status, out = run_cmd(ssh, f"cd /opt/viet-erp && docker compose -f docker-compose.prod.yml --env-file .env.production up -d {' '.join(working)}")
        print(out)
        if status == 0:
            print("Successfully started working services!")
        else:
            print("Some services failed to start.")

    ssh.close()

if __name__ == '__main__':
    main()
