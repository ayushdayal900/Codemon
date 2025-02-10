// points_update.js
let userInfo = {};

window.fetchAndUpdateUserPoints = function(score) {
    fetch("http://127.0.0.1:5000/get_users", { credentials: "include" })
        .then(response => response.json())
        .then(data => {
            console.log("Fetched data:", data);  // Log full response

            if (!data || data.error) {
                throw new Error(data.error || "User not authenticated");
            }

            // If data is an array, use the first element; otherwise, use data directly.
            userInfo = Array.isArray(data) ? data[0] : data;
            console.log("User Info:", userInfo);

            if (!userInfo || !userInfo.username) {
                throw new Error("Username not found in response.");
            }

            if (!("points" in userInfo) || typeof userInfo.points !== "number") {
                throw new Error(`Invalid points data received: ${JSON.stringify(userInfo)}`);
            }

            // Update the points by adding the score passed as a parameter.
            const newPoints = userInfo.points + score;
            console.log(`Updating ${userInfo.username} points to:`, newPoints);

            const requestBody = JSON.stringify({ points: newPoints });
            console.log("Request Payload:", requestBody);

            return fetch(`http://127.0.0.1:5000/users/${userInfo.username}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: requestBody
            });
        })
        .then(response => {
            console.log("Response Status:", response.status);
            return response.json().then(data => ({ data, response }));
        })
        .then(({ data, response }) => {
            if (!response.ok) {
                throw new Error(`Failed to update points: ${data.error || response.statusText}`);
            }
            console.log("Updated User Points:", data);
        })
        .catch(error => console.error("Error:", error));
};
