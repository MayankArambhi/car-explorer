// ASYNCHRONOUS WISHLIST

async function add_wishlist(car_id){
    const response = await fetch(`/atw/${car_id}`);
    const data = await response.text();
    if(data==="0"){
        alert("Car already exist in wishlist");
        return;
    }
    const btn = document.getElementById(`wl-${car_id}`);
    await btn.setAttribute("onclick", `rem_wishlist(${car_id})`);
    btn.innerHTML = await "- Wishlist";
}

async function rem_wishlist(car_id){
    const response = await fetch(`/rfw/${car_id}`);
    const data = await response.text();
    if(data==="0"){
        alert("Car doesn't exist in your wishlist");
        return;
    }
    const btn = document.getElementById(`wl-${car_id}`);
    await btn.setAttribute("onclick", `add_wishlist(${car_id})`);
    btn.innerHTML = await "+ Wishlist";
}