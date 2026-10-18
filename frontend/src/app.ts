// QHSJ-AIGC Route Tester — single-page app.
// Calls the backend /route endpoint and renders the match result.

interface RouteResult {
  matched: boolean;
  route_id?: string;
  gate_level?: string;
  blocks_on_failure?: boolean;
  matched_triggers?: string[];
  score?: number;
  error_code?: string;
  candidates?: { id: string; gate_level: string; score: number }[];
}

interface HealthResult {
  status: string;
  name: string;
  version: string;
  declared_counts: { capabilities: number; workflows: number; references: number };
}

const API_BASE = ""; // same-origin via Vite proxy in dev

export function initApp(root: HTMLElement) {
  root.innerHTML = `
    <header class="hdr">
      <h1>QHSJ-AIGC 路由测试器</h1>
      <p id="health" class="health">检测后端…</p>
    </header>
    <main class="main">
      <section class="panel">
        <label for="query">输入创作意图（中文）：</label>
        <textarea id="query" rows="4" placeholder="例如：帮我做角色资产锁定"></textarea>
        <div class="actions">
          <button id="submit">匹配路由</button>
          <button id="clear" class="ghost">清空</button>
        </div>
      </section>
      <section class="panel result">
        <h2>匹配结果</h2>
        <pre id="output">等待输入…</pre>
      </section>
    </main>
    <footer class="ftr">
      <span>v7.0.0 · 路由匹配单一数据源：routes.json</span>
    </footer>
  `;

  const queryEl = document.getElementById("query") as HTMLTextAreaElement;
  const outputEl = document.getElementById("output") as HTMLPreElement;
  const healthEl = document.getElementById("health") as HTMLElement;
  const submitBtn = document.getElementById("submit") as HTMLButtonElement;
  const clearBtn = document.getElementById("clear") as HTMLButtonElement;

  checkHealth(healthEl);

  submitBtn.addEventListener("click", () => doMatch(queryEl, outputEl));
  clearBtn.addEventListener("click", () => {
    queryEl.value = "";
    outputEl.textContent = "等待输入…";
  });
  queryEl.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
      e.preventDefault();
      doMatch(queryEl, outputEl);
    }
  });
}

async function checkHealth(el: HTMLElement) {
  try {
    const resp = await fetch(`${API_BASE}/health`);
    const data: HealthResult = await resp.json();
    el.textContent = `● ${data.name} v${data.version} · 能力 ${data.declared_counts.capabilities} · 工作流 ${data.declared_counts.workflows} · 知识库 ${data.declared_counts.references}`;
    el.classList.add("ok");
  } catch {
    el.textContent = "● 后端未连接（请启动 uvicorn backend.app.main:app）";
    el.classList.add("err");
  }
}

async function doMatch(queryEl: HTMLTextAreaElement, outputEl: HTMLPreElement) {
  const query = queryEl.value.trim();
  if (!query) {
    outputEl.textContent = "请输入非空意图。";
    return;
  }
  outputEl.textContent = "匹配中…";
  try {
    const resp = await fetch(`${API_BASE}/route`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });
    const data: RouteResult = await resp.json();
    outputEl.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    outputEl.textContent = `请求失败：${(e as Error).message}`;
  }
}
