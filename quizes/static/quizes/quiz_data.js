
const url = window.location.href

const quizForm = document.getElementById('quiz-form')
const quiz_name=  document.getElementById('quiz-form').name
const n_questions=  quizForm.getAttribute('data-n_of_questions')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const elements = [...document.getElementsByTagName('input')]


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

    $.ajax({
        type:'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            console.log(response)
        },
        error: function(error){
            console.log(error)
        }
    
    })
}



quizForm.addEventListener('submit', e=> {
    e.preventDefault()
    sendData()
})