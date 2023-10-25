var nombres = document.getElementById('myAreaChartPago').getAttribute('data-pago').split(',').filter(Boolean);
var conteos = document.getElementById('myAreaChartPago').getAttribute('data-conteo').split(',').filter(Boolean);

// Asegúrate de que los conteos sean números
conteos = conteos.map(Number);

var ctx = document.getElementById("myAreaChartPago");
var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: nombres,
        datasets: [{
            label: "Preferencias de Pago",
            backgroundColor: "rgba(249,245,27, 0.5)",
            borderColor: "rgba(78, 115, 223, 1)",
            borderWidth: 1,
            data: conteos,
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
    }
});