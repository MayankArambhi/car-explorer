async function add_wishlist(car_id){
    response = await fetch(`/atw/${car_id}`);
        if(response.text()==="0"){
            alert("Car already exist in wishlist");
            return;
        }
    const btn = document.getElementById(`wl-${car_id}`);
    btn.setAttribute("onclick", `rem_wishlist(${car_id})`);
    btn.innerHTML = "- Wishlist";
}

async function rem_wishlist(car_id){
    response = await fetch(`/rfw/${car_id}`);
    if(response.text()==="0"){
        alert("Car doesn't exist in your wishlist");
        return;
    }
    const btn = document.getElementById(`wl-${car_id}`);
    btn.setAttribute("onclick", `add_wishlist(${car_id})`);
    btn.innerHTML = "+ Wishlist";
}