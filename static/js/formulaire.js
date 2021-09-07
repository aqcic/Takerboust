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

