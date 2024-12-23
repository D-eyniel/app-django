import { TaskService } from '../../static/js/TaskService.js';
import { TaskView } from '../../static/js/TaskView.js';

document.addEventListener('DOMContentLoaded', () => {
    const taskService = new TaskService();
    const taskView = new TaskView(taskService);
    taskView.renderTasks();
});