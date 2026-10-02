// AUTHENTICATION PAGE

const div = document.getElementById("auth");
const h_title = document.querySelector("title");
const title = document.getElementById("title");

async function login() {
    const response = await fetch("/login-page");
    const html = await response.text();
    h_title.innerHTML = await "Login";
    title.innerHTML = await "Login to use Car Explorer";
    div.innerHTML = await html;
}

async function signup() {
    const response = await fetch("/signup-page");
    const html = await response.text();
    h_title.innerHTML = await "Sign up";
    title.innerHTML = await "Sign up to use Car Explorer";
    div.innerHTML = await html;
}