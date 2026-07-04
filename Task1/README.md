# 🤖 Task 1 — Rule-Based Chatbot

**Internship Program** | DecodeLab  
**Language** : Python

---

## 📌 Overview

As part of my internship at **DecodeLab**, Task 1 involved building the foundational skeleton of a chatbot that uses a rule-based approach to understand and respond to user inputs — entirely from scratch, without any external libraries or AI models.

The core idea is simple: map user inputs to predefined responses using a Python dictionary. If the input is recognized, the bot replies with the mapped response. If not, it falls back gracefully with `"I don't know!"`.

---

## 🗂️ Project Structure

```
Task1/
├── task1.py        # Main chatbot script
└── README.md       # Project documentation
```

---

## ⚙️ How It Works

```python
reply = responses.get(user_input, "I don't know!")
```

1. User types a message → input is lowercased and stripped
2. Bot looks up the input in the `responses` dictionary
3. Match found → returns mapped response
4. No match → returns fallback message
5. Typing `bye`, `quit`, or `q` exits the chat

---

## 💬 Sample Interactions

| User Input       | Bot Response                                      |
|------------------|---------------------------------------------------|
| `hello`          | Hi there!                                         |
| `how are you`    | I'm just code, but I'm running fine!              |
| `tell me a joke` | Why don't programmers like nature? Too many bugs! |
| `who are you`    | I'm a rule-based chatbot built for Project 1.     |
| `decode labs`    | DecodeLabs is powering this training project.     |
| `bye` / `quit`   | GoodBye 👋                                        |

---

## 🧠 Why Rule-Based? — Solving the Hallucination Problem

Modern AI/LLM chatbots (GPT, Gemini, etc.) suffer from **hallucination** — confidently generating responses that are factually wrong or completely made up. This is a critical problem in real-world deployments.

| Factor                 | Rule-Based Chatbot ✅        | AI/LLM Chatbot ❌             |
|------------------------|------------------------------|-------------------------------|
| Response accuracy      | 100% controlled & verified   | Can hallucinate                |
| Predictability         | Always same output per input | Non-deterministic              |
| Transparency           | Fully auditable logic        | Black-box model                |
| External dependency    | None — runs fully offline    | Requires API / GPU             |
| Production safety      | Zero unexpected output       | Needs heavy guardrails         |

> **Key Insight:** A rule-based bot can *only* say what you explicitly define. Zero chance of invented answers — making it the most reliable choice when accuracy is non-negotiable.

---

## 🚀 How to Run

```bash
python task1.py
```

---

## 📚 Key Learnings

- Built a working chatbot from scratch using pure Python
- Understood intent matching via dictionary-based lookup
- Explored why hallucination is a critical flaw in generative AI
- Learned how deterministic systems provide full control over bot behavior

---

## 👨💻 Intern Details

- **Company** : DecodeLab
- **Task** : Task 1 — Rule-Based Chatbot
- **Tech Stack** : Python (No external libraries)

---


