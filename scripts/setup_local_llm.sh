#!/usr/bin/env bash
# Setup Local LLM (Ollama) — Linux/macOS
# Uso: bash scripts/setup_local_llm.sh
# Requisito: curl, bash 4+

set -euo pipefail

DEFAULT_MODEL="${OLLAMA_MODEL:-llama3}"
OLLAMA_BASE_URL="${OLLAMA_BASE_URL:-http://localhost:11434}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$(dirname "$SCRIPT_DIR")/.env"

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; CYAN='\033[0;36m'; NC='\033[0m'

echo -e "${CYAN}=====================================${NC}"
echo -e "${CYAN} Personal AI Core — Local LLM Setup ${NC}"
echo -e "${CYAN}=====================================${NC}"

# --- 1. Verificar/instalar Ollama ---
echo -e "\n${YELLOW}[1/4] Verificando Ollama...${NC}"

# Caminhos comuns de instalação
OLLAMA_PATHS=("/usr/local/bin/ollama" "/usr/bin/ollama" "/bin/ollama" "$(command -v ollama 2>/dev/null || echo '')")
OLLAMA_EXEC=""

for path in "${OLLAMA_PATHS[@]}"; do
    if [[ -x "$path" ]]; then
        OLLAMA_EXEC="$path"
        break
    fi
done

# Se não encontrou binário, tenta API
if [[ -z "$OLLAMA_EXEC" ]]; then
    if curl -sf "${OLLAMA_BASE_URL}/api/tags" > /dev/null; then
        echo -e "${GREEN}Ollama API detectada em ${OLLAMA_BASE_URL}. Prosseguindo...${NC}"
        OLLAMA_EXEC="ollama" # Fallback para comando global
    fi
fi

if [[ -z "$OLLAMA_EXEC" || "$OLLAMA_EXEC" == "ollama" && ! $(command -v ollama &>/dev/null) ]]; then
    if [[ -z "$OLLAMA_EXEC" ]]; then
        echo -e "${YELLOW}Ollama não encontrado. Instalando...${NC}"
        curl -fsSL https://ollama.com/install.sh | sh
        OLLAMA_EXEC="ollama"
    fi
else
    echo -e "${GREEN}Ollama detectado em: ${OLLAMA_EXEC}${NC}"
fi

# --- 2. Iniciar servidor Ollama (background) ---
echo -e "\n${YELLOW}[2/4] Iniciando servidor Ollama...${NC}"
if ! pgrep -x "ollama" > /dev/null; then
    "$OLLAMA_EXEC" serve &>/dev/null &
    sleep 3
    echo -e "${GREEN}Servidor Ollama iniciado.${NC}"
else
    echo -e "${GREEN}Servidor Ollama já está rodando.${NC}"
fi

# --- 3. Pull do modelo ---
echo -e "\n${YELLOW}[3/4] Fazendo pull do modelo '${DEFAULT_MODEL}'...${NC}"
if "$OLLAMA_EXEC" pull "$DEFAULT_MODEL"; then
    echo -e "${GREEN}Modelo '${DEFAULT_MODEL}' disponível!${NC}"
else
    echo -e "${RED}ERRO: Falha ao baixar modelo '${DEFAULT_MODEL}'.${NC}"
    exit 1
fi

# --- 4. Atualizar .env ---
echo -e "\n${YELLOW}[4/4] Atualizando arquivo .env...${NC}"
declare -A ENV_VARS=(
    ["LLM_PROVIDER"]="ollama"
    ["OLLAMA_MODEL"]="$DEFAULT_MODEL"
    ["OLLAMA_BASE_URL"]="$OLLAMA_BASE_URL"
)
if [[ -f "$ENV_FILE" ]]; then
    for key in "${!ENV_VARS[@]}"; do
        value="${ENV_VARS[$key]}"
        if grep -q "^${key}=" "$ENV_FILE"; then
            sed -i "s|^${key}=.*|${key}=${value}|" "$ENV_FILE"
            echo -e "  Atualizado: ${key}=${value}"
        else
            echo "${key}=${value}" >> "$ENV_FILE"
            echo -e "  Adicionado: ${key}=${value}"
        fi
    done
else
    echo -e "${YELLOW}AVISO: .env não encontrado em ${ENV_FILE}. Copie .env.example e execute novamente.${NC}"
fi

# --- Verificação final ---
echo -e "\n${YELLOW} Verificando servidor Ollama...${NC}"
if curl -sf "${OLLAMA_BASE_URL}/api/tags" > /dev/null; then
    echo -e "${GREEN}✓ Ollama respondendo em ${OLLAMA_BASE_URL}${NC}"
else
    echo -e "${YELLOW}⚠ Ollama não respondeu em ${OLLAMA_BASE_URL}. Inicie com: ollama serve${NC}"
fi

echo -e "\n${CYAN}=====================================${NC}"
echo -e "${GREEN} Setup concluído!${NC}"
echo -e " Reinicie o backend: ${CYAN}npm run dev:backend${NC}"
echo -e " Para voltar ao Google AI, edite .env: ${CYAN}LLM_PROVIDER=google${NC}"
echo -e "${CYAN}=====================================${NC}"
