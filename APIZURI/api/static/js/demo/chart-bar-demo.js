
  var nombres = document.getElementById('myBarChart').getAttribute('data-api').split(',').filter(Boolean);
  var conteos = document.getElementById('myBarChart').getAttribute('data-conteo').split(',').filter(Boolean);

  // Asegúrate de que los conteos sean números
  conteos = conteos.map(Number);

  var ctx = document.getElementById("myBarChart");
  var myBarChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: nombres,
          datasets: [{
              label: "Preferencias de Entrega",
              backgroundColor: "rgba(78, 115, 223, 0.05)",
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

