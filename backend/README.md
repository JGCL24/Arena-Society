# Backend (FastAPI) - Gerenciador de Estoque

Rápido para rodar:

1. Pré-requisitos: Python 3.10+
2. No PowerShell, dentro da pasta `backend`:

```powershell
# criar e ativar ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# instalar dependências
pip install -r requirements.txt

# iniciar a API (modo desenvolvimento)
python run.py
```

Ao executar `python run.py` o console exibirá os links da aplicação e da documentação. Exemplo de saída:

```
Starting Gerenciador de Estoque (development mode)
App: http://localhost:8000
Docs: http://localhost:8000/docs
```

- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

Observação: Banco padrão: SQLite em `backend/database.db`.

Você pode executar `python check_prereqs.py` dentro de `backend/` para checar rapidamente se os pacotes Python necessários estão instalados.

**Migração do campo `min_quantity`:** o backend tenta adicionar automaticamente a coluna `min_quantity` em bases antigas; se preferir recriar o DB, apague `backend/database.db` durante desenvolvimento e reinicie a API.

**Verificação de pré-requisitos:** use `scripts\check_prereqs.ps1` (Windows PowerShell) ou `scripts/check_prereqs.sh` (macOS/Linux) para checar se Python / Node / npm estão instalados.

---

## 🧪 Testes

Os testes do backend foram implementados usando `pytest` e o `TestClient` do FastAPI. Para executar:

```powershell
cd backend
pip install -r requirements.txt
python -m pytest -q
```

### Testes implementados

- **test_create_and_get_product** — cria um produto via `POST /products` e valida `GET /products/{id}` (campos `id`, `name`, `quantity`).
- **test_update_and_delete_product** — atualiza com `PUT /products/{id}` e valida que `DELETE /products/{id}` remove o produto (seguido por `GET` retornando 404).
- **test_list_products** — garante que `GET /products` retorna uma lista de produtos e contém os produtos criados.
- **test_get_product_not_found** — valida que `GET /products/{id}` para id inexistente retorna 404.

- **test_create_movement_entrada_increases_quantity** — cria um movimento do tipo `entrada` e verifica aumento da quantidade do produto.
- **test_create_movement_saida_decreases_quantity** — cria um movimento do tipo `saida` e verifica diminuição da quantidade do produto.
- **test_create_movement_cannot_remove_more_than_available** — verifica que tentar remover mais que o disponível retorna 400.
- **test_create_movement_invalid_type_or_product** — valida tipos inválidos (400) e movimentações para produto inexistente (404).
- **test_list_movements** — garante que `GET /movements` retorna a lista de movimentos e inclui os movimentos criados.

