document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("scanForm");
    const textArea = document.getElementById("text");
    const result = document.getElementById("result");

    form.addEventListener("submit", function (event) {

        event.preventDefault();

        const message = textArea.value.trim().toLowerCase();

        if (message === "") {
            result.innerHTML = "<p style='color:red;'>Please enter a transaction or communication.</p>";
            return;
        }

        const suspiciousWords = [
            "fraud",
            "bribe",
            "money laundering",
            "illegal",
            "black money",
            "fake invoice",
            "kickback"
        ];

        let detected = false;
        let keyword = "";

        for (let i = 0; i < suspiciousWords.length; i++) {

            if (message.includes(suspiciousWords[i])) {
                detected = true;
                keyword = suspiciousWords[i];
                break;
            }

        }

        if (detected) {

            result.innerHTML = `
                <h2 style="color:red;">⚠ Compliance Alert</h2>
                <p><strong>Risk Level:</strong> High</p>
                <p><strong>Detected Keyword:</strong> ${keyword}</p>
                <p>Status: Suspicious Communication</p>
            `;

        } else {

            result.innerHTML = `
                <h2 style="color:green;">✅ Safe Communication</h2>
                <p>No compliance violations detected.</p>
            `;

        }

    });

});
