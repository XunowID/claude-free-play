"""FC-Play constants — providers, model lists, branding."""

from __future__ import annotations

# Branding (no AI/Claude mentions in UI-facing names)
APP_NAME = "fc-play"
APP_DISPLAY = "FC-Play"
APP_TAGLINE = "Multi-provider model gateway. Fast. Flexible. Fabulous."
APP_DESCRIPTION = "Proxy gateway for 20+ model providers — route, manage, and monitor."

# HTTP
HTTP_READ_TIMEOUT = 120
HTTP_WRITE_TIMEOUT = 10
HTTP_CONNECT_TIMEOUT = 30

# ─── All supported providers ────────────────────────────────────────────────
# Format: slug → display name
PROVIDERS = {
    "custom": "Direct API",
    "anthropic": "Anthropic",
    "openai": "OpenAI",
    "openrouter": "OpenRouter",
    "gemini": "Gemini",
    "deepseek": "DeepSeek",
    "mistral": "Mistral",
    "codestral": "Codestral",
    "groq": "Groq",
    "fireworks": "Fireworks",
    "together": "Together",
    "nvidia_nim": "NVIDIA NIM",
    "cerebras": "Cerebras",
    "kimi": "Kimi",
    "wafer": "Wafer",
    "opencode": "OpenCode",
    "zai": "Z.ai",
    "ollama": "Ollama",
    "lmstudio": "LM Studio",
    "llamacpp": "llama.cpp",
}

# Provider prefixes for model routing
PROVIDER_PREFIXES = {
    "custom": "Direct API",
    "anthropic": "Anthropic",
    "openai": "OpenAI",
    "openrouter": "OpenRouter",
    "gemini": "Gemini",
    "deepseek": "DeepSeek",
    "mistral": "Mistral",
    "codestral": "Codestral",
    "groq": "Groq",
    "fireworks": "Fireworks",
    "together": "Together",
    "nvidia_nim": "NVIDIA NIM",
    "cerebras": "Cerebras",
    "kimi": "Kimi",
    "wafer": "Wafer",
    "opencode": "OpenCode",
    "opencode_go": "OpenCode Go",
    "zai": "Z.ai",
    "ollama": "Ollama",
    "lmstudio": "LM Studio",
    "llamacpp": "llama.cpp",
}

# ─── Model families ─────────────────────────────────────────────────────────
# Opus-tier (capability tier, not brand-specific)
MODELS_OPUS = [
    "claude-opus-4-20250514",
    "claude-opus-4-20250514-v1",
    "claude-opus-4-8-20250601",
    "claude-opus-4-8",
    "claude-opus-4-7",
    "claude-opus-4-6",
    "claude-opus-4-5",
    "claude-opus-4",
    "claude-opus-3-5",
    "claude-opus-3",
]

# Sonnet-tier
MODELS_SONNET = [
    "claude-sonnet-4-20250514",
    "claude-sonnet-4-20250514-v1",
    "claude-sonnet-4-6",
    "claude-sonnet-4",
    "claude-sonnet-3-5",
    "claude-sonnet-3",
    "claude-3-5-sonnet",
    "claude-3-sonnet",
]

# Haiku-tier
MODELS_HAIKU = [
    "claude-haiku-4-20250514",
    "claude-haiku-4-20250514-v1",
    "claude-haiku-4-5",
    "claude-haiku-4-6",
    "claude-haiku-4",
    "claude-haiku-3-5",
    "claude-haiku-3",
]

MODELS_ALL = MODELS_OPUS + MODELS_SONNET + MODELS_HAIKU
