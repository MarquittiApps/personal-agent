# Setup Local LLM (Ollama) — Windows PowerShell
# Uso: .\scripts\setup_local_llm.ps1
# Requisito: PowerShell 5.1+, Windows 10/11

$ErrorActionPreference = "Stop"
$OllamaUrl = "https://ollama.com/download/OllamaSetup.exe"
$DefaultModel = if ($env:OLLAMA_MODEL) { $env:OLLAMA_MODEL } else { "llama3" }
$OllamaBaseUrl = if ($env:OLLAMA_BASE_URL) { $env:OLLAMA_BASE_URL } else { "http://localhost:11434" }
$EnvFile = Join-Path (Split-Path $PSScriptRoot -Parent) ".env"

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host " Personal AI Core — Local LLM Setup " -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan

# --- 1. Verificar/instalar Ollama ---
Write-Host "`n[1/4] Verificando Ollama..." -ForegroundColor Yellow

# Caminhos comuns de instalacao no Windows
$DefaultPaths = @(
    "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe",
    "$env:ProgramFiles\Ollama\ollama.exe",
    "ollama.exe"
)

$OllamaExec = ""
foreach ($path in $DefaultPaths) {
    $found = Get-Command $path -ErrorAction SilentlyContinue
    if ($found) {
        $OllamaExec = $found.Source
        break
    }
}

# Se nao encontrou via Get-Command, tenta checar se a API ja esta respondendo
if (-not $OllamaExec) {
    try {
        $apiCheck = Invoke-RestMethod -Uri "$OllamaBaseUrl/api/tags" -Method Get -TimeoutSec 2 -ErrorAction SilentlyContinue
        if ($apiCheck) {
            Write-Host "Ollama API detectada em $OllamaBaseUrl. Prosseguindo..." -ForegroundColor Green
            # Se a API responde mas nao temos o binario, podemos tentar o pull via API depois ou avisar
        }
    } catch { }
}

if (-not $OllamaExec) {
    Write-Host "Ollama nao encontrado no PATH ou caminhos padrao. Baixando instalador..." -ForegroundColor Yellow
    $installer = "$env:TEMP\OllamaSetup.exe"
    Invoke-WebRequest -Uri $OllamaUrl -OutFile $installer
    Write-Host "Executando instalador..." -ForegroundColor Yellow
    # Nao usamos -Wait para que o usuario possa interagir se o instalador travar ou pedir confirmacao
    Start-Process -FilePath $installer -Wait
    
    # Tenta encontrar novamente apos instalacao
    foreach ($path in $DefaultPaths) {
        $found = Get-Command $path -ErrorAction SilentlyContinue
        if ($found) { $OllamaExec = $found.Source; break }
    }
    
    if (-not $OllamaExec) {
        Write-Host "AVISO: Ollama instalado mas nao encontrado no PATH. Tente reiniciar o terminal." -ForegroundColor Yellow
        $OllamaExec = "ollama" # Fallback
    }
} else {
    Write-Host "Ollama detectado em: $OllamaExec" -ForegroundColor Green
}

# --- 2. Iniciar servidor Ollama (background) ---
Write-Host "`n[2/4] Iniciando servidor Ollama..." -ForegroundColor Yellow
$ollamaProcess = Get-Process -Name "ollama" -ErrorAction SilentlyContinue
if (-not $ollamaProcess) {
    Start-Process -FilePath $OllamaExec -ArgumentList "serve" -WindowStyle Hidden
    Start-Sleep -Seconds 3
}

# --- 3. Pull do modelo ---
Write-Host "`n[3/4] Fazendo pull do modelo '$DefaultModel'..." -ForegroundColor Yellow
& $OllamaExec pull $DefaultModel
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERRO: Falha ao baixar modelo '$DefaultModel'. Verifique se o Ollama server esta rodando." -ForegroundColor Red
    exit 1
}
Write-Host "Modelo '$DefaultModel' disponivel!" -ForegroundColor Green

# --- 4. Atualizar .env ---
Write-Host "`n[4/4] Atualizando arquivo .env..." -ForegroundColor Yellow
$envVars = @{
    "LLM_PROVIDER"     = "ollama"
    "OLLAMA_MODEL"     = $DefaultModel
    "OLLAMA_BASE_URL"  = $OllamaBaseUrl
}
if (Test-Path $EnvFile) {
    $content = Get-Content $EnvFile -Raw
    foreach ($key in $envVars.Keys) {
        $value = $envVars[$key]
        if ($content -match "^$key=") {
            $content = $content -replace "(?m)^$key=.*", "$key=$value"
            Write-Host "  Atualizado: $key=$value" -ForegroundColor DarkGray
        } else {
            $content += "`n$key=$value"
            Write-Host "  Adicionado: $key=$value" -ForegroundColor DarkGray
        }
    }
    Set-Content -Path $EnvFile -Value $content
} else {
    Write-Host "AVISO: .env nao encontrado. Copie .env.example e execute novamente." -ForegroundColor Yellow
}

# --- Verificacao final ---
Write-Host "`n Verificando servidor Ollama..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$OllamaBaseUrl/api/tags" -Method Get -TimeoutSec 5
    Write-Host "Ollama respondendo em $OllamaBaseUrl" -ForegroundColor Green
    Write-Host "Modelos disponiveis: $($response.models.name -join ', ')" -ForegroundColor Green
} catch {
    Write-Host "AVISO: Ollama nao respondeu em $OllamaBaseUrl. Inicie o servidor com: ollama serve" -ForegroundColor Yellow
}

Write-Host "`n=====================================" -ForegroundColor Cyan
Write-Host " Setup concluido!" -ForegroundColor Green
Write-Host " Reinicie o backend para usar o modelo local:" -ForegroundColor White
Write-Host "   npm run dev:backend" -ForegroundColor White
Write-Host " Para voltar ao Google AI, edite .env:" -ForegroundColor White
Write-Host "   LLM_PROVIDER=google" -ForegroundColor White
Write-Host "=====================================" -ForegroundColor Cyan
