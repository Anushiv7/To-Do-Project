# Streamlit To-Do List Management System

🚀 **Live Demo:** [https://to-do-x.streamlit.app/](https://to-do-x.streamlit.app/)

A dynamic, interactive To-Do List application built using Python and Streamlit[cite: 1]. This application allows users to add tasks, mark items complete with interactive checkboxes, manage pending/completed lists independently, and maintain state across user interactions.

---

## 🚀 Features

* **Task Creation:** Sidebar form input allowing seamless addition of new tasks without unexpected page reruns.
* **Interactive Completion Checkboxes:** Check off active tasks to automatically move them into a dedicated completed section with visual strike-through styling.
* **Bi-directional Toggle:** Unchecking a completed item returns it back to the active pending list.
* **Session State Management:** Built using Streamlit `session_state` to keep track of tasks across user input triggers.
* **Bulk Clearing:** Single-click option to clear all completed tasks at once.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** [Streamlit](https://streamlit.io/)[cite: 1]

---

## 📁 Repository Structure

```text
├── app.py              # Main Streamlit application code
├── requirements.txt    # Project dependencies
└── README.md           # Documentation and setup instructions
