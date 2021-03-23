//Initilazing SpeechRecognition api
var speechRecognition = window.webkitSpeechRecognition

var recognition = new speechRecognition()

//Setting recognition language
recognition.lang = 'en-in'


var textbox = $("#textbox")

var instructions = $("#instructions")

var content = ''

// Intermediate results, fast recognition
recognition.interimResults = true

// Continuously listening...
recognition.continuous = true


// recognition is started

recognition.onstart = function () {
    instructions.text("Speak something...")
}

recognition.onspeechend = function () {
    instructions.text("processing")
}

recognition.onerror = function () {
    instructions.text("Try Again")
}

recognition.addEventListener('result', e => {


    const transcript = Array.from(e.results)
    .map(result => result[0])
    .map(result => result.transcript)
    .join('')

    //Putting the values in textarea
    textbox.val(transcript)

    console.log(transcript)

})

// (Speech recognition)
$('#start-btn').click(function (event) {
    recognition.start()
})

$('#stop-btn').click(function (event) {
    recognition.stop()
})

$('#reload-btn').click(function (event) {
    document.location.reload(true)
})

textbox.on('input', function () {
    content = $(this).val()
})