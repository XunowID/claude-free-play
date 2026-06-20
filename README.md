# ⬡ FC-Play — Multi-Provider Model Gateway

> **20+ model providers. One endpoint. Beautiful UI. Zero friction.**

<p align="center">
  <img src="https://img.shields.io/badge/python-3.12+-blue?style=flat&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat" alt="MIT">
  <img src="https://img.shields.io/badge/providers-20%2B-orange?style=flat" alt="Providers">
  <img src="https://img.shields.io/badge/status-active-brightgreen?style=flat" alt="Status">
</p>

---

## ✨ What is FC-Play?

**FC-Play** is a universal model gateway — a proxy server that routes requests from any client to 20+ model providers through a single endpoint. It comes with:

- 🖥️ **Beautiful terminal dashboard** — Rich-based TUI with 3 themes
- 🌐 **Modern admin console** — Web UI with warm amber design
- ⚡ **20+ providers** — Anthropic, OpenAI, OpenRouter, Gemini, DeepSeek, Mistral, Groq, and more
- 🎯 **Per-tier routing** — Route opus/sonnet/haiku to different providers
- 🔌 **Client compatible** — Works with any tool that speaks Anthropic Messages or OpenAI Chat APIs

---

## 🔧 Prerequisites

Sebelum install, pastikan sudah siap:

### macOS / Linux
| Tool | Cara Install |
|------|-------------|
| **Python 3.12+** | `uv python install 3.12` (via uv) atau [python.org](https://python.org) |
| **uv** (wajib) | `curl -LsSf https://astral.sh/uv/install.sh | sh` |
| **Git** | `brew install git` atau `apt install git` / `pacman -S git` |
| **Claude CLI** (untuk `fc-play`) | `npm install -g @anthropic-ai/claude-code` |
| **curl** | Usually pre-installed |

### Windows (PowerShell)
| Tool | Cara Install |
|------|-------------|
| **Python 3.12+** | `uv python install 3.12` (via uv) atau [python.org](https://python.org) |
| **uv** (wajib) | `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"` |
| **Git** | [git-scm.com](https://git-scm.com) atau `winget install Git.Git` |
| **Claude CLI** (untuk `fc-play`) | `npm install -g @anthropic-ai/claude-code` |

> **Catatan:** Claude CLI (`claude`) hanya diperlukan kalau mau pakai `fc-play` untuk masuk ke Claude. Kalau cuma mau proxy servernya aja, cukup Python + uv.

---

## 🚀 Quick Install

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/XunowID/fc-play/main/scripts/install.sh | sh

# Windows (PowerShell)
Invoke-Expression (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/XunowID/fc-play/main/scripts/install.ps1").Content
```

### Or from source

```bash
git clone https://github.com/XunowID/fc-play.git
cd fc-play
uv sync
```

---

## 🎯 Commands

### Prefixes — Pilih sesuai kebutuhan

| Command | Fungsi |
|---------|--------|
| `fc-play` | 🎮 Masuk ke Claude via proxy |
| `fc-server` | 🌐 Start proxy server + buka admin otomatis |
| `fc-admin` | 🖥️ Buka panel admin di browser |
| `fc-play-tui` | 📊 Launch terminal dashboard |

### Detail

```bash
# Masuk ke Claude via proxy (auto-start server jika belum jalan)
fc-play

# Start proxy server + langsung buka admin panel
fc-server

# Buka admin panel di browser (server harus sudah jalan)
fc-admin

# Launch terminal dashboard
fc-play-tui --theme midnight

# Atau via subcommand (sama aja)
fc-play server --open
fc-play admin
fc-play tui --theme emerald
fc-play status
fc-play version
```

---

## 🔌 Supported Providers (20+)

| Provider | Type | Key Env Var |
|----------|------|-------------|
| **Anthropic** | ☁️ Direct API | `ANTHROPIC_API_KEY` |
| **OpenAI** | ☁️ Direct API | `OPENAI_API_KEY` |
| **OpenRouter** | 🌐 Multi-model | `OPENROUTER_API_KEY` |
| **Gemini** | ☁️ Google | `GEMINI_API_KEY` |
| **DeepSeek** | ☁️ Direct API | `DEEPSEEK_API_KEY` |
| **Mistral** | ☁️ Direct API | `MISTRAL_API_KEY` |
| **Codestral** | ☁️ Coding-focused | `CODESTRAL_API_KEY` |
| **Groq** | ☁️ Ultra-fast | `GROQ_API_KEY` |
| **Fireworks** | ☁️ Hosted OSS | `FIREWORKS_API_KEY` |
| **Together** | ☁️ Hosted OSS | `TOGETHER_API_KEY` |
| **NVIDIA NIM** | ☁️ NVIDIA | `NVIDIA_NIM_API_KEY` |
| **Cerebras** | ☁️ Ultra-fast | `CEREBRAS_API_KEY` |
| **Kimi** | ☁️ Moonshot | `KIMI_API_KEY` |
| **Wafer** | ☁️ Anthropic-compat | `WAFER_API_KEY` |
| **OpenCode** | ☁️ Coding | `OPENCODE_API_KEY` |
| **Z.ai** | ☁️ Anthropic-compat | `ZAI_API_KEY` |
| **Ollama** | 🏠 Local | `OLLAMA_BASE_URL` |
| **LM Studio** | 🏠 Local | `LMSTUDIO_BASE_URL` |
| **llama.cpp** | 🏠 Local | `LLAMACPP_BASE_URL` |

---

## ⚙️ Configuration

Edit `~/.fc-play/.env` or use the admin console:

```env
# Your API keys
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
OPENROUTER_API_KEY=sk-or-...

# Model routing (provider/model-name)
MODEL=custom/claude-sonnet-4-20250514
MODEL_OPUS=custom/claude-opus-4-20250514

# Server
PORT=3010
HOST=0.0.0.0
```

---

## 🎨 Themes

```bash
fc-play-tui --theme midnight   # indigo + dark
fc-play-tui --theme emerald    # green + dark
fc-play-tui --theme ruby       # crimson + dark
```

---

## 🏗️ Project Structure

```
fc-play/
├── server.py                     # ASGI entry point
├── fc_play/
│   ├── api/                      # FastAPI routes + admin console
│   │   └── admin_static/         # 🎨 Warm amber admin UI
│   ├── cli/                      # Typer command interface
│   ├── config/                   # Pydantic settings, 20+ provider keys
│   ├── tui/                      # 🎨 Rich terminal dashboard
│   ├── core/                     # Protocol handlers
│   └── providers/                # Provider transports
├── scripts/                      # Install/uninstall/CI
├── tests/
└── smoke/
```

---

## 🛠️ Development

```bash
git clone https://github.com/XunowID/fc-play.git
cd fc-play
uv sync
uv run ruff format .
uv run ruff check --fix .
uv run pytest -v
```

---

## 👥 Authors

- **XunowID** — Project lead
- **zahrinurrasyiid** — Contributor

---

## 📄 License

MIT — do what you want, just don't blame us.

---

*⬡ FC-Play — Multi-provider model gateway. Fast. Flexible. Fabulous.*
