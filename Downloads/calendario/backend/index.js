require('dotenv').config();
const express = require('express');
const cors    = require('cors');
const { Pool } = require('pg');

const app  = express();
const pool = new Pool({ connectionString: process.env.DATABASE_URL, ssl: { rejectUnauthorized: false } });

app.use(cors({ origin: process.env.FRONTEND_URL || '*' }));
app.use(express.json());

// ── DB INIT ────────────────────────────────────────────────────────────────
async function initDB() {
  await pool.query(`
    CREATE TABLE IF NOT EXISTS projects (
      id         SERIAL PRIMARY KEY,
      name       TEXT NOT NULL,
      position   INTEGER DEFAULT 0,
      created_at TIMESTAMPTZ DEFAULT NOW()
    );

    CREATE TABLE IF NOT EXISTS segments (
      id         SERIAL PRIMARY KEY,
      project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
      label      TEXT NOT NULL,
      start_date DATE NOT NULL,
      end_date   DATE NOT NULL,
      status     TEXT NOT NULL DEFAULT 'planejado',
      position   INTEGER DEFAULT 0,
      created_at TIMESTAMPTZ DEFAULT NOW()
    );
  `);
  console.log('✅ Banco de dados pronto.');
}

// ── PROJECTS ───────────────────────────────────────────────────────────────

// GET /projects — lista todos os projetos com seus segmentos
app.get('/projects', async (req, res) => {
  try {
    const { rows: projects } = await pool.query(
      'SELECT * FROM projects ORDER BY position, created_at'
    );
    const { rows: segments } = await pool.query(
      'SELECT * FROM segments ORDER BY position, created_at'
    );
    const result = projects.map(p => ({
      ...p,
      segments: segments.filter(s => s.project_id === p.id)
    }));
    res.json(result);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// POST /projects — cria novo projeto
app.post('/projects', async (req, res) => {
  const { name } = req.body;
  if (!name) return res.status(400).json({ error: 'name é obrigatório' });
  try {
    const { rows } = await pool.query(
      'INSERT INTO projects (name) VALUES ($1) RETURNING *',
      [name]
    );
    res.status(201).json({ ...rows[0], segments: [] });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// PUT /projects/:id — atualiza nome do projeto
app.put('/projects/:id', async (req, res) => {
  const { name } = req.body;
  try {
    const { rows } = await pool.query(
      'UPDATE projects SET name=$1 WHERE id=$2 RETURNING *',
      [name, req.params.id]
    );
    if (!rows.length) return res.status(404).json({ error: 'Projeto não encontrado' });
    res.json(rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// DELETE /projects/:id — exclui projeto (cascata nos segmentos)
app.delete('/projects/:id', async (req, res) => {
  try {
    await pool.query('DELETE FROM projects WHERE id=$1', [req.params.id]);
    res.json({ ok: true });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ── SEGMENTS ───────────────────────────────────────────────────────────────

// POST /projects/:id/segments — cria segmento em um projeto
app.post('/projects/:id/segments', async (req, res) => {
  const { label, start_date, end_date, status } = req.body;
  if (!label || !start_date || !end_date)
    return res.status(400).json({ error: 'label, start_date e end_date são obrigatórios' });
  try {
    const { rows } = await pool.query(
      `INSERT INTO segments (project_id, label, start_date, end_date, status)
       VALUES ($1,$2,$3,$4,$5) RETURNING *`,
      [req.params.id, label, start_date, end_date, status || 'planejado']
    );
    res.status(201).json(rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// PUT /segments/:id — atualiza segmento
app.put('/segments/:id', async (req, res) => {
  const { label, start_date, end_date, status } = req.body;
  try {
    const { rows } = await pool.query(
      `UPDATE segments SET label=$1, start_date=$2, end_date=$3, status=$4
       WHERE id=$5 RETURNING *`,
      [label, start_date, end_date, status, req.params.id]
    );
    if (!rows.length) return res.status(404).json({ error: 'Segmento não encontrado' });
    res.json(rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// DELETE /segments/:id — exclui segmento
app.delete('/segments/:id', async (req, res) => {
  try {
    await pool.query('DELETE FROM segments WHERE id=$1', [req.params.id]);
    res.json({ ok: true });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ── HEALTH CHECK ───────────────────────────────────────────────────────────
app.get('/health', (_, res) => res.json({ status: 'ok' }));

// ── START ──────────────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
initDB().then(() => {
  app.listen(PORT, () => console.log(`🚀 API rodando na porta ${PORT}`));
});
