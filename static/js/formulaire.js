const loadStudentForm = () => {
    let employeCard = document.getElementById("employeCard");
    let studentCard = document.getElementById("studentCard");
    employeCard.classList.remove("card-active")
    studentCard.classList.add("card-active")
}

const loadEmployeForm = () => {
    let employeCard = document.getElementById("employeCard");
    let studentCard = document.getElementById("studentCard");
    employeCard.classList.add("card-active")
    studentCard.classList.remove("card-active")
}

