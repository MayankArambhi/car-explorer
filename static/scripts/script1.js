async function fetch_car(car_id) {
    const det = await fetch(`/car-details/${car_id}`);
    const data = await det.json();
    const box = document.getElementById("details");
    box.innerHTML = `
        ${data.brand} ${data.name}<br>
        ${data.body_type}<br>
        Price: ${data.price}<br>
        Launch year: ${data.launch_date}<br>
        Safety rating: ${data.safety} Stars<br>
        Sales: ${data.sales}<br>
        `;
}