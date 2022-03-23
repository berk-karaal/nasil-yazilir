let questions = []

let users_answers = []

const getJSON = async url => {
    const response = await fetch(url);
    if (!response.ok) // check if response worked (no 404 errors etc...)
        throw new Error(response.statusText);

    const data = response.json(); // get JSON from the response
    return data; // returns a promise, which resolves to this data value
}

let question_index = 0;
let score = 0;
let correct_option = undefined; // 1 or 2 (opt1 or opt2)

let answer_was_given = false;

const quiz_div = document.getElementById("quiz-div");
const quiz_div_color = "#c46b3b";
const quiz_div_wrong_color = "#9e2e2e";
const quiz_div_correct_color = "#3a9434";
const continue_button = document.getElementById("continue-button");
const question_text = document.getElementById("quiestion-text");
const quiz_loading_div = document.getElementById("quiz-loading-div");
let options = [document.getElementById("opt1"), document.getElementById("opt2")]


getJSON("https://nasil-yazilir.herokuapp.com/daily/?format=json").then(data => {
    questions = data["words"];
    quiz_is_ready();
    display_question(0);
}).catch(error => {
    console.error(error);
    fetch_failed();
});

function fetch_failed() {
    quiz_loading_div.style.display = "none";
    quiz_div.style.display = "none";
    document.getElementById("fetch-error-div").style.display = "block";
}

function quiz_is_ready() {
    quiz_loading_div.style.display = "none";
    quiz_div.style.display = "block";
}

function option_clicked(opt_num) {
    if (!answer_was_given) {
        answer_was_given = true;
        if (opt_num == correct_option) {
            quiz_div.style.backgroundColor = quiz_div_correct_color;
            users_answers.push(questions[question_index]["correct_spelling"]);
            score += 1;
        } else {
            users_answers.push(questions[question_index]["wrong_spelling"]);
            quiz_div.style.backgroundColor = quiz_div_wrong_color;
        }
        options[0].style.opacity = options[1].style.opacity = "0.5";
        options[correct_option - 1].style.opacity = "1";
        continue_button.style.visibility = "visible";
    }
}

function display_question(question_num) {

    answer_was_given = false;

    continue_button.style.visibility = "hidden";
    quiz_div.style.backgroundColor = quiz_div_color;
    options[0].style.opacity = options[1].style.opacity = "1";

    let title = document.getElementById("question-title");
    title.innerText = "SORU " + String(question_index + 1) + "/" + questions.length;

    correct_option = Math.round(Math.random()) + 1;
    options[0].innerHTML = options[1].innerHTML = questions[question_num].wrong_spelling;
    options[correct_option - 1].innerHTML = questions[question_num].correct_spelling;
}

function continue_clicked() {
    if (question_index + 1 == questions.length) {
        quiz_ended();
    } else {
        question_index += 1;
        display_question(question_index);
    }
}

function quiz_ended() {
    document.getElementById("quiz-div").style.display = "none";
    document.getElementById("result-div").style.display = "block";

    document.getElementById("result-p").innerText = String(questions.length) + " sorudan " + String(score) + " tanesini doğru yaptın.\n";

    for (let i = 0; i < users_answers.length; i++) {
        add_row_to_results_table(users_answers[i], questions[i]["correct_spelling"], users_answers[i] == questions[i]["correct_spelling"]);
    }

}

function add_row_to_results_table(user_answer, correct_answer, is_succes) {
    let results_table_body = document.getElementById("results_table_body");

    let new_row = results_table_body.insertRow();

    new_row.classList.add(is_succes ? "bg-success" : "bg-danger");

    cel1 = new_row.insertCell();
    cel2 = new_row.insertCell();

    cel1.innerText = user_answer;
    cel2.innerText = correct_answer;
}