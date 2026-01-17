# 🧾 Gerenciador de Estoque — FastAPI + React

Pequeno sistema de gestão de estoque com backend em **FastAPI + SQLite** e frontend em **React + Vite**.

---

## 📚 Sumário
- [Pré-requisitos](#-pré-requisitos)
- [Quick start](#-quick-start)
- [Backend (FastAPI)](#-backend-fastapi)
- [Frontend (Vite + React)](#-frontend-vite--react)
- [Observações importantes](#-observações-importantes)
- [Scripts úteis](#-scripts-úteis)
- [Próximos passos](#-próximos-passos)

---

## ⚙️ Pré-requisitos
- Python 3.10+ (recomendado 3.10 ou 3.11)
- pip (geralmente instalado com Python)
- Node.js (LTS recomendado, >=16)
- npm (vem com Node.js)

Verifique rapidamente com os scripts:
- Windows (PowerShell): `scripts\check_prereqs.ps1` (se o PowerShell bloquear a execução, use `powershell -ExecutionPolicy Bypass -File .\scripts\check_prereqs.ps1`)
- macOS / Linux: `scripts/check_prereqs.sh` (torne executável: `chmod +x scripts/check_prereqs.sh`)

---

## 🚀 Quick start
Siga estes passos básicos: execute a API e, em seguida, o frontend.

### Windows (PowerShell)
```powershell
# Backend
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py

# Em outro terminal, Frontend
cd frontend
npm install
npm run dev
```

### macOS / Linux (Terminal)
```bash
# Backend
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py

# Em outro terminal, Frontend
cd frontend
npm install
npm run dev
```

Abra o frontend em: `http://localhost:5173` (por padrão) e a API em `http://localhost:8000`.

---

## 🖥️ Backend (FastAPI)
- Iniciar (desenvolvimento): `python run.py` — o script mostra os links da app e da documentação (Swagger: `/docs`).
- Banco padrão: `backend/database.db` (SQLite).
- Migração do campo `min_quantity`: o backend tenta adicionar automaticamente essa coluna em bases antigas; em ambiente de desenvolvimento, apagar `backend/database.db` recria o schema caso necessário.
- Checagem rápida de dependências Python: `python check_prereqs.py` (dentro de `backend/`).

---

## 🌐 Frontend (Vite + React)
- Inicie em `frontend/` com `npm install` e `npm run dev`.
- Configure a URL da API criando `frontend/.env` a partir de `frontend/.env.example` (variável `VITE_API_URL`).

---

## ⚠️ Observações importantes
- CORS já está configurado para o frontend `http://localhost:5173`.
- Se algo não funcionar (ex.: migrations), tente apagar `backend/database.db` e reiniciar a API (apenas em desenvolvimento).

---

## 🛠️ Scripts úteis
- `scripts/check_prereqs.ps1` — checa Python / Node / npm (Windows PowerShell).
- `scripts/check_prereqs.sh` — checa Python / Node / npm (macOS / Linux).
- `backend/check_prereqs.py` — checa se os pacotes Python essenciais estão instalados.
- `frontend/.env.example` — exemplo de configuração para o frontend.

---

## ✅ Próximos passos (opções)
- Adicionar Docker + docker-compose (execução em qualquer OS) 🐳
- Adicionar testes automatizados (pytest) ✅
- Configurar CI/CD (GitHub Actions) 🔁

---

## 🧪 Testes

### Backend
- Implementado com `pytest` + `TestClient` (FastAPI). Rode em `backend/` com:

```powershell
pip install -r backend/requirements.txt
python -m pytest -q
```

**Testes implementados**:
- `test_create_and_get_product` — cria e recupera produto; valida campos e `GET /products/{id}`.
- `test_update_and_delete_product` — atualiza produto com `PUT` e verifica `DELETE` remove o registro.
- `test_list_products` — valida `GET /products`.
- `test_get_product_not_found` — checa 404 para produto inexistente.
- `test_create_movement_entrada_increases_quantity` — movimento `entrada` aumenta quantidade.
- `test_create_movement_saida_decreases_quantity` — movimento `saida` diminui quantidade.
- `test_create_movement_cannot_remove_more_than_available` — garante erro ao retirar mais que disponível.
- `test_create_movement_invalid_type_or_product` — valida tipos inválidos e produto inexistente.
- `test_list_movements` — valida `GET /movements` retorna movimentos.

---

## 🔁 Integração Contínua (GitHub Actions)

Criei um workflow para CI em `.github/workflows/ci.yml` que:

- Executa os testes do backend (`pytest`) em Python 3.11.
- Faz build do frontend (Node 18) para validar que o frontend compila sem erros.

A pipeline é disparada em `push` e `pull_request` nas branches `main`/`master`. Se quiser, posso ajustar a workflow para rodar checks adicionais (linters, coverage, etc.).

