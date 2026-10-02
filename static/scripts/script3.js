// AUTHENTICATION PAGE

const wrapper = document.getElementById("wrapper");
const div = document.getElementById("auth");
const h_title = document.querySelector("title");
const title = document.getElementById("title");

async function login() {
    wrapper.style.opacity = 0.5;
    const elem = document.querySelectorAll("input, button");
    elem.forEach(element => {
        element.disabled = true;
    });
    const response = await fetch("/login-page");
    const html = await response.text();
    h_title.innerHTML = await "Login";
    title.innerHTML = await "Login to use Car Explorer";
    div.innerHTML = await html;
    wrapper.style.opacity = 1;
}

async function signup() {
    wrapper.style.opacity = 0.5;
    const elem = document.querySelectorAll("input, button");
    elem.forEach(element => {
        element.disabled = true;
    });
    const response = await fetch("/signup-page");
    const html = await response.text();
    h_title.innerHTML = await "Sign up";
    title.innerHTML = await "Sign up to use Car Explorer";
    div.innerHTML = await html;
    wrapper.style.opacity = 1;
}