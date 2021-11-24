const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')  
const questionContainerElement = document.getElementById('question-container') 
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons') 
const resultTea = document.getElementById('result')

let mixQuestions, currentQuestionIndex

startButton.addEventListener('click', startQuiz)
nextButton.addEventListener('click', () => {
  currentQuestionIndex++
  renderNextQuestion()
})


  function renderNextQuestion() {
    resetState()
    showQuestion(mixQuestions[currentQuestionIndex])
  }

  
function startQuiz() {
  startButton.classList.add('invisible')
  mixQuestions = questions.sort(() => Math.random() - .5)
  currentQuestionIndex = 0
  questionContainerElement.classList.remove('hide')
  resultTea.classList.add('hide')
  renderNextQuestion()
}

function showQuestion(question) {
  questionElement.innerText = question.question
  question.answers.forEach(answer => {
    const button = document.createElement('button')
    button.innerText = answer.text
    button.classList.add('btn')
    if (answer.assign) {
      button.dataset.assign = answer.assign
    }
    button.addEventListener('click', selectAnswer)
    answerButtonsElement.appendChild(button)
  })
}

function resetState() {
  nextButton.classList.add('invisible')
  while (answerButtonsElement.firstChild) {
    answerButtonsElement.removeChild(answerButtonsElement.firstChild)
  }
}

function selectAnswer(e) {
  const selectedButton = e.target
  const assign = selectedButton.dataset.assign.split(',').map(Number)
  console.log(assign)
  incrementTeaScore(assign)
  if (mixQuestions.length > currentQuestionIndex + 1) {
    nextButton.classList.remove('invisible')
  } else {
    let tea = getTotalScore(teaObject);
    document.getElementById('tea-question').classList.add('hide')
    document.getElementById('answer-buttons').classList.add('hide')
    // document.getElementById('start-btn').classList.add('hide')

    resultTea.classList.remove('hide')
    questionContainerElement.classList.add('hide')
    // startButton.classList.remove('invisible')
    let card = document.getElementById('card')


    if(tea == 'blackTea'){
      // update image, name,
      $.get('/quiz_result/' + 1, response => {
        console.log(JSON.parse(response))
        let jsonResponse = JSON.parse(response);
        document.getElementById('teaimage').src = jsonResponse.image
        console.log(jsonResponse.name)
        document.getElementById('nametea').innerHTML = jsonResponse.name
        document.getElementById('teaid').href = "/teas/" + jsonResponse.id
      })
    }
    if(tea == 'greenTea'){
      // update image, name,
      $.get('/quiz_result/' + 2, response => {
        console.log(JSON.parse(response))
        let jsonResponse = JSON.parse(response);
        document.getElementById('teaimage').src = jsonResponse.image
        console.log(jsonResponse.name)
        document.getElementById('nametea').innerHTML = jsonResponse.name
        document.getElementById('teaid').href = "/teas/" + jsonResponse.id
      })
    }
    if(tea == 'oolongTea'){
      // update image, name,
      $.get('/quiz_result/' + 3, response => {
        console.log(JSON.parse(response))
        let jsonResponse = JSON.parse(response);
        document.getElementById('teaimage').src = jsonResponse.image
        console.log(jsonResponse.name)
        document.getElementById('nametea').innerHTML = jsonResponse.name
        document.getElementById('teaid').href = "/teas/" + jsonResponse.id
      })
    }
      if(tea == 'puerhTea'){
        // update image, name,
        $.get('/quiz_result/' + 4, response => {
          console.log(JSON.parse(response))
          let jsonResponse = JSON.parse(response);
          document.getElementById('teaimage').src = jsonResponse.image
          console.log(jsonResponse.name)
          document.getElementById('nametea').innerHTML = jsonResponse.name
          document.getElementById('teaid').href = "/teas/" + jsonResponse.id
        })
      }
        if(tea == 'whiteTea'){
          // update image, name,
          $.get('/quiz_result/' + 5, response => {
            console.log(JSON.parse(response))
            let jsonResponse = JSON.parse(response);
            document.getElementById('teaimage').src = jsonResponse.image
            console.log(jsonResponse.name)
            document.getElementById('nametea').innerHTML = jsonResponse.name
            document.getElementById('teaid').href = "/teas/" + jsonResponse.id
          })
        }
        if(tea == 'chamomileTea'){
        // update image, name,
        $.get('/quiz_result/' + 6, response => {
        console.log(JSON.parse(response))
        let jsonResponse = JSON.parse(response);
        document.getElementById('teaimage').src = jsonResponse.image
        console.log(jsonResponse.name)
        document.getElementById('nametea').innerHTML = jsonResponse.name
        document.getElementById('teaid').href = "/teas/" + jsonResponse.id
        })
        }
        if(tea == 'gingerTea'){
        // update image, name,
        $.get('/quiz_result/' + 7, response => {
        console.log(JSON.parse(response))
        let jsonResponse = JSON.parse(response);
        document.getElementById('teaimage').src = jsonResponse.image
        console.log(jsonResponse.name)
        document.getElementById('nametea').innerHTML = jsonResponse.name
        document.getElementById('teaid').href = "/teas/" + jsonResponse.id
        })
        }
        if(tea == 'hibiscusTea'){
        // update image, name,
        $.get('/quiz_result/' + 8, response => {
        console.log(JSON.parse(response))
        let jsonResponse = JSON.parse(response);
        document.getElementById('teaimage').src = jsonResponse.image
        console.log(jsonResponse.name)
        document.getElementById('nametea').innerHTML = jsonResponse.name
        document.getElementById('teaid').href = "/teas/" + jsonResponse.id
        })
        }
        if(tea == 'mintTea'){
        // update image, name,
        $.get('/quiz_result/' + 9, response => {
        console.log(JSON.parse(response))
        let jsonResponse = JSON.parse(response);
        document.getElementById('teaimage').src = jsonResponse.image
        console.log(jsonResponse.name)
        document.getElementById('nametea').innerHTML = jsonResponse.name
        document.getElementById('teaid').href = "/teas/" + jsonResponse.id
        })
        }
        if(tea == 'rooibosTea'){
        // update image, name,
        $.get('/quiz_result/' + 10, response => {
        console.log(JSON.parse(response))
        let jsonResponse = JSON.parse(response);
        document.getElementById('teaimage').src = jsonResponse.image
        console.log(jsonResponse.name)
        document.getElementById('nametea').innerHTML = jsonResponse.name
        document.getElementById('teaid').href = "/teas/" + jsonResponse.id
        })
        }

        }
        }

 
