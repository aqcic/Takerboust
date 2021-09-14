var ctx = document.getElementById('myBar');
var myBar = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['ST', 'SM', 'MI', 'GAT', 'Français', 'Anglais', 'Arabe', 'Tamaziɣt', 'Droit'],
        datasets: [{
            label: 'Licence 1',
            data: [50, 5, 13, 3, 20, 3, 4, 25, 5],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'red'
            ],
            borderWidth: 3
        },
        {
            label: 'Licence 2',
            data: [46, 4, 15, 5, 15, 2, 6, 20, 12],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)' 
            ],
            borderColor: [
                'black'
            ],
            borderWidth: 3
        },
        {
            label: 'Licence 3',
            data: [55, 6, 4, 3, 13, 6, 4, 30, 11],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)' 
            ],
            borderColor: [
                '#3498db'
            ],
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


/*Http requests for charts data

fetch("/api/", {
    method: 'GET',
    headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    },
})
.then((res) => res.json())
.then((data) => {})

*/