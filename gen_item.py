import html

script = '''
    <script>
        function buttonClick(button) {
            let item = button.dataset.item
            let value = parseInt(button.dataset.value)
            let sendvalue;
            if(parseInt(button.dataset.active)) {
                sendvalue = 0
            }
            else {
                sendvalue = value
            }
            fetch(
                new Request(window.location.href, {
                    method: 'PUT',
                    headers: {'Content-Type': 'application/json'},
                    body: '{"item": "' + item + '","value": "' + sendvalue + '"}'
                })
            ).then(response => {
                if(response.ok) {
                    let delta = sendvalue - document.querySelector('[data-counted="' + item +'"]').dataset.currentVote
                    console.log(document.querySelectorAll('[data-counted="' + item +'"]'))
                    for(let counter of document.querySelectorAll('[data-counted="' + item +'"]')){
                        counter.innerHTML = parseInt(counter.innerHTML) + delta
                        counter.dataset.currentVote = sendvalue
                    }
                    let newstyledown = "color:black"
                    let newstyleup = "color:black"
                    let newactivedown = 0
                    let newactiveup = 0
                    if(sendvalue === 1) {
                        newstyleup = "color:green"
                        newactiveup = 1
                    }
                    else if(sendvalue === -1) {
                        newstyledown = "color:red"
                        newactivedown = 1
                    }
                    for(let arrow of document.querySelectorAll('[data-item="' + item +'"]')){
                        if (arrow.dataset.value === "-1"){
                            arrow.setAttribute('style', newstyledown)
                            arrow.dataset.active = newactivedown
                        }
                        else {
                            arrow.setAttribute('style', newstyleup)
                            arrow.dataset.active = newactiveup
                        }
                    }
                }
            })
        }
    </script>
    '''

def gen_item(name, diets, votes, currentvote): 
    up = f'''
        <span style="{'color:green' if currentvote == 1 else 'color:black'}" data-item="{html.escape(name)}" data-value="1" data-active="{1 if currentvote == 1 else 0}" onClick="buttonClick(this)">▲</span>
        '''
    score = f'''
        <span data-counted="{html.escape(name)}" data-current-vote="{currentvote}">{votes}</span>
        '''
    down = f'''
        <span style="{'color:red' if currentvote == -1 else 'color:black'}" data-item="{html.escape(name)}" data-value="-1" data-active="{1 if currentvote == -1 else 0}" onClick="buttonClick(this)">▼</span>
        '''
    return f'''
        {down} {score} {up} &nbsp; {name} {' '.join(diets)}
        </br>
        '''