let teaObject = {
    blackTea: 0,
    greenTea: 0,
    oolongTea: 0, 
    puerhTea: 0, 
    chamomileTea: 0, 
    whiteTea: 0,
    hibiscusTea: 0, 
    rooibosTea: 0, 
    gingerTea: 0, 
    mintTea: 0 
}


function incrementTeaScore(assign) {
  console.log(assign)
    for (num of assign){
        if (num === 1){
          teaObject.blackTea+= 1
        }
        if (num === 2){
            teaObject.greenTea+= 1
        }
        if (num === 3){
            teaObject.oolongTea+= 1
        }
        if (num === 4){
            teaObject.puerhTea+= 1
        }
        if (num === 5){
            teaObject.whiteTea+= 1
        }
        if (num === 6){
            teaObject.chamomileTea+= 1
        }
        if (num === 7){
            teaObject.gingerTea+= 1
        }
        if (num === 8){
            teaObject.hibiscusTea+= 1
        }
        if (num === 9){
            teaObject.mintTea+= 1
        }
        if (num === 10){
          console.log(num)
            teaObject.rooibosTea+= 1
        }
    }
  };

  
  function getTotalScore(teaObject){
    let tea = Object.keys(teaObject).reduce((a, b) => teaObject[a] > teaObject[b] ? a : b);
    return tea
  }

const questions = [
  {
    question: 'Do you like caffeine?',
    answers: [
      { text: 'Yes', assign: [1] },
      { text: 'No', assign: [6, 7, 9] },
      { text: 'Sometimes', assign: [3, 2, 5]}
    ]
  },
  // {
  //   question: 'What is most important for you?',
  //   answers: [
  //     { text: 'Sleep', assign: [6] },
  //     { text: 'Keeping Healthy', assign: [10, 8, 2] },
  //     { text: 'Beauty', assign: [1, 3, 5 ]},
  //     { text: 'Being Happy', assign: [6, 7] },
  //     { text: 'Being Creative', assign: [2, 7] }

  //   ]
  // },
  // {
  //   question: 'How do you enjoy your teas?',
  //   answers: [
  //     { text: 'Iced and Sweetened', assign: [6] },
  //     { text: 'Iced and Unsweetened', assign: [2, 10] },
  //     { text: 'Warm', assign: [1] },
  //     { text: 'Hot', assign: [5, 2, 3]}
  //   ]
  // },
  // {
  //   question: 'What time of day do you like your tea?',
  //   answers: [
  //     { text: 'Morning', assign: [3, 1, 5] },
  //     { text: 'Afternoon', assign: [9] },
  //     { text: 'Night', assign: [6]}
  //   ]
  // },
  // {
  //   question: 'What benefit are you hoping to gain?',
  //   answers: [
  //     { text: 'Support in Heart Health', assign: [3, 2, 1, 4, 10]},
  //     { text: 'Support in Brain Health', assign: [2, 3, 4, 5]  },
  //     { text: 'Support in Digestion', assign:  [8]  },
  //     { text: 'Support in Liver Health', assign: [6, 9]  },
  //     { text: 'Reduce in Motion Sickness', assign: [7] },
  //     { text: 'Strong Teeth and Bones', assign: [10] }
  //   ]
  // },
  // {
  //   question: 'On a scale of 1 to never how often do you drink tea weekly?',
  //   answers: [
  //     { text: '1-3 times a week', assign: [8] },
  //     { text: '4-7 almost daily', assign: [5] },
  //     { text: '8+, if i was getting paid to drink tea id be a millionarie', assign: [3] }
  //   ]
  // }
]