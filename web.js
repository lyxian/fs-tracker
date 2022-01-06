function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

document.querySelectorAll('a.button')[1].remove()

for (let i = 0; i < 50; i++) {
    document.querySelector('a.button').click()
    await sleep(1500);
}