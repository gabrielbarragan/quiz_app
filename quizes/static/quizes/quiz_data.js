
const url = window.location.href

const quizForm = document.getElementById('quiz-form')
const quiz_name=  document.getElementById('quiz-form').name
const n_questions=  quizForm.getAttribute('data-n_of_questions')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const elements = [...document.getElementsByTagName('input')]
const noBtn = document.getElementById('no-button')

// modal elements
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalTitle = document.getElementById('modaltitle')
const modalText = document.getElementById('confirm-text')
const modalList = document.getElementById('modal-list-confirm')
const startBtn = document.getElementById('start-button')


const sendData = () => {
    const data = {}
    
    data['csrfmiddlewaretoken']= csrf[0].value

    for (i=0;i<elements.length;i++) {

        if(elements[i].checked == true) {
          data[elements[i].name]=parseInt(elements[i].value)
        }

        else {
            if (!data[elements[i].name]) {
                data[elements[i].name] = null
            }
        }

      }
    data['quiz_name'] = quiz_name
    data['n_question'] = n_questions
    console.log(data)
    modalTitle.innerText= data['quiz_name']


    $.ajax({
        type:'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            const results= response.results
            const score = response.score
            const result_list=[]
            const show_results = results.map((result)=>{
                for (const [question, answer] of Object.entries(result)){
                    console.log(answer)
                    if (answer.answered===answer.correct_answer){
                        result_list.push(`<li class="list-group-item list-group-item-success"><b>Pregunta:</b> ${question} <br><b>Respuesta:</b> ${answer.answered} </li>
                        `)
                    }
                    else{
                        if (answer.answered !== answer.correct_answer){
                            result_list.push(`<li class="list-group-item list-group-item-danger"><b>Pregunta:</b> ${question} <br><b>Respuesta:</b> ${answer.answered} </li>
                            `)
                        }
                    }

                }

                return console.log(result)
            })
            score_html=`<b>Puntaje:</b> ${score} </li>`
            modalList.innerHTML=result_list.join(' ')
            modalList.innerHTML = modalList.innerHTML+score_html
        },
        error: function(error){
            console.log(error)
        }
    
    })
    startBtn.addEventListener('click', ()=>{
        startBtn.setAttribute('href',`..`)
    })

}




quizForm.addEventListener('submit', e=> {
    e.preventDefault()
    sendData()
})