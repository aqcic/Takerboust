const loadStudentForm = () => {
    let employeCard = document.getElementById("employeCard");
    let studentCard = document.getElementById("studentCard");
    let employeForm = document.getElementById("employeForm");
    let studentForm = document.getElementById("studentForm");
    employeCard.classList.remove("card-active")
    studentCard.classList.add("card-active")
    employeForm.classList.add("hide-form")
    studentForm.classList.remove("hide-form")
}

const loadEmployeForm = () => {
    let employeCard = document.getElementById("employeCard");
    let studentCard = document.getElementById("studentCard");
    let employeForm = document.getElementById("employeForm");
    let studentForm = document.getElementById("studentForm");
    employeCard.classList.add("card-active")
    studentCard.classList.remove("card-active")
    employeForm.classList.remove("hide-form")
    studentForm.classList.add("hide-form")
}

function addEventHandler(elem, eventType, handler) {
    if (elem.addEventListener)
        elem.addEventListener (eventType, handler, false);
    else if (elem.attachEvent)
        elem.attachEvent ('on' + eventType, handler); 
}

addEventHandler(document, 'DOMContentLoaded', function() {
    addEventHandler(document.getElementById('niveau_etude'), 'change', function() {
        fetch("/api/get-formations-by-degree", {
            method: 'POST',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({degree: document.getElementById("niveau_etude").value}),
        })
        .then((res) => res.json())
        .then((data) => {
            specialiteSelect = document.getElementById('specialite');
            specialiteSelect.innerHTML = "";
            data.forEach(element => {
                specialiteSelect.options[specialiteSelect.options.length] = new Option(element, element);
            });
        })
    });
});