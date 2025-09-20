(function(){
  const D = window.TGSEC_DATA || {};
  function renderSecrets(){
    const wrap = document.getElementById('secrets');
    const items = (D.scan_secrets || []);
    if(!items.length){ wrap.innerHTML = '<span class="badge ok">✅ No secrets found</span>'; return; }
    wrap.innerHTML = items.map(x=>`
      <div class="item">
        <span class="badge high">🛑 ${x.type}</span>
        <code>${x.file}</code>
        <span> · ${x.snippet}</span>
      </div>
    `).join('');
  }
  function renderLinks(){
    const wrap = document.getElementById('links');
    const items = (D.risky_links || []);
    if(!items.length){ wrap.innerHTML = '<span class="badge ok">✅ No suspicious links</span>'; return; }
    wrap.innerHTML = items.map(x=>`
      <div class="item"><span class="badge warn">⚠️ risky</span> ${x}</div>
    `).join('');
  }
  function renderWebhooks(){
    const wrap = document.getElementById('webhooks');
    const items = (D.webhooks || []);
    if(!items.length){ wrap.innerHTML = '<span class="badge ok">✅ No checks</span>'; return; }
    wrap.innerHTML = items.map(r=>{
      const cls = r.ok ? 'ok':'high';
      const emj = r.ok ? '✅':'🛑';
      return `<div class="item"><span class="badge ${cls}">${emj} ${r.status||'ERR'}</span> ${r.url} · ${r.latency_ms||'-'} ms</div>`;
    }).join('');
  }
  renderSecrets(); renderLinks(); renderWebhooks();
})();
