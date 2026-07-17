# Voice Hub | AI Agent 語音回答與設定中心

本專案旨在提供同一台電腦上多個 AI Agent 的全域語音助手與輸入清洗（文字正規化）設定指南與配套程式。

## 🌟 專案特點
- **網頁控制台 (Dashboard)**：內置現代感十足、玻璃擬物化 (Glassmorphism) 風格的靜態單頁網頁，提供前端 Web Speech API 的台灣中文語音合成測試 Playground。
- **全域規則與指南**：整理「語音輸入文字正規化 (清洗功能)」與「AI Agent 全域語意與同步規範」的一鍵複製區塊。
- **設定檔放置指南**：詳細列出 Codex, Claude Code, Gemini/AntiGravity, OpenCode 的全域設定檔路徑。
- **Speak 技能實作**：隨附 `speak.py` 用於呼叫 `edge-tts` 與 Windows 系統的背景語音合成與播放。

---

## 🛠️ Speak 技能使用方法
1. **安裝依賴套件**：
   ```bash
   pip install edge-tts
   ```
2. **基本執行**：
   在 terminal 中傳入欲播放的文字：
   ```bash
   python speak.py "你好，歡迎使用語音回答功能。"
   ```
   腳本會自動合成本地語音，並在 Windows 電腦背景隱形播放，完成後自動清除暫存檔。

---

## ⚙️ 全域設定檔路徑對照
- **ChatGPT Codex**: `~/.codex/AGENTS.md`
- **Claude Code**: `~/.claude/CLAUDE.md` 及 `~/.claude/rules/voice-input-normalization.md`
- **Google Antigravity**: `~/.gemini/GEMINI.md`
- **OpenCode**: `~/.config/opencode/opencode.json` (加入相對應路徑到 `instructions` 陣列)
