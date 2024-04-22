document.addEventListener('DOMContentLoaded', function () {
    loadTasks();
});

function loadTasks() {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    const taskList = document.getElementById('taskList');

    taskList.innerHTML = '';

    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.classList.add('task-item');
        if (task.completed) {
          li.classList.add('completed-task')
        }

        const taskCheckbox = document.createElement('input');
        taskCheckbox.type = 'checkbox';
        taskCheckbox.checked = task.completed;
        taskCheckbox.addEventListener('change', () => {
            toggleTaskStatus(index);
        });

        const taskInput = document.createElement('input');
        taskInput.type = 'text';
        taskInput.value = task.title;
        taskInput.disabled = true;

        const editButton = document.createElement('button');
        editButton.textContent = taskInput.disabled ? 'Edit' : 'Save';
        editButton.addEventListener('click', () => {
            if (taskInput.disabled) {
                taskInput.disabled = false;
                editButton.textContent = 'Save';
            } else {
                taskInput.disabled = true;
                editButton.textContent = 'Edit';
                updateTask(index, taskInput.value);
            }
        });

        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.addEventListener('click', () => {
            removeTask(index);
        });

        const creationDateSpan = document.createElement('span');
        creationDateSpan.textContent = `Created on: ${task.creationDate}`;

        li.appendChild(taskCheckbox);
        li.appendChild(taskInput);
        li.appendChild(editButton);
        li.appendChild(removeButton);
        li.appendChild(creationDateSpan);

        taskList.appendChild(li);
    });
}

function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskTitle = taskInput.value.trim();
    if (taskTitle !== '') {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        const currentDate = new Date().toISOString().split('T')[0];
        tasks.push({
            title: taskTitle,
            completed: false,
            creationDate: currentDate
        });
        localStorage.setItem('tasks', JSON.stringify(tasks));
        taskInput.value = '';
        loadTasks();
    }
}

function removeTask(index) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.splice(index, 1);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    loadTasks();
}

function toggleTaskStatus(index) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks[index].completed = !tasks[index].completed;
    localStorage.setItem('tasks', JSON.stringify(tasks));
    loadTasks();
}

function updateTask(index, newTitle) {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks[index].title = newTitle;
    localStorage.setItem('tasks', JSON.stringify(tasks));
    loadTasks();
}