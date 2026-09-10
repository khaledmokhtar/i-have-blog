# Proprietary Knowledge Base Guide

The **Proprietary Knowledge Layer** is what transforms `i-have-blog` from a generic summarizer of top Google results into an authoritative, differentiated editorial voice.

---

## Directory Structure

```
knowledge/
├── brand.json               # Brand voice, reading level, forbidden buzzwords
├── audience.json            # Target personas, acute pain points, domain vocabulary
├── expertise/               # Deep domain playbooks and contrarian insights
│   ├── media_buying.md
│   ├── ecommerce_cod.md
│   └── ai_automation.md
└── frameworks/              # Exact calculations, sensitivity tables, matrices
    └── profitability_matrix.md
```

---

## 1. Customizing Brand Voice (`brand.json`)

Configure your editorial personality and banned terms:

```json
{
  "brand_name": "Your Brand Name",
  "voice_attributes": {
    "direct": true,
    "analytical": true,
    "practical": true,
    "contrarian": true,
    "generic_motivational": false
  },
  "forbidden_buzzwords": [
    "game-changer",
    "paradigm shift",
    "in today's world",
    "marketing magic"
  ],
  "preferred_terminology": [
    "Contribution Margin",
    "Blended CAC",
    "Net Cash Velocity"
  ]
}
```

---

## 2. Adding Domain Expertise Documents (`knowledge/expertise/*.md`)

Create focused markdown files documenting your real-world experience, client teardowns, and operational math. The system queries these files during the **Strategy** and **Writing** stages to inject:
- Contrarian observations that disprove surface-level blog advice.
- Real-world failure points that competitors omit.
- Actual mathematical trade-offs and formulas.
