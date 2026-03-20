# Configuração: Workload Identity Federation (GitHub -> GCP)

Este guia detalha como configurar a autenticação segura entre o GitHub Actions e o Google Cloud Platform (GCP) sem o uso de chaves Service Account JSON (Zero-Trust).

## 1. Variáveis de Ambiente
Substitua os valores abaixo pelos correspondentes ao seu projeto:
- `PROJECT_ID`: ID do seu projeto no GCP.
- `POOL_NAME`: `github-pool` (sugerido).
- `PROVIDER_NAME`: `github-provider` (sugerido).
- `REPO`: `username/repo_name` (seu repositório no GitHub).

## 2. Comandos GCP CLI (gcloud)

### A. Ativar APIs Necessárias
```bash
gcloud services enable iamcredentials.googleapis.com \
  --project="${PROJECT_ID}"
```

### B. Criar o Pool de Identidade
```bash
gcloud iam workload-identity-pools create "${POOL_NAME}" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --display-name="GitHub Actions Pool"
```

### C. Obter o ID Completo do Pool
```bash
gcloud iam workload-identity-pools describe "${POOL_NAME}" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --format="value(name)"
```
*(Guarde este valor como `WORKLOAD_IDENTITY_POOL_ID`)*

### D. Criar o Provedor OIDC
```bash
gcloud iam workload-identity-pools providers create-oidc "${PROVIDER_NAME}" \
  --project="${PROJECT_ID}" \
  --location="global" \
  --workload-identity-pool="${POOL_NAME}" \
  --display-name="GitHub Provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository" \
  --issuer-uri="https://token.actions.githubusercontent.com"
```

### E. Vincular a Service Account ao Repositório
Crie uma Service Account dedicada (ex: `github-actions-deploy@PROJECT_ID.iam.gserviceaccount.com`) e execute:

```bash
gcloud iam service-accounts add-iam-policy-binding "github-actions-deploy@${PROJECT_ID}.iam.gserviceaccount.com" \
  --project="${PROJECT_ID}" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/${WORKLOAD_IDENTITY_POOL_ID}/attribute.repository/${REPO}"
```

## 3. Configuração no GitHub
Adicione os seguintes segredos (Secrets) ao seu repositório:
- `GCP_PROJECT_ID`: O ID do seu projeto GCP.
- `GCP_WIF_PROVIDER`: O nome completo do provedor (ex: `projects/123456789/locations/global/workloadIdentityPools/github-pool/providers/github-provider`).
- `GCP_SERVICE_ACCOUNT`: O e-mail da Service Account criada.
