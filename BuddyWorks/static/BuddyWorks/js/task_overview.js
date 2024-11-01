document.addEventListener('DOMContentLoaded', () => {
    fetch('/task-overview/')
        .then(response => response.json())
        .then(data => {
            console.log(data);

            const pendingCount = data.pending;
            const inProgressCount = data.inProgress;
            const completedCount = data.completed;

            document.getElementById('pending-count').textContent = pendingCount;
            document.getElementById('in-progress-count').textContent = inProgressCount;
            document.getElementById('completed-count').textContent = completedCount;

            const totalTasks = pendingCount + inProgressCount + completedCount;

            if (totalTasks > 0) {
                updateProgressBar('pending-fill', pendingCount, totalTasks, 'pending-tasks');
                updateProgressBar('in-progress-fill', inProgressCount, totalTasks, 'in-progress-tasks');
                updateProgressBar('completed-fill', completedCount, totalTasks, 'completed-tasks');
            }
        })
        .catch(error => {
            console.error('Error fetching task data:', error);
        });

    function updateProgressBar(fillElementId, count, total, summaryElementId) {
        const percentage = (count / total) * 100;
        const progressBar = document.getElementById(fillElementId);
        const summaryElement = document.getElementById(summaryElementId);

        if (progressBar) {
            progressBar.style.width = `${percentage}%`;
            progressBar.textContent = `${count} / ${total}`; // Display count inside the bar

            summaryElement.style.color = percentage > 50 ? 'green' : 'red'; // Change color based on count
        }
    }
});

