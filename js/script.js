selected = [];

$(document).ready(function(){
    $(".emojis").children()[0].classList.remove("hidden")
    $(".emojis").children()[1].classList.remove("hidden")
    $(".emoji").click(function(){
        $(this).parent().children().each(function(){
            // this.removeClass("selected")
            this.classList.remove("selected")
            var index = selected.indexOf(this)
            if (index !== -1) selected.splice(index, 1)
        })
        $(this).addClass("selected")
        selected.push($(this)[0])
        if (selected.length > 2) {
            selected[0].classList.remove("selected")
            selected.shift()

        }
        if (selected.length === 2) {
            if (selected[0].innerText === selected[1].innerText) {
                selected[0].parentNode.remove()
                selected[1].parentNode.remove()
                $(".emojis").children()[0].classList.remove("hidden")
                $(".emojis").children()[1].classList.remove("hidden")
            }
        }
    })
})