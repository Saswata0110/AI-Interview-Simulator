const sendBtn = document.getElementById("sendBtn");
const messageInput = document.getElementById("message");
const chatBox = document.getElementById("chat-box");

function addUserMessage(message) {

    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}

function addAIMessage(message) {

    chatBox.innerHTML += `
        <div class="ai-message">
            ${message.replace(/\n/g, "<br>")}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {

    const message = messageInput.value.trim();

    if (message === "") return;

    addUserMessage(message);

    messageInput.value = "";

    addAIMessage("⏳ Thinking...");

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        document.querySelector(".ai-message:last-child").remove();

        if (data.success) {

            addAIMessage(data.answer);

        } else {

            addAIMessage(data.message);

        }

    } catch (error) {

        document.querySelector(".ai-message:last-child").remove();

        addAIMessage("Server Error");

    }

}

sendBtn.addEventListener("click", sendMessage);

messageInput.addEventListener("keypress", function(e){

    if(e.key==="Enter"){

        sendMessage();

    }

});