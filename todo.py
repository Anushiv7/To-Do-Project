import streamlit as st

# Initialize session state lists
if "tasks" not in st.session_state:
    st.session_state.tasks = []
if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = []

st.sidebar.title("To-Do List")

# Sidebar Form to add new tasks
with st.sidebar.form(key="add_task_form", clear_on_submit=True):
    new_task = st.text_input("Add a task")
    submit_button = st.form_submit_button("Add Task")
    
    if submit_button and new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        st.rerun()

st.title("My To-Do List")

# --- ACTIVE TASKS SECTION ---
st.subheader("📌 Pending Tasks")

if st.session_state.tasks:
    for idx, task in enumerate(st.session_state.tasks):
        # Key forces uniqueness; default value is False (unchecked)
        is_done = st.checkbox(task, value=False, key=f"active_{idx}_{task}")
        if is_done:
            st.session_state.tasks.remove(task)
            st.session_state.completed_tasks.append(task)
            st.rerun()
else:
    st.info("No pending tasks! Add one from the sidebar.")

st.divider()

# --- COMPLETED TASKS SECTION ---
st.subheader("✅ Completed Tasks")

if st.session_state.completed_tasks:
    for idx, task in enumerate(st.session_state.completed_tasks):
        # Render with strike-through text and default value True (checked)
        is_still_done = st.checkbox(f"~~{task}~~", value=True, key=f"completed_{idx}_{task}")
        if not is_still_done:
            st.session_state.completed_tasks.remove(task)
            st.session_state.tasks.append(task)
            st.rerun()
            
    if st.button("Clear Completed Tasks"):
        st.session_state.completed_tasks.clear()
        st.rerun()
else:
    st.caption("No completed tasks yet.")