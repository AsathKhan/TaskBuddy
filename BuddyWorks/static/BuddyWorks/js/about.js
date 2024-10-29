document.addEventListener("DOMContentLoaded", () => {
    const features = document.querySelectorAll(".feature");

    features.forEach(feature => {
        feature.addEventListener("click", () => {
            const targetId = feature.dataset.toggle;
            const description = document.getElementById(targetId);
            description.classList.toggle("hidden");
        });
    });
});