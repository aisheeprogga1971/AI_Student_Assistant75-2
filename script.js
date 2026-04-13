const API = "http://127.0.0.1:8000";

console.log("JS loaded"); // DEBUG

// ---------------- REGISTER ----------------
async function register() {
    console.log("Register clicked");

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/register`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    const data = await res.json();
    document.getElementById("auth-msg").innerText = data.message || data.detail;
}

// ---------------- LOGIN ----------------
async function login() {
    console.log("Login clicked");

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });

    const data = await res.json();

    if (data.access_token) {
        localStorage.setItem("token", data.access_token);
        document.getElementById("status").innerText = "Logged in as " + username;
        document.getElementById("auth-msg").innerText = "Login successful!";
    } else {
        document.getElementById("auth-msg").innerText = data.detail;
    }
}

// ---------------- LOGOUT ----------------
function logout() {
    console.log("Logout clicked");

    localStorage.removeItem("token");
    document.getElementById("status").innerText = "Using as Guest";
    document.getElementById("auth-msg").innerText = "Logged out";
}

// ---------------- ASK AI ----------------
async function askAI() {
    console.log("Ask clicked");

    const userMessage = document.getElementById("input").value;

    try {
        const res = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: userMessage
            })
        });

        const data = await res.json();
        console.log("Response:", data);

        document.getElementById("output").innerText = data.answer;

    } catch (error) {
        console.error("Fetch error:", error);
    }
}