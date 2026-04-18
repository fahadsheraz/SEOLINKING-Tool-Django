document.addEventListener("DOMContentLoaded", function () {
    const copyButtons = document.querySelectorAll(".copy-button");
    copyButtons.forEach((button) => {
        button.addEventListener("click", async () => {
            const text = button.dataset.copy;
            try {
                await navigator.clipboard.writeText(text);
                button.textContent = "Copied!";
                setTimeout(() => {
                    button.textContent = "Copy Suggestion";
                }, 1600);
            } catch (error) {
                console.error(error);
                button.textContent = "Copy failed";
            }
        });
    });

    const exportButton = document.getElementById("export-button");
    if (exportButton) {
        exportButton.addEventListener("click", () => {
            const exportText = exportButton.dataset.exportText;
            const blob = new Blob([exportText], { type: "text/plain;charset=utf-8" });
            const link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = "internal-linking-suggestions.txt";
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
    }
});
