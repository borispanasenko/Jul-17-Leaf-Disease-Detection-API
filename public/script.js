document.getElementById("analyzeForm").addEventListener(
    "submit", async (e) => {
    e.preventDefault();
    const errorEl = document.getElementById("error");
    const resultEl = document.getElementById("result");
    errorEl.classList.add("hidden");
    resultEl.classList.add("hidden");

    const formData = new FormData();
    formData.append("image", document.getElementById("image").files[0]);

    try {
        const fileInput = document.getElementById("image");
        if (!fileInput.files[0]) {
            errorEl.textContent = "Please select an image file";
            errorEl.classList.remove("hidden");
            return;
        }

        const allowedExtensions = ['jpg', 'jpeg', 'png'];
        const fileExt = fileInput.files[0].name.split('.').pop().toLowerCase();
        if (!allowedExtensions.includes(fileExt)) {
            errorEl.textContent = "Invalid file type (must be .jpg, .jpeg, .png)";
            errorEl.classList.remove("hidden");
            return;
        }

        const response = await fetch("http://localhost:5000/analyze", {
            method: "POST",
            body: formData
        });
        if (!response.ok) {
            const data = await response.json().catch(() => ({}));
            throw new Error(data.error || `HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        document.getElementById("disease").textContent = `Disease: ${data.disease || 'N/A'}`;
        document.getElementById("confidence").textContent = `Confidence: ${(data.confidence * 100).toFixed(2)}%`;
        document.getElementById("description").textContent = `Description: ${data.description || 'No description available'}`;
        document.getElementById("treatment").textContent = `Treatment: ${data.treatment || 'No treatment info available'}`;
        document.getElementById("id").textContent = `Detection ID: ${data.id || 'N/A'}`;

        resultEl.classList.remove("hidden");
    } catch (error) {
        errorEl.textContent = `Error: ${error.message}`;
        errorEl.classList.remove("hidden");
    }
});