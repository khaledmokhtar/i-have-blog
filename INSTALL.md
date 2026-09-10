# Installation & Setup Guide

`i-have-blog` can be deployed as a **standalone Python CLI**, a **Claude Code plugin**, a **Cursor IDE skill**, a **Codex integration**, or a **Gemini CLI extension**.

---

## 1. Quickstart: Standalone Python CLI

### Requirements
- Python 3.10 or higher
- Git

### Installation
```bash
# Clone repository
git clone https://github.com/khaledmokhtar/i-have-blog.git
cd i-have-blog

# Install in editable mode
pip install -e .
```

### Basic Commands
```bash
# Run full editorial pipeline for a topic
blog-engine run --topic "Facebook Ads ROAS vs MER" --keyword "roas vs mer"

# Calculate content decay and refresh strategy for an existing post
blog-engine refresh --target "https://myblog.com/facebook-ads-guide" --age 18 --traffic-loss 35.0

# Run evaluation benchmark suite
blog-engine evals

# Run blind LLM judge simulation
blog-engine judge
```

---

## 2. Claude Code Integration

To install `i-have-blog` in Anthropic's Claude Code:

```bash
# Option A: From local clone
claude plugin add path/to/i-have-blog/.claude-plugin

# Option B: Add repository directly
claude plugin marketplace add khaledmokhtar/i-have-blog
claude plugin install blog-writer@i-have-blog
```

Once installed, invoke using:
```text
/blog "Write an authoritative guide comparing blended MER to in-platform ROAS"
```

---

## 3. Cursor IDE Setup

Cursor automatically discovers skills located in `.cursor/skills/`.

1. Open this repository or copy `.cursor/skills/blog-writer` to your target project's `.cursor/skills/`.
2. Open Cursor Chat (Cmd+L / Ctrl+L).
3. Type:
   ```text
   Use the blog-writer skill to research and outline an article about E-Commerce Cash on Delivery delivery rates.
   ```

---

## 4. Google Gemini CLI Extension

1. Ensure `gemini-extension.json` and `GEMINI.md` reside in your workspace root.
2. In Gemini CLI, the extension automatically binds editorial constraints to long-form generation requests.

---

## 5. Codex & OpenCode Support

- **Codex**: Place `.codex-plugin/plugin.json` in your Codex configurations.
- **OpenCode**: Point `opencode.json` to `skills/blog-writer`.
