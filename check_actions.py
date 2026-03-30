import urllib.request
import json
import ssl
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {'Authorization': 'token \" + __import__("os").environ.get("GITHUB_TOKEN", "") + \"'}

req = urllib.request.Request('https://api.github.com/repos/superdien-debug/vieterp/actions/runs', headers=HEADERS)
try:
    response = urllib.request.urlopen(req, context=ctx)
    data = json.loads(response.read().decode())
    runs = data.get('workflow_runs', [])
    if not runs:
        print("No runs found")
        sys.exit(0)
    
    run = runs[0]
    print(f"Latest run: {run['name']} - Status: {run['status']} - Conclusion: {run['conclusion']}")
    
    # Try fetching jobs
    jobs_url = run.get('jobs_url')
    if jobs_url:
        jobs_req = urllib.request.Request(jobs_url, headers=HEADERS)
        jobs_data = json.loads(urllib.request.urlopen(jobs_req, context=ctx).read().decode())
        
        for job in jobs_data.get('jobs', []):
            if job['conclusion'] != 'success':
                print(f"Job failed: {job['name']}")
                for step in job.get('steps', []):
                    if step['conclusion'] == 'failure':
                        print(f"  Failed step: {step['name']}")

except Exception as e:
    print(f"Error: {e}")
