var count = 10;
    var guesses = null
    randVal=null
    console.log("Random Value :" + randVal)
    countVal = document.getElementById('count')
    countVal.innerHTML = count
    comment = document.getElementById('comment')
    comment.innerHTML = "Lets Begin!"

    startGame=()=>{
        randVal = Math.round((Math.random() * 100) + 1, 0)
        console.log("Random Value :" + randVal)
        game=document.getElementsByClassName('game')
        game[0].style.display='block'
        start=document.getElementsByClassName('start')
        start[0].style.display="none"
    }

    counterUpdate=(guesses,val)=>{
        if (val == 'greater' || val == 'lesser'){
            count -= 1
            countVal.innerHTML = count
            document.getElementById('guess').value= ""
            document.getElementById('guess').focus()
        }else if(val=="game over"){
            count = 10
            countVal.innerHTML = count
            document.getElementById('guess').value= ""
            document.getElementById('guess').focus()
        }
        console.log("Entered");
        
    }

    endGame=()=>{
        game=document.getElementsByClassName('game')
        game[0].style.display='none'
        start=document.getElementsByClassName('start')
        start[0].style.display="block"
    }

    guessNumber = () => {
        guesses = document.getElementById('guess').value
        if (count != 0) {
            if (guesses != "" || isNaN(guesses)) {
                if (guesses == randVal) {
                    comment.innerHTML = "Vola Geuessed Correct!.."
                    randVal = Math.round((Math.random() * 10) + 1, 0)
                    counterUpdate(guesses,"game over")
                    endGame()
                }
                else if (guesses < randVal) {
                    comment.innerHTML = "Guessed Number is less"
                    counterUpdate(guesses,"lesser")
                }
                else if (guesses > randVal) {
                    comment.innerHTML = "Guessed Number is Greater"
                    counterUpdate(guesses,"greater")
                }
            }
            else {
                comment.innerHTML = "You must enter a Number to Guess :("
                guesses.value = ""

            }
        }
        else {
            randVal = Math.round((Math.random() * 10) + 1, 0)
            comment.innerHTML = "Lets Start Again"
            counterUpdate(guesses,'game over')
            endGame()
        }
    }