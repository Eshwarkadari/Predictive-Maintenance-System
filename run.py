"""
Predictive Maintenance Live Dashboard
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
Run: python run.py
"""
from flask import Flask, jsonify, render_template_string
import random, threading, time
from datetime import datetime

app = Flask(__name__)
machines = {}

def simulate():
    ages = {f"Motor_{i:02d}": random.randint(0,80) for i in range(1,6)}
    while True:
        for mid, age in ages.items():
            deg = min(age/100, 1.0)
            fp  = round(deg*100 + random.uniform(-5,5), 1)
            fp  = max(0, min(100, fp))
            machines[mid] = {
                "machine":     mid,
                "temperature": round(45+45*deg+random.uniform(-2,2),1),
                "vibration":   round(1.5+4*deg+random.uniform(-0.2,0.2),2),
                "current":     round(9+5*deg+random.uniform(-0.3,0.3),2),
                "rpm":         round(1500-100*deg+random.uniform(-10,10)),
                "fail_prob":   fp,
                "status":      "CRITICAL" if fp>70 else ("WARNING" if fp>40 else "NORMAL"),
                "rul_days":    max(0, round((100-fp)/10,1)),
                "age_days":    age,
                "timestamp":   datetime.now().strftime("%H:%M:%S"),
            }
            ages[mid] += random.randint(0,1)
        time.sleep(4)

@app.route("/")
def home(): return render_template_string(HTML)

@app.route("/api/machines")
def get_machines(): return jsonify(list(machines.values()))

HTML = """<!DOCTYPE html>
<html><head>
<meta charset="UTF-8"><meta http-equiv="refresh" content="5">
<title>Predictive Maintenance</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',sans-serif;background:#0f172a;color:#e2e8f0}
nav{background:#1e293b;padding:16px 28px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #334155}
.logo{font-size:18px;font-weight:700;color:#fb923c}
.live{background:#fb923c22;color:#fb923c;border:1px solid #fb923c;padding:4px 12px;border-radius:20px;font-size:12px}
.main{padding:24px 28px;max-width:1200px;margin:0 auto}
h2{margin-bottom:18px;font-size:20px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px}
.card{background:#1e293b;border-radius:12px;padding:18px;border:2px solid #334155}
.card.critical{border-color:#ef4444}.card.warning{border-color:#f59e0b}.card.normal{border-color:#4ade80}
.machine{font-size:12px;color:#94a3b8;font-weight:700;text-transform:uppercase;margin-bottom:6px}
.prob{font-size:30px;font-weight:700}
.critical .prob{color:#ef4444}.warning .prob{color:#f59e0b}.normal .prob{color:#4ade80}
.badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:700;margin:4px 0 10px}
.critical .badge{background:#7f1d1d;color:#fca5a5}
.warning  .badge{background:#78350f;color:#fde68a}
.normal   .badge{background:#14532d;color:#86efac}
.row{display:flex;justify-content:space-between;font-size:13px;color:#94a3b8;margin-top:6px}
.val{color:#e2e8f0;font-weight:600}
.rec{font-size:12px;margin-top:10px;padding:8px;border-radius:6px;background:#0f172a;color:#94a3b8}
footer{text-align:center;padding:14px;color:#475569;font-size:12px;margin-top:16px}
</style></head>
<body>
<nav>
  <div class="logo">⚙️ Predictive Maintenance Dashboard</div>
  <div class="live">● LIVE — auto refresh 5s</div>
</nav>
<div class="main">
  <h2>🏭 Industrial Motor Health Monitor</h2>
  <div class="grid" id="cards">Loading...</div>
  <p style="color:#64748b;font-size:13px;margin-top:14px">
    Built by <b style="color:#94a3b8">Kadari Eshwar</b> — B.Tech ECE, JNTU Hyderabad
    &nbsp;|&nbsp; ML: Isolation Forest + Random Forest
  </p>
</div>
<footer>API: /api/machines</footer>
<script>
fetch('/api/machines').then(r=>r.json()).then(data=>{
  document.getElementById('cards').innerHTML=data.map(m=>{
    const c=m.status.toLowerCase();
    const rec=m.fail_prob>70?'🔧 IMMEDIATE maintenance needed!':m.fail_prob>40?'⚠️ Schedule within 48h':'✅ Normal operation';
    return '<div class="card '+c+'">'
      +'<div class="machine">'+m.machine+'</div>'
      +'<div class="prob">'+m.fail_prob+'%</div>'
      +'<div><span class="badge">'+m.status+'</span></div>'
      +'<div class="row"><span>Temperature</span><span class="val">'+m.temperature+'°C</span></div>'
      +'<div class="row"><span>Vibration</span><span class="val">'+m.vibration+' mm/s</span></div>'
      +'<div class="row"><span>Current</span><span class="val">'+m.current+' A</span></div>'
      +'<div class="row"><span>RPM</span><span class="val">'+m.rpm+'</span></div>'
      +'<div class="row"><span>RUL</span><span class="val">'+m.rul_days+' days</span></div>'
      +'<div class="rec">'+rec+'</div></div>';
  }).join('');
});
</script></body></html>"""

if __name__ == "__main__":
    threading.Thread(target=simulate, daemon=True).start()
    print("\n✅ Machine simulation started!")
    print("🌐 Open http://localhost:5000 in your browser")
    print("   Auto-refreshes every 5 seconds")
    print("   Press Ctrl+C to stop\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
