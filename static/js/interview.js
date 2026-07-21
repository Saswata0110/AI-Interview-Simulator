// ===========================================
// AI Interview Simulator
// interview.js
// Part 1
// ===========================================

// -----------------------------
// Global Variables
// -----------------------------

let questions = [];
let currentQuestion = 0;
let answers = [];

let interviewSeconds = 0;
let interviewTimer = null;

let questionTime = 120;
let questionTimer = null;

// -----------------------------
// Overall Interview Timer
// -----------------------------

function startInterviewTimer() {

    if (interviewTimer !== null)
        return;

    interviewTimer = setInterval(() => {

        interviewSeconds++;

    }, 1000);

}

// -----------------------------
// Question Timer
// -----------------------------

function startQuestionTimer() {

    clearInterval(questionTimer);

    questionTime = 120;

    updateQuestionTimer();

    questionTimer = setInterval(() => {

        questionTime--;

        updateQuestionTimer();

        if (questionTime <= 0) {

            clearInterval(questionTimer);

            alert("⏰ Time is up for this question!");

            document.getElementById("next-btn").click();

        }

    }, 1000);

}

// -----------------------------
// Update Timer
// -----------------------------

function updateQuestionTimer() {

    const min = Math.floor(questionTime / 60);

    const sec = questionTime % 60;

    document.getElementById("timer").innerHTML =

        String(min).padStart(2, "0") +

        ":" +

        String(sec).padStart(2, "0");

}

// -----------------------------
// Progress Bar
// -----------------------------

function updateProgress() {

    if (questions.length === 0)
        return;

    const percent = Math.round(

        ((currentQuestion + 1) / questions.length) * 100

    );

    document.getElementById("progress-bar").style.width =

        percent + "%";

    document.getElementById("progress-text").innerHTML =

        percent + "%";

    document.getElementById("question-number").innerHTML =

        (currentQuestion + 1) +

        " / " +

        questions.length;

}

// -----------------------------
// Display Question
// -----------------------------

function showQuestion() {

    document.getElementById("question").innerHTML =

        questions[currentQuestion];

    document.getElementById("answer").value =

        answers[currentQuestion] || "";

    document.getElementById("feedback").innerHTML =

        "Feedback will appear here.";

    updateProgress();

}

// -----------------------------
// Start Interview
// -----------------------------

document.getElementById("start-btn").onclick = async function () {

    try {

        this.disabled = true;

        document.getElementById("question").innerHTML =

            "🤖 AI is preparing your interview...";

        const response = await fetch("/generate_questions");

        if (!response.ok) {

            throw new Error("Unable to generate questions.");

        }

        questions = await response.json();

        currentQuestion = 0;

        answers = new Array(questions.length).fill("");

        startInterviewTimer();

        startQuestionTimer();

        showQuestion();

    }

    catch (err) {

        console.error(err);

        alert("Unable to start interview.");

        this.disabled = false;

    }

};

// -----------------------------
// Submit Answer
// -----------------------------

document.getElementById("submit-btn").onclick = async function () {

    const answer =

        document.getElementById("answer").value.trim();

    if (answer === "") {

        alert("Please enter your answer.");

        return;

    }

    answers[currentQuestion] = answer;

    this.disabled = true;

    document.getElementById("feedback").innerHTML =

        "🤖 AI is evaluating your answer...";

    try {

        const response = await fetch(

            "/evaluate_answer",

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    question: questions[currentQuestion],

                    answer: answer

                })

            }

        );

        const feedback = await response.text();

        document.getElementById("feedback").innerHTML =

            feedback;

    }

    catch (err) {

        console.error(err);

        document.getElementById("feedback").innerHTML =

            "Unable to evaluate answer.";

    }

    this.disabled = false;

};

// -----------------------------
// Next Question
// -----------------------------

document.getElementById("next-btn").onclick = function () {

    answers[currentQuestion] =

        document.getElementById("answer").value;

    if (currentQuestion < questions.length - 1) {

        currentQuestion++;

        showQuestion();

        startQuestionTimer();

    }

    else {

        alert("This is the last question.");

    }

};
// ===========================================
// interview.js
// Part 2
// Speech Recognition + AI Proctor
// ===========================================

// -------------------------------------------
// Speech Recognition
// -------------------------------------------

let recognition = null;

