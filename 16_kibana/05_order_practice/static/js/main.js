function fmtPrice(v) {
    return Number(v).toLocaleString() + "원";
}

function fmtDate(v) {
    return String(v).slice(0, 10);
}

const BADGE = {
    "결제완료": "badge-blue",
    "배송중": "badge-yellow",
    "배송완료": "badge-green",
    "취소": "badge-red",
};

function showToast(msg, type = "success") {
    const t = document.getElementById("toast");
    if (!t) return;
    t.textContent = msg;
    t.className = `toast ${type} show`;
    setTimeout(() => {
        t.className = "toast";
    }, 2000);
}


async function seedData() {
    const count = +document.getElementById("seedCount").value || 20;
    document.getElementById("toast-msg").textContent = "생성 중...";
    const data = await fetch("/api/seed", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({count}),
    }).then(r => r.json());

    document.getElementById("toast-msg").textContent = `${data.added}건 추가 (전체 ${data.total}건)`;
    location.reload();
}

async function deleteAll() {
    if (!confirm("전체 데이터를 삭제할까요?")) return;
    await fetch("/api/delete_all", {method: "DELETE"});
    location.reload();
}


async function loadOrders(page = 1) {
    const data = await fetch(`/api/orders?page=${page}&per=10`).then(r => r.json());
    const tbody = document.getElementById("orderTbody");
    if (!tbody) return;

    tbody.innerHTML = data.orders.map(o => `
        <tr>
            <td>${o.id}</td>
            <td>${o.user_name}</td>
            <td>${o.product_name}</td>
            <td>${o.category}</td>
            <td>${o.quantity}</td>
            <td>${fmtPrice(o.total_price)}</td>
            <td><span class="badge ${BADGE[o.status] || ''}">${o.status}</span></td>
            <td>${fmtDate(o.created_at)}</td>
        </tr>
    `).join("") || "<tr><td colspan='8' style='text-align:center;color:#aaa'>데이터 없음</td></tr>";

    const pg = document.getElementById("pagination");
    if (!pg) return;
    pg.innerHTML = "";
    for (let i = 1; i <= data.pages; i++) {
        const btn = document.createElement("button");
        btn.textContent = i;
        btn.className = (i === page ? " active" : "");
        btn.onclick = () => loadOrders(i);
        pg.appendChild(btn);
    }
}

async function loadStats() {
    const d = await fetch("/api/stats").then(r => r.json());

    const set = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.textContent = val;
    };
    set("statOrders", d.total_orders);
    set("statUsers", d.total_users);
    set("statProducts", d.total_products);
    set("statES", d.elasticsearch);

    const sg = document.getElementById("statusChips");
    if (sg) {
        sg.innerHTML = Object.entries(d.status || {})
            .map(([s, c]) => `<div class="badge ${BADGE[s] || ''}" style="padding:6px 14px; font-size:0.82rem;">${s} <strong>${c}</strong>건</div>`)
            .join("");
    }
}

async function searchOrders() {
    const q = document.getElementById("searchInput")?.value.trim();
    if (!q) {
        loadOrders(1);
        return;
    }

    const data = await fetch(`/api/search?q=${encodeURIComponent(q)}`).then(r => r.json());
    const tbody = document.getElementById("orderTbody");
    if (!tbody) return;

    tbody.innerHTML = (data.hits || []).map(o => `
        <tr>
            <td>${o.id}</td>
            <td>${o.user_name}</td>
            <td>${o.product_name}</td>
            <td>${o.category}</td>
            <td>${o.quantity}</td>
            <td>${fmtPrice(o.total_price)}</td>
            <td><span class="badge ${BADGE[o.status] || ''}">${o.status}</span></td>
            <td>${fmtDate(o.created_at)}</td>
        </tr>
    `).join("") || "<tr><td colspan='8' style='text-align:center;color:#aaa'>검색 결과 없음</td></tr>";

    const rc = document.getElementById("resultCount");
    if (rc) rc.textContent = `ES 검색 결과 ${data.total}건`;
}


let qty = 1;

function changeQty(delta) {
    qty = Math.max(1, qty + delta);
    const el = document.getElementById("qtyDisplay");
    if (el) el.textContent = qty;
    updateTotal();
}

function updateTotal() {
    const el = document.getElementById("totalPrice");
    if (el) el.textContent = fmtPrice(window.PRODUCT_PRICE * qty);
}

async function submitOrder() {
    const name = document.getElementById("inputName")?.value.trim();
    const email = document.getElementById("inputEmail")?.value.trim();
    if (!name || !email) {
        showToast("이름과 이메일을 입력하세요", "error");
        return;
    }

    const res = await fetch("/api/order", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            product_id: window.PRODUCT_ID,
            quantity: qty,
            user_name: name,
            user_email: email,
        }),
    }).then(r => r.json());

    if (res.ok) {
        showToast(`주문 완료! 결제금액: ${fmtPrice(res.total)}`, "success");
        closeModal();
    } else {
        showToast(res.msg || "주문 실패", "error");
    }
}

function openModal() {
    document.getElementById("orderModal")?.classList.add("open");
}

function closeModal() {
    document.getElementById("orderModal")?.classList.remove("open");
}