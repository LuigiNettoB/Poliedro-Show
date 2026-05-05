# 📅 Calendário de Projetos — Deploy no Railway

Stack: Node.js + Express + PostgreSQL (backend) · HTML puro (frontend)

---

## 🚀 Deploy em 5 passos no Railway

### 1. Criar conta no Railway
Acesse https://railway.app e entre com sua conta GitHub.

### 2. Subir o backend

1. Faça upload da pasta `backend/` para um repositório GitHub (ou use o Railway CLI)
2. No Railway, clique em **New Project → Deploy from GitHub repo**
3. Selecione o repositório do backend
4. O Railway detecta automaticamente que é Node.js

### 3. Adicionar o banco PostgreSQL

1. No seu projeto Railway, clique em **+ New → Database → PostgreSQL**
2. O Railway cria o banco e injeta automaticamente a variável `DATABASE_URL` no seu serviço Node

### 4. Configurar variáveis de ambiente do backend

No painel do serviço Node, vá em **Variables** e adicione:
```
FRONTEND_URL=https://seu-frontend.railway.app   ← preencha após subir o frontend
PORT=3000                                         ← Railway já define, mas deixe aqui por segurança
```
> `DATABASE_URL` já é injetado automaticamente pelo Railway — não precisa adicionar manualmente.

### 5. Subir o frontend

**Opção A — Railway (mais simples):**
1. Crie outro serviço no mesmo projeto: **+ New → Empty Service**
2. Faça upload da pasta `frontend/` para outro repositório GitHub
3. Em Settings, defina o Start Command como: `npx serve . -p $PORT`
4. Adicione a variável: `PORT=3000`

**Opção B — Qualquer hospedagem estática:**
Você pode hospedar `index.html` no GitHub Pages, Vercel, Netlify ou até no SharePoint.

---

## ⚙️ Configurar a URL da API no frontend

Abra `frontend/index.html` e altere a linha:

```js
const API_URL = 'https://SUA-API.railway.app';
```

Substitua pela URL real do seu serviço backend no Railway
(ex: `https://calendario-api-production.up.railway.app`).

---

## 📋 Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/projects` | Lista projetos com segmentos |
| POST | `/projects` | Cria projeto `{ name }` |
| PUT | `/projects/:id` | Renomeia projeto `{ name }` |
| DELETE | `/projects/:id` | Exclui projeto (cascata) |
| POST | `/projects/:id/segments` | Cria bloco `{ label, start_date, end_date, status }` |
| PUT | `/segments/:id` | Atualiza bloco |
| DELETE | `/segments/:id` | Exclui bloco |
| GET | `/health` | Health check |

---

## 💻 Rodar localmente

```bash
cd backend
npm install
cp .env.example .env
# edite .env com sua string de conexão PostgreSQL local
npm run dev
```

Abra `frontend/index.html` no navegador (ou use Live Server no VS Code).

---

## 🏢 Adicionar como aba no Teams

1. Hospede o `frontend/index.html` (Railway, Vercel, SharePoint etc.)
2. No canal do Teams, clique em **+** para nova aba
3. Escolha **Website**
4. Cole a URL do frontend
5. Pronto — todos da equipe acessam o mesmo calendário com dados em tempo real!