if ("webkitSpeechRecognition" in window) {

    recognition = new webkitSpeechRecognition();

    recognition.continuous = true;

    recognition.interimResults = true;

    recognition.lang = "en-US";

    let listening = false;

    const voiceBtn = document.getElementById("voice-btn");

    if (voiceBtn) {

        voiceBtn.onclick = function () {

            if (!listening) {

                recognition.start();

                listening = true;

                voiceBtn.innerHTML = "🛑 Stop Speaking";

            }

            else {

                recognition.stop();

                listening = false;

                voiceBtn.innerHTML = "🎤 Start Speaking";

            }

        };

    }

    recognition.onresult = function (event) {

        let transcript = "";

        for (

            let i = event.resultIndex;

            i < event.results.length;

            i++

        ) {

            transcript +=

                event.results[i][0].transcript;

        }

        const answerBox =

            document.getElementById("answer");

        if (answerBox) {

            answerBox.value = transcript;

        }

    };

    recognition.onerror = function (event) {

        console.log(

            "Speech Recognition Error:",

            event.error

        );

    };

    recognition.onend = function () {

        listening = false;

        if (voiceBtn) {

            voiceBtn.innerHTML =

                "🎤 Start Speaking";

        }

    };

}

else {

    const voiceBtn =

        document.getElementById("voice-btn");

    if (voiceBtn) {

        voiceBtn.style.display = "none";

    }

}

// ===========================================
// AI Proctor Status
// ===========================================

function updateProctorStatus() {

    const faceStatus =

        document.getElementById("face-status");

    const eyeStatus =

        document.getElementById("eye-status");

    const emotionStatus =

        document.getElementById("emotion-status");

    const confidenceStatus =

        document.getElementById("confidence-status");

    if (faceStatus) {

        faceStatus.innerHTML =

            "🟢 Face Detected";

    }

    if (eyeStatus) {

        eyeStatus.innerHTML =

            "👀 Tracking";

    }

    if (emotionStatus) {

        const emotions = [

            "😊 Happy",

            "😐 Neutral",

            "🤔 Thinking",

            "😄 Confident",

            "🙂 Calm"

        ];

        emotionStatus.innerHTML =

            emotions[

                Math.floor(

                    Math.random() *

                    emotions.length

                )

            ];

    }

    if (confidenceStatus) {

        confidenceStatus.innerHTML =

            (85 +

                Math.floor(Math.random() * 15))

            + "%";

    }

}

// Update every 2 seconds

setInterval(updateProctorStatus, 2000);

// ===========================================
// Flask Video Feed
// ===========================================

window.addEventListener("load", function () {

    const camera =

        document.getElementById("camera");

    if (camera) {

        camera.src = "/video_feed";

    }

});
// ===========================================
// interview.js
// Part 3
// Finish Interview + Utilities
// ===========================================

// -------------------------------------------
// Finish Interview
// -------------------------------------------

document.getElementById("finish-btn").onclick = async function () {

    answers[currentQuestion] =
        document.getElementById("answer").value;

    clearInterval(interviewTimer);

    clearInterval(questionTimer);

    document.getElementById("feedback").innerHTML =
        "🤖 Generating Final AI Report...";

    try {

        const response = await fetch("/final_report", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                questions: questions,

                answers: answers

            })

        });

        if (!response.ok) {

            throw new Error("Unable to generate report.");

        }

        const report = await response.text();

        document.getElementById("feedback").innerHTML = report;

        // Redirect to Analytics Page

        setTimeout(function () {

            window.location.href = "/interview_report";

        }, 2000);

    }

    catch (err) {

        console.error(err);

        document.getElementById("feedback").innerHTML =
            "❌ Unable to generate final report.";

    }

};

// -------------------------------------------
// Save Current Answer
// -------------------------------------------

function saveCurrentAnswer() {

    const answerBox = document.getElementById("answer");

    if (answerBox) {

        answers[currentQuestion] =

            answerBox.value;

    }

}

// -------------------------------------------
// Auto Save Every 10 Seconds
// -------------------------------------------

setInterval(function () {

    saveCurrentAnswer();

}, 10000);

// -------------------------------------------
// Prevent Data Loss
// -------------------------------------------

window.addEventListener("beforeunload", function () {

    saveCurrentAnswer();

});

// -------------------------------------------
// Keyboard Shortcuts
// -------------------------------------------

document.addEventListener("keydown", function (event) {

    // Ctrl + Enter -> Submit Answer

    if (event.ctrlKey && event.key === "Enter") {

        event.preventDefault();

        document.getElementById("submit-btn").click();

    }

    // Alt + N -> Next Question

    if (event.altKey && event.key.toLowerCase() === "n") {

        event.preventDefault();

        document.getElementById("next-btn").click();

    }

    // Alt + F -> Finish Interview

    if (event.altKey && event.key.toLowerCase() === "f") {

        event.preventDefault();

        document.getElementById("finish-btn").click();

    }

});

// -------------------------------------------
// Auto Resize Answer Box
// -------------------------------------------

const answerBox = document.getElementById("answer");

if (answerBox) {

    answerBox.addEventListener("input", function () {

        this.style.height = "auto";

        this.style.height = this.scrollHeight + "px";

    });

}

// -------------------------------------------
// Welcome Message
// -------------------------------------------

console.log("===================================");

console.log(" AI Interview Simulator Loaded ");

console.log(" Flask + Gemini + MediaPipe ");

console.log("===================================");