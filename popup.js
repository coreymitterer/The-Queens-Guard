document.getElementById("submit").addEventListener("click", function () {
    let count = document.getElementById("count").value;

    if (!count || isNaN(count) || count <= 0) {
        alert("Please enter a valid number!");
        return;
    }

    //alert("Checking " + count + " emails...");

    // Call Python script with count
    const { spawn } = require("child_process");
    const pythonProcess = spawn("python", ["email_checker.py", count]);

    pythonProcess.stdout.on("data", (data) => {
        alert(`Output: ${data.toString()}`);
    });

    pythonProcess.stderr.on("data", (data) => {
        alert(`Error: ${data.toString()}`);
    });

    pythonProcess.on("close", (code) => {
        alert(`Python script exited with code ${code}`);
    });
});
