document.addEventListener('DOMContentLoaded', () => {
    // Fetch task data from the server
    fetch('/task-overview/')
        .then(response => response.json())
        .then(data => {
            console.log(data); // Log data for debugging

            // Extract counts from the fetched data
            const pendingCount = data.pending;
            const inProgressCount = data.inProgress;
            const completedCount = data.completed;

            // Display counts in the HTML
            document.getElementById('pending-count').textContent = pendingCount;
            document.getElementById('in-progress-count').textContent = inProgressCount;
            document.getElementById('completed-count').textContent = completedCount;

            // Calculate total tasks for progress bar percentage calculations
            const totalTasks = pendingCount + inProgressCount + completedCount;

            // Update progress bars if total tasks are greater than 0
            if (totalTasks > 0) {
                updateProgressBar('pending-fill', pendingCount, totalTasks, 'pending-tasks');
                updateProgressBar('in-progress-fill', inProgressCount, totalTasks, 'in-progress-tasks');
                updateProgressBar('completed-fill', completedCount, totalTasks, 'completed-tasks');
            }
        })
        .catch(error => {
            console.error('Error fetching task data:', error);
        });

    // Function to update the width of the progress bar
    function updateProgressBar(fillElementId, count, total, summaryElementId) {
        const percentage = (count / total) * 100;
        const progressBar = document.getElementById(fillElementId);
        const summaryElement = document.getElementById(summaryElementId);

        if (progressBar) {
            progressBar.style.width = `${percentage}%`;
            progressBar.textContent = `${count} / ${total}`; // Display count inside the bar

            // Update the summary element with additional styling if desired
            summaryElement.style.color = percentage > 50 ? 'green' : 'red'; // Change color based on count
        }
    }
});
