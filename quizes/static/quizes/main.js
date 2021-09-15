console.log('Hello World')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalText = document.getElementById('confirm-text')
const modalList = document.getElementById('modal-list-confirm')
const startBtn = document.getElementById('start-button')

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    const pk = modalBtn.getAttribute('data-pk')
    const name= modalBtn.getAttribute('data-quiz')
    const questions= modalBtn.getAttribute('data-questions')
    const difficulty= modalBtn.getAttribute('data-difficulty')
    const time= modalBtn.getAttribute('data-time')
    const ScorePass= modalBtn.getAttribute('data-pass')

    modalText.innerHTML=`
        ¿Estás seguro que quieres realizar el quiz <b>${name}</b>?
    `
    modalList.innerHTML=`
        <li><b>Dificultad: </b> ${difficulty}</li>
        <li><b>Cantidad de preguntas: </b> ${questions}</li>
        <li><b>tiempo: </b> ${time} min</li>
        <li><b>Puntaje para pasar: </b> ${ScorePass}%</li>
    `

    startBtn.addEventListener('click', ()=>{
        startBtn.setAttribute('href',pk)
    })
}))